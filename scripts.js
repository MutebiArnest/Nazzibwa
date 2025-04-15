const counter=document.getElementById("counterlabel");
const decrease=document.getElementById("decreasebtn");
const reset=document.getElementById("resetbtn");
const increase=document.getElementById("increasebtn");
let count=0;

increase.onclick=function(){
    count++;
    counter.textContent=count;
}
decrease.onclick=function(){
    count--;
    counter.textContent=count;
}
reset.onclick=function(){
    count=0;
    counter.textContent=count;
}

const button=document.getElementById("mybutton");
const label=document.getElementById("mylabel");
const min=1;
const max=6;
let randomnum;

button.onclick=function(){
    randomnum=Math.floor((Math.random()*max)+min)
    label.textContent=randomnum;
}
//checked property
const myCheckbox=document.getElementById("myCheckbox");
const visa=document.getElementById("visaBtn");
const mastercard=document.getElementById("masterCardBtn");
const paypal=document.getElementById("payPalBtn");
const sad=document.getElementById("mySubmit");
const result=document.getElementById("subResult");
const payment=document.getElementById("paymentResult");

sad.onclick = function(){
    if(myCheckbox.checked){
        result.textContent="You are subscribed";

    }
    else{
        result.textContent="You are not subscribed";
    }

    if(visa.checked){
        payment.textContent="You are paying with visa";
    }
    else if(mastercard.checked){
        payment.textContent="You are paying with master card";

    }else if(paypal.checked){
        payment.textContent="You are paying with paypal";
    }
    else{
        payment.textContent="You must select the payment method"
    }
}

