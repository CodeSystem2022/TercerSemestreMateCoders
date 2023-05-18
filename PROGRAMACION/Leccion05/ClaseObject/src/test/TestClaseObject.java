
package test;

import domain.*;


public class TestClaseObject {
    
    public static void main(String[] args) {
      Empleado Empleado1 = new Empleado("Juan",500);
      Empleado Empleado2 = new Empleado("Juan",500);
      
      if(Empleado1 == Empleado2){
          System.out.println("Tiene la misma referencia en memoria");
      }
      else{
          System.out.println("Tienen distinta referencia en memoria");
      }
      
      if(Empleado1.equals(Empleado2)){
          System.out.println("Los objetos son iguales en contenido");
      }
      else{
          System.out.println("los objetos son distintos en contenido");
      }
      
      if(Empleado1.hashCode() == Empleado2.hashCode()){
              System.out.println("El valor hascode es igual");
      }
      else{
          System.out.println("El valor hascode es diferente");
      }
      
    }

    @Override
    protected void finalize() throws Throwable {
        super.finalize(); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/OverriddenMethodBody
    }

    @Override
    public String toString() {
        return super.toString(); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/OverriddenMethodBody
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone(); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/OverriddenMethodBody
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/OverriddenMethodBody
    }

    @Override
    public int hashCode() {
        return super.hashCode(); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/OverriddenMethodBody
    }
    
     
    
}
