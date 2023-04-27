miFuncion(8, 2); // Esto se conoce como hosting, una función puede ser llamada antes de ser declarada

// Declaración de función
function miFuncion(a, b){
    console.log("sumamos: "+ (a+b));
}

// Llamado de la función
miFuncion(5, 4);

// Palabra return 
function miFuncion2(a, b){
    return a + b;
}

let resultado = miFuncion2(6, 7);
console.log(resultado);

// Declaramos una función de tipo expresión
let x = function (a, b) {return a + b}; // Necesita cierre con ";"
resultado = x(5, 6); // Al llamarla se pone la variable y paréntesis
console.log(resultado);

// Funciones que se llaman a si mismas
// Funciones de tipo self y invoking
(function (a, b){
    console.log("Ejecutando la función: "+(a+b));
})(9,6);

console.log(typeof miFuncion);

function miFuncionDos(a, b) {
    console.log(arguments.length);
    // return a + b;
}
miFuncionDos(5, 7);

// toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

// Funciones flecha
const sumarFuncionFlecha = (a,b) => a + b;
resultado = sumarFuncionFlecha(3,7);
console.log(resultado);

// Concepto de 
let sumar = function(a, b){
    console.log(arguments[0]);
    
}
