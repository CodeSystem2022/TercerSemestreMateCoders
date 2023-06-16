class productos{
    
    static contadorProductos = 0;

    constructor(nombre,precio){
        this._idProducto = ++productos.contadorProductos;
        this._nombre = nombre;
        this._precio = precio;

    }
    get idProducto(){
        return this._idProducto;
    }
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get precio(){
        return this._precio;
    }
    set precio(precio){
        this._precio = precio;
    }
    toString(){
        return `idProducto : ${this._idProducto}, nombre: ${this._nombre}, precio: $${this._precio}`;
    }
}

class Orden{

    static contadorOrdenes = 0;

    static getMAX_PRODUCTOS(){
        return 5;
    }

    constructor (){
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this._contadorProdAgreg = 0;
    }
    get idOrden(){
        return this._idOrden;
    }
    agregarProducto(producto){
        if(this._productos.length < Orden.getMAX_PRODUCTOS()){
            //this._productos.push(producto);
            this._productos[this._contadorProdAgreg++] = producto;
        }
        else{
            console.log('No se pueden agregar mas productos')
        }

    }
    calcularTotal(){
        let totalVenta = 0;
        for(let producto of this._productos){
            totalVenta += producto.precio
        }
        return totalVenta;
    }
    mostrarOrden(){
        let productoOrden = ' ';
        for(let producto of this._productos){
        productoOrden += '\n{ '+producto.toString()+' }';
        }
        console.log(`Orden: ${this._idOrden}, Total: $${this.calcularTotal()}, Productos: ${productoOrden}`);

    }
}

let producto1 = new productos('Pantalon',200);
let producto2 = new productos('Camisa',150);
let producto3 = new productos('Cinturon',50);
let producto4 = new productos('Remera',300);
let producto5 = new productos('Medias',25);
let orden1 = new Orden();//constructor
let orden2 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden2.agregarProducto(producto4);
orden2.agregarProducto(producto5);
orden2.agregarProducto(producto1);
orden1.mostrarOrden();
orden2.mostrarOrden();
