
function check_register(){
    var name = $("#name").val();
    var pass = $("#password").val();
	var repass = $("#repassword").val();
    var email = $("#email").val();
	
	if(email!="" && name!="" && pass!="" && repass!="" && pass==repass){
		var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$");
		if(!reg.test(email)){
			alert("Invalid email address");
		}else if(pass.length<6){
			alert("password must have more than 6 digits or characters");
		}else{
			alert("success");
			windows.open('gamepage.html');
		}
	 }
	 else{
		 alert("Wrong input, please enter again!");
	 }
}