function enrich_data() {
    const csvFile = document.getElementById('csv-file').files[0]
    const formData = new FormData();
    formData.append('textFile', csvFile);
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/update-domain', true);
    xhr.responseType = 'blob';
    // xhr.onload = function (e) {
    //     let blob = e.currentTarget.response;
    //     console.log("blob is", blob)
    //     saveBlob(blob, `${date} newCsv.csv`);
    // }
    xhr.send(formData);
    // let link = 'download'
    // location.replace(link)

}