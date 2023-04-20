
package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;


public class TestEnumeraciones {
    public static void main(String[] args) {
        System.out.println("Dia 1: "+Dias.LUNES);
        indicarDiaSemana(Dias.MARTES);// las enumeraciones se tratan como cadenas
        //Ahora nose deben utilizar comillas, se aacede a traves de el operador de punto.
        
        System.out.println("Continentes N. 1: "+Continentes.AMERICA);
        System.out.println("N de paises en el 1to. continente: "+Continentes.AMERICA.getPaises());
        System.out.println("N. de habitantes en el 1to. continente: "
                        +Continentes.AMERICA.getHabitantes() );
        
        System.out.println("Continentes N. 2: "+Continentes.ABRICA);
        System.out.println("N de paises en el 2to. continente: "+Continentes.ABRICA.getPaises());
        System.out.println("N. de habitantes en el 2to. continente: "
                        +Continentes.ABRICA.getHabitantes() );
        
        System.out.println("Continentes N. 3: "+Continentes.ASIA);
        System.out.println("N de paises en el 3to. continente: "+Continentes.ASIA.getPaises());
        System.out.println("N. de habitantes en el 3to. continente: "
                        +Continentes.ASIA.getHabitantes() );
        
        System.out.println("Continentes N. 4: "+Continentes.EUROPA);
        System.out.println("N de paises en el 4to. continente: "+Continentes.EUROPA.getPaises());
        System.out.println("N. de habitantes en el 4to. continente: "
                        +Continentes.EUROPA.getHabitantes() );
        
        System.out.println("Continentes N. 5: "+Continentes.OCEANIA);
        System.out.println("N de paises en el 5to. continente: "+Continentes.OCEANIA.getPaises());
        System.out.println("N. de habitantes en el 5to. continente: "
                        +Continentes.OCEANIA.getHabitantes() );
        
    }
    
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer dia de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana");
                break;
            case DOMINGO:
                System.out.println("Septimo dia de la semana");
                break;
            default:
                System.out.println("Esa variable no corresponde");
        }
    }
    
}
