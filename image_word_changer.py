# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import time

# OCR機能を吉相するため、sys、pyocrをインポート
import sys
from PIL import Image
import pyocr
import pyocr.builders

# 監視対象ディレクトリを指定する
target_dir = 'static/upload_images'

# 対象ファイルの文字を認識
def createWordImage(filename):

    tools = pyocr.get_available_tools() # 使用可能なOCRツールの数
    if len(tools) == 0:
        print('使用できるOCRツールがありません')
        sys.exit(1)
    tool = tools[0]
    print(f'使用可能なOCRツール: {tool.get_name()}')

    langs = tool.get_available_languages() # 対応可能な言語
    print('対応可能な言語: %s' % ', '.join(langs))
    print(f'対象ファイル名:{filename}')
    print('--------------------------------------------')

    # txtに翻訳した文字を代入
    txt = tool.image_to_string(
        Image.open(f'{target_dir}/{filename}'),
        lang='jpn',
        builder=pyocr.builders.TextBuilder()
    )

    filename = filename.split('.')[0]
    
    # テキストファイルの生成
    f = open(f'static/output_files/{filename}.txt', 'w')
    f.write(txt)
    f.close
    
    print(txt)

    print('--------------------------------------------')
    print('ファイルのアップロードを待機中')

# FileSystemEventHandler の継承クラスを作成
class FileChangeHandler(FileSystemEventHandler):

    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        if(filename != 'upload_images' and filename != '.DS_Store'):
            createWordImage(filename)

    # ファイル変更時のイベント
    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        if(filename != 'upload_images' and filename != '.DS_Store'):
            createWordImage(filename)

# コマンド実行の確認
if __name__ == "__main__":
    # ファイル監視の開始
    print('ファイルのアップロードを待機中', end = '\n')
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, target_dir, recursive=True)
    observer.start()
    # 処理が終了しないようスリープを挟んで無限ループ
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join() 