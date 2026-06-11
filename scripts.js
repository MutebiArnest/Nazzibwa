//counter program
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

//Random number generator
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
//NUMBER GUESSING GAME
const minnum = 1;
const maxnum = 100;
const answer = Math.floor(Math.random() * (maxnum-minnum+1))+minnum;

let attempts = 0;
let guess;
let running = true;

while(running){
    guess = window.prompt(`Guess a number between ${minnum} - ${maxnum}`);
    guess = Number(guess);
    if(isNaN(guess)){
        window.alert("Please enter a valid number");
    }
    else if(guess < minnum || guess > maxnum){
        window.alert("Please enter a valid number");
    }
    else{
        attempts++;
        if(guess < answer){
            window.alert("TOO LOW! TRY AGAIN");
        }
        else if(guess > answer){
            window.alert("TOO HIGH! TRY AGAIN");
        }
        else{
            window.alert(`CORRECT! The answer was ${answer}. It took you ${attempts} attempts `);
        running = false;
        }
    }
}