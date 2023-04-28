package leccion03.ModificadoresAcceso.Private;

public class Clase4 {

	private String atributoPrivate = "atributo Privado";
	
	private Clase4() {
		System.out.println("Constructor privado");
	}
	// CREAMOS UN CONSTRUCTOR PUBLICO PARA PODER CREAR OBJETOS
	// Aqui se puede llamar al constructor vacio
	public Clase4(String argumentos) {
		this();
		System.out.println("Constructor publico");
	}
	
	// Metodo private
	@SuppressWarnings("unused")
	private void metodoPrivado() {
		System.out.println("Constructor publico");
	}
	public String getAtributoPrivate() {
		return atributoPrivate;
	}
	public void setAtributoPrivate(String atributoPrivate) {
		this.atributoPrivate = atributoPrivate;
	}
	
}
