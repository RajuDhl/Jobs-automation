const months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
const d = new Date();
let date = d.getDate() + months[d.getMonth()] ;

function combine_data() {
     const jobsFile = document.getElementById('jobs-file').files[0]
     const emailFile = document.getElementById('email-file').files[0]
    const formData = new FormData();
    formData.append('jobsFile', jobsFile);
    formData.append('emailFile', emailFile);
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/combine-final', true);
    xhr.responseType = 'blob';
    xhr.onload = function (e) {
        let blob = e.currentTarget.response;
        console.log("blob is", blob)
        saveBlob(blob, `${date} finalData.csv`);
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