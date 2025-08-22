#!/usr/bin/env python3
"""
Scripts to drive a donkey 2 car

Usage:
    manage.py (drive) [--model=<model>] [--js] [--type=(linear|categorical)] [--camera=(single|stereo)] [--meta=<key:value> ...] [--myconfig=<filename>]
    manage.py (train) [--tubs=tubs] (--model=<model>) [--type=(linear|inferred|tensorrt_linear|tflite_linear)]

Options:
    -h --help               Show this screen.
    --js                    Use physical joystick.
    -f --file=<file>        A text file containing paths to tub files, one per line. Option may be used more than once.
    --meta=<key:value>      Key/Value strings describing describing a piece of meta data about this drive. Option may be used more than once.
    --myconfig=filename     Specify myconfig file to use.
                            [default: myconfig.py]
"""

# manage.py for TatamiRacer
# based on donkey v4.2.0

#TatamiRacer Actuator Parts Class
import numpy as np
import pigpio

import os
import time
import logging
from docopt import docopt

import donkeycar as dk
from donkeycar.parts.transform import TriggeredCallback, DelayedTrigger
from donkeycar.parts.tub_v2 import TubWriter
from donkeycar.parts.datastore import TubHandler
from donkeycar.parts.controller import LocalWebController, JoystickController, WebFpv
from donkeycar.parts.throttle_filter import ThrottleFilter
from donkeycar.parts.behavior import BehaviorPart
from donkeycar.parts.file_watcher import FileWatcher
from donkeycar.parts.launch import AiLaunch
from donkeycar.utils import *

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


#Steering parts for TatamiRacer
class PWMSteering_TATAMI:
    def __init__(self,cfg):
        import pigpio
        import time
        import numpy as np

        self.gpio_pin = 14 #Servo PWM pin

        self.pi = pigpio.pi()
        self.pigpio = pigpio

        if not self.pi.connected:
            print("ERROR: Can't connect to pigpio daemon for steering!")
            print("Make sure pigpio daemon is running: sudo pigpiod")
            return
        else:
            print("Successfully connected to pigpio daemon")

        # Set GPIO pin as output
        self.pi.set_mode(self.gpio_pin, pigpio.OUTPUT)

        #tatamiRacer Steering Control Tunable Parameter
        self.left_pulse = cfg.TATAMI_STEERING_LEFT_PWM #LEFT PWM
        self.right_pulse = cfg.TATAMI_STEERING_RIGHT_PWM #RIGHT PWM
        self.steering_feel = cfg.TATAMI_STEERING_FEEL #Steering Feeling Adjustment (Angle Level at Steering 50%)
        self.steering_balance = cfg.TATAMI_STEERING_BALANCE #Steering L/R Balance -1.0(L)..+1.0(R)

        self.half_range = abs(self.right_pulse - self.left_pulse)/2
        self.center = min(self.left_pulse,self.right_pulse) + self.half_range

        self.servo_idle_time0 = time.time()
        self.servo_p0 = 0
        self.last_angle = None  # Track last angle to reduce debug output
        self.debug_counter = 0  # Only print debug every N calls

        # Test servo at center position
        self.pi.set_servo_pulsewidth(self.gpio_pin, int(self.center))

        print('PWM Steering for TatamiRacer Created.')

    def update(self):
        pass

    def run_threaded(self, steering):
        import time
        import numpy as np

        self.debug_counter += 1

        # Only print debug for significant changes or errors
        if steering is None:
            steering = 0.0

        # Only debug print every 50 calls or when steering changes significantly
        debug_this_call = (self.debug_counter % 50 == 0 or
                          self.last_angle is None or
                          abs(steering - (self.last_angle or 0)) > 0.1)

        original_steering = steering

        #Steering Feeling Adjustment
        ang_abs=np.abs(steering)
        steering_half=0.5
        if ang_abs < steering_half:
            slope = self.steering_feel/steering_half
            steering = np.sign(steering)*ang_abs*slope
        else:
            slope = (1.0-self.steering_feel)/(1.0-steering_half)
            steering = np.sign(steering)* (self.steering_feel+(ang_abs-steering_half)*slope)

        #Steering Balance Adjustment
        if steering>0:
            steering =  steering * (1.0+self.steering_balance)
        else:
            steering =  steering * (1.0-self.steering_balance)

        #Steering PWM Calculation - Fixed logic to match test file
        servo_p = int(self.center - self.half_range * steering)

        # Fix the limit checking logic
        servo_max = max(self.left_pulse, self.right_pulse)
        servo_min = min(self.left_pulse, self.right_pulse)

        servo_p_before_limit = servo_p
        if servo_p > servo_max:
            servo_p = servo_max
        elif servo_p < servo_min:
            servo_p = servo_min

        if self.servo_p0 != servo_p: #PWM changed
            self.servo_idle_time0=time.time() #Reset idle time
            servo_idle_time = 0
        else:
            servo_idle_time=time.time()-self.servo_idle_time0

        self.servo_p0 = servo_p

        if servo_idle_time <= 5.0:
            self.pi.set_servo_pulsewidth(self.gpio_pin, servo_p)
        else:
            self.pi.set_servo_pulsewidth(self.gpio_pin, 0)

        self.last_angle = original_steering

    def run(self, steering):
        self.run_threaded(steering)

    def shutdown(self):
        self.pi.set_servo_pulsewidth(self.gpio_pin, 0)  # Turn off servo first
        self.pi.set_mode(self.gpio_pin, self.pigpio.INPUT)
        self.pi.stop()

