from flask import Flask, request, render_template, jsonify
import os

UPLOAD_FOLDER = './static/upload_images'
FILE_TYPE = set(['jpg', 'png'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        if file.filename == "":
            return render_template('main.html', result_message="ファイルが選択されていません")

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return render_template('main.html', result_message="アップロードが完了しました")

    return render_template('main.html')
    
@app.route('/changed_files')
def changed_files():
    return render_template('changed_files.html')

@app.route('/files_list')
def files_list():
    # 配列初期化
    imagesJson = {}
    # 画像ファイル名を取得（ディレクトリも取得するので注意）
    filenamesList = os.listdir(UPLOAD_FOLDER)
    # FILE_TYPEで指定されている形式のみを抽出
    filenamesList = [i for i in filenamesList if i.rsplit('.', 1)[1].lower() in FILE_TYPE]
    # ファイル数の情報を辞書に追加
    imagesJson["length"] = len(filenamesList)
    # ファイル名を辞書に逐次追加
    for index, f in enumerate(filenamesList):
        imagesJson[str(index)] = f
    return jsonify(imagesJson)
    
if __name__ == "__main__":
    app.run()