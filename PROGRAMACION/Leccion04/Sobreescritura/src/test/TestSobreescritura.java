
package test;

import domain.*;


public class TestSobreescritura {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan", 10000);
        imprimir(empleado1);
        //System.out.println("empleado1 = " + empleado1.obtenerDetalles());
        empleado1 = new Gerente ("Jose", 5000, "Sistema");
        imprimir(empleado1);
        //System.out.println("gerente1 = " + gerente1.obtenerDetalles());
    }
    
    public static void imprimir(Empleado empleado){
        String detalles = empleado.obtenerDetalles();
        System.out.println("detalles = " + detalles);
    }
    //aqui aplicamos polimorfismo ya que llamamos como referencia de la clase padre empleado o 
    //tb desde la clase hija gerente sin problema pq esta relacionadas, o sea que el metodo obtener detalle
    //puede ser llamado de la clase hija gerente a traves de la herencia
    //el objetivo es tener metodos mas genericos, como en el caso imprimir ya que imprimos los dos metodos de clase padre e hija
}
