[Japanese](https://github.com/covao/TatamiRacer/blob/master/README_JP.md) / [English](https://github.com/covao/TatamiRacer/blob/master/README.md)

![TatamiRacerLogo](img/TatamiRacer_LogoM.png)

### ver 2.0

TatamiRacerは、[「タミヤ ミニ四駆」キット](https://www.tamiya.com/english/mini4wd/m4item/m4item.htm)に基づいた小型自動運転車です。約1.8m x 0.9mの1畳のスペースで動作可能です。車はディープラーニングと自動運転制御のために["Donkey Car"](http://docs.donkeycar.com/)ソフトウェアを使用しています。興味深いことに、日本語の「畳」という言葉は、ニューラルネットワークの畳み込み演算も連想させます。

### YouTube

- TatamiRacer

[![](https://img.youtube.com/vi/b-pkVy8e3DA/0.jpg)](https://www.youtube.com/watch?v=b-pkVy8e3DA)

- Maker Faire Tokyo 2022でのTatamiRacer

[![](https://img.youtube.com/vi/s3ll8Y1OPn8/0.jpg)](https://www.youtube.com/watch?v=s3ll8Y1OPn8)

# リリース履歴

### [ver 1.0](https://github.com/covao/TatamiRacer/tree/1.0) 2023-05-28

### [ver 2.0](https://github.com/covao/TatamiRacer)

- 3Dパーツの更新
- モバイルバッテリーのサイズと重量を削減
- Raspberry Pi Zero 2のインストールをサポート

# 部品表（BOM）

| 部品名 | 備考 | 最低構成 | 推奨構成 | Amazon-JP | Amazon-US |
|:---|:---|:---:|:---:|:---:|:---:|
| Raspberry Pi Zero2 W ||+|| [リンク](https://www.amazon.co.jp/dp/B09LH5SBPS/) | [リンク](https://www.amazon.com/dp/B09LH5SBPS) |
| Raspberry Pi 4 |2GB、4GB、または8GB RAMを選択||+| [リンク](https://www.amazon.co.jp/dp/B09GRVDPCX/) | [リンク](https://www.amazon.com/dp/B07TC2BK1X) |
| Raspberry Pi カメラモジュール | v1.3:OV5647(Omnivision)またはv2.1:IMX219Pq3(SONY)|+|+| [v1.3](https://www.amazon.co.jp/dp/B073RCXGQS/), [v2.1](https://www.amazon.co.jp/dp/B01F1SWTZE)| [v1.3](https://www.amazon.com/dp/B07QNSJ32M/),  [v2.1](https://www.amazon.com/dp/B01ER2SKFS)|
| Micro SD カード | 16GB以上|+|+| [e.g. SanDisk](https://www.amazon.co.jp/dp/B0CH2WM7QY/) | [e.g. SanDisk](https://www.amazon.com/dp//B08J4HJ98L) |
| モバイルバッテリー | サイズ:53x85x9.0mm 電圧:5V 電流:最大2.1A |+|+|[Meisei C0303](https://www.amazon.co.jp/dp/B07Q5M3CLQ/) | [Atom Tech Super Slim Power Bank](https://www.amazon.com/dp/B07JZCZSH9/) |
| モータードライバーモジュール| DCモーター用/Hブリッジ|+|+| [L298N ](https://www.amazon.co.jp/dp/B083DT2DMV/) |[L298N ](https://www.amazon.com/dp/B07Y1QJZK3/) |
| ピンヘッダー | オス 90度 / モータードライバー用|+|+| [リンク](https://www.amazon.co.jp/dp/B00V4V703O/) |[リンク](https://www.amazon.com/dp/B0979568B3/) |
| 130 DC モーター | 低速 (<8000 RPM) 低電流(<500mA)|+|+|[TAMIYA](https://www.amazon.co.jp/dp/B005AFBLIA/),[uxcell](https://www.amazon.co.jp/dp/B07CWLWRYJ/) | [uxcell](https://www.amazon.com/dp/B01ERLPVJW) |
| マイクロサーボ |TowerPro SG90(0.1sec/60度)|+|+| [リンク](https://www.amazon.co.jp/dp/B016FKJJ8M/) | [リンク](https://www.amazon.com/dp/B07MLR1498/) |
| タミヤ ミニ四駆 キット |VZシャーシとお好きなボディ。ギア比3.5:1または5:1を選択（推奨5:1ギア）|+|+| [ぞうさん5:1ギア](https://www.amazon.co.jp/dp/B08VX3W3Q6/), [トヨタ ヤリス 3.5:1 ギア](https://www.amazon.co.jp/dp/B08C5FM9HM/), [ホンダ e 3.5:1 ギア](https://www.amazon.co.jp/dp/B08HK7HWCM/), [デュアル リッジ Jr](https://www.amazon.co.jp/dp/B088FK3NC2/) | [ぞうさん5:1ギア](https://www.amazon.com/dp/B08VX3W3Q6/), [トヨタ ヤリス 3.5:1 ギア](https://www.amazon.com/dp/B08C5FM9HM/), [ホンダ e 3.5:1 ギア](https://www.amazon.com/dp/B08HK7HWCM/), [デュアル リッジ Jr](https://www.amazon.com/dp/B088FK3NC2/) |
|タミヤ ギアセット |ギア比を変更する場合（例: 5:1）|||[15516](https://www.amazon.co.jp/dp/B0043RN7W4/)|[15516](https://www.amazon.com/dp/B0043RN7W4/)|
| タミヤ ミニ四駆 ローラーパーツ | スペーサーとM2x10ネジが必要|+|+| [15381](https://www.amazon.co.jp/dp/B001E40PXI/), [95391](https://www.amazon.co.jp/dp/B07F8RLJBQ/),[15435](https://www.amazon.co.jp/dp/B005GJCC9C/)|[15435](https://www.amazon.com/dp/B005GJCC9C/) |
| M2x15またはM2x16 mm ボルト | フロントホイールシャフト用 |+|+| [15508](https://www.amazon.co.jp/dp/B01MXVKDOM/),  [15233](https://www.amazon.co.jp/dp/B001VZE9MS/)| [リンク](https://www.amazon.com/dp/B07YS5ZSZH/) |
| タミヤ ミニ四駆 72mm シャフト | 延長リアシャフト用|+|+| [リンク](https://www.amazon.co.jp/dp/B003GALRS0/) | [リンク](https://www.amazon.com/dp/B002CAO2IC/) |
| ジャンパーケーブル | メスコネクタからメスコネクタ 10cm|+|+| [リンク](https://www.amazon.co.jp/dp/B07MR1SVVR/) | [リンク](https://www.amazon.com/dp/B0742RS6YL) |
| Type-C USB ケーブル（L型ヘッダー） | ショートケーブル15-20cm ||+| [e.g. aceyoon](https://www.amazon.co.jp/dp/B0B4JQ41SW/)| [e.g. aceyoon](https://www.amazon.com/dp/B096VYVR17/) |
| ゲームパッド | USBまたはBluetooth | |+| [F710](https://www.amazon.co.jp/dp/B00CDG7994/), [PS4互換ゲームパッド](https://www.amazon.co.jp/dp/B0C4NW3G8J/)  | [F710](https://www.amazon.com/dp/B0041RR0TW/), [PS4互換ゲームパッド](https://www.amazon.com/dp/B0C4NW3G8J/) |
||  || |  |  |
| 概算コスト（Raspberry Piとmicro SDカードを除く） |  |6,000円 |10,000円 |  |  |

# 3Dプリントパーツ

## 組み立て

[3Dビューアー](3d/tatamiracer_assembly.stl)を参照
<img src="img/TatamiRacer_3D_Assembly.png" alt="" title="" width="640" height="">

## 3Dプリント用キット

[3Dビューアー](3d/tatamiracer_kit.stl)を参照
<img src="img/TatamiRacer_3D_Kit.png" alt="" title="" width="640" height="">

# 回路図

<img src="img/TatamiRacer_Circuit.png" alt="" title="" width="640" height="">

# ボディ

様々な種類のミニ四駆のボディを取り付け可能です。例: [Amazon JP](https://www.amazon.co.jp/s?k=%E3%83%9F%E3%83%8B%E5%9B%9B%E9%A7%86+and+%E3%83%97%E3%83%A9%E3%83%A2%E3%83%87%E3%83%AB+and+%E3%82%B7%E3%83%A3%E3%83%BC%E3%82%B7&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss), [Amazon US](https://www.amazon.com/s?k=tamiya+1%2F32+mini4wd&ref=nb_sb_noss)
<img src="img/Body_Selection.jpg" alt="" title="" width="640" height="">

# 畳サーキットコース

<img src="img/tatami_circuit_150cmx100cm_preview.jpg" alt="" title="" width="640" height="">

## プリントファブリック用画像データ

ファブリック印刷サービスが利用可能
- [畳サーキット 150cmx100cm 200dpi](img/tatami_circuit_150cmx100cm_200dpi.jpg)
- [畳サーキット 110cmx100cm 200dpi](img/tatami_circuit_110cmx100cm_200dpi.jpg)

# [TatamiRacer組み立て手順](doc/Assembly_Instructions.md)

[TatamiRacer組み立て手順](doc/Assembly_Instructions.md)を参照
<img src="img/TatamiRacerBuild.jpg" alt="" title="" width="640" height="">

# [ソフトウェアのセットアップ方法](doc/HowToSetupSoftware.md)

[ソフトウェアのセットアップ方法](doc/HowToSetupSoftware.md)を参照
<img src="img/TatamiRacer_Shortcut.jpg" alt="" title="" width="640" height="">

# [TatamiRacerのキャリブレーション方法](doc/HowToCalibrateTatamiRacer.md)

[TatamiRacerのキャリブレーション方法](doc/HowToCalibrateTatamiRacer.md)を参照
<img src="img/tatamiracer_test.jpg" alt="" title="" width="640" height="">

# [操作方法](doc/HowToGetDriving.md)

[操作方法](doc/HowToGetDriving.md)を参照
<img src="img/DonkeyCopilot.jpg" alt="" title="" width="640" height="">

UI操作画面を見るにはクリックしてください
[Donkey Copilot ブラウザデモ](https://covao.github.io/DonkeyCopilot/copilot.html?demo)

----
## PCBWay

$35=¥5000 (送料 $25)

<img src="./img/2025-07-24-10-00-32.png" width="600" class="popup-image">

## 本体価格

| 製品名 | 価格 | リンク |
|:---|:---|:---|
| Raspberry Pi 4 Model B | ￥9,200 | [商品ページ](https://akizukidenshi.com/catalog/g/g114839/) |
| Raspberry Pi 3 Model A+ | ￥4,620 | [商品ページ](https://akizukidenshi.com/catalog/g/g114878/) |
| Raspberry Pi Zero 2 W | ￥3,190 | [商品ページ](https://akizukidenshi.com/catalog/g/g117398/) |


<img src="./img/2025-07-24-10-28-33.png" width="300" class="popup-image">
¥800

---

## 部品価格一覧

|   | 部品名                                                                                          | 価格    | 備考・リンク                                                                                                                                                                                                                                       |
|:---|:------------------------------------------------------------------------------------------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A | ミニ四駆 キット (ぞうさん5:1ギア)                                                               | ￥1,500 | [Amazon](https://www.amazon.co.jp/dp/B08VX3W3Q6/) <br> <img src="./img/2025-07-24-10-05-45.png" width="400" class="popup-image">                                                                                                                   |
|   | F710                                                                                            | ￥5,200 | [Amazon](https://www.amazon.co.jp/dp/B00CDG7994/?th=1) <br> <img src="./img/2025-07-23-14-14-07.png" width="600" class="popup-image">                                                                                                              |
| A | バッテリー (明誠 C0303 モバイルバッテリー)  <br> <br> ※Type A to Type CのUSBで充電                                                  | ￥1,450 | [Amazon](https://www.amazon.co.jp/dp/B07Q5M3CLQ/?th=1) <br> <img src="./img/2025-07-24-09-56-27.png" width="200" class="popup-image">                                                                                                              |
| A<br>(残2) | TypC- USB L型                                                                                   | ￥1,000 | ショートケーブル15-20cm <br> [e.g. aceyoon](https://www.amazon.co.jp/dp/B0B4JQ41SW/) <img src="./img/2025-07-23-14-12-21.png" width="600" class="popup-image">                                                                                     |
| A | カメラ V2                                                                                       | ￥3,000 | [秋月 商品ページ](https://akizukidenshi.com/catalog/g/g110518/) <br> <a href="https://www.amazon.co.jp/exec/obidos/ASIN/B086MK17K5/beatnix06-22/">Amazon 1500円</a><br> <img src=ω"./img/2025-07-24-09-57-07.png" width="400" class="popup-image"> |
| A<br>(残1)| サーボ (TowerPro SG90)                                                                          | ￥1,200 | TowerPro SG90(0.1sec/60度) <br>  [リンク](https://www.ωamazon.co.jp/dp/B016FKJJ8M/) <br><img src="./img/2025-07-23-13-59-53.png" width="600" class="popup-image">                                                                                  |
| A<br>(残2)| DCモーター用/Hブリッジ L298N                                                                    | ￥700   | [Amazon](https://www.amazon.co.jp/dp/B083DT2DMV/) <br> <img src="./img/2025-07-23-13-57-35.png" width="600" class="popup-image">                                                                                                                   |
|   | ピンヘッダー                                                                                    | ￥700   | オス 90度 / モータードライバー用 <br> 単行 40ポジション 2.54 mmピッチ 2個 <br> [Amazon](https://www.amazon.co.jp/dp/B00V4V703O/) <br> <img src="./img/2025-07-23-13-57-07.png" width="600" class="popup-image">                                    |
|   | ジャンパーケーブル                                                                              | ￥700   | メスコネクタからメスコネクタ 10cm <br> <img src="./img/2025-07-23-14-11-32.png" width="600" class="popup-image">                                                                                                                                   |
| A | タミヤ 130 DC モーター 75028                                                                    | ￥1,400 | タミヤ エレクラフトシリーズ No.28 低回転型130モーター 模型工作用モーター 75028 <br> [Amazon](https://www.amazon.co.jp/dp/B005AFBLIA/) <br> <img src="./img/2025-07-23-13-59-24.png" width="600" class="popup-image">                               |
| Y | タミヤ グレードアップ No.381 GP.381低摩擦プラローラーセット 15381 <br><br>または<br><br>タミヤ ミニ四駆 グレードアップパーツシリーズ 15435 <br>ファーストトライパーツ<br>ローラーパーツ | ¥220 <br> <br>￥600   | スペーサーとM2x10ネジが必要 <br> <img src="./img/2025-07-29-12-52-29.png" width="600" class="popup-image"><br><br> <img src="./img/2025-07-23-14-05-24.png" width="600" class="popup-image">                                                                                                                                         |
| Y | タミヤ ミニ四駆 グレードアップパーツシリーズ <br> ステンレスビスセット                          | ￥300   | M2x15またはM2x16 mm ボルト <br> No.508 GP.508 ステンレスビスセット 15・20・25・30mm 15508 <br> <img src="./img/2025-07-23-14-07-22.png" width="600" class="popup-image">                                                                           |
| Y<br>(残3)| タミヤ ミニ四駆 グレードアップパーツシリーズ <br>72mm シャフト                                  | ￥150   | Tamiya Grade-Up Parts Series Black Reinforced Shaft (4 Pieces), 2.8 inches / 72 mm, GP.417, 15417 <br> [Amazon](https://www.amazon.co.jp/dp/B003GALRS0/) <br> <img src="./img/2025-07-23-14-09-49.png" width="600" class="popup-image">            |


---

**合計部品費（Raspberry Piとmicro SDカードを除く）**
**約 18,000円**

合計

- rapsi (3200~9200円) + SDカード (1000円) + PCBWay 5000円

=> 27400円 ~ 32400円

----

ジャンパーケーブル: ¥700

TypC- USB L型: ¥1,000

F710: ¥5,200

=>
  18000円

---
カメラ　
  V2
  ￥3,000
  https://akizukidenshi.com/catalog/g/g110518/

  ¥1400 RasTech Raspberry Pi Camera Module, Raspberry Pi Camera 5 Megapixels

  >ov5647

  https://www.amazon.co.jp/exec/obidos/ASIN/B086MK17K5/beatnix06-22/

---
バッテリー
  明誠 C0303 モバイルバッテリー 4000mAh
  1450円
  https://www.amazon.co.jp/dp/B07Q5M3CLQ/?th=1

---
DCモーター用/Hブリッジ ⭐️
  L298N
  ¥700
  https://www.amazon.co.jp/dp/B083DT2DMV/



---
ピンヘッダー ⭐️
  ¥700
  オス 90度 / モータードライバー用
  単行 40ポジション 2.54 mmピッチ 2個
  https://www.amazon.co.jp/dp/B00V4V703O/




---
130 DC モーター
  ¥1400
  タミヤ エレクラフトシリーズ No.28 低回転型130モーター 模型工作用モーター 75028
  https://www.amazon.co.jp/dp/B005AFBLIA/



---
サーボ
  ¥1200
  TowerPro SG90(0.1sec/60度)



---
ミニ四駆 キット
  ぞうさん5:1ギア
  ¥1500
  https://www.amazon.co.jp/dp/B08VX3W3Q6/

---
ローラーパーツ
  スペーサーとM2x10ネジが必要
  ¥600


---
タミヤ ミニ四駆 グレードアップパーツシリーズ
  ¥300
  M2x15またはM2x16 mm ボルト
  No.508 GP.508 ステンレスビスセット 15・20・25・30mm 15508


---
タミヤ ミニ四駆 72mm シャフト
  ¥150
  Tamiya Grade-Up Parts Series Black Reinforced Shaft (4 Pieces), 2.8 inches / 72 mm, GP.417, 15417
  https://www.amazon.co.jp/dp/B003GALRS0/



---
ジャンパーケーブル
  ¥700
  メスコネクタからメスコネクタ 10cm


---
TypC- USB L型
  ¥1000
  ショートケーブル15-20cm


---
F710
  ¥5200
  https://www.amazon.co.jp/dp/B00CDG7994/?th=1


<img src="./img/2025-07-24-13-22-32.png" width="600" class="popup-image">

- Shipped with 日本郵便 Tracking ID 421049153162

- [x]raspi
- [x]sdcard
- [x]ピンヘッダー
  どこで使う？
- [x]ジャンパーケーブル (メス)

KAIT QT
- [ ] raspi3A+
- [ ] keeper 18350
- [ ] F710 Faboから借りる

WiFi ルーター
- [ ] Faboから借りる



---

ゆうパケット - Yahoo

- [ ] 679364306611

  <img src="./img/2025-07-26-09-28-17.png" width="600" class="popup-image">

ヤマト from amaozn
- [x] 503-6072152-2431021

  <img src="./img/2025-07-26-09-33-46.png" width="600" class="popup-image">

- [x] 503-9357226-4950233

  <img src="./img/2025-07-26-09-29-21.png" width="600" class="popup-image">

- [x] 503-7522781-5623054

  <img src="./img/2025-07-26-09-30-53.png" width="600" class="popup-image">

- [x] 503-1516758-2159868

  <img src="./img/2025-07-26-09-35-21.png" width="600" class="popup-image">

- [ ] DCモーター用/Hブリッジ
  <img src="./img/2025-07-26-10-02-30.png" width="600" class="popup-image">

---

- [x] ニッパー
- [x] ハンダこて

----
https://www.tamiya.com/japan/cms/mini4wdsettingguide_basic.html

  https://www.youtube.com/watch?v=t5xuVLtgMZA

http://www.miniyonku.net/assemble-miniyonku

----

ミニ四駆「ぞうさん」（正式型番 95569、VZシャーシ）のキットには、**標準のノーマル（標準回転数）タイプの 130φ モーター**が付属しています。これはタミヤの一般的なキットに搭載される「SMC 標準モーター」であり、**Low RPM Type 130** とは異なります ([Tamiya][1])。

* 「Low RPM Type 130」とは、回転数が抑えられたトルク重視の特殊モーターで、標準キットには基本的に採用されていません。
* ぞうさんキットに標準で入っているのは「ノーマルモーター（SMC製）」で、**速度もトルクも中程度のバランス型**です ([ムーチョのミニ四駆ブログ][2], [ミニ四駆マスターズ][3], [Tamiya][1])。

そのため、ご質問の「Low RPM Type 130 ですか？」に対しては、**いいえ**となります。キット付属のモーターは「**Low RPM Type**」ではなく、**標準のノーマルタイプ**です。

もしトルク重視の低速仕様モーターをお探しであれば、例えば「トルクチューン2」などへの交換が可能です。ノーマルより遅めですが、安定したカーブや上り坂での走行に適しています ([ムーチョのミニ四駆ブログ][4])。

---

### ✅ まとめ

| 項目              | キット付属のモーター                 |
| --------------- | -------------------------- |
| モータータイプ         | 標準ノーマル（SMC製 Type 130）      |
| Low RPM Type か？ | **いいえ**                    |
| 性能傾向            | バランス型（中速・中トルク）             |
| トルク重視で低回転が欲しい場合 | 「トルクチューン2 モーター」などへの交換をおすすめ |

ご不明点や他のモーターとの比較などもあれば、お気軽にどうぞ！

[1]: https://www.tamiya.com/japan/products/95569/index.html?utm_source=chatgpt.com "タミヤ ミニ四駆特別企画　ミニ四駆ぞうさん | タミヤ"
[2]: https://www.mini4wd.tech/archives/mini4wd-motor-recommendation-list.html?utm_source=chatgpt.com "〖2025年〗ミニ四駆のおすすめモーターランキング｜種類と選び方も紹介 | ムーチョのミニ四駆ブログ"
[3]: https://mini4-masters.com/mini-yonku-shoshinsha-kaumono-guide/?utm_source=chatgpt.com "ミニ四駆を始める初心者が買うもの全部見せます！予算3000円から楽しめる！速く走らせるコツも‼｜ミニ四駆マスターズ"
[4]: https://www.mini4wd.tech/archives/mini4wd-animalseries-modification.html?utm_source=chatgpt.com "〖ミニ四駆アニマルシリーズ〗ぞうさんのポテンシャル｜簡単な改造パーツで安定した走りに | ムーチョのミニ四駆ブログ"


----

The chip on the board is labeled **MX1508**. This is a different H-bridge driver with different pinouts and capabilities than the L298N.

The MX1508 is a compact, low-cost dual H-bridge motor driver, often used for small DC motors. It can typically handle voltages from 2V to 10V and currents up to 1.5A per channel (2.5A peak).

Let's break down how to connect this **MX1508 module** to your Raspberry Pi and a DC motor, based on the labels visible in your image:

**MX1508 Module Pins and Their Functions:**

  * **+ (VCC):** Power input for the motors. Connect this to the positive terminal of your external DC motor power supply (e.g., 3V to 10V, depending on your motor).
  * **- (GND):** Ground connection for the motor power supply. Connect this to the negative terminal of your external motor power supply AND a GND pin on your Raspberry Pi.
  * **IN1, IN2:** Input control pins for **Motor A**. Connect these to two GPIO pins on your Raspberry Pi.
  * **IN3, IN4:** Input control pins for **Motor B**. Connect these to two other GPIO pins on your Raspberry Pi.
  * **MOTOR-A (or OUT1, OUT2 - based on typical MX1508 layout):** Output terminals for **Motor A**. Connect your first DC motor here.
  * **MOTOR-B (or OUT3, OUT4 - based on typical MX1508 layout):** Output terminals for **Motor B**. Connect your second DC motor here.

**Key Difference from L298N for the MX1508:**

The MX1508 typically **does not have separate enable (ENA/ENB) pins** like the L298N for PWM control. Instead, you usually control the speed by applying a **PWM signal directly to one of the INx pins** while keeping the other INx pin for that motor LOW, or by using a software PWM approach to toggle both INx pins appropriately. For simple on/off and direction control, you just set INx pins HIGH/LOW.

**Wiring Instructions (for one DC Motor, assuming "MOTOR-A" in your diagram refers to the outputs for IN1/IN2):**

1.  **External DC Motor Power Supply:**

      * Connect the **positive (+) terminal** of your external DC motor power supply (e.g., 3V to 6V battery pack, depending on your motor's voltage requirements) to the **'+' terminal** on the MX1508 module.
      * Connect the **negative (-) terminal** of your external DC motor power supply to the **'-' terminal (GND)** on the MX1508 module.

2.  **Raspberry Pi to MX1508 Module (Control Signals):**

      * Connect a **Raspberry Pi GND pin** to the **'-' terminal (GND)** on the MX1508 module. (This creates a common ground for everything).
      * Connect a **Raspberry Pi GPIO pin** (e.g., BCM pin 17) to the **IN1** pin on the MX1508 module.
      * Connect another **Raspberry Pi GPIO pin** (e.g., BCM pin 18) to the **IN2** pin on the MX1508 module.

3.  **DC Motor to MX1508 Module:**

      * Connect one terminal of your DC motor to one of the **MOTOR-A** output screw terminals on the MX1508 module.
      * Connect the other terminal of your DC motor to the other **MOTOR-A** output screw terminal on the MX1508 module.

    *(If you had a second motor, you would use IN3/IN4 and MOTOR-B outputs similarly.)*

**Control Logic (Python using RPi.GPIO for one DC Motor):**

To control the DC motor's direction and speed using the MX1508, you'll manipulate the IN1 and IN2 pins. For speed control, you'll apply PWM to one of the input pins.

```python
import RPi.GPIO as GPIO
from time import sleep

# --- MX1508 (DC Motor) setup ---
# GPIO pin assignments (BCM mode, adjust as needed)
MOTOR_IN1 = 17 # Connect to IN1 on MX1508
MOTOR_IN2 = 18 # Connect to IN2 on MX1508

GPIO.setmode(GPIO.BCM)
GPIO.setup([MOTOR_IN1, MOTOR_IN2], GPIO.OUT)

# For speed control, we'll apply PWM to one of the pins
# For example, to go forward, set IN1 HIGH and apply PWM to IN2 (or vice-versa, depending on desired direction)
# Let's assume applying PWM to IN2 for forward, and IN1 for backward.
PWM_PIN_FOR_SPEED = MOTOR_IN2 # For forward direction
# You might want a dedicated PWM instance if controlling both directions with speed
# Or handle PWM logic within the functions

# Setting up a single PWM instance for one of the IN pins for simplicity in speed control example
# Note: You can also implement software PWM by rapidly toggling the pins, or use hardware PWM if available on your chosen pins.
# For simplicity, we'll use a single PWM for one direction here.
# For the MX1508, typically you hold one INx low and apply PWM to the other INx to control speed.
# Let's set up a PWM on MOTOR_IN2 for forward movement speed.
# You could set up another PWM on MOTOR_IN1 for backward movement speed, or handle it differently.
pwm_motor_speed = GPIO.PWM(PWM_PIN_FOR_SPEED, 100) # 100 Hz frequency
pwm_motor_speed.start(0) # Start with 0% duty cycle (motor off)

def motor_forward(speed):
    """
    Drives the motor forward at a given speed (0-100).
    Here, IN1 is HIGH, IN2 receives PWM.
    """
    GPIO.output(MOTOR_IN1, GPIO.HIGH)
    # The speed is controlled by the duty cycle of IN2
    pwm_motor_speed.ChangeDutyCycle(speed)
    print(f"Motor Forward at {speed}% speed")

def motor_backward(speed):
    """
    Drives the motor backward at a given speed (0-100).
    Here, IN2 is HIGH, IN1 receives PWM.
    NOTE: You would need to reconfigure pwm_motor_speed to MOTOR_IN1 for this to work directly as coded.
    A more robust solution involves toggling the PWM pin or managing two PWM instances.
    For simplicity here, let's just reverse the HIGH/LOW and skip direct PWM on backward for this example.
    To control speed backward, you'd apply PWM to MOTOR_IN1 and keep MOTOR_IN2 HIGH.
    A simpler approach for MX1508 is often just direct digital control for direction, and applying PWM
    to the "active" input.
    Let's refine this to be more common for MX1508:
    """
    GPIO.output(MOTOR_IN2, GPIO.HIGH)
    # To control backward speed, you'd apply PWM to MOTOR_IN1.
    # For this example, let's just set MOTOR_IN1 to a fixed state for direction, no speed control on backward.
    # To properly control speed in both directions with a single PWM instance, you'd need more complex logic
    # or control the PWM duty cycle after setting the direction.
    GPIO.output(MOTOR_IN1, GPIO.LOW) # For fixed backward
    # To control speed backward, you'd actually want something like:
    # pwm_motor_speed.ChangeFrequency(100) # Ensure frequency is set
    # pwm_motor_speed.ChangeDutyCycle(0) # Stop current PWM
    # GPIO.output(MOTOR_IN1, GPIO.LOW) # Set direction
    # GPIO.output(MOTOR_IN2, GPIO.HIGH)
    # pwm_motor_speed.ChangeDutyCycle(speed) # Apply PWM to the correct pin

    # Let's redefine for common MX1508 PWM usage:
    # One pin is HIGH/LOW, the other is PWM.
    # If IN1=HIGH, IN2=PWM_DUTY_CYCLE -> Motor A in one direction, speed controlled by PWM
    # If IN1=PWM_DUTY_CYCLE, IN2=HIGH -> Motor A in other direction, speed controlled by PWM

    # For now, let's simplify to direct control with full speed for backward.
    GPIO.output(MOTOR_IN1, GPIO.LOW)
    GPIO.output(MOTOR_IN2, GPIO.HIGH)
    pwm_motor_speed.ChangeDutyCycle(speed) # If PWM_PIN_FOR_SPEED is IN2, this will still be forward.
                                         # A single PWM is tricky for both directions this way.
                                         # Let's adjust the simple example to only show forward speed.

    print(f"Motor Backward at {speed}% speed (Note: Speed control might be simplified here)")
    # For robust speed control in both directions with MX1508, you usually:
    # 1. Set one IN pin LOW, the other IN pin to PWM.
    # 2. To reverse, set the first IN pin to PWM, the other IN pin LOW.
    # The RPi.GPIO PWM instance is tied to a specific pin.
    # So, you would likely need to stop/start PWM on different pins, or use a library that abstracts this.

    # Simpler approach: set direction, then apply PWM
    # For forward: IN1=HIGH, IN2=PWM(speed)
    # For backward: IN1=PWM(speed), IN2=HIGH
    # This requires dynamically managing which pin the PWM instance is on, or having two PWM instances.

    # Let's revise the functions to handle speed control more realistically for MX1508:
    # We will use one PWM instance and switch which pin is high/low.

def set_motor_speed_and_direction(direction, speed):
    """
    Controls the motor direction and speed (0-100).
    direction: 'forward', 'backward', 'stop'
    """
    if direction == 'forward':
        GPIO.output(MOTOR_IN1, GPIO.HIGH)
        # Apply PWM to IN2 for forward speed
        # Ensure pwm_motor_speed is managing IN2. This is the tricky part with a single PWM object.
        # A more direct way is to set duty cycle and then set the other pin.
        GPIO.output(MOTOR_IN2, GPIO.LOW) # Set IN2 low initially
        # Then, apply PWM to IN2 by toggling it or dynamically changing PWM source
        # For simplicity, we'll use a direct digital approach if no hardware PWM is on *both* pins needed.

        # Let's use software PWM or just simple on/off for basic example given the MX1508.
        # If speed control is needed, you set one pin high and apply PWM to the other.
        # This typically means pwm_motor_speed needs to be associated with MOTOR_IN2 for forward.
        # And if going backward, it needs to be associated with MOTOR_IN1.
        # This implies changing the PWM pin, or having two PWM instances, or managing a single one carefully.

        # For this example, let's just do simple direction control first, then add basic speed later.
        GPIO.output(MOTOR_IN1, GPIO.HIGH)
        GPIO.output(MOTOR_IN2, GPIO.LOW)
        if speed > 0:
            # Simple speed control: cycle between ON/OFF based on speed
            # This is not RPi.GPIO.PWM, but a conceptual software PWM
            # For actual PWM, you'd use pwm_motor_speed.ChangeDutyCycle(speed)
            # but you'd need to ensure pwm_motor_speed is applied to the correct pin.
            # Let's assume you've set pwm_motor_speed on MOTOR_IN2, for forward.
            # And for backward, you'd set it on MOTOR_IN1. This needs re-initialization.

            # Easiest way for MX1508 with speed:
            # Define two PWM objects if you want fine control in both directions
            # OR, use a single PWM object on a specific pin and set the other pin HIGH/LOW
            # and only control speed when that PWM pin is the active one.

            # Revert to the basic on/off and then explain PWM nuance.
            # Basic digital control for MX1508:
            # IN1 | IN2 | Motor Action
            # --- | --- | ------------
            # LOW | LOW | Stop
            # HIGH| LOW | Forward
            # LOW | HIGH| Reverse
            # PWM | LOW | Forward (Speed controlled by PWM)
            # LOW | PWM | Reverse (Speed controlled by PWM)

            # Given this, let's redefine the motor control functions without a global pwm_motor_speed.
            # We will use RPi.GPIO.PWM directly within the functions, or assume a fixed PWM pin.
            # The most flexible way: Use a function that takes 'pin_to_pwm' and 'pin_to_set_low'.
            # But that requires passing the PWM object.

            # Let's use a clear, basic approach for controlling direction, and then integrate a single PWM for one direction.
            # For real bidirectional speed, use pigpio or a more advanced library.

            # Simple forward with speed (PWM on IN2)
            pwm_motor_forward = GPIO.PWM(MOTOR_IN2, 100) # PWM on IN2
            pwm_motor_forward.start(0)
            GPIO.output(MOTOR_IN1, GPIO.HIGH) # Set IN1 high
            pwm_motor_forward.ChangeDutyCycle(speed)
            print(f"Motor Forward at {speed}% speed (PWM on IN2)")
            return pwm_motor_forward # Return PWM object to stop later

    elif direction == 'backward':
        # Simple backward with speed (PWM on IN1)
        pwm_motor_backward = GPIO.PWM(MOTOR_IN1, 100) # PWM on IN1
        pwm_motor_backward.start(0)
        GPIO.output(MOTOR_IN2, GPIO.HIGH) # Set IN2 high
        pwm_motor_backward.ChangeDutyCycle(speed)
        print(f"Motor Backward at {speed}% speed (PWM on IN1)")
        return pwm_motor_backward # Return PWM object to stop later

    elif direction == 'stop':
        GPIO.output(MOTOR_IN1, GPIO.LOW)
        GPIO.output(MOTOR_IN2, GPIO.LOW)
        print("Motor Stopped")
        return None # No PWM object to return

try:
    print("Motor Forward at 70% speed...")
    current_pwm = set_motor_speed_and_direction('forward', 70)
    sleep(2)
    if current_pwm: current_pwm.stop() # Stop previous PWM

    print("Motor Backward at 50% speed...")
    current_pwm = set_motor_speed_and_direction('backward', 50)
    sleep(2)
    if current_pwm: current_pwm.stop() # Stop previous PWM

    set_motor_speed_and_direction('stop', 0)
    sleep(1)

except KeyboardInterrupt:
    pass
finally:
    # Ensure all GPIO pins are set to LOW and cleaned up
    GPIO.output(MOTOR_IN1, GPIO.LOW)
    GPIO.output(MOTOR_IN2, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleanup complete.")
```

**Important Notes for MX1508:**

  * **PWM for Speed:** For the MX1508, to control speed, you typically keep one INx pin HIGH and apply a PWM signal to the other INx pin for that motor. Reversing direction then involves switching which pin receives the PWM and which is held HIGH. The `RPi.GPIO.PWM` object is tied to a specific pin. For bidirectional speed control, you might need to create and stop/start `PWM` objects on different pins, or use a library like `pigpio` which offers more flexible software PWM across all GPIOs. The example above illustrates how to start a new PWM for each direction for clarity.
  * **Voltage:** Ensure your external power supply's voltage matches your DC motor's rated voltage and is within the MX1508's operating range (typically 2V-10V).
  * **Current:** The MX1508 is suitable for small motors. If your DC motor draws significant current (over 1.5A continuous), this module might not be sufficient, and you would need a more powerful driver.
  * **Common Ground:** Always connect the GND of your external motor power supply to a GND pin on your Raspberry Pi.

This setup should allow you to control your DC motors with the MX1508 driver from your Raspberry Pi. Remember to adjust the GPIO pin numbers in the code to match your actual wiring.

----

<img src="./img/2025-07-30-11-09-04.png" width="1600" class="popup-image">

<img src="./img/roller_stopper_spacer.png" width="100" class="popup-image">

<img src="./img/M2_15.png" width="100" class="popup-image">

---

<img src="./img/2025-07-30-12-18-33.png" width="600" class="popup-image">

<img src="./img/2025-07-30-17-11-37.png" width="600" class="popup-image">

----

<img src="./img/2025-07-30-17-12-29.png" width="600" class="popup-image">
<img src="./img/2025-07-30-17-12-44.png" width="600" class="popup-image">

<img src="./img/2025-08-02-12-27-51.png" width="600" class="popup-image">

<img src="./img/2025-07-30-12-42-32.png" width="600" class="popup-image">

----

<img src="./img/2025-07-30-17-09-14.png" width="1600" class="popup-image">

<img src="./img/2025-07-30-17-13-12.png" width="1600" class="popup-image">

横上から滑り入れる

<img src="./img/2025-07-30-18-02-54.png" width="400" class="popup-image">

<img src="./img/2025-07-30-18-45-08.png" width="600" class="popup-image">

<img src="./img/2025-07-30-18-53-19.png" width="600" class="popup-image">

<img src="./img/2025-07-30-19-23-33.png" width="600" class="popup-image">

----

<img src="./img/2025-07-30-19-21-57.png" width="600" class="popup-image">

<img src="./img/M2_10.png" width="600" class="popup-image">

<img src="./img/2025-07-30-19-49-41.png" width="600" class="popup-image">

<img src="./img/2025-07-30-20-03-35.png" width="600" class="popup-image">

----

<img src="./img/2025-07-30-20-15-43.png" width="1600" class="popup-image">

<img src="./img/2025-07-30-20-14-33.png" width="600" class="popup-image">

<img src="./img/2025-07-30-20-26-04.png" width="600" class="popup-image">

<img src="./img/2025-08-02-10-56-24.png" width="1600" class="popup-image">

----

- [x] rapi zero camera cable
- [x] USB micro to A for raspi zero power
- [x] USB micro to A fro F710 donggle

tatamiracerzero.local

BIRDS Coworking×FUKUROI
----

短いUSBケーブル（A-microBタイプ）10cm
https://www.switch-science.com/products/2844

<img src="./img/2025-08-04-10-03-44.png" width="600" class="popup-image">


USBをMicro-Bへ変換するアダプタ
https://www.switch-science.com/products/3702

<img src="./img/2025-08-04-09-59-32.png" width="600" class="popup-image">

  Raspberry Pi 公式OTGケーブル（USB A－microB、8 cm）
  https://www.switch-science.com/products/10310

  <img src="./img/2025-08-04-09-58-48.png" width="600" class="popup-image">

https://www.amazon.co.jp/-/en/RasTech-Raspberry-Camera-Megapixels-ZERO1-3/dp/B086MK17K5

<img src="./img/2025-08-04-10-00-40.png" width="600" class="popup-image">


アマゾン L型 Micro USB 10cm under ¥600
<img src="./img/2025-08-04-10-12-53.png" width="600" class="popup-image">


---

Raspi imager

{{<img src="./img/2025-08-10-14-51-34.png" width="600" class="popup-image">}}

- General

  {{<img src="./img/2025-08-10-14-53-42.png" width="600" class="popup-image">}}

  - hostname: tatamiracer-zero.local
  - username: pi
  - wifi SSID: Your WiFi (2.4GHz)

- Enable SSH : don't make it true

  put `ssh` empty file in boot/ directory of the sd card

  {{<img src="./img/2025-08-10-14-52-53.png" width="600" class="popup-image">}}


  ```
  ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no pi@192.168.68.50
  ```

config.txt

  Before
  ```
  #hdmi_safe=1
  #framebuffer_width=1280
  #framebuffer_height=720
  dtoverlay=vc4-kms-v3d
  ```

  After
  ```
  hdmi_safe=1
  framebuffer_width=1280
  framebuffer_height=720
  #dtoverlay=vc4-kms-v3d
  ```

 wpa_supplicant.conf

 ```
 country=JP
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1
  network={
      ssid="BIRDS Coworking×FUKUROI"
      psk="xxxxx"
  }
  ```

https://docs.donkeycar.com/guide/robot_sbc/setup_raspberry_pi/

Installation for Donkeycar <= 4.5 using Raspberry Pi OS Buster

- [step6](https://docs.donkeycar.com/guide/robot_sbc/setup_raspberry_pi/#step-6-update-and-upgrade)

```
sudo apt-get update --allow-releaseinfo-change
sudo apt-get upgrade
```

```
sudo raspi-config
```
- i2c
- camera
- expand filesystem

Step 8

```
sudo apt-get install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-picamera python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev libgeos-dev git ntp
```

Step 10

```
python3 -m virtualenv -p python3 env --system-site-packages
echo "source ~/env/bin/activate" >> ~/.bashrc
source ~/.bashrc
```

Step 11

```
mkdir projects
cd projects

git clone https://github.com/autorope/donkeycar
cd donkeycar
git fetch --all --tags -f
git checkout 4.5.1
```

⭐️Install opencv-python**

```
pip install opencv-python==4.5.1.48

```

```
pip install -e .[pi]
pip install https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.2.0/tensorflow-2.2.0-cp37-none-linux_armv7l.whl
```

- Check tensorflow version

  ```
  python -c "import tensorflow; print(tensorflow.__version__)"
  ```

  - Fix

    ```
    pip install protobuf==3.20.1
    ```

---

https://github.com/covao/TatamiRacer/blob/master/doc/HowToSetupSoftware.md#install-donkey-car-application-for-raspberry-pi

### VNC

```
sudo apt install realvnc-vnc-server realvnc-vnc-viewer
sudo raspi-config nonint do_vnc 0
```

  - https://www.freva.com/how-to-fix-cannot-currently-show-the-desktop-on-raspberry-pi/

  ```
  echo 'hdmi_force_hotplug=1'>> /boot/config.txt
  echo 'hdmi_group=2'>> /boot/config.txt
  echo 'hdmi_mode=51'>> /boot/config.txt
  ```


  ```
  sudo apt install xserver-xorg lightdm lxde-core lxterminal
  ```

## Create mycar

```
donkey createcar --path ~/mycar
```

[Setup TatamiRacer by Shell Script](https://github.com/covao/TatamiRacer/blob/master/doc/HowToSetupSoftware.md#setup-tatamiracer-by-shell-script)

```
wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/install/setup_tatamiracer.sh" -O "setup_tatamiracer.sh"
sh -x setup_tatamiracer.sh
```

```
arp -a | grep 2c:cf
```

camera


- raspistill

  ```
  vcgencmd get_camera

  sudo raspistill -o image.jpg
  ```

- raspivid

- libcamera-hello

```
sudo apt install libcamera-apps
```

https://zenn.dev/kobayutapon/articles/490d93ab683337

- V1 camera (OV5647)	dtoverlay=ov5647
- V2 camera (IMX219)	dtoverlay=imx219

```
sudo raspi-config nonint do_legacy 0
```

```
hdmi_force_hotplug=1
hdmi_group=2
hdmi_mode=51

[all]
dtoverlay=vc4-fkms-v3d
#dtoverlay=vc4-kms-v3d,nocomposite
#dtoverlay=ov5647
dtoverlay=imx219

## Setup TatamiRacer by Shell Script

wget "https://raw.githubusercontent.com/covao/TatamiRacer/master/raspi/install/setup_tatamiracer.sh" -O "setup_tatamiracer.sh"
sh -x setup_tatamiracer.sh


bullseys
https://zenn.dev/kobayutapon/articles/490d93ab683337


----

前輪とサーボ

{{<img src="./img/2025-08-21-11-15-00.png" width="600" class="popup-image">}}

{{<img src="./img/2025-08-21-11-16-34.png" width="600" class="popup-image">}}

sudo systemctl restart pigpiod