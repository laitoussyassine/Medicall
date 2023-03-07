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

    if(count === 120) {
        clearInterval(interval)
    } 
    
}, 50);


let interval2 = setInterval(() => {
    count2++
    elem2.innerText = count2 + '+' 
    if(count2 === 142) {
        clearInterval(interval2)
    }
}, 50);

let interval3 = setInterval(() => {
    count3++
    elem3.innerText = count3 + '+' 
    if(count3 === 112) {
        clearInterval(interval3)
    }
},50);

let interval4 = setInterval(() => {
    count4++
    elem4.innerText = count4 + '+'
    if(count4 === 842) {
        clearInterval(interval4)
    }
}, 10);



$(document).ready(function () {
    $(".customer-logos").slick({
      slidesToShow: 6,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 2000,
      arrows: false,
      dots: false,
      pauseOnHover: true,
      responsive: [
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 4
          }
        },
        {
          breakpoint: 520,
          settings: {
            slidesToShow: 3
          }
        }
      ]
    });
  });
  