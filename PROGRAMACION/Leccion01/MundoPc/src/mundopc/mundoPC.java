
package mundopc;

import ar.com.system2023.mundopc.*;

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13); //IMPORTAR LA CLASE
        Teclado tecladoHP = new Teclado("Bluetooth","HP"); //IMPORTAR LA CLASE
        Raton ratonHP = new Raton("Bluetooth", "HP");
        
        Computadora computadoraHP = new Computadora("Computadora HP",monitorHP,tecladoHP,ratonHP);
        
        //CREACION DE VARIOS OBJETOS
        Monitor monitorGamer = new Monitor("Gamer", 32); //IMPORTAR LA CLASE
        Teclado tecladoGamer = new Teclado("Bluetooth","Gamer"); //IMPORTAR LA CLASE
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        
        Computadora computadoraGamer = new Computadora("Computadora Gamer",monitorGamer,tecladoGamer,ratonGamer);
        
        
        Computadora computadoraVarias1 = new Computadora("Computadora de varias marcas: ",monitorHP,tecladoGamer,ratonHP);
        
        //CREOAMOS OBJETOS DE TIPO ORDEN
        Orden orden1 = new Orden(); // 9inicializamos el arreglo vacio
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        
        Orden orden2 = new Orden(); // nueva lista para el obj orden2
        orden2.agregarComputadora(computadoraVarias1);
        
        
        //Mostrar orden
          //orden1.mostrarOrden();
          //orden2.mostrarOrden();
        
        //TAREA
        //Crear mas objetos de tipo computadora con todos sus elementos
        //completar una lista en el objeto orden1 que llegue a los 10 elementos
        //probar de esta manera los metodos al maximo rendimiento
        
        
        //CREACION DE OBJETOS
        Monitor monitorSamnsung = new Monitor("Samnsung", 19); //IMPORTAR LA CLASE
        Teclado tecladoSamnsung = new Teclado("Bluetooth","Samnsung"); //IMPORTAR LA CLASE
        Raton ratonSamnsung = new Raton("Bluetooth", "Samnsung");
        
        Computadora computadoraSamnsung = new Computadora("Computadora Samnsung",monitorSamnsung,tecladoSamnsung,ratonSamnsung);
        
        Monitor monitorLG = new Monitor("LG", 19); //IMPORTAR LA CLASE
        Teclado tecladoLG = new Teclado("Bluetooth","LG"); //IMPORTAR LA CLASE
        Raton ratonLG = new Raton("Bluetooth", "LG");
        
        Computadora computadoraLG = new Computadora("Computadora LG",monitorLG,tecladoLG,ratonLG);
        
        Monitor monitorBangho = new Monitor("Bangho", 20); //IMPORTAR LA CLASE
        Teclado tecladoBangho = new Teclado("Bluetooth","Bangho"); //IMPORTAR LA CLASE
        Raton ratonBangho = new Raton("Bluetooth", "Bangho");
        
        Computadora computadoraBangho = new Computadora("Computadora Bangho",monitorBangho,tecladoBangho,ratonBangho);
        
        Monitor monitorSony = new Monitor("Sony", 17); //IMPORTAR LA CLASE
        Teclado tecladoSony = new Teclado("Bluetooth","Sony"); //IMPORTAR LA CLASE
        Raton ratonSony = new Raton("Bluetooth", "Sony");
        
        Computadora computadoraSony = new Computadora("Computadora Sony",monitorSony,tecladoSony,ratonSony);
        
        Monitor monitorCompaq = new Monitor("Compaq", 23); //IMPORTAR LA CLASE
        Teclado tecladoCompaq = new Teclado("Bluetooth","Compaq"); //IMPORTAR LA CLASE
        Raton ratonCompaq = new Raton("Bluetooth", "Compaq");
        
        Computadora computadoraCompaq = new Computadora("Computadora Compaq",monitorCompaq,tecladoCompaq,ratonCompaq);
        
        
        Computadora computadoraVarias2 = new Computadora("Computadora de varias marcas2: ",monitorLG,tecladoBangho,ratonSamnsung);
        Computadora computadoraVarias3 = new Computadora("Computadora de varias marcas3: ",monitorSamnsung,tecladoGamer,ratonHP);
        Computadora computadoraVarias4 = new Computadora("Computadora de varias marcas4: ",monitorHP,tecladoSamnsung,ratonLG);
        Computadora computadoraVarias5 = new Computadora("Computadora de varias marcas5: ",monitorSamnsung,tecladoLG,ratonHP);
        
        //Creamos la orden 3 tarea
        Orden orden3 = new Orden(); // nueva lista para el obj orden2
        orden3.agregarComputadora(computadoraSamnsung);
        orden3.agregarComputadora(computadoraLG);
        orden3.agregarComputadora(computadoraBangho);
        orden3.agregarComputadora(computadoraSony);
        orden3.agregarComputadora(computadoraCompaq);
        orden3.agregarComputadora(computadoraVarias1);
        orden3.agregarComputadora(computadoraVarias2);
        orden3.agregarComputadora(computadoraVarias3);
        orden3.agregarComputadora(computadoraVarias4);
        orden3.agregarComputadora(computadoraVarias5);
        
        // superamos la orden de 10 esta computadora no sale
        orden3.agregarComputadora(computadoraHP);
        
        //Mostrar orden
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        orden3.mostrarOrden();
    }
}
