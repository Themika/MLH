"use strict";
import './style.css'

let form = document.forms[0];

let input = form.elements.q;

let button = document.getElementById("button")
button.addEventListener("click", sort);

let array = Array();

function sort(){
    let tmp = input.value.split(",");
    let array = tmp.map(function(str){
        return parseInt(str);
    });
    
    for(let i = 0; i < array.length; i++){
        for(let j = 0; j < array.length - 1; j++){
            if(array[j] > array[j+1]){
                let tmpA = array[j];
                let tmpB = array[j+1];
                array[j] = tmpB;
                array[j+1] = tmpA;
            }
        }
    }
    
    console.log(String(array))
}