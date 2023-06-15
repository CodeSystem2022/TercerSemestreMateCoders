
package test;

import domain.Persona;

public class TestJavaBeans {
    public static void main(String[] args) {
        Persona persona = new Persona();
        persona.setNombre("Martin");
        persona.setApellido("Torres");
        System.out.println("persona = " + persona);
        
        System.out.println("Persona Nombre= " + persona.getNombre() );
        System.out.println("Persona Apellido= " + persona.getApellido() );
        
        
        
    }
}
