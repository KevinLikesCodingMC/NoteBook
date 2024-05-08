function upload_edit() {
    document:main_form.submit();
}
function upload_del(name) {
    var r = confirm("Confirm to delete this notebook");
    if (r == true){
       　window.location.href　= '/upload/del/' + name
    }
}