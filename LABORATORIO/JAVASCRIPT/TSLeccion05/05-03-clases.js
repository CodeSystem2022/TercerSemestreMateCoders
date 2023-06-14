//Clases: Creamos una clase y luego objetos de esta clase
//Una clase es una plantilla, en esta definimos los atributos y metodos que queremos que contengan nuestros objetos
//A partir de las clases creadas podemos crear instancias (objetos) y cada uno de estos va a tener sus propios valores para los mismos atributos.

//let persona3 = new Persona("Carla", "Ponce"); //Esto no se puede hacer, primero se debe inicializar la clase

class Persona{  //Clase padre
    static contadorPersonas = 0;
    //static contadorObjetosPersona = 0; //Atributo statico
    //email = 'Valor dafault email'; //Atributo NO statico

    static get MAX_OBJ(){// ESTE METODO SIMULA UNA CONSTANTE
        return 5;
    }
    constructor(nombre, apellido){
        this._nombre = nombre; //Atributo
        this._apellido = apellido; //Atributo
        if(Persona.contadorPersonas< Persona.MAX_OBJ){
            this.idpersona = ++Persona.contadorPersonas;
        }
        else{
            console.log('Se ah superado el maximo de objetos permitidos')
        }
        //Persona.contadorObjetosPersona++;
        //this.idpersona = ++Persona.contadorPersonas
        //console.log('Se incrementa el contador: '+Persona.contadorObjetosPersona);
    }

    //Metodo get
    get nombre(){
        return this._nombre;
    }
    get apellido(){
        return this._apellido;
    }

    //Metodo set
    set nombre(nombre){
        this._nombre = nombre;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    // Metodo nombreCompleto
    nombreCompleto(){
        return this.idpersona+' '+this._nombre+' '+this._apellido;
    }

    // Sobre escribimos el método de la clase padre (Object)
    toString(){ // Regresa un String
        // Se aplica el polimorfismo que significa = multiples formas en tiempo de ejecución
        // El método que se ejecuta depende si una referencia de tipo padre o hija
        return this.nombreCompleto();
    }

    static saludar(){
        console.log("saludo desde este metodo static");
    }
    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido);
    }
}

class Empleado extends Persona{  //Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);  //Debemos pasar los parametros de la clase padre
        this._departamento = departamento;
    }

    //Metodo get
    get departamento(){
        return this._departamento;
    }

    //Metodo set
    set departamento(departamento){
        this._departamento = departamento
    }

    // Sobre escritura del método de la clase padre
    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento
    }
}

//Objeto 1:
let persona1 = new Persona("Martin", "Perez");
console.log(persona1.nombre);  //Con el get mostramos el nombre
persona1.nombre = "Juan Carlos"; //Con el set cambiamos el nombre
console.log(persona1.nombre);  //Volvemos a mostrar nombre con el get
console.log(persona1.apellido); //Mostramos apellido con el get
persona1.apellido = "Testa"; //Cambiamos apellido con el set
console.log(persona1.apellido); //Volvemos a mostrar apellido con el get
//console.log(persona1);


//Objeto 2:
let persona2 = new Persona("Carlos", "Lara");
console.log(persona2.nombre);
persona2.nombre = "Maria Laura";
console.log(persona2.nombre);
console.log(persona2.apellido);
persona2.apellido = "Pichi";
console.log(persona2.apellido);
//console.log(persona2);

//Metodo get (para poder leer la informacion de los atributos) y set (para modificarlo)


//Hoisting y clases
//No se puede crear un objeto antes de inicializar la clase!!

//Creamos un objeto de la clase hija
let empleado1 = new Empleado("Gabriel", "Romero", "Gerencia");
console.log(empleado1);
console.log(empleado1.nombre);  //El nombre se esta heredando de la clase padre

// accedemos al metodo heredado de la clase padre
console.log(empleado1.nombreCompleto());

//Object.prototype.toString; // Esta es la manera de acceder a métodos y atributos de forma dinámica
console.log(empleado1.toString())
console.log(persona1.toString())


//metodo static
//no se puede utilizar desde el objeto sino de la clase misma
//persona1.saludar();
Persona.saludar(); // SE MUESTRA ATRAVES DE METODO o en la consola
Persona.saludar2(persona1);// SE MUESTRA ATRAVES DE METODO o en la consola

Empleado.saludar();
Empleado.saludar2(empleado1);

//no se debe acceder atrades del objeto sino de la clase
//console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona);

//atributos no estaticos
console.log(persona1.email);
console.log(empleado1.email);
//No se puede acceder desde la clase
//console.log(Persona.email); // por que no es estatico


console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);

let persona3 = new Persona('Martin','Torres');
console.log(persona3.toString());
console.log(Persona.contadorPersonas);

//creacion de constantes staticas
// no se puede utilicar la palabra const
console.log(Persona.MAX_OBJ);
Persona.MAX_OBJ = 10;// NO SE PUEDE MODIFICAR NI ALTERAR
console.log(Persona.MAX_OBJ);

let pesona4 = new Persona('Franco','Diaz');
console.log(pesona4.toString());

let pesona5 = new Persona('liliana','paz');
console.log(pesona5.toString());
