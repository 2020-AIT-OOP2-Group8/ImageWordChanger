# Image Word Changer
## 画像をテキストファイルに変換するWebサイト
Webサイトから画像をアップロードするだけで、簡単にテキストファイルに変換することができます。

## 動作確認環境
開発時には以下の環境で動作確認を行っています。

- Python      3.8.5
- Flask       1.1.2
- watchdog    0.10.4
- Tessearact  4.1.1

## 導入の仕方
実行にはPython3.xとFlaskとwatchdogとpyocrとTessearactとのインストールとjpn.traineddataの取得が必要です。

### Tessearactのインストール方法
```zsh
$ sudo pip install pyocr
$ brew install tesseract
```
### jpn.traineddataの取得方法

```zsh
$ wget https://github.com/tesseract-ocr/tessdata/raw/4.00/jpn.traineddata
$ mv jpn.traineddata /usr/local/Cellar/tesseract/4.1.1/share/tessdata/
```

このプロジェクトのプログラム自体は、実行可能形式のためインストールの必要はありません。

## 実行方法
以下を実行して[ローカルホストにアクセス](http://localhost:5000)
### ソースファイルのダウンロード
```zsh
$ git clone https://github.com/2020-AIT-OOP2-Group8/ImageWordChanger
```
### 画像処理プログラムの実行
```zsh
$ cd ImageWordChanger
$ python image_word_changer.py
```
### Webサーバの実行
```zsh
$ cd ImageWordChanger
$ python web.py
```

## 制作者
- K19104 宮村一希 : リーダー
- K19009 伊藤聰真 : Webスタイル
- K19059 鈴木楓 : Webトップページ
- K19088 平岩健 : 画像処理・文字認識
- K17033 大谷慎吾 : Web画像一覧表示
