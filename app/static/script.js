var clk = 0;
var clk2 = 0;
if(window.location.href == "http://127.0.0.1:5000/VcStart"){
    window.location.href = "http://127.0.0.1:5000/";
    console.log(1);
}
function calcBmi(){
    console.log("Hello")
    var ele = document.getElementById("BMI-calc")
    if(ele.style.visibility == "hidden"){
        ele.style.visibility = "visible";
        document.getElementById("bmi-but").innerHTML = "Enter";
        clk = 1;
    }
    else if(ele.style.visibility == "visible" || clk == 1){
        ele.style.visibility = "hidden";
        clk = 0;
        var bmi = 0;
        var str = "";
        var h = document.getElementById("hght").value;
        var w = document.getElementById("wght").value;
        bmi = ((w/h)/h)*10000;
        bmi = bmi.toFixed(1);
        if(isNaN(bmi)){
            bmi = 0;
        }
        if(bmi <= 18.5){
            str = " \n(Underweight)";
        }
        else if(bmi > 18.5 && bmi <= 24.9){
            str = " \n(Normal Weight)";
        }
        else if(bmi > 24.9 && bmi <= 29.9){
            str = " \n(Overweight)";
        }
        else{
            str = " \n(Obesity)";
        }
        document.getElementById("bmi-but").innerHTML = bmi + str;
    }
}
//function AiToggle(){
//    let ai = document.getElementById("AiAssist");
//    if(clk2 == 0){
//        clk2 = 1;
//        ai.href = "{{ url_for('killVoice') }}";
//    }
//    else if(clk2 == 1){
//        clk2 = 0;
//        ai.href = "{{ url_for('voice') }}";
//    }
//    console.log(clk2);
//}