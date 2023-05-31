package leccion03.ModificadoresAcceso.Class.Public;

public class Clase1 {
	public String atributoPublic = "Valor atributo public";
	protected String atributoProtected = "Valor atributo protected";
	public Clase1() {
		System.out.println("Constructor public");
	}
	protected Clase1(String atributopublic) {
		System.out.println("Constructor protected");
	}
	public void metodoPublico() {
		System.out.println("Constructor Publico");
	}
	
	protected void metodoProtected() {
		System.out.println("Metodo Protected");
	}
}
