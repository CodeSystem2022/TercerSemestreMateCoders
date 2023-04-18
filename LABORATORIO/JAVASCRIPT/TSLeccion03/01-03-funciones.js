//Hoisting
miFuncion(8,2);

function miFuncion(a,b) {
    //console.log("Sumamos: " +(a + b));
    return a + b;
}
miFuncion(5,4);

let resultado = miFuncion(6,7);
console.log(resultado);

//Declaramos una funcion de tipo exprecion
let x = function (a,b) {return a + b};//necesita cierre con ;
resultado = x(5,6); // al llamarla se pone la variable y parentesis
console.log(resultado);

//funciones que se llaman a si misma
//Funciones de tipo self y invoking
(function (a,b){
    console.log("Ejecutando la funcion: " +(a + b));
})(9,6);

console.log(typeof miFuncion);
function miFuncionDos(a,b) {
    console.log(arguments.length);
    //return a + b;
}
miFuncionDos(5,7);

//toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

//Funciones flecha
const sumarFuncionFlecha = (a,b) => a + b;
resultado = sumarFuncionFlecha(3,7);
console.log(resultado);

//consepto de 
let sumar = function(a,b){
    console.log(arguments[0]);
    console.log(arguments[1]);
    console.log(arguments[2]);
    return a + b+ arguments[2];
}
resultado = sumar(3,2,9);
console.log(resultado);

// sumar todos los argumentos
let respuesta = sumarTodo(5,4,13,10,9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for (let i = 0; i < arguments.length; i++){
        suma += arguments[i];
    }
    return suma;
}

//Tipos primitivos 
//:paso por valor
let k = 10;
// no cambia el valor de k
function cambiarValor(a){
    a = 20;
}
cambiarValor(k);
console.log(k);
//:paso por referencia
// cambia el valor 
const persona = {
    nombre: 'Juan',
    apellido: 'Lepez',
}
console.log(persona);
function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
}
cambiarValorObjeto(persona);
console.log(persona);

