from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
import datetime

UPLOAD_FOLDER = './static/upload_images'
FILE_TYPE = set(['jpg', 'png', 'jpeg', 'gif'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allwed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPE

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method=='POST':
        time = datetime.datetime.now()
        file = request.files['file']
        # "'%02d' % "ですべてのときに2桁にする
        filename = str(time.year)+str('%02d' % time.month)+str('%02d' % time.day)+str('%02d' % time.hour)+str('%02d' % time.minute)+str('%02d' % time.second)+".jpg"
        cause_message = ""

        if file.filename=="":
            return render_template('main.html', result_message="ファイルが選択されていません")

        if allwed_file(file.filename):
            if(allwed_file(filename)):
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filename = secure_filename(filename)
                result_message = "'{}'を'{}'としてアップロードしました".format(file.filename,filename)
                return render_template('main.html', result_message=result_message, cause_message=cause_message)
        else:
            result_message = "'{}'のアップロードに失敗しました".format(file.filename)
            cause_message = "'.jpg','.png'ファイルのみアップロードできます"
            return render_template('main.html', result_message=result_message, cause_message=cause_message)

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