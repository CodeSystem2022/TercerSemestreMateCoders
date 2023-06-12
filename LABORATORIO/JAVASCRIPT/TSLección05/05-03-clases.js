//Clases: Creamos una clase y luego objetos de esta clase
//Una clase es una plantilla, en esta definimos los atributos y metodos que queremos que contengan nuestros objetos
//A partir de las clases creadas podemos crear instancias (objetos) y cada uno de estos va a tener sus propios valores para los mismos atributos.

//let persona3 = new Persona("Carla", "Ponce"); //Esto no se puede hacer, primero se debe inicializar la clase

class Persona{  //Clase padre

    //Definimos un atributo estatico que va a pertenecer a la clase y no al objeto
    static contadorPersonas = 0;
    //Definimos un atributo NO estatico
    //email = "Valor default email";

    //Creamos el metodo que simula la constante estatica
    static get MAX_OBJ(){
        return 5;
    }

    
    constructor(nombre, apellido){
        this._nombre = nombre; //Atributo
        this._apellido = apellido; //Atributo
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
            this.idPersona = ++Persona.contadorPersonas;

        }
        else{
            console.log("Se ha superado el maximo de objetos permitidos");
        }
        //Persona.contadorObjetosPersona++;
        //console.log("Se incrementa el contador: "+Persona.contadorObjetosPersona);
        
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

    //Metodo definido en la clase padre
    nombreCompleto(){
        return this.idPersona+" "+this._nombre+" "+this._apellido;
    }

    //Sobreescribiendo el metodo de la clase padre (Object)
    //Metodo toString (este me regresa un string)
    toString(){
        //Se aplica el polimorfismo que significa = multiples formas en tiempo de ejecucion
        //El metodo que se ejecuta depende si es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }

    //Agregamos el metodo static (este se va asociar a la clase y no a los objetos)
    static saludar(){
        console.log("Saludos desde este metodo static");
    }

    static saludar2(persona){
        console.log(persona.nombre+" "+persona.apellido);
    }
}

class Empleado extends Persona{  //Clase hija de la clase persona (si o si debemos agregar el extends). Hace una extencion de la clase object o padre
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

    //Sobreescritura (modificar el comportamiento de un metodo definido en la clase padre)
    nombreCompleto(){
        return super.nombreCompleto()+", "+this._departamento;
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

//Objeto 3: Creamos un objeto de la clase hija
let empleado1 = new Empleado("Gabriel", "Romero", "Gerencia");
console.log(empleado1);
console.log(empleado1.nombreCompleto());  //El nombre se esta heredando de la clase padre


//Metodo toString
//Object.prototype.toString //Esta es la manera de acceder a atributos y metodos de manera dinamica
console.log(empleado1.toString()); //Como vemos el metodo to string (heredado de la clase padre) retorna el metodo nombreCompleto de la clase hija
// por ello tamb nos devuelve ademas del nombre y apellido, el departamento. Esto se debe a que llamamos al objeto empleado1 de la clase hija.
console.log(persona1.toString()); //Como vemos aqui solo nos muestra el nombre y apellido ya que llamamos a un objeto de la clase padre.

//Llamamos al metodo static
//persona1.saludar(); //No lo podemos usar desde el objeto, debemos usarlo desde la clase
Persona.saludar();
Persona.saludar2(persona1);
// EN LOS METODOS ESTATICOS SOLO PODEMOS VER LA SALIDA DESDE LA CONSOLA

Empleado.saludar();
Empleado.saludar2(empleado1);

//Usamos el atributo definido en la clase padre
//console.log(persona1.contadorObjetosPersona())
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona);  //Como vemos me muestra los tres objetos creados (persona1, persona2, empleado1)

//Accedemos al atributo NO estatico (este se asocia a los objetos de ambas clases pero no a la clase)
console.log(persona1.email);
console.log(empleado1.email);
//console.log(Persona.emai); //No podemos acceder desde la clases solo desde los objetos

//Hacemos uso del idPersona con el toString
console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);


//Objeto 4:
let persona3 = new Persona("Carla", "Pertosi");
console.log(persona3.toString());
console.log(Persona.contadorPersonas)

//Creamos una constante estatica (cuando queremos agregar una variable estatica pero que no pueda ser modificada)
//Debemos crear un metodo estatico y llamarla desde ahi
console.log(Persona.MAX_OBJ);
Persona.MAX_OBJ = 10;  //No se puede midificar ni alterar
console.log(Persona.MAX_OBJ);


//Probamos el contador de personas creando dos objetos mas
//Objeto 5:
let persona4 = new Persona("Franco", "Diaz");
console.log(persona4.toString());

//Objeto 6:
let persona5 = new Persona("Liliana", "Paz");
console.log(persona5.toString()); //En este caso se ejecuta el else del constructor
