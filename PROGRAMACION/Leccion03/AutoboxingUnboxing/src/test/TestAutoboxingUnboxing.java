package test;

public class TestAutoboxingUnboxing {
    public static void main(String[] args) {
        // Clases envolventes o Wrapper
        /*
            Clases envolventes de tipos primitivos 
            int = la clase envolvente es Integer
        
            Al utilizar la clase envolvente, tenemos acceso a muchos metodos 
            que son implementados, y que la clase primitiva, no tiene.
        */
        
        int enteroPrim = 10; // Tipo primitivo
        Integer entero = 10; // Tipo object
        System.out.println("enteroPrim = " + enteroPrim);
        System.out.println("entero = " + entero);
        
    }
}
