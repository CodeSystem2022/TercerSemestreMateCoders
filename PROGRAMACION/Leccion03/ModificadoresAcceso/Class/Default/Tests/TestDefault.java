package leccion03.ModificadoresAcceso.Class.Default.Tests;


import leccion03.ModificadoresAcceso.Class.Default.ClaseHija2;
import leccion03.ModificadoresAcceso.Private.Clase4;

public class TestDefault {

	public static void main(String[] args){
		ClaseHija2 claseH2 = new ClaseHija2();
		claseH2.atributoPublic = "Cambio desde la Prueba";
		System.out.println("ClaseH2 = " + claseH2.atributoPublic);
		Clase4 clase4 = new Clase4("Publico");
		clase4.setAtributoPrivate("Cambio");
		System.out.print("Cambio en el atributo: " + clase4.getAtributoPrivate());
	}

}
