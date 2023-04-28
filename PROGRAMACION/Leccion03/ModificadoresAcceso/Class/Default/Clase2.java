package leccion03.ModificadoresAcceso.Class.Default;

import leccion03.ModificadoresAcceso.Class.Public.Clase1;

public class Clase2 extends Clase1{
	String atributoDefault = "Valor del tributo default";
	
	public Clase2() {
		super();
		this.atributoDefault = "Modificadores del atributo default";
		System.out.println("atributoDefault = " + this.atributoDefault);
		this.metodoDefault();
	}

	void metodoDefault() {
		System.out.println("Metodo Default");
	}
}
