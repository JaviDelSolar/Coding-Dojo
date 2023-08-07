console.log("hola");

var username= document.querySelector("#username");

function editar() {
    username.innerText = "Laura Lopez";

}

function rechazar(id) {
    var elemento= document.querySelector(id);
    elemento.remove();
}

var sumar = 2;

var h2 = document.querySelector ("h2");
var Mas = document.querySelector ("Mas");
var countElement = document.querySelector ("#Mas");

function agregar(){
    sumar ++;
    countElement.innerText = sumar;
    console.log(sumar);
}

var restar = 500;

var h2 = document.querySelector ("h2");
var Menos = document.querySelector ("Menos");
var countElement1 = document.querySelector ("#Menos");

function disminuir(){
    restar --;
    countElement1.innerText = restar;
    console.log(restar);
}
