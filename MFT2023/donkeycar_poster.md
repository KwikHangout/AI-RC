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
<small > FacebookグループのコミュニティURL <br>
<img src="./img/2023-10-03-19-53-51.png" width="100">
</small></div>


# AIでRCカーを走らせよう！ コミュニティ

- **AIカーの魅力と可能性**：AI（人工知能）で自動走行する模型の自動車「AIカー」
- **AIカーの今後の展望**：AIカーをレースのような形で突き詰めることで、自動運転の技術革新につながる可能性を示唆。
- **AI/ロボットの楽しさや教育性**: Generative AIやIoT, メカトロニクスを伝える。

<br>
<div align="center">The next big thing will start out looking like a toy <br> <small>Innovators's Dilemma by Clay Christensen</small></div>


<div align="right">
<small>
<br> AIやIoT・ロボットに取り組む方ならば、<br>誰でも入れるオンライングループです
<br>2023.10.14
</small>
</div>

<div class="colwrap">
<div class="left">
</div>
<div class="right">
</div>

---
<!--_header: 'https://www.mdpi.com/2079-9292/10/17/2102'-->

<div class="colwrap">
<div class="left">
</div>
<div class="right">
</div>
<br>

カメラ、コンピューター、モータ制御
1. 人間が操作して10～15周くらいコース上を走らせます
2. 人間の操作からAIが運転方法を取得(AIの学習モデル構築)
3. カメラの画像からAIが「こんな風景のときは“ステアリング”と“スロットル”こうだったよねと自動走行します。

<img src="./img/2023-08-29-20-14-57.png" width="1200">


---
chatGPTと同じTransformerのAIモデルへと進化中
<img src="./img/2023-08-30-10-43-17.png" width="1200">

---

<img src="./img/2023-08-30-10-42-05.png" width="1200">
