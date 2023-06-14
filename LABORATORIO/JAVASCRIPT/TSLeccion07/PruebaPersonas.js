class Persona{
    static contadorPersonas = 0;

    constructor(nombre, apellido, edad) {
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }
    get idPersona() {
        return this._idPersona;
    }

    get nombre() {
        this._nombre;
    }
    set nombre(nombre) {
        this._nombre = nombre;
    }
    get apellido() {
        this._apellido;
    }
    set apellido(apellido) {
        this._apellido = apellido;
    }
    get edad() {
        this._edad;
    }
    set edad(edad) {
        this._edad = edad;
    }
    toString() {
        return `${this._idPersona} ${this._nombre} ${this._apellido} ${this._edad}`;
    }

}
class Empleado extends Persona{
    static contadorEmpleado = 0;

    constructor( nombre, apellido, edad, sueldo){
        super(nombre, apellido, edad);
        this._idEmpleado = ++Empleado.contadorEmpleado;
        this._sueldo = sueldo;
    }
    get idEmpleado(){
        this._idEmpleado;
    }
    get sueldo(){
        this._sueldo;
    }
    set sueldo(sueldo){
        this._sueldo = sueldo;
    }
    toString(){
        return `${super.toString()} ${this._idEmpleado} ${this._sueldo}`;
    }

}
class Cliente extends Persona{
    static contadorClientes = 0;

    constructor( nombre, apellido, edad, fecharegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fecharegistro = fecharegistro;
    }
    get idCliente(){
        this._idCliente;
    }
    get fecharegistro(){
        this._fecharegistro;
    }
    set fecharegistro(fecharegistro){
        this._fecharegistro = fecharegistro;
    }
    toString(){
        return `${super.toString()} ${this._idCliente}${this._fecharegistro}`;
    }
}

//Prueba clase persona
let persona1 = new Persona('Juan', 'Perez', 32);
console.log(persona1.toString());

let persona2 = new Persona('Carla', 'Ortega', 22);
console.log(persona2.toString());

//Prueba clase empleado
let empleado1 = new Empleado('Pedro', 'Roman', 32, 5000);
console.log(empleado1.toString());

let empleado2 = new Empleado('Jonas', 'Torres', 30, 7000);
console.log(empleado2.toString());

//Prueba clase cliente
let cliente1 = new Cliente('Pedro', 'Roman', 32, new Date());
console.log(cliente1.toString());

let cliente2 = new Cliente('Martin', 'Torres', 31, new Date());
console.log(cliente2.toString());


