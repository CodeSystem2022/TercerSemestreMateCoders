package leccion03.ModificadoresAcceso.Class.Protected;

import leccion03.ModificadoresAcceso.Class.Public.Clase1;

//clase 3 hija de clase 1
public class Clase3 extends Clase1 {
	public Clase3() {
		// trabajamos con el constructor tipo protected
		super("protected");
		this.atributoProtected = "Accedemos desde la clase hija";
		System.out.println("AtributoProtected = " + this.atributoProtected);
		this.atributoPublic = "es totalmente publico";
	}
}