#Throttle parts for TatamiRacer
class PWMThrottle_TATAMI:
    def __init__(self, cfg):
        import pigpio
        self.pi = pigpio.pi()
        if not self.pi.connected:
            print("Error: Can't connect to pigpio daemon!")
            return

        # Setup GPIO pins for motor control
        self.gpio_pin0 = 13  # Motor pin 1
        self.gpio_pin1 = 19  # Motor pin 2

        # Configure pins as outputs
        self.pi.set_mode(self.gpio_pin0, pigpio.OUTPUT)
        self.pi.set_mode(self.gpio_pin1, pigpio.OUTPUT)

        # Initialize PWM parameters
        self.pi.set_PWM_range(self.gpio_pin0, 100)
        self.pi.set_PWM_range(self.gpio_pin1, 100)
        self.pi.set_PWM_frequency(self.gpio_pin0, 490)
        self.pi.set_PWM_frequency(self.gpio_pin1, 490)

        # TatamiRacer specific config parameters
        self.throttle_deadzone = 0.01

        # Load parameters from config
        if hasattr(cfg, 'TATAMI_THROTTLE_START_BOOST_TIME'):
            self.throttle_start_boost_time = cfg.TATAMI_THROTTLE_START_BOOST_TIME
        else:
            self.throttle_start_boost_time = 0.3

        if hasattr(cfg, 'TATAMI_THROTTLE_START_BOOST'):
            self.throttle_start_boost = cfg.TATAMI_THROTTLE_START_BOOST
        else:
            self.throttle_start_boost = 0.2

        if hasattr(cfg, 'TATAMI_THROTTLE_UPPER_LIMIT'):
            self.throttle_upper_limit = cfg.TATAMI_THROTTLE_UPPER_LIMIT
        else:
            self.throttle_upper_limit = 0.5

        if hasattr(cfg, 'TATAMI_THROTTLE_LOWER_LIMIT'):
            self.throttle_lower_limit = cfg.TATAMI_THROTTLE_LOWER_LIMIT
        else:
            self.throttle_lower_limit = 0.1

        if hasattr(cfg, 'TATAMI_THROTTLE_STEERING_BOOST'):
            self.throttle_steering_boost = cfg.TATAMI_THROTTLE_STEERING_BOOST
        else:
            self.throttle_steering_boost = 0.25

        # Time tracking for boost
        self.throttle_start_boost_time0 = time.time()

        # Store last values
        self.stored_throttle = 0
        self.stored_angle = 0

        print('PWM Throttle for TatamiRacer created.')

    def update(self):
        pass

    def run_threaded(self, throttle, steering):
        # Add input validation
        if throttle is None:
            throttle = 0.0
        if steering is None:
            steering = 0.0

        # Store values
        self.stored_throttle = throttle
        self.stored_angle = steering

        # Process throttle input
        throttle_abs = np.abs(throttle)
        if throttle_abs <= self.throttle_deadzone:
            self.throttle_start_boost_time0 = time.time()
            throttle = 0.0
            self.pi.set_PWM_dutycycle(self.gpio_pin0, 0)  # PWM off
            self.pi.set_PWM_dutycycle(self.gpio_pin1, 0)  # PWM off
            return  # Don't return the throttle value

        # Throttle Boost - add boost after idle
        t = time.time() - self.throttle_start_boost_time0
        if t <= self.throttle_start_boost_time:
            boost = self.throttle_start_boost  # Boost mode
        else:
            boost = 0.0

        # Steering Resistance Adjustment
        angle_adjust = self.throttle_lower_limit + np.abs(steering) * (self.throttle_steering_boost - self.throttle_lower_limit)

        # Throttle Feeling
        if throttle_abs < self.throttle_lower_limit:
            throttle_feel = self.throttle_lower_limit
        elif throttle_abs > self.throttle_upper_limit:
            throttle_feel = self.throttle_upper_limit
        else:
            slope = self.throttle_upper_limit - self.throttle_lower_limit
            throttle_feel = self.throttle_lower_limit + throttle_abs * slope

        if throttle_abs > self.throttle_deadzone:
            throttle = np.sign(throttle) * max(boost, angle_adjust, throttle_feel)

        # Set Motor PWM
        motor_v = int(100 * throttle)  # PWM max is 100
        if np.abs(motor_v) > 100:
            motor_v = int(np.sign(motor_v) * 100)

        if throttle > 0:
            # Forward
            self.pi.set_PWM_dutycycle(self.gpio_pin0, motor_v)
            self.pi.set_PWM_dutycycle(self.gpio_pin1, 0)
        else:
            # Backward
            self.pi.set_PWM_dutycycle(self.gpio_pin1, abs(motor_v))
            self.pi.set_PWM_dutycycle(self.gpio_pin0, 0)

        # Don't return anything - this is an actuator part

    def run(self, throttle, steering):
        # This method should also not return anything
        self.run_threaded(throttle, steering)


    def shutdown(self):
        self.pi.set_PWM_dutycycle(self.gpio_pin0, 0)  # PWM off
        self.pi.set_PWM_dutycycle(self.gpio_pin1, 0)  # PWM off
        self.pi.stop()


def add_user_controller(V, cfg, use_joystick, input_image='cam/image_array'):
    """
    Add the web controller and any other
    configured user input controller.
    :param V: the vehicle pipeline.
              On output this will be modified.
    :param cfg: the configuration (from myconfig.py)
    :param use_joystick: whether to use joystick
    :param input_image: the input image for the controller
    :return: the controller
    """

    #
    # This web controller will create a web server that is capable
    # of managing steering, throttle, and modes, and more.
    #
    ctr = LocalWebController(port=cfg.WEB_CONTROL_PORT, mode=cfg.WEB_INIT_MODE)
    V.add(ctr,
          inputs=[input_image, 'tub/num_records', 'user/mode', 'recording'],
          outputs=['user/steering', 'user/throttle', 'user/mode', 'recording', 'web/buttons'],
          threaded=True)

    #
    # also add a physical controller if one is configured
    #
    if use_joystick or cfg.USE_JOYSTICK_AS_DEFAULT:
        #
        # RC controller
        #
        if cfg.CONTROLLER_TYPE == "pigpio_rc":  # an RC controllers read by GPIO pins. They typically don't have buttons
            from donkeycar.parts.controller import RCReceiver
            ctr = RCReceiver(cfg)
            V.add(
                ctr,
                inputs=['user/mode', 'recording'],
                outputs=['user/steering', 'user/throttle',
                         'user/mode', 'recording'],
                threaded=False)
        else:
            #
            # custom game controller mapping created with
            # `donkey createjs` command
            #
            if cfg.CONTROLLER_TYPE == "custom":  # custom controller created with `donkey createjs` command
                from my_joystick import MyJoystickController
                ctr = MyJoystickController(
                    throttle_dir=cfg.JOYSTICK_THROTTLE_DIR,
                    throttle_scale=cfg.JOYSTICK_MAX_THROTTLE,
                    steering_scale=cfg.JOYSTICK_STEERING_SCALE,
                    auto_record_on_throttle=cfg.AUTO_RECORD_ON_THROTTLE)
                ctr.set_deadzone(cfg.JOYSTICK_DEADZONE)
            elif cfg.CONTROLLER_TYPE == "MM1":
                from donkeycar.parts.robohat import RoboHATController
                ctr = RoboHATController(cfg)
            elif cfg.CONTROLLER_TYPE == "mock":
                from donkeycar.parts.controller import MockController
                ctr = MockController(steering=cfg.MOCK_JOYSTICK_STEERING,
                                     throttle=cfg.MOCK_JOYSTICK_THROTTLE)
            else:
                #
                # game controller
                #
                from donkeycar.parts.controller import get_js_controller
                ctr = get_js_controller(cfg)
                if cfg.USE_NETWORKED_JS:
                    from donkeycar.parts.controller import JoyStickSub
                    netwkJs = JoyStickSub(cfg.NETWORK_JS_SERVER_IP)
                    V.add(netwkJs, threaded=True)
                    ctr.js = netwkJs
            V.add(
                ctr,
                inputs=[input_image, 'user/mode', 'recording'],
                outputs=['user/steering', 'user/throttle',
                         'user/mode', 'recording'],
                threaded=True)
    return ctr


