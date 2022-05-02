const months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
const d = new Date();
let date = d.getDate() + months[d.getMonth()] ;

function filter_data() {
    const csvFile = document.getElementById('csv-file').files[0]
    const formData = new FormData();
    formData.append('textFile', csvFile);
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/filter-people', true);
    xhr.responseType = 'blob';
    xhr.onload = function (e) {
        let blob = e.currentTarget.response;
        console.log("blob is", blob)
        saveBlob(blob, `${date} stateFiltered.csv`);
    }
    xhr.send(formData);
    // let link = 'download'
    // location.replace(link)

}

function saveBlob(blob, fileName) {
    let a = document.createElement('a');
    a.href = window.URL.createObjectURL(blob);
    a.download = fileName;
    a.dispatchEvent(new MouseEvent('click'));
}