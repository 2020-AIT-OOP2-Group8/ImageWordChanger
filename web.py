from flask import Flask, request, render_template, jsonify
import os

UPLOAD_FOLDER = './static/upload_images'

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

if __name__ == "__main__":
    app.run()