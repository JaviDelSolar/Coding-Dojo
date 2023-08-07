console.log("correcto"); 

/* Remover donate*/

function ocultarBoton(elemento) {
    elemento.remove();
}

/* Alerta al seleccionar una mascota*/

function alertaclick(){
    var elementoSeleccionado = document.getElementById("anyPet");
    var animalSeleccionado = elementoSeleccionado.value;
    if (animalSeleccionado !== "") {
        alert("Your are loooking of a: " + animalSeleccionado);
    }
}

/* Sumar Petting*/

var pettingcount = 3;

var h2 = document.querySelector ("h2");
var count = document.querySelector ("count");
var countElement = document.querySelector ("#count");

function agregar(){
    pettingcount ++;
    countElement.innerText = pettingcount + " petting (s)";
    console.log(pettingcount);
}

var pettingcount1 = 5;

var h2 = document.querySelector ("h2");
var count1 = document.querySelector ("count1");
var countElement1 = document.querySelector ("#count1");

function agregar1(){
    pettingcount1 ++;
    countElement1.innerText = pettingcount1 + " petting (s)";
    console.log(pettingcount1);
}

var pettingcount2 = 8;

var h2 = document.querySelector ("h2");
var count2 = document.querySelector ("count2");
var countElement2 = document.querySelector ("#count2");

function agregar2(){
    pettingcount2 ++;
    countElement2.innerText = pettingcount2 + " petting (s)";
    console.log(pettingcount2);
}