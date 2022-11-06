function load_data(data_id) {
    let div = document.getElementById("content_for_"+data_id);
    let response = fetch("/load/"+data_id)
        .then(response => {
            return response.text()
        })
        .then(html => {
            div.innerHTML = html;
        });
}


