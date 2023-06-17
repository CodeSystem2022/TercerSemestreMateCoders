import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Definimos la lista fuera del ciclo while
        List<Persona> personas = new ArrayList<>();
        //Empazamos el menu
        var salir = false;
        while (!salir){
            mostrarMenu();
            try{
                salir = ejecutarOperacion(entrada,personas);
            }catch (Exception e){
                System.out.println("Ocurrio un error: "+e.getMessage());
            }
            System.out.println();
        }//Fin del ciclo while
    }//Fin del metodo main

    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas) {
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        //Revisamos la opcion digita a traves de un swich
        switch (opcion){
            case 1 -> {
                System.out.println("Digite el nombre: ");
                var nombre = entrada.nextLine();
                System.out.println("Digite el telefono: ");
                var tel = entrada.nextLine();
                System.out.println("Digite el correo: ");
                var email = entrada.nextLine();
                //creamos el objeto persona
                var persona = new Persona(nombre,tel,email);
                //Agregamos la persona a la lista
                personas.add(persona);
                System.out.println("La lista tiene: "+personas.size()+" elementos");
            }//fin del caso 1
            case 2 -> {
                System.out.println("Listado de personas: ");
                //Mejoras con lambda y el metodo de referencia
                //personas.forEach((persona) -> System.out.println(persona));
                personas.forEach(System.out::println);
            }//fin del caso 2
            case 3 -> {
                System.out.println("Hasta Pronto...");
                salir = true;
            }//fin del caso 3
            default -> System.out.println("Opcion incorrecta: "+opcion);
        }//Fin del swith
        return salir;
    }//Fin ejecutarOperacion

    private static void mostrarMenu() {
        //Mostramos las opciones
        System.out.print("""
                ******** Listado de personas ********
                1. Agregar.
                2. Listar.
                3. Salir
                """);
        System.out.print("Digite una de las Opciones: ");
    }//Fin del metodo mastrar menu

}//Fin de la clase ListadoPersonasApp