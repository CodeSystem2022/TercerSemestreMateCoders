
package test;

import domain.*;


public class TestInstanceOf {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan", 10000);
//por tipo nos referimos a lo que esta del lado derecho por eso instanceof nos permite saber a que 
//referencia (lo que apunta la memoria)
        determinarTipo(empleado1);
        empleado1 = new Gerente ("Jose", 5000, "Sistema");
        //determinarTipo(empleado1);
    }
    
    public static void determinarTipo(Empleado empleado){
        if(empleado instanceof Gerente){
            System.out.println("Es de tipo Gerente");
            //Gerente gerente = (Gerente)empleado;//convertimos a un tipo gerente (como convertir un string a un entero)
            ((Gerente) empleado).getDepartamento();//hace la conversion automaticamente
            System.out.println("gerente = "+empleado);
            

        }
        else if (empleado instanceof Empleado){
            System.out.println("Es de tipo Empleado");
            //Gerente gerente = (Gerente)empleado;
            //System.out.println("gerente = "+gerente.getDepartamento());
        }
        else if (empleado instanceof Object){
            System.out.println("Es de tipo Object");
        }
    }

}
