function fileDownload(params) {
    console.log('download now...')
}

fetch(`/files_list`)
    .then(response => {
        console.log(response.status)    // OK(200)//NotFound(400)
        return response.json().then(data => {
            /*
            ex.json == {"length":2, "0":aaa.png, "1":bbb.jpg}
            */

            const baseDiv = document.getElementById('upload_images');

            // Jsonで受け取ったlengthの回数を回す
            for (let index = 0; index < data['length']; index++) {
                // 画像のファイル名を取得
                let imgFilename = data[index];
                // div要素を生成
                let newDivElement = document.createElement('div');
                
                // img要素を生成
                let newImageElement = document.createElement('img');
                newImageElement.setAttribute('class', 'upload_image');
                newImageElement.src = './static/upload_images/' + imgFilename;
                newImageElement.alt = '元の画像' + imgFilename;
                // ファイル名要素を生成
                let newFilenameElement = document.createElement('p');
                let newFilenameText = document.createTextNode(imgFilename);
                newFilenameElement.appendChild(newFilenameText);
                newFilenameElement.setAttribute('class', 'upload_name')
                // ダウンロードボタンを生成
                let newDownloadElement = document.createElement('a');
                newDownloadElement.href = './static/output_files/' + imgFilename + '.txt';
                newDownloadElement.setAttribute('download', '');
                let newDownloadText = document.createTextNode('画像ダウンロード');
                newDownloadElement.appendChild(newDownloadText);
                newDownloadElement.setAttribute('class', 'download_button')

                // 画像1つ分の要素をdivにまとめて親divに追加
                newDivElement.appendChild(newImageElement);
                newDivElement.appendChild(newFilenameElement);
                newDivElement.appendChild(newDownloadElement);
                baseDiv.appendChild(newDivElement);
            }
        });
    });