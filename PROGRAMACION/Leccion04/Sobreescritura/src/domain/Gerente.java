
package domain;


public class Gerente extends Empleado{
    private String departamento;
    
    public Gerente(String nombre, double sueldo, String departamento){
        super(nombre,sueldo);
        this.departamento = departamento;
        
    }
    
    @Override
    public String obtenerDetalles(){//no puede ser private
        return super.obtenerDetalles()+", Departamento: "+this.departamento;
    }
    
}
//polimorfismo: multiples comportamientos
