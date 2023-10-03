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

<div align="right"> 2023.09.25 山本直也 </div>

更新内容 0925

 - ラジコン写真と使用者名
 - 0724の提出のヨコモを追加
 - (参考)申請外のニッケル水素, ニッカドマンガン　搭載の車体も参考に追加

更新内容 0825

1. PS３コントローラの利用は取りやめました。

1. プロポバッテリー FT2F1700BV2
  =>
  FT2F1700B V2 で　2100mAhではなく1700mAhに修正。製品ラベルは 6.4VDC-1700mAhが貼られている。


1. モバイルバッテリー (PD対応)のV数については ラズパイやJetsonの小型コンピュータに供給する5V/3Aを想定しています。


---
Email
* ymmtny@gmail.com

出展者ID
* M0218

---
出展者名
* 「AIでRCカーを走らせよう!」コミュニティ


---
## コントローラ

>作品のロボットはリモコンで操作しますか？>
>リモコンにリチウムイオン電池が使用されている場合はV数、容量、数量を例の通りに記載してください。

```
6.6v2100mAh*1 Turing
6.4v1700mAh*1 FT2F1700B
6.6v1100mAh*1 T7PXR
```

  - ~~PS3 コントローラ 1250mAh 3.7V  x1個~~ (PS3のコントローラは出展を取りやめました)

---
<div class="colwrap">
<div class="left">


  - プロポ用バッテリー

    - Turnigy nano-tech 2100mAh 2S, 6.6V x1個
    - 所有者 Atsushi Urakawa

    <img src="./img/2023-09-25-08-58-12.png" width="500">

</div><div class="right">
      <img src="./img/2023-08-24-18-04-59.png" width="400">
</div>

  ---
<div class="colwrap">
<div class="left">

  - FT2F1700B V2 1700mAh(6.4V) x１個　
  - 所有者 Nagayama Takeo

    > プロポ_FUTABA(FT2F1700BV2 ) BA0140　送信機専用Li-Fe電池FT2F1700BV2 2セル 6.4V [BA0140] - 6,545円 _ SPIRAL - RC CAR SHOP Webストア.pdf

    <img src="./img/2023-09-25-09-06-51.png" width="600">

  </div><div class="right">
  <img src="./img/2023-08-24-18-30-32.png" width="800">
  </div>


  ---

  <div class="colwrap">
<div class="left">


  - プロポ (バッテイリ内蔵)
    - T7PXR(LiFe/6.6V/1100mAh) x１個　

  - 所有者 Mitsuhiro Matsuura
    <img src="./img/2023-09-25-08-59-36.png" width="600">
</div><div class="right">
    <img src="./img/2023-08-24-18-40-09.png" width="600">
</div>


---


コントローラ（プロポ）だけでなく、追加のリチウムイオン電池/LiFeバッテリー、モバイルバッテリの使用予定がありましたので　合わせて記載してございます。

## リチウムポリマー電池
  ```
  7.6v6000mAh*2  Zeee
  6.6v1100mAh*2  Tamiya
  7.4v3800mAh*1 SUNPADOW
  ```

---
<div class="colwrap">
<div class="left">

  - Zeee 7.6V 100C 2S 6000mAhx 2個
  - 所有者 Mitsuhiro Matsuura

  <img src="./img/2023-09-25-08-50-37.png" width="600">
  </div><div class="right">
    <img src="./img/2023-08-25-15-54-40.png" width="300">
    <img src="./img/2023-08-25-15-52-19.png" width="400">
</div>

---
<div class="colwrap">
<div class="left">

  - Tamiya LF1100-6.6V レーシングパック（M） x2個
  - 所有者 Atsushi Urakawa

    <img src="./img/2023-09-25-08-57-41.png" width="200">

  - 所有者 Jiro Hattori

    <img src="./img/2023-09-25-09-19-28.png" width="200">


  </div><div class="right">
    <img src="./img/2023-08-25-15-53-58.png" width="400">
  </div>

---
<div class="colwrap">
<div class="left">

  - SUNPADOW 7.4V / 3800mAh / 130C LiPo Battery x1個
  - 所有者 Nagayama Takeo

      <img src="./img/2023-09-25-09-36-24.png" width="400">


  </div><div class="right">
    <img src="./img/2023-08-25-15-55-31.png" width="300">
    <img src="./img/2023-08-25-15-56-28.png" width="400">
</div>

---
<div class="colwrap">
<div class="left">

  - YB-L400 7.4V / 7.4V 4000mAh/ x1個

  - 所有者 Tsuyoshi Kumazawa

    <img src="./img/2023-09-25-08-49-10.png" width="400">

  </div><div class="right">
  <img src="./img/2023-09-25-08-47-54.png" width="400">

  - https://teamyokomo.com/parts/YB-L400C/
</div>

