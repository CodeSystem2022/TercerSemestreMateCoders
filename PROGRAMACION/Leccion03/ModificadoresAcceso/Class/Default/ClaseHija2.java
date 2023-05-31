package leccion03.ModificadoresAcceso.Class.Default;

public class ClaseHija2 extends Clase2 {

	public ClaseHija2() {
		super();
		this.atributoDefault = "Modificacion del atributo Default";
		System.out.println("atributoDefault : " + this.atributoDefault);
		this.metodoDefault();
	}

}
