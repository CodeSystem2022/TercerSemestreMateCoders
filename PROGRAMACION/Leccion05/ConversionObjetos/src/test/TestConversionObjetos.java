
package test;

import domain.*;


public class TestConversionObjetos {
    
    public static void main(String[] args) {
        Empleado empleado;
        empleado = new Escritor("Juan", 5000, TipoEscritura.CLASICO);
        
        //System.out.println("empleado = "+empleado);
        //System.out.println(empleado.obtenerDetalles());//si queremos acceder a metodos Escritor
        
        //Downcasting
        //((Escritor) empleado).getTipoEscritura();// Tenemos 2 opcionesd: esta es una
        Escritor escritor = (Escritor)empleado;//Esta es la segunda
        escritor.getTipoEscritura();
       
       //Upcasting
        Empleado Empleado2 = escritor;
        System.out.println(Empleado2.obtenerDetalles());
        
        
        
        
    }
    
    
}
