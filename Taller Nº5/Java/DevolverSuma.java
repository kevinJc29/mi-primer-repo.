import java.util.Scanner; // Importamos Scanner para entrada del usuario

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Crear objeto Scanner

        System.out.print("Ingresa un número entero positivo: ");
        int numero = scanner.nextInt(); // Leer el número

        if (numero > 0) {
            int resultado = sumaDigitos(numero); // Llamamos a la función
            System.out.println("La suma de los dígitos de " + numero + " es: " + resultado);
        } else {
            System.out.println("El número debe ser entero y positivo.");
        }
    }

    // Función que suma los dígitos del número
    public static int sumaDigitos(int n) {
        int suma = 0;
        while (n > 0) {
            suma += n % 10; // Tomamos el último dígito
            n = n / 10;     // Eliminamos el último dígito
        }
        return suma; // Devolvemos la suma total
    }
}
