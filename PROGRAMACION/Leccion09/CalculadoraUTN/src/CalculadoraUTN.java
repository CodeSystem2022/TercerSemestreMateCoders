import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while (true) {
            System.out.println("******  Aplicación Calculadora  ******");
            mostrarMenu();

            try{
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {
                    ejecutarOperacion(operacion, entrada);
                } else if (operacion == 5) {
                    System.out.println("Hasta pronto...");
                    break;
                } else {
                    System.out.println("Opción errónea: " + operacion);
                }
            } catch (Exception e){
                System.out.println("Error: "+ e.getMessage());
            }

            // Salto de línea y nuevo ciclo
            System.out.println();
        }
    }

    private static void mostrarMenu() {
        // Mostramos el menú
        System.out.println("""
                    1. Suma
                    2. Resta
                    3. Multiplicación
                    4. Division
                    5. Salir
                    """);
        System.out.print("Operación a realizar?");
    }

    private static void ejecutarOperacion(int operacion, Scanner entrada){
        System.out.print("Digite el valor para el operando1: ");
        var operando1 = Integer.parseInt(entrada.nextLine());
        System.out.print("Digite el valor para el operando1: ");
        var operando2 = Integer.parseInt(entrada.nextLine());
        int resultado;

        switch (operacion) {
            case 1 -> { // Suma
                resultado = operando1 + operando2;
                System.out.println(operando1 + " + " + operando2 + " = " + resultado);
            }
            case 2 -> { // Resta
                resultado = operando1 - operando2;
                System.out.println(operando1 + " - " + operando2 + " = " + resultado);
            }
            case 3 -> { // Multiplicación
                resultado = operando1 * operando2;
                System.out.println(operando1 + " * " + operando2 + " = " + resultado);
            }
            case 4 -> { // Division
                resultado = operando1 / operando2;
                System.out.println(operando1 + " / " + operando2 + " = " + resultado);
            }
        }
    }
}
