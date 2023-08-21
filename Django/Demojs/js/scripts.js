function check(a){
//     if(a>0){
//         console.log("so duong");
//     }else{
//         console.log("so am");
//     }
//     for(let i = 0;i<=a;i++){
//         console.log(i);
//     }
//     // mang
//     let arr = [1,2,3,4,5];
//     console.log(arr[0]);
    let user = document.getElementById("user").value;
    let pass = document.getElementById("pass").value;
    let loi_user = document.getElementById("loi_user");
    if(user.length == 0){
        loi_user.innerHTML = "khong de trong user";
        loi_user.setAttribute("style","color:red;");
    }else{
        loi_user.setAttribute("style","color:white;");
    }

}

function check2(){
    let pass = document.getElementById("pass").value;
    let loi_pass = document.getElementById("loi_pass");
    if(pass.length == 0){
        loi_pass.innerHTML ="ko de trong"
        loi_pass.setAttribute("style","color:red;");

    }else{
        loi_pass.setAttribute("style","color:white;");
    }
}
$(document).ready(function(){

    $("#xoa").click(function(){
        $("#user").val("");
        $("#pass").val("");
        $("#xoa").css("background","red");
        alert("hello ddsggsd")
    });
});