function submit_people_form() {
    const company = document.getElementById('companies').files[0]
    const jobs = document.getElementById('jobs').files[0]
    let number_pages = document.getElementById('number').value;
    let start_pages = document.getElementById('start').value;
    console.log(start_pages, number_pages)
    const formData = new FormData();
    formData.append('companies', company);
    formData.append('jobs', jobs);
    // console.log(formData['companies'])
    let data = {
            'company': company,
            'jobs': jobs
        }
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/uploader', true);
    xhr.send(formData);

}

function deleteMe() {
    let loan = 'loan'
    let status = 'status'
    let r = confirm("Are you sure you want to delete " + loan + "?");
    if (r) {

        let data = {
            'loan': loan,
            'status': status
        }
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/delete-repo', false);
        xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        xhr.send(JSON.stringify(data));
        let msg = 'Deleted ' + loan;
        location.replace(window.location.pathname = "/repo-log?msg=" + msg)
    }

}

