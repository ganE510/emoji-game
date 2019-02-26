
function check_register(){
submit_frm(){
            var frm = document.getElementById("userID");
            frm.action = "/onePlayer";
            frm.method = "post";
            frm.submit();
        }
}