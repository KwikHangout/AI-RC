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


<div class="colwrap">
<div class="left">

<center>
<img src="./img/AI_RC_CAR_half.png">
<br>since 2018

<br> AIやIoT・ロボットに取り組む方ならば、誰でも入れる Facebookのオンライングループやってます <br>
<img src="./img/2023-10-03-19-53-51.png" width="100"></center>

</div>

<div class="right">

自己紹介

- 山本直也
- 静岡県掛川市在住
- 得意技

  - Solar2D
  - App development extension for Adobe Photoshop
  https://kwiksher.com/
  - Storyboard Editor Plugin For AdobeXD
    https://storyboard.ink/

    <img src="./img/2024-07-28-10-33-13.png" width="300">
    <img src="./img/2024-07-28-10-33-42.png" width="300">

</div>

---
<div class="colwrap">
<div class="left">

- **AIカーの魅力と可能性**：AI（人工知能）で自動走行する模型の自動車「AIカー」
- **AIカーの今後の展望**：AIカーをレースのような形で突き詰めることで、自動運転の技術革新につながる可能性を示唆。
- **AI/ロボットの楽しさや教育性**: Generative AIやIoT, メカトロニクスを伝える。

<br>
<div align="center">The next big thing will start out looking like a toy <br> <small>Innovators's Dilemma by Clay Christensen</small></div>

</div>
<div class="right">
<img src="./img/2024-07-28-10-13-35.png" height="500">
<br>1/16 HSP-94186, Raspberry Pi 3A+
