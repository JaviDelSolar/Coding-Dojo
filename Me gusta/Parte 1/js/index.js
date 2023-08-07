console.log("hola");

var likecount = 3

var h2 = document.querySelector ("h2");
var count = document.querySelector ("count");
var countElement = document.querySelector ("#count");



function agregar(){
    likecount ++;
    countElement.innerText = likecount + " likes (s)";
    console.log(likecount);
}
