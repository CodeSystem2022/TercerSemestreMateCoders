package leccion03.AutoboxinUnboxing;

public class TestAutoboxinUnboxing {

	
	public static void main(String[] args) {
		// Clases envolventes o Wrapper
		
		/*
		 * Clases envolventes de tipos primitivos
		 * int = la clase envolventes es Integer
		 * long = la clase envolvente es Long
		 * float = la clase envolvente es Double
		 * boolean = la clase envolvente es Boolean
		 * byte = la clase envolvente es Byte
		 * char = la clase envolvente es Character
		 * short = la clase envolvente es Short
		 */
		int entero = 10; // Tipos primitivos
		System.out.println("Entero = " + entero);
		Integer enteros = 11;// Un entero de Tipo Objeto con la clase integer
		System.out.println("Entero = " + enteros.toString());
		// Las literales son diferentes de un tipo Primitivo a un tipo Object.
		// Autoboxing
		System.out.println("Entero = " + enteros.doubleValue());
		// el objeto se le asigna a una variable primitiva
		int entero2 = entero;
		System.out.println("Entero = " + entero2);
	}

}
