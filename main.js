"use strict";
import './style.css'

let form = document.forms[0];

let input = form.elements.q;

let button = document.getElementById("button")
button.addEventListener("click", sort);
let outputBox = document.querySelector('.outputBox');

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
    array.sort();
    console.log(String(array))
    outputBox.innerHTML = '<p>Sorted Array: ' + array.join(', ') + '</p>';
}

function swap(a, b){
    let tmpA = array[a];
    let tmpB = array[b];

    array[a] = tmpB;
    array[b] = tmpA;
}