function load_data(button, data_id) {
    // if (button.dataset.resolved){
        let div = document.getElementById("content_for_"+data_id);
        let response = fetch("/load/"+data_id)
        .then(response => {
            return response.text()
        })
        .then(html => {
            div.innerHTML = html;
            // button.dataset.resolved = true;
        });
    // }
}


