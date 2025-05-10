import java.util.Scanner; // Importamos Scanner para leer datos del usuario

public class Main { // Clase principal llamada "Main", debe coincidir con el nombre del archivo
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Creamos objeto para leer desde consola

        System.out.print("Ingresa un año: "); // Mensaje al usuario
        int año = scanner.nextInt(); // Leemos el año como entero

        // Usamos la función para verificar si el año es bisiesto
        if (esBisiesto(año)) {
            System.out.println(año + " es un año bisiesto.");
        } else {
            System.out.println(año + " no es un año bisiesto.");
        }
    }

    // Función que determina si el año es bisiesto
    public static boolean esBisiesto(int año) {
        // Un año es bisiesto si:
        // - Es divisible por 4 Y no es divisible por 100
        // - O es divisible por 400
        return (año % 4 == 0 && año % 100 != 0) || (año % 400 == 0);
    }
}
