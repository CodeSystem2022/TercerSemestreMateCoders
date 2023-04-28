package leccion03.ModificadoresAcceso.Test;

import leccion03.ModificadoresAcceso.Class.Protected.Clase3;
import leccion03.ModificadoresAcceso.Class.Public.*;

public class TestModificadoresAcceso {
	
	public static void main(String[] args) {
		Clase1 clase1 = new Clase1();
		System.out.println("clase1 = " + clase1.atributoPublic);
		// Constructor publico.
		clase1.metodoPublico();
		// Clase hija 3
		Clase3 claseHija = new Clase3();
		System.out.println("claseHija = " + claseHija);
	}

}
