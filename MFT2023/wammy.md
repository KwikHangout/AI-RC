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

# Wammyで AI ラジコンカーをデコレーション

<div align="right">
<small > AIでRCカーを走らせよう！MFT2023<br> 2023.08.25</small></div>

> コクヨ・Wammy（ワミー） https://www.kokuyo-st.co.jp/stationery/wammy/ <br>曲げたり間を通したりして様々なつなぎ方ができ、アイデア次第で多彩なカタチが作れます


---
<div class="colwrap">
<div class="left">
<img src="img/20230903_161922.jpg" width="400">
</div><div class="right">
<img src="img/20230903_161946.jpg" width="400">

---
<div class="colwrap">
<div class="left">
<img src="img/20230903_162010.jpg" width="400">
</div><div class="right">
<img src="img/20230903_162440.jpg" width="400">

---

現在
<div align="center">
<img src="img/20230903_162532.jpg" width="600">
</div>

---
<!--_header: 'https://www.facebook.com/594Wammy'-->

<div class="colwrap">
<div class="left">
<img src="./img/2023-09-03-09-58-58.png" width="600">
</div><div class="right">
<img src="./img/2023-09-03-09-50-35.png" width="600">
</div>

---
<!--_header: 'https://www.facebook.com/594Wammy'-->
<div class="colwrap">
<div class="left">
<img src="./img/2023-09-03-10-02-50.png" width="600">
</div><div class="right">
<img src="./img/2023-09-03-09-54-54.png" width="1000">
</div>

---
<!--_header: 'https://www.facebook.com/594Wammy'-->

<div class="colwrap">
<div class="left">
<img src="./img/2023-09-03-09-59-42.png" width="600">
</div><div class="right">
<img src="./img/2023-09-03-09-58-16.png" width="600">
</div>

---
<!--_header: 'https://www.facebook.com/594Wammy'-->
<div class="colwrap">
<div class="left">
<img src="./img/2023-09-03-09-56-27.png" width="600">
</div><div class="right">
<img src="./img/2023-09-03-10-04-15.png" width="600">
</div>

---
<!--_header: 'https://www.facebook.com/594Wammy'-->

<div class="colwrap">
<div class="left">
<img src="./img/2023-09-03-09-57-08.png" width="600">
</div><div class="right">
<img src="./img/2023-09-03-09-57-36.png" width="600">
</div>

---

<div class="colwrap">
<div class="left">

- https://ameblo.jp/hirosakihanazonohoikuen/entry-11455853923.html

<img src="./img/2023-09-03-10-13-29.png" width="600">
</div><div class="right">

- https://www.kokuyo-st.co.jp/stationery/wammy/for-example/index.html

<img src="./img/2023-09-03-10-14-03.png" width="600">
</div>

----

<div class="colwrap">
<div class="left">

- コクヨ・Wammy（ワミー）
  https://www.youtube.com/watch?v=LJyTFeXtvdY

  <img src="./img/2023-09-03-09-52-49.png" width="400">

</div><div class="right">

- https://www.youtube.com/watch?v=Lh6YT3sxfZQ

  【ワミー】ボールをつくる（5才から） #家で一緒にやってみよう
    https://www.youtube.com/watch?v=G9ed_gU-q6o

  <img src="./img/2023-09-03-09-53-37.png" width="600">

</div>