const months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
const d = new Date();
let date = d.getDate() + months[d.getMonth()] ;


function convert_text_to_csv() {
    const textFile = document.getElementById('text-file').files[0]
    const formData = new FormData();
    formData.append('textFile', textFile);
    let site = document.querySelector('input[name="source"]:checked').value;
    let logged_in = 'false'
    try {
        logged_in =  document.querySelector('input[name="logged-on"]:checked').value;
    }
    catch {
        logged_in =  'false'
    }

    formData.append('site', site)
    formData.append('logged_in', logged_in)
    console.log(formData)
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/text-csv', true);
    xhr.responseType = 'blob';
    xhr.onload = function (e) {
        let blob = e.currentTarget.response;
        console.log("blob is", blob)
        saveBlob(blob, `${date} text2csv.csv`);
    }
    xhr.send(formData);
    let link = 'download'
    // location.replace(link)

}

function more_options(type) {
    document.getElementById('linkedin-extra').style.display = type;
    if (type === 'none'){
        document.getElementById('logged-on-true').checked = false
        document.getElementById('logged-on-false').checked = false
    }
}


function saveBlob(blob, fileName) {
    let a = document.createElement('a');
    a.href = window.URL.createObjectURL(blob);
    a.download = fileName;
    a.dispatchEvent(new MouseEvent('click'));
}