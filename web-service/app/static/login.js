var userName = document.getElementById("user");
var passWord = document.getElementById("pwd");


function makeLogin() {
    var data = new FormData()
   
    data.append('username',userName.value)
    data.append('password',passWord.value)
    console.log(data);
    fetch("/login", {
        method: "POST",

        body: data
    })
    .then(resp => {
        if (resp.ok) {
            window.location.href = '/';
        }else{
            window.alert("Oops! Something went wrong.");
        }
    })
    .catch(err => {
        console.log("An error occured", err.message);
        window.alert("Oops! Something went wrong.");
    });
    
}