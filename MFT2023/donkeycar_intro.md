---
marp: true
theme: default
header: ""
paginate: true
style: |
  section.split {
      overflow: visible;
      display: grid;
      grid-template-columns: 500px 600px;
      grid-template-rows: 30px auto;
      grid-template-areas:
          "slideheading slideheading"
          "leftpanel rightpanel";
  }

  /* debug */
  section.split h3,
  section.split .ldiv,
  section.split .rdiv
  section.split h3 {
      grid-area: slideheading;
  }
  section.split .ldiv { grid-area: leftpanel; }
  section.split .rdiv { grid-area: rightpanel; }
  li { font-size: 20px }
  table { font-size: 20px }
  blockquote {font-size: 16px}

  small{font-size:16px}

---
<style>
div.colwrap {
  background-color: inherit;
  color: inherit;
  width: 100%;
  height: 100%;
}
div.colwrap div h1:first-child, div.colwrap div h2:first-child {
  margin-top: 0px !important;
}
div.colwrap div.left, div.colwrap div.right {
  position: absolute;
  top: 0;
  bottom: 0;
  padding: 70px 35px 70px 70px;
}
div.colwrap div.left {
  position: absolute;
  top:40px;
  right: 50%;
  left: 0;
}
div.colwrap div.right {
  position: absolute;
  top:40px;
  left: 50%;
  right: 0;
}
li { font-size: 20px }

</style>

<div align="right">
<small > https://www.facebook.com/groups/2249059025382644 <br> 2023.08.25</small></div>

# AIでRCカーを走らせよう！MFT2023

>AI(人工知能)でラジコンカーを走らせる Facebookのコミュニティ 2018年からやってます。

<div align="right">
<small>発起人
<br> 遠藤諭 佐々木陽 山本直也
</small>
</div>

<div class="colwrap">
<div class="left">
</div>
<div class="right">
</div>

---
<div class="colwrap">
<div class="left">
New Fabo 1/28 カー

<img src="./img/2023-08-29-19-55-32.png" width="900">
</div>
<div class="right">
1/16 HSP-94186  (ドンキーカー)

<img src="./img/2023-08-29-20-01-00.png" width="600"></div>

---
<!--_header: 'https://www.mdpi.com/2079-9292/10/17/2102'-->

<div class="colwrap">
<div class="left">
</div>
<div class="right">
</div>
<br>
カメラ、コンピューター、モータ制御
<img src="./img/2023-08-29-20-14-57.png" width="1200">



---
<!--_header: 'https://github.com/NVIDIA-AI-IOT/jetracer'-->


<img src="./img/2023-08-29-21-02-49.png" width="1000">

---

<img src="fabo/FaBo_JetRacer_Kit_Red.png" width="1200">

---
chatGPTと同じTransformerのAIモデルへと進化中
<img src="./img/2023-08-30-10-43-17.png" width="1200">

---

<img src="./img/2023-08-30-10-42-05.png" width="1200">

---
ぬりえ

<img src="img/Firefly 20231003155203.png" width="1200">
