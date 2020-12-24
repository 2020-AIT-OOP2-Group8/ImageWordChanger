var dropArea = document.getElementById('dropArea');

var inputFile = document.getElementById('file_select');

dropArea.addEventListener('dragover', function(e){
    e.stopPropagation();
    e.preventDefault();
    dropArea.classList.add('dragover');
    this.style.background = '#a9a9a9';
});

dropArea.addEventListener('dragleave', function(e){
    e.stopPropagation();
    e.preventDefault();
    dropArea.classList.remove('dragover');
    this.style.background = '#ffffff';
});

dropArea.addEventListener('drop', function(e){
    e.stopPropagation();
    e.preventDefault();
    dropArea.classList.remove('dragover');
    this.style.background = '#ffffff';

    var files = e.dataTransfer.files;

    inputFile.files = files;
});