---
## モバイルバッテリ

  ```
  3.7v5000mAh*1 Novoo
  5v10000mAh*1 INIU
  5v5000mAh*1 POWERADD
  5v6700mAh*1 RAVPower
  5v10000mAh*1 MOXNICE
  5v10000mAh*1 Anker
  ```
---
<div class="colwrap">
<div class="left">

- Novoo PowerCube 5000 mAh x 1個
  - 5V/3A, 9V/2A, 12V/1.5A
  - 5V/2.1A

- 使用者　Hiromi KONDO

  <img src="./img/2023-09-25-08-52-14.png" width="350">

  </div><div class="right">
    <img src="./img/2023-08-24-18-55-46.png" width="600">
</div>

---
<div class="colwrap">
<div class="left">

  - INIU モバイルバッテリー (BI-B3)  5V 10000mAh x1個
    - 5V/3A
  - 所有者 Masato Kawamura
  <img src="./img/2023-09-25-09-00-36.png" width="600">
  </div><div class="right">
      <img src="./img/2023-08-24-19-15-26.png" width="600">
</div>

---
<div class="colwrap">
<div class="left">

  - POWERADD 5000mAh   2.4A   5v x 1個
  - 所有者 Masato Kawamura

    <img src="./img/2023-09-25-09-01-51.png" width="600">

  </div><div class="right">
    <img src="./img/2023-08-24-19-23-04.png" width="600">
</div>

---
<div class="colwrap">
<div class="left">

  - RAVPower 6700mAh モバイルバッテリー (5V/2.4A) x1個
  - 所有者 Masato Kawamura

    <img src="./img/2023-09-25-09-02-22.png" width="600">

  </div><div class="right">
    <img src="./img/2023-08-24-19-32-56.png" width="600">
</div>

---
<div class="colwrap">
<div class="left">

  - MOXNICE 10,000 mAh, PD18W(5v 2.4A)  x 1個
  - 所有者 Nagayama Takeo

    <img src="./img/2023-09-25-09-36-24.png" width="400">


  </div><div class="right">
    <img src="./img/2023-08-24-19-40-04.png" width="200">
    <img src="./img/2023-08-24-19-33-52.png" width="400">
</div>

---
<div class="colwrap">
<div class="left">

  - Anker Power Bank (10,000 mAh, 30 W) x1個
  - 所有者 Nagayama Takeo

    <img src="./img/2023-09-25-09-36-24.png" width="400">


  </div><div class="right">
    <img src="./img/2023-08-24-19-40-42.png" width="200">

    https://www.ankerjapan.com/products/a1256

  - USB-C : 5V⎓3A / 9V⎓3A / 10V⎓2.25A / 12V⎓2.5A / 15V⎓2A / 20V⎓1.5A (単ポート最大 30W)
  - USB-A : 5V⎓3A / 9V⎓2A / 10V⎓2.25A / 12V⎓1.5A (単ポート最大 22.5W)
  - 10000mAh ※モバイルバッテリー本体には5000mAh 7.2Vdc / 36Whで印字されていますが、本製品のセル容量は 10000mAh (2 × 5000mAh) です。

</div>

---
<div class="colwrap">
<div class="left">

## Li-Feﾊﾞｯﾃﾘｰ

- EA550R 550mAh 3.3V x10個

  - 所有者 Akira Sasaki

    <img src="./img/2023-09-25-09-17-16.png" width="600">

  </div><div class="right">
  <img src="./img/2023-08-25-16-00-30.png" width="400">
  </div>

---
<div class="colwrap">
<div class="left">

## (参考) ニッケル水素, ニッカド　製品搭載

> リチウムイオン以外とコンピュータ製品

  ニッケル水素

  - 所有者 Seiji Komiya
  7.2V 3800mAh 2個セット タミヤラジコン対応ニッケル水素バッテリー

  <img src="./img/2023-09-25-09-50-04.png" width="400">

  </div><div class="right">

  - 所有者 Tasuku Hori

    <img src="./img/2023-09-25-09-42-57.png" height="250">

    > [Raspberry Pi 4 ](https://www.amazon.co.jp/Raspberry-%E3%83%90%E3%83%83%E3%83%86%E3%83%AA%E3%83%BC%E3%83%91%E3%83%83%E3%82%AF-UPS%E3%80%81RPI-10000mAh-%E6%9C%80%E6%96%B0%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3/dp/B07Y213F8S/ref=sr_1_3?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=JS0NGSOM2KBC&keywords=raspberry+pi+4+%E3%83%90%E3%83%83%E3%83%86%E3%83%AA%E3%83%BC%E3%83%91%E3%83%83%E3%82%AF+up&qid=1693194435&s=computers&sprefix=raspberry+pi+4+%E3%83%90%E3%83%83%E3%83%86%E3%83%AA%E3%83%BC%E3%83%91%E3%83%83%E3%82%AF+ups%2Ccomputers%2C177&sr=1-3)

  - ニッカドマンガン (ドンキーカ)

    <img src="./img/2023-09-25-09-51-42.png" width="300">

　</div>