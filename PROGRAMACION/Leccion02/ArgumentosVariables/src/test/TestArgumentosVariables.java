
package test;


public class TestArgumentosVariables {
    public static void main(String[] args) {
    imprimirNumeros(3,4,5);
    imprimirNumeros(2,1);
    }
    
    private static void imprimirNumeros(int ...numeros){
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Elementos: "+numeros[i]);
        }
    }
    
}
