# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import time

# 画像処理
import cv2

# 監視対象ディレクトリを指定する
target_dir = 'static/upload_images'

# 対象ファイルの文字を認識
def createWordImage(filename):

    pass

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