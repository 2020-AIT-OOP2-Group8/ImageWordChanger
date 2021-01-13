fetch(`/files_list`)
    .then(response => {
        console.log(response.status)    // OK(200)//NotFound(400)
        return response.json().then(data => {
            /*
            ex.json == {"length":2, "0":aaa.png, "1":bbb.jpg}
            */

            const baseDiv = document.getElementById('upload_image_list');

            // Jsonで受け取ったlengthの回数を回す
            for (let index = 0; index < data['length']; index++) {
                // 画像のファイル名を取得
                let imgFilename = data[index];
                // div要素を生成
                let newDivElement = document.createElement('div');
                newDivElement.setAttribute('class', 'upload_image_set');
                
                // img要素を生成
                let newImageElement = document.createElement('img');
                newImageElement.setAttribute('class', 'upload_image');
                newImageElement.src = './static/upload_images/' + imgFilename;  // ./static/upload_images/20201215
                newImageElement.alt = '元の画像' + imgFilename;
                let newImageDivElement = document.createElement('div');
                newImageDivElement.setAttribute('class', 'upload_image_box');
                newImageDivElement.appendChild(newImageElement);
                // ファイル名要素を生成
                let newFilenameElement = document.createElement('p');
                // let newFilenameText = document.createTextNode(imgFilename.split('.')[0]);   // 20201215
                let FileNameList= imgFilename.split('');
                let makeDate = FileNameList[0] + FileNameList[1] + FileNameList[2] + FileNameList[3] + '年' + FileNameList[4] + FileNameList[5] + '月' + FileNameList[6] + FileNameList[7] + '日' + FileNameList[8] + FileNameList[9] + '時' + FileNameList[10] + FileNameList[11] + '分';
                let newFilenameText = document.createTextNode(makeDate);   // 20201215

                newFilenameElement.appendChild(newFilenameText);
                newFilenameElement.setAttribute('class', 'upload_name')
                // ダウンロードボタンを生成
                let newDownloadElement = document.createElement('a');
                newDownloadElement.href = './static/output_files/' + imgFilename.split('.')[0] + '.txt';    // ./static/output_files/20201215.txt
                newDownloadElement.setAttribute('download', '');
                let newDownloadText = document.createTextNode('テキストをダウンロード');
                newDownloadElement.appendChild(newDownloadText);
                newDownloadElement.setAttribute('class', 'download_button')

                // 画像1つ分の要素をdivにまとめて親divに追加
                newDivElement.appendChild(newImageDivElement);
                newDivElement.appendChild(newFilenameElement);
                newDivElement.appendChild(newDownloadElement);
                baseDiv.appendChild(newDivElement);
            }
        });
    });