def drive(cfg, model_path=None, use_joystick=False, model_type=None,
          camera_type='single', meta=[]):
    """
    Construct a working robotic vehicle from many parts. Each part runs as a
    job in the Vehicle loop, calling either it's run or run_threaded method
    depending on the constructor flag `threaded`. All parts are updated one
    after another at the framerate given in cfg.DRIVE_LOOP_HZ assuming each
    part finishes processing in a timely manner. Parts may have named outputs
    and inputs. The framework handles passing named outputs to parts
    requesting the same named input.
    """
    logger.info(f'PID: {os.getpid()}')
    if cfg.DONKEY_GYM:
        #the simulator will use cuda and then we usually run out of resources
        #if we also try to use cuda. so disable for donkey_gym.
        os.environ["CUDA_VISIBLE_DEVICES"]="-1"

    if model_type is None:
        if cfg.TRAIN_LOCALIZER:
            model_type = "localizer"
        elif cfg.TRAIN_BEHAVIORS:
            model_type = "behavior"
        else:
            model_type = cfg.DEFAULT_MODEL_TYPE

    #Initialize car
    V = dk.vehicle.Vehicle()

    #Initialize logging before anything else to allow console logging
    if cfg.HAVE_CONSOLE_LOGGING:
        logger.setLevel(logging.getLevelName(cfg.LOGGING_LEVEL))
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter(cfg.LOGGING_FORMAT))
        logger.addHandler(ch)

    if cfg.HAVE_MQTT_TELEMETRY:
        from donkeycar.parts.telemetry import MqttTelemetry
        tel = MqttTelemetry(cfg)

    if cfg.HAVE_ODOM:
        if cfg.ENCODER_TYPE == "GPIO":
            from donkeycar.parts.encoder import RotaryEncoder
            enc = RotaryEncoder(mm_per_tick=0.306096, pin = cfg.ODOM_PIN, debug = cfg.ODOM_DEBUG)
            V.add(enc, inputs=['throttle'], outputs=['enc/speed'], threaded=True)
        elif cfg.ENCODER_TYPE == "arduino":
            from donkeycar.parts.encoder import ArduinoEncoder
            enc = ArduinoEncoder()
            V.add(enc, outputs=['enc/speed'], threaded=True)
        else:
            print("No supported encoder found")

    logger.info("cfg.CAMERA_TYPE %s"%cfg.CAMERA_TYPE)
    if camera_type == "stereo":

        if cfg.CAMERA_TYPE == "WEBCAM":
            from donkeycar.parts.camera import Webcam

            camA = Webcam(image_w=cfg.IMAGE_W, image_h=cfg.IMAGE_H, image_d=cfg.IMAGE_DEPTH, iCam = 0)
            camB = Webcam(image_w=cfg.IMAGE_W, image_h=cfg.IMAGE_H, image_d=cfg.IMAGE_DEPTH, iCam = 1)

        elif cfg.CAMERA_TYPE == "CVCAM":
            from donkeycar.parts.cv import CvCam

            camA = CvCam(image_w=cfg.IMAGE_W, image_h=cfg.IMAGE_H, image_d=cfg.IMAGE_DEPTH, iCam = 0)
            camB = CvCam(image_w=cfg.IMAGE_W, image_h=cfg.IMAGE_H, image_d=cfg.IMAGE_DEPTH, iCam = 1)
        else:
            raise(Exception("Unsupported camera type: %s" % cfg.CAMERA_TYPE))

        V.add(camA, outputs=['cam/image_array_a'], threaded=True)
        V.add(camB, outputs=['cam/image_array_b'], threaded=True)

        from donkeycar.parts.image import StereoPair

        V.add(StereoPair(), inputs=['cam/image_array_a', 'cam/image_array_b'],
            outputs=['cam/image_array'])
    elif cfg.CAMERA_TYPE == "D435":
        from donkeycar.parts.realsense435i import RealSense435i
        cam = RealSense435i(
            enable_rgb=cfg.REALSENSE_D435_RGB,
            enable_depth=cfg.REALSENSE_D435_DEPTH,
            enable_imu=cfg.REALSENSE_D435_IMU,
            device_id=cfg.REALSENSE_D435_ID)
        V.add(cam, inputs=[],
              outputs=['cam/image_array', 'cam/depth_array',
                       'imu/acl_x', 'imu/acl_y', 'imu/acl_z',
                       'imu/gyr_x', 'imu/gyr_y', 'imu/gyr_z'],
              threaded=True)

    else:
        if cfg.DONKEY_GYM:
            from donkeycar.parts.dgym import DonkeyGymEnv

        inputs = []
        outputs = ['cam/image_array']
        threaded = True
        if cfg.DONKEY_GYM:
            from donkeycar.parts.dgym import DonkeyGymEnv
            #rbx
            cam = DonkeyGymEnv(cfg.DONKEY_SIM_PATH, host=cfg.SIM_HOST, env_name=cfg.DONKEY_GYM_ENV_NAME, conf=cfg.GYM_CONF, record_location=cfg.SIM_RECORD_LOCATION, record_gyroaccel=cfg.SIM_RECORD_GYROACCEL, record_velocity=cfg.SIM_RECORD_VELOCITY, delay=cfg.SIM_ARTIFICIAL_LATENCY)
            threaded = True
            inputs  = ['angle', 'throttle']
        elif cfg.CAMERA_TYPE == "PICAM":
            from donkeycar.parts.camera import PiCamera
            cam = PiCamera(image_w=cfg.IMAGE_W, image_h=cfg.IMAGE_H, image_d=cfg.IMAGE_DEPTH, framerate=cfg.CAMERA_FRAMERATE, vflip=cfg.CAMERA_VFLIP, hflip=cfg.CAMERA_HFLIP)
        elif cfg.CAMERA_TYPE == "WEBCAM":
            from donkeycar.parts.camera import Webcam
            cam = Webcam(image_w=cfg.IMAGE_W, image_h=cfg.IMAGE_H, image_d=cfg.IMAGE_DEPTH)
        elif cfg.CAMERA_TYPE == "CVCAM":
            from donkeycar.parts.cv import CvCam
            cam = CvCam(image_w=cfg.IMAGE_W, image_h=cfg.IMAGE_H, image_d=cfg.IMAGE_DEPTH)
        elif cfg.CAMERA_TYPE == "CSIC":
            from donkeycar.parts.camera import CSICamera
            cam = CSICamera(image_w=cfg.IMAGE_W, image_h=cfg.IMAGE_H, image_d=cfg.IMAGE_DEPTH, framerate=cfg.CAMERA_FRAMERATE, gstreamer_flip=cfg.CSIC_CAM_GSTREAMER_FLIP_PARM)
        elif cfg.CAMERA_TYPE == "V4L":
            from donkeycar.parts.camera import V4LCamera
            cam = V4LCamera(image_w=cfg.IMAGE_W, image_h=cfg.IMAGE_H, image_d=cfg.IMAGE_DEPTH, framerate=cfg.CAMERA_FRAMERATE)
        elif cfg.CAMERA_TYPE == "MOCK":
            from donkeycar.parts.camera import MockCamera
            cam = MockCamera(image_w=cfg.IMAGE_W, image_h=cfg.IMAGE_H, image_d=cfg.IMAGE_DEPTH)
        elif cfg.CAMERA_TYPE == "IMAGE_LIST":
            from donkeycar.parts.camera import ImageListCamera
            cam = ImageListCamera(path_mask=cfg.PATH_MASK)
        elif cfg.CAMERA_TYPE == "LEOPARD":
            from donkeycar.parts.leopard_imaging import LICamera
            cam = LICamera(width=cfg.IMAGE_W, height=cfg.IMAGE_H, fps=cfg.CAMERA_FRAMERATE)
        else:
            raise(Exception("Unkown camera type: %s" % cfg.CAMERA_TYPE))

        # add lidar
        if cfg.USE_LIDAR:
            from donkeycar.parts.lidar import RPLidar
            if cfg.LIDAR_TYPE == 'RP':
                print("adding RP lidar part")
                lidar = RPLidar(lower_limit = cfg.LIDAR_LOWER_LIMIT, upper_limit = cfg.LIDAR_UPPER_LIMIT)
                V.add(lidar, inputs=[],outputs=['lidar/dist_array'], threaded=True)
            if cfg.LIDAR_TYPE == 'YD':
                print("YD Lidar not yet supported")

        # Donkey gym part will output position information if it is configured
        if cfg.DONKEY_GYM:
            if cfg.SIM_RECORD_LOCATION:
                outputs += ['pos/pos_x', 'pos/pos_y', 'pos/pos_z', 'pos/speed', 'pos/cte']
            if cfg.SIM_RECORD_GYROACCEL:
                outputs += ['gyro/gyro_x', 'gyro/gyro_y', 'gyro/gyro_z', 'accel/accel_x', 'accel/accel_y', 'accel/accel_z']
            if cfg.SIM_RECORD_VELOCITY:
                outputs += ['vel/vel_x', 'vel/vel_y', 'vel/vel_z']

        V.add(cam, inputs=inputs, outputs=outputs, threaded=threaded)

    #
    # maintain run conditions for user mode and autopilot mode parts.
    #
    class UserPilotCondition:
        def __init__(self, show_pilot_image:bool = False) -> None:
            """
            :param show_pilot_image:bool True to show pilot image in pilot mode
                                     False to show user image in pilot mode
            """
            self.show_pilot_image = show_pilot_image

        def run(self, mode, user_image, pilot_image):
            """
            Maintain run condition and which image to show in web ui
            :param mode: 'user'|'local_angle'|'local_pilot'
            :param user_image: image to show in manual (user) pilot
            :param pilot_image: image to show in auto pilot
            :return: tuple of (user-condition, autopilot-condition, web image)
            """
            if mode == 'user':
                return True, False, user_image
            else:
                return False, True, pilot_image if self.show_pilot_image else user_image

    # Add this BEFORE the user controller so ui/image_array exists
    V.add(UserPilotCondition(show_pilot_image=getattr(cfg, 'SHOW_PILOT_IMAGE', False)),
          inputs=['user/mode', "cam/image_array", "cam/image_array"],
          outputs=['run_user', "run_pilot", "ui/image_array"])

    #
    # add the user input controller(s)
    # - this will add the web controller
    # - it will optionally add any configured 'joystick' controller
    #
    has_input_controller = hasattr(cfg, "CONTROLLER_TYPE") and cfg.CONTROLLER_TYPE != "mock"
    ctr = add_user_controller(V, cfg, use_joystick, input_image='ui/image_array')

    #
    # convert 'user/steering' to 'user/angle' to be backward compatible with deep learning data
    #
    from donkeycar.parts.pipe import Pipe
    V.add(Pipe(), inputs=['user/steering'], outputs=['user/angle'])

    #
    # explode the buttons input map into individual output key/values in memory
    #
    from donkeycar.parts.explode import ExplodeDict
    V.add(ExplodeDict(V.mem, "web/"), inputs=['web/buttons'])

    #
    # For example: adding a button handler is just adding a part with a run_condition
    # set to the button's name, so it runs when button is pressed.
    #
    from donkeycar.parts.transform import Lambda
    V.add(Lambda(lambda v: print(f"web/w1 clicked")), inputs=["web/w1"], run_condition="web/w1")
    V.add(Lambda(lambda v: print(f"web/w2 clicked")), inputs=["web/w2"], run_condition="web/w2")
    V.add(Lambda(lambda v: print(f"web/w3 clicked")), inputs=["web/w3"], run_condition="web/w3")
    V.add(Lambda(lambda v: print(f"web/w4 clicked")), inputs=["web/w4"], run_condition="web/w4")
    V.add(Lambda(lambda v: print(f"web/w5 clicked")), inputs=["web/w5"], run_condition="web/w5")

    #this throttle filter will allow one tap back for esc reverse
    th_filter = ThrottleFilter()
    V.add(th_filter, inputs=['user/throttle'], outputs=['user/throttle'])

    #See if we should even run the pilot module.
    #This is only needed because the part run_condition only accepts boolean
    class PilotCondition:
        def run(self, mode):
            if mode == 'user':
                return False
            else:
                return True

    V.add(PilotCondition(), inputs=['user/mode'], outputs=['run_pilot'])

    class LedConditionLogic:
        def __init__(self, cfg):
            self.cfg = cfg

        def run(self, mode, recording, recording_alert, behavior_state, model_file_changed, track_loc):
            #returns a blink rate. 0 for off. -1 for on. positive for rate.

            if track_loc is not None:
                led.set_rgb(*self.cfg.LOC_COLORS[track_loc])
                return -1

            if model_file_changed:
                led.set_rgb(self.cfg.MODEL_RELOADED_LED_R, self.cfg.MODEL_RELOADED_LED_G, self.cfg.MODEL_RELOADED_LED_B)
                return 0.1
            else:
                led.set_rgb(self.cfg.LED_R, self.cfg.LED_G, self.cfg.LED_B)

            if recording_alert:
                led.set_rgb(*recording_alert)
                return self.cfg.REC_COUNT_ALERT_BLINK_RATE
            else:
                led.set_rgb(self.cfg.LED_R, self.cfg.LED_G, self.cfg.LED_B)

            if behavior_state is not None and model_type == 'behavior':
                r, g, b = self.cfg.BEHAVIOR_LED_COLORS[behavior_state]
                led.set_rgb(r, g, b)
                return -1 #solid on

            if recording:
                return -1 #solid on
            elif mode == 'user':
                return 1
            elif mode == 'local_angle':
                return 0.5
            elif mode == 'local':
                return 0.1
            return 0

    if cfg.HAVE_RGB_LED and not cfg.DONKEY_GYM:
        from donkeycar.parts.led_status import RGB_LED
        led = RGB_LED(cfg.LED_PIN_R, cfg.LED_PIN_G, cfg.LED_PIN_B, cfg.LED_INVERT)
        led.set_rgb(cfg.LED_R, cfg.LED_G, cfg.LED_B)

        V.add(LedConditionLogic(cfg), inputs=['user/mode', 'recording', "records/alert", 'behavior/state', 'modelfile/modified', "pilot/loc"],
              outputs=['led/blink_rate'])

        V.add(led, inputs=['led/blink_rate'])

    def get_record_alert_color(num_records):
        col = (0, 0, 0)
        for count, color in cfg.RECORD_ALERT_COLOR_ARR:
            if num_records >= count:
                col = color
        return col

    class RecordTracker:
        def __init__(self):
            self.last_num_rec_print = 0
            self.dur_alert = 0
            self.force_alert = 0

        def run(self, num_records):
            if num_records is None:
                return 0

            if self.last_num_rec_print != num_records or self.force_alert:
                self.last_num_rec_print = num_records

                if num_records % 10 == 0:
                    print("recorded", num_records, "records")

                if num_records % cfg.REC_COUNT_ALERT == 0 or self.force_alert:
                    self.dur_alert = num_records // cfg.REC_COUNT_ALERT * cfg.REC_COUNT_ALERT_CYC
                    self.force_alert = 0

            if self.dur_alert > 0:
                self.dur_alert -= 1

            if self.dur_alert != 0:
                return get_record_alert_color(num_records)

            return 0

    rec_tracker_part = RecordTracker()
    V.add(rec_tracker_part, inputs=["tub/num_records"], outputs=['records/alert'])

    if cfg.AUTO_RECORD_ON_THROTTLE and isinstance(ctr, JoystickController):
        #then we are not using the circle button. hijack that to force a record count indication
        def show_record_acount_status():
            rec_tracker_part.last_num_rec_print = 0
            rec_tracker_part.force_alert = 1
        ctr.set_button_down_trigger('circle', show_record_acount_status)

    if cfg.AUTO_RECORD_ON_THROTTLE:
        def show_record_count_status():
            rec_tracker_part.last_num_rec_print = 0
            rec_tracker_part.force_alert = 1
        if (cfg.CONTROLLER_TYPE != "pigpio_rc") and (cfg.CONTROLLER_TYPE != "MM1"):  # these controllers don't use the joystick class
            if isinstance(ctr, JoystickController):
                ctr.set_button_down_trigger('circle', show_record_count_status) #then we are not using the circle button. hijack that to force a record count indication
        else:
            show_record_count_status()

    #Sombrero
    if cfg.HAVE_SOMBRERO:
        from donkeycar.parts.sombrero import Sombrero
        s = Sombrero()

    #IMU
    if cfg.HAVE_IMU:
        from donkeycar.parts.imu import IMU
        imu = IMU(sensor=cfg.IMU_SENSOR, dlp_setting=cfg.IMU_DLP_CONFIG)
        V.add(imu, outputs=['imu/acl_x', 'imu/acl_y', 'imu/acl_z',
            'imu/gyr_x', 'imu/gyr_y', 'imu/gyr_z'], threaded=True)

    # Use the FPV preview, which will show the cropped image output, or the full frame.
    if cfg.USE_FPV:
        V.add(WebFpv(), inputs=['cam/image_array'], threaded=True)

    #Behavioral state
    if cfg.TRAIN_BEHAVIORS:
        bh = BehaviorPart(cfg.BEHAVIOR_LIST)
        V.add(bh, outputs=['behavior/state', 'behavior/label', "behavior/one_hot_state_array"])
        try:
            ctr.set_button_down_trigger('L1', bh.increment_state)
        except:
            pass

        inputs = ['cam/image_array', "behavior/one_hot_state_array"]
    #IMU
    elif cfg.USE_LIDAR:
        inputs = ['cam/image_array', 'lidar/dist_array']

    elif cfg.HAVE_ODOM:
        inputs = ['cam/image_array', 'enc/speed']

    elif model_type == "imu":
        assert(cfg.HAVE_IMU)
        #Run the pilot if the mode is not user.
        inputs=['cam/image_array',
            'imu/acl_x', 'imu/acl_y', 'imu/acl_z',
            'imu/gyr_x', 'imu/gyr_y', 'imu/gyr_z']
    elif cfg.USE_LIDAR:
        inputs = ['cam/image_array', 'lidar/dist_array']
    else:
        inputs=['cam/image_array']

    def load_model(kl, model_path):
        start = time.time()
        print('loading model', model_path)
        kl.load(model_path)
        print('finished loading in %s sec.' % (str(time.time() - start)) )

    def load_weights(kl, weights_path):
        start = time.time()
        try:
            print('loading model weights', weights_path)
            kl.model.load_weights(weights_path)
            print('finished loading in %s sec.' % (str(time.time() - start)) )
        except Exception as e:
            print(e)
            print('ERR>> problems loading weights', weights_path)

    def load_model_json(kl, json_fnm):
        start = time.time()
        print('loading model json', json_fnm)
        from tensorflow.python import keras
        try:
            with open(json_fnm, 'r') as handle:
                contents = handle.read()
                kl.model = keras.models.model_from_json(contents)
            print('finished loading json in %s sec.' % (str(time.time() - start)) )
        except Exception as e:
            print(e)
            print("ERR>> problems loading model json", json_fnm)

    if model_path:
        #When we have a model, first create an appropriate Keras part
        kl = dk.utils.get_model_by_type(model_type, cfg)

        model_reload_cb = None

        if '.h5' in model_path or '.uff' in model_path or 'tflite' in model_path or '.pkl' in model_path:
            #when we have a .h5 extension
            #load everything from the model file
            load_model(kl, model_path)

            def reload_model(filename):
                load_model(kl, filename)

            model_reload_cb = reload_model

        elif '.json' in model_path:
            #when we have a .json extension
            #load the model from there and look for a matching
            #.wts file with just weights
            load_model_json(kl, model_path)
            weights_path = model_path.replace('.json', '.weights')
            load_weights(kl, weights_path)

            def reload_weights(filename):
                weights_path = filename.replace('.json', '.weights')
                load_weights(kl, weights_path)

            model_reload_cb = reload_weights

        else:
            print("ERR>> Unknown extension type on model file!!")
            return

        #this part will signal visual LED, if connected
        V.add(FileWatcher(model_path, verbose=True), outputs=['modelfile/modified'])

        #these parts will reload the model file, but only when ai is running so we don't interrupt user driving
        V.add(FileWatcher(model_path), outputs=['modelfile/dirty'], run_condition="ai_running")
        V.add(DelayedTrigger(100), inputs=['modelfile/dirty'], outputs=['modelfile/reload'], run_condition="ai_running")
        V.add(TriggeredCallback(model_path, model_reload_cb), inputs=["modelfile/reload"], run_condition="ai_running")

        outputs=['pilot/steering', 'pilot/throttle']

        if cfg.TRAIN_LOCALIZER:
            outputs.append("pilot/loc")

        V.add(kl, inputs=inputs,
              outputs=outputs,
              run_condition='run_pilot')

    if cfg.STOP_SIGN_DETECTOR:
        from donkeycar.parts.object_detector.stop_sign_detector import StopSignDetector
        V.add(StopSignDetector(cfg.STOP_SIGN_MIN_SCORE, cfg.STOP_SIGN_SHOW_BOUNDING_BOX), inputs=['cam/image_array', 'pilot/throttle'], outputs=['pilot/throttle', 'cam/image_array'])

    #
    # choose between user and pilot mode based on mode
    #
    class DriveMode:
        def __init__(self, ai_throttle_mult=1.0):
            """
            :param ai_throttle_mult: scale throttle in autopilot mode
            """
            self.ai_throttle_mult = ai_throttle_mult

        def run(self, mode,
                user_steering, user_throttle,
                pilot_steering, pilot_throttle):
            """
            Main final steering and throttle values based on user mode
            :param mode: 'user'|'local_angle'|'local_pilot'
            :param user_steering: steering value in user (manual) mode
            :param user_throttle: throttle value in user (manual) mode
            :param pilot_steering: steering value in autopilot mode
            :param pilot_throttle: throttle value in autopilot mode
            :return: tuple of (steering, throttle) where throttle is
                     scaled by ai_throttle_mult in autopilot mode
            """
            if mode == 'user':
                return user_steering, user_throttle
            elif mode == 'local_angle':
                return pilot_steering if pilot_steering else 0.0, user_throttle
            return (pilot_steering if pilot_steering else 0.0,
                   pilot_throttle * self.ai_throttle_mult if pilot_throttle else 0.0)

    V.add(DriveMode(cfg.AI_THROTTLE_MULT),
          inputs=['user/mode', 'user/steering', 'user/throttle',
                  'pilot/steering', 'pilot/throttle'],
          outputs=['steering', 'throttle'])


    #to give the car a boost when starting ai mode in a race.
    aiLauncher = AiLaunch(cfg.AI_LAUNCH_DURATION, cfg.AI_LAUNCH_THROTTLE, cfg.AI_LAUNCH_KEEP_ENABLED)

    V.add(aiLauncher,
        inputs=['user/mode', 'throttle'],
        outputs=['throttle'])

    if isinstance(ctr, JoystickController):
        ctr.set_button_down_trigger(cfg.AI_LAUNCH_ENABLE_BUTTON, aiLauncher.enable_ai_launch)

    class AiRunCondition:
        '''
        A bool part to let us know when ai is running.
        '''
        def run(self, mode):
            if mode == "user":
                return False
            return True

    V.add(AiRunCondition(), inputs=['user/mode'], outputs=['ai_running'])

    #Ai Recording
    class ToggleRecording:
        def __init__(self, auto_record_on_throttle, record_in_autopilot):
            """
            Donkeycar Part that manages the recording state.
            """
            self.auto_record_on_throttle = auto_record_on_throttle
            self.record_in_autopilot = record_in_autopilot
            self.recording_latch: bool = None
            self.toggle_latch: bool = False
            self.last_recording = None

        def set_recording(self, recording: bool):
            """
            Set latched recording value to be applied on next call to run()
            :param recording: True to record, False to not record
            """
            self.recording_latch = recording

        def toggle_recording(self):
            """
            Force toggle of recording state on next call to run()
            """
            self.toggle_latch = True

        def run(self, mode: str, recording: bool):
            """
            Set recording based on user/autopilot mode
            :param mode: 'user'|'local_angle'|'local_pilot'
            :param recording: current recording flag
            :return: updated recording flag
            """
            recording_in = recording
            if recording_in != self.last_recording:
                logger.info(f"Recording Change = {recording_in}")

            if self.toggle_latch:
                if self.auto_record_on_throttle:
                    logger.info(
                        'auto record on throttle is enabled; ignoring toggle of manual mode.')
                else:
                    recording = not self.last_recording
                self.toggle_latch = False

            if self.recording_latch is not None:
                recording = self.recording_latch
                self.recording_latch = None

            if recording and mode != 'user' and not self.record_in_autopilot:
                logger.info("Ignoring recording in auto-pilot mode")
                recording = False

            if self.last_recording != recording:
                logger.info(f"Setting Recording = {recording}")

            self.last_recording = recording

            return recording

    # Ai Recording
    recording_control = ToggleRecording(cfg.AUTO_RECORD_ON_THROTTLE, cfg.RECORD_DURING_AI)
    V.add(recording_control, inputs=['user/mode', "recording"], outputs=["recording"])

    #Drive train setup
    if cfg.DONKEY_GYM or cfg.DRIVE_TRAIN_TYPE == "MOCK":
        pass
    elif cfg.DRIVE_TRAIN_TYPE == "SERVO_ESC":
        from donkeycar.parts.actuator import PCA9685, PWMSteering, PWMThrottle

        steering_controller = PCA9685(cfg.STEERING_CHANNEL, cfg.PCA9685_I2C_ADDR, busnum=cfg.PCA9685_I2C_BUSNUM)
        steering = PWMSteering(controller=steering_controller,
                                        left_pulse=cfg.STEERING_LEFT_PWM,
                                        right_pulse=cfg.STEERING_RIGHT_PWM)

        throttle_controller = PCA9685(cfg.THROTTLE_CHANNEL, cfg.PCA9685_I2C_ADDR, busnum=cfg.PCA9685_I2C_BUSNUM)
        throttle = PWMThrottle(controller=throttle_controller,
                                        max_pulse=cfg.THROTTLE_FORWARD_PWM,
                                        zero_pulse=cfg.THROTTLE_STOPPED_PWM,
                                        min_pulse=cfg.THROTTLE_REVERSE_PWM)

        V.add(steering, inputs=['steering'], threaded=True)
        V.add(throttle, inputs=['throttle'], threaded=True)


    elif cfg.DRIVE_TRAIN_TYPE == "DC_STEER_THROTTLE":
        from donkeycar.parts.actuator import Mini_HBridge_DC_Motor_PWM

        steering = Mini_HBridge_DC_Motor_PWM(cfg.HBRIDGE_PIN_LEFT, cfg.HBRIDGE_PIN_RIGHT)
        throttle = Mini_HBridge_DC_Motor_PWM(cfg.HBRIDGE_PIN_FWD, cfg.HBRIDGE_PIN_BWD)

        V.add(steering, inputs=['steering'])
        V.add(throttle, inputs=['throttle'])


    elif cfg.DRIVE_TRAIN_TYPE == "DC_TWO_WHEEL":
        from donkeycar.parts.actuator import TwoWheelSteeringThrottle, Mini_HBridge_DC_Motor_PWM

        left_motor = Mini_HBridge_DC_Motor_PWM(cfg.HBRIDGE_PIN_LEFT_FWD, cfg.HBRIDGE_PIN_LEFT_BWD)
        right_motor = Mini_HBridge_DC_Motor_PWM(cfg.HBRIDGE_PIN_RIGHT_FWD, cfg.HBRIDGE_PIN_RIGHT_BWD)
        two_wheel_control = TwoWheelSteeringThrottle()

        V.add(two_wheel_control,
                inputs=['throttle', 'steering'],
                outputs=['left_motor_speed', 'right_motor_speed'])

        V.add(left_motor, inputs=['left_motor_speed'])
        V.add(right_motor, inputs=['right_motor_speed'])

    elif cfg.DRIVE_TRAIN_TYPE == "DC_TWO_WHEEL_L298N":
        from donkeycar.parts.actuator import TwoWheelSteeringThrottle, L298N_HBridge_DC_Motor

        left_motor = L298N_HBridge_DC_Motor(cfg.HBRIDGE_L298N_PIN_LEFT_FWD, cfg.HBRIDGE_L298N_PIN_LEFT_BWD, cfg.HBRIDGE_L298N_PIN_LEFT_EN)
        right_motor = L298N_HBridge_DC_Motor(cfg.HBRIDGE_L298N_PIN_RIGHT_FWD, cfg.HBRIDGE_L298N_PIN_RIGHT_BWD, cfg.HBRIDGE_L298N_PIN_RIGHT_EN)
        two_wheel_control = TwoWheelSteeringThrottle()

        V.add(two_wheel_control,
                inputs=['throttle', 'steering'],
                outputs=['left_motor_speed', 'right_motor_speed'])

        V.add(left_motor, inputs=['left_motor_speed'])
        V.add(right_motor, inputs=['right_motor_speed'])


    elif cfg.DRIVE_TRAIN_TYPE == "SERVO_HBRIDGE_PWM":
        from donkeycar.parts.actuator import ServoBlaster, PWMSteering
        steering_controller = ServoBlaster(cfg.STEERING_CHANNEL) #really pin
        #PWM pulse values should be in the range of 100 to 200
        assert(cfg.STEERING_LEFT_PWM <= 200)
        assert(cfg.STEERING_RIGHT_PWM <= 200)
        steering = PWMSteering(controller=steering_controller,
                                        left_pulse=cfg.STEERING_LEFT_PWM,
                                        right_pulse=cfg.STEERING_RIGHT_PWM)


        from donkeycar.parts.actuator import Mini_HBridge_DC_Motor_PWM
        motor = Mini_HBridge_DC_Motor_PWM(cfg.HBRIDGE_PIN_FWD, cfg.HBRIDGE_PIN_BWD)

        V.add(steering, inputs=['steering'], threaded=True)
        V.add(motor, inputs=["throttle"])

    elif cfg.DRIVE_TRAIN_TYPE == "MM1":
        from donkeycar.parts.robohat import RoboHATDriver
        V.add(RoboHATDriver(cfg), inputs=['steering', 'throttle'])

    elif cfg.DRIVE_TRAIN_TYPE == "PIGPIO_PWM":
        from donkeycar.parts.actuator import PWMSteering, PWMThrottle, PiGPIO_PWM
        steering_controller = PiGPIO_PWM(cfg.STEERING_PWM_PIN, freq=cfg.STEERING_PWM_FREQ, inverted=cfg.STEERING_PWM_INVERTED)
        steering = PWMSteering(controller=steering_controller,
                                        left_pulse=cfg.STEERING_LEFT_PWM,
                                        right_pulse=cfg.STEERING_RIGHT_PWM)

        throttle_controller = PiGPIO_PWM(cfg.THROTTLE_PWM_PIN, freq=cfg.THROTTLE_PWM_FREQ, inverted=cfg.THROTTLE_PWM_INVERTED)
        throttle = PWMThrottle(controller=throttle_controller,
                                            max_pulse=cfg.THROTTLE_FORWARD_PWM,
                                            zero_pulse=cfg.THROTTLE_STOPPED_PWM,
                                            min_pulse=cfg.THROTTLE_REVERSE_PWM)
        V.add(steering, inputs=['steering'], threaded=True)
        V.add(throttle, inputs=['throttle'], threaded=True)

    elif cfg.DRIVE_TRAIN_TYPE == "PIGPIO_TATAMI": # PIGPIO Drive for TatamiRacer
        from donkeycar.parts.actuator import PWMSteering, PWMThrottle
        steering = PWMSteering_TATAMI(cfg)
        throttle = PWMThrottle_TATAMI(cfg)
        V.add(steering, inputs=['steering'], threaded=True)
        V.add(throttle, inputs=['throttle','steering'], threaded=True)

    # OLED setup
    if cfg.USE_SSD1306_128_32:
        from donkeycar.parts.oled import OLEDPart
        auto_record_on_throttle = cfg.USE_JOYSTICK_AS_DEFAULT and cfg.AUTO_RECORD_ON_THROTTLE
        oled_part = OLEDPart(cfg.SSD1306_128_32_I2C_BUSNUM, auto_record_on_throttle=auto_record_on_throttle)
        V.add(oled_part, inputs=['recording', 'tub/num_records', 'user/mode'], outputs=[], threaded=True)

    #add tub to save data

    if cfg.USE_LIDAR:
        inputs = ['cam/image_array', 'lidar/dist_array', 'user/steering', 'user/throttle', 'user/mode']
        types = ['image_array', 'nparray','float', 'float', 'str']
    else:
        inputs=['cam/image_array','user/steering', 'user/throttle', 'user/mode']
        types=['image_array','float', 'float','str']

    if cfg.USE_LIDAR:
        inputs += ['lidar/dist_array']
        types += ['nparray']

    if cfg.HAVE_ODOM:
        inputs += ['enc/speed']
        types += ['float']

    if cfg.TRAIN_BEHAVIORS:
        inputs += ['behavior/state', 'behavior/label', "behavior/one_hot_state_array"]
        types += ['int', 'str', 'vector']

    if cfg.CAMERA_TYPE == "D435" and cfg.REALSENSE_D435_DEPTH:
        inputs += ['cam/depth_array']
        types += ['gray16_array']

    if cfg.HAVE_IMU or (cfg.CAMERA_TYPE == "D435" and cfg.REALSENSE_D435_IMU):
        inputs += ['imu/acl_x', 'imu/acl_y', 'imu/acl_z',
            'imu/gyr_x', 'imu/gyr_y', 'imu/gyr_z']

        types +=['float', 'float', 'float',
           'float', 'float', 'float']

    # rbx
    if cfg.DONKEY_GYM:
        if cfg.SIM_RECORD_LOCATION:
            inputs += ['pos/pos_x', 'pos/pos_y', 'pos/pos_z', 'pos/speed', 'pos/cte']
            types  += ['float', 'float', 'float', 'float', 'float']
        if cfg.SIM_RECORD_GYROACCEL:
            inputs += ['gyro/gyro_x', 'gyro/gyro_y', 'gyro/gyro_z', 'accel/accel_x', 'accel/accel_y', 'accel/accel_z']
            types  += ['float', 'float', 'float', 'float', 'float', 'float']
        if cfg.SIM_RECORD_VELOCITY:
            inputs += ['vel/vel_x', 'vel/vel_y', 'vel/vel_z']
            types  += ['float', 'float', 'float']

    if cfg.RECORD_DURING_AI:
        inputs += ['pilot/steering', 'pilot/throttle']
        types += ['float', 'float']

    if cfg.HAVE_PERFMON:
        from donkeycar.parts.perfmon import PerfMonitor
        mon = PerfMonitor(cfg)
        perfmon_outputs = ['perf/cpu', 'perf/mem', 'perf/freq']
        inputs += perfmon_outputs
        types += ['float', 'float', 'float']
        V.add(mon, inputs=[], outputs=perfmon_outputs, threaded=True)

    # do we want to store new records into own dir or append to existing
    tub_path = TubHandler(path=cfg.DATA_PATH).create_tub_path() if \
        cfg.AUTO_CREATE_NEW_TUB else cfg.DATA_PATH
    tub_writer = TubWriter(tub_path, inputs=inputs, types=types, metadata=meta)
    V.add(tub_writer, inputs=inputs, outputs=["tub/num_records"], run_condition='recording')

    # Telemetry (we add the same metrics added to the TubHandler
    if cfg.HAVE_MQTT_TELEMETRY:
        telem_inputs, _ = tel.add_step_inputs(inputs, types)
        V.add(tel, inputs=telem_inputs, outputs=["tub/queue_size"], threaded=True)

    if cfg.PUB_CAMERA_IMAGES:
        from donkeycar.parts.network import TCPServeValue
        from donkeycar.parts.image import ImgArrToJpg
        pub = TCPServeValue("camera")
        V.add(ImgArrToJpg(), inputs=['cam/image_array'], outputs=['jpg/bin'])
        V.add(pub, inputs=['jpg/bin'])

    if has_input_controller:
        print("You can now move your controller to drive your car.")
        if isinstance(ctr, JoystickController):
            ctr.set_tub(tub_writer.tub)
            ctr.print_controls()

    if cfg.DONKEY_GYM:
        print("You can now go to http://localhost:%d to drive your car." % cfg.WEB_CONTROL_PORT)
    else:
        print("You can now go to <your hostname.local>:%d to drive your car." % cfg.WEB_CONTROL_PORT)

    #run the vehicle for 20 seconds
    V.start(rate_hz=cfg.DRIVE_LOOP_HZ, max_loop_count=cfg.MAX_LOOPS)

if __name__ == '__main__':
    args = docopt(__doc__)
    cfg = dk.load_config(myconfig=args['--myconfig'])

    if args['drive']:
        model_type = args['--type']
        camera_type = args['--camera']
        drive(cfg, model_path=args['--model'], use_joystick=args['--js'],
              model_type=model_type, camera_type=camera_type,
              meta=args['--meta'])
    elif args['train']:
        print('Use python train.py instead.\n')
