function validatel_login(){

    const email=document.getElementById("email").value;
    const password1=document.getElementById("password1").value;
    let error=false;
    //email number
    if(email ===""){
        document.getElementById("email_error").innerHTML="Enter email number.";
        error=true;
    }
    else{
        document.getElementById("email_error").innerHTML="";
    }

    //Password
    
    if(password1 ===""){
        document.getElementById("password1_error").innerHTML="Empty password field";
        error=true;
    }
    else if(password1.length < 5 || password1.length >8){
        document.getElementById("password1_error").innerHTML="Incorrect password lenght. <br>Enter between 5-8 characters.";
        error=true;
    }
    else if(!password1.match(/[0-9]/)){
        document.getElementById("password1_error").innerHTML="Must contain a digit.";
        error=true;
    }
    else{
        document.getElementById("password1_error").innerHTML="";
    }

    if(error){
        
        return false;
    }
    else{
        alert("Successful")
        return true;
    }

}

function validate_register(){
    console.log("Inside register")
    const name = document.getElementById("name").value;
    console.log(typeof name,name);
    const mobile=document.getElementById("mobile").value;
    const email=document.getElementById("email").value;
    const password1=document.getElementById("password").value;
    const password2=document.getElementById("password2").value;
    let error=false;
    //Name
    if(name === ""){
        document.getElementById("name_error").innerHTML="Name is required.";
        error=true;
    }
    else{
        document.getElementById("name_error").innerHTML="";
    }
    //mobile number
    if(mobile ===""){
        document.getElementById("mobile_error").innerHTML="Enter mobile number.";
        error=true;
    }
    else if(sic.length != 10 || isNaN(sic)){
        document.getElementById("mobile_error").innerHTML="Please Enter a valid 10 digit mobile number.";
        error=true;
    }
    else{
        document.getElementById("mobile_error").innerHTML="";
    }
    //Email
    let atpos=email.indexOf("@");
    let atposs=email.lastIndexOf("@");
    let dotpos=email.lastIndexOf(".");
    if(email === ""){
        document.getElementById("email_error").innerHTML="Email is required.";
        error=true;
    }
    else if(atpos<=0||dotpos<=0||[dotpos-atpos]<=4||dotpos==email.length -1|| atpos!=atposs){
        document.getElementById("email_error").innerHTML="Please Enter a valid Email.";
        error=true;
    }
    else{
        document.getElementById("email_error").innerHTML="";
    }

    //Password
    
    if(password1 ===""){
        document.getElementById("password1_error").innerHTML="Empty password field";
        error=true;
    }
    else if(password1.length < 5 || password1.length >8){
        document.getElementById("password1_error").innerHTML="Incorrect password lenght.<br>Enter 5-8 characters";
        error=true;
    }
    else if(!password1.match(/[0-9]/)){
        document.getElementById("password1_error").innerHTML="Must contain a digit.";
        error=true;
    }
    else{
        document.getElementById("password1_error").innerHTML="";
    }

    // confirm password

    if(password2 ===""){
        document.getElementById("password2_error").innerHTML="Empty password field";
        error=true;
    }
    else if(password2 !== password1){
        document.getElementById("password2_error").innerHTML="Password doesnot match.";
        error=true;
    }
    else{
        document.getElementById("password2_error").innerHTML="";
    }

    if(error){
        
        return false;
    }
    else{
        alert("Successful")
        return true;
    }

}
