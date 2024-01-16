#!/usr/bin/env python
# coding: utf-8

# In[10]:


from IPython.display import display, clear_output
import ipywidgets as widgets
import os
import asyncio
import sys
import subprocess

cmd_wc="ls -l ../mycar/data/images|wc -l"
cmd_del="cd ../mycar;rm -rf ./data/*"
cmd_run="cd ../mycar;python manage.py drive --js"
cmd_train="cd ../mycar;donkey train --tub ./data --model ./models/mypilot.h5"
cmd_autopilot="cd ../mycar;python manage.py drive --js --model ./models/mypilot.h5"

#cmd_run="cd ../mycar; source ./run_car.sh"

output =  widgets.Output()
current_proc = 0

# https://qiita.com/megmogmog1965/items/091aa0304017d775bc1e
def run_and_capture(cmd):
    '''
    :param cmd: str 実行するコマンド.
    :rtype: str
    :return: 標準出力.
    '''
    # ここでプロセスが (非同期に) 開始する.
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.pid)
    buf = []
    current_proc = proc

    while True:
        # バッファから1行読み込む.
        line = proc.stdout.readline()
        buf.append(line)
        sys.stdout.write(line)

        # バッファが空 + プロセス終了.
        if not line and proc.poll() is not None:
            break

    return b''.join(buf)

### wc -l
def clicked_wc(arg):
    #clear_output(True)
    #print("button has been clicked!")
    with output:
        #output.clear_output()  # 前のクリック時の出力を消す
        print(cmd_wc) 
        print(os.popen(cmd_wc).read())

button_wc = widgets.Button(description = 'images count')   
button_wc.on_click(clicked_wc)

### del
def clicked_del(arg):
    #clear_output(True)
    #print("button has been clicked!")
    with output:
        #output.clear_output()  # 前のクリック時の出力を消す
        print(cmd_wc) 
        print(os.popen(cmd_del).read())

button_del = widgets.Button(description = 'del data')   
button_del.on_click(clicked_del)


### run car
def clicked_run(arg):
    with output:
        output.clear_output()  # 前のクリック時の出力を消す
        print(cmd_run) 
        #print(os.popen(cmd_run).read())
        msg = run_and_capture(cmd_run)
        print(msg)


button_run = widgets.Button(description = 'run car')   
button_run.on_click(clicked_run)

### train 
def clicked_train(arg):
    with output:
        output.clear_output()  # 前のクリック時の出力を消す
        print(cmd_train) 
        #print(os.popen(cmd_train).read())
        msg = run_and_capture(cmd_train)


button_train = widgets.Button(description = 'train car')   
button_train.on_click(clicked_train)

### auto pilot
def clicked_autopilot(arg):
    with output:
        output.clear_output()  # 前のクリック時の出力を消す
        print(cmd_train) 
        #print(os.popen(cmd_train).read())
        msg = run_and_capture(cmd_autopilot)


button_autopilot = widgets.Button(description = 'run AI')   
button_autopilot.on_click(clicked_autopilot)

display(button_wc,button_del, button_run, button_train, button_autopilot, output)


# In[ ]:




