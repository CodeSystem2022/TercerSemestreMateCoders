//Creacion de array
// let autos = new Array('Ferrari','Renault','Bmw'); // esta es la sintaxis vieja

const autos = ['Ferrari','Renault','Bmw']; // esta es la sintaxis que se utiliza actualmente
console.log(autos);

//Recorremos los elementos del array
console.log(autos[0]);
console.log(autos[1]);
console.log(autos[2]);

for (let i = 0; i < autos.length; i++){
    console.log(i+' : '+autos[i]);
}
//Modificar el element del array
autos[1] = 'volvo';
console.log(autos[1]);


//agregar el element al array
autos.push('Audi');
console.log(autos.length);
//Otra forma de agregar el element al array
autos[autos.length] = 'Porche';
console.log(autos);

//Tersera forma de agregar
// hay que tener cuidado con esta forma por que agrega espacios en blanco
// y genera mucho espacio de memoria
autos[3] = 'chevrolet';
console.log(autos);


//Como preguntar si es un array
//primera manera
console.log(Array.isArray(autos)); //booleano
//segunda
console.log(autos instanceof Array); //booleano



