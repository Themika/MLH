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
    console.log(array)
    
    for(let i = 0; i < array.length; i++){
        for(let j = 0; j < array.length - 1; j++){
            if(array[j] > array[j+1]){
                swap(j, j + 1);
            }
        }
    }

    console.log(String(array))
}

function swap(a, b){
    let tmpA = array[a];
    let tmpB = array[b];

    array[a] = tmpB;
    array[b] = tmpA;
}