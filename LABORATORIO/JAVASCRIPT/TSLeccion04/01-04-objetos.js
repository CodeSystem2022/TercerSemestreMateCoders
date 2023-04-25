let x = 10; // variable de tipo primitivo

console.log(x.length); //

//objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    // *
    nombreCompleto: function () { 
        return this.nombre + ' ' + this.apellido;
    }
}
console.log(persona.nombre); //
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);

//agregar metodos a los objetos
// *
console.log(persona.nombreCompleto());

//otra forma de crear obj
let persona2 = new Object();
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '654651258';
console.log(persona2.telefono);

//forma de ver el objeto metodo for in
console.log(persona['apellido']);

for(propidad in persona){
    //formas
    console.log(propidad);
    console.log(persona[propidad]);

}
//agregar propiedades a nuestro obj
persona.apellida = 'Betancud'; //cambiamos dinamicamente el valor de un obj
delete persona.apellida;

console.log(persona);

//Distintas formas de imprimir un obj
//Numero 1: la mas sensilla: concatenar cada valor de la propiedad
console.log(persona.nombre+', '+persona.apellido);

//Numero 2: a traves del ciclo for in
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion Object.values()
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: utilizaremos el metodo JESON.stringify
let personaString = JSON.stringify(persona);
console.log(personaString);


