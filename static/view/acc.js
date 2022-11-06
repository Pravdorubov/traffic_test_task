document.getElementsByClassName('accordion-button').onclick = function (){
    let data_id = this.data(id);
    let response = async fetch("load/"+data_id);
    let div = document.getElementById("acc_dep_"+data_id);
    div.innerHTML = response.text();
};