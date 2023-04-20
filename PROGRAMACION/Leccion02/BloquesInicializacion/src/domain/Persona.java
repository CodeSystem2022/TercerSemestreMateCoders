
package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersona;
    
    static{// Bloque de Inicializacion estatico
        System.out.println("Ejecucion del bloque estatico");
        ++Persona.contadorPersona;
    }
    
    { //Bloque de inicializacion NO estatico (contexto dinamico)
        System.out.println("Ejecucion del bloque No estatico");
        this.idPersona = Persona.contadorPersona++;// Incrementar el atributo
        
    }
    // Los bloques de inicializacion se ajecutan antes del contructor de nuestra clase

    public Persona() {
        System.out.println("Ejecucion del contructor");
    }

    public int getIdPersona() {
        return idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
    
    
}
