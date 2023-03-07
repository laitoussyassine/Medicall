let count = 0
let count2 = 0
let count3 = 0
let count4 = 0
const elem = document.getElementById('clockdiv')
const elem2 = document.getElementById('clockdiv2')
const elem3 = document.getElementById('clockdiv3')
const elem4 = document.getElementById('clockdiv4')
 
let interval = setInterval(() => {
    count++
    
    elem.innerText = count + '+'   

    if(count === 45) {
        clearInterval(interval)
    } 
    
}, 50);


let interval2 = setInterval(() => {
    count2++
    elem2.innerText = count2 + '+' 
    if(count2 === 7) {
        clearInterval(interval2)
    }
}, 50);

let interval3 = setInterval(() => {
    count3++
    elem3.innerText = count3 + '+' 
    if(count3 === 12) {
        clearInterval(interval3)
    }
},50);

let interval4 = setInterval(() => {
    count4++
    elem4.innerText = count4 + '+'
    if(count4 === 42) {
        clearInterval(interval4)
    }
}, 10);