var content = document.getElementById("content");
content.innerText='happy';
$.ajax({
        url: "oneplayerCont",
        type: "POST",
        dataType: "json",
//        data:data,
        success: function (data) {
            console.log(data)
        }
})

function showRes() {
    userAns = document.getElementById("textarea").value;
    var info1 = document.getElementById("info1");
    info1.innerText = "Your sequence is "+ userAns;
    var data = userAns ;
    var x=100
    if (userAns == data ){
        var info2 = document.getElementById("info2");
        info1.innerText = "Your sequence is "+ x +"% similar with computer's";
    }
}

function nextCont() {
    var content = document.getElementById("content");
    content.innerText = "war";
    if(content=="war"){
        content.innerText = "passage";
    }else if(content=="passage"){
        content.innerText = "headache";
    }else{
        content.innerText = "shadow";
    }
    data='next'
    $.ajax({
        url: "oneplayerRes",
        type: "POST",
        dataType: "json",
        data:data,
        success: function (data) {
            console.log(data)
        }
    })
}