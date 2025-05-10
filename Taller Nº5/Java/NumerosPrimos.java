import java.util.Scanner; // Importamos Scanner para leer entrada del usuario

public class Main { // Clase principal
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Creamos objeto Scanner para entrada

        System.out.print("Ingresa el primer número: ");
        int a = scanner.nextInt(); // Leemos el primer número

        System.out.print("Ingresa el segundo número: ");
        int b = scanner.nextInt(); // Leemos el segundo número

        int resultado = sumaPrimosEnRango(a, b); // Llamamos a la función para obtener la suma

        System.out.println("La suma de los números primos entre " + a + " y " + b + " es: " + resultado);
    }

    // Función para verificar si un número es primo
    public static boolean esPrimo(int n) {
        if (n < 2) {
            return false; // Los números menores a 2 no son primos
        }
        for (int i = 2; i <= Math.sqrt(n); i++) { // Recorremos hasta la raíz cuadrada
            if (n % i == 0) {
                return false; // Si tiene un divisor, no es primo
            }
        }
        return true; // Si no se encontró divisor, es primo
    }

    // Función para sumar primos en el rango [a, b]
    public static int sumaPrimosEnRango(int a, int b) {
        int suma = 0;
        int inicio = Math.min(a, b); // Determinar el valor menor
        int fin = Math.max(a, b);    // Determinar el valor mayor

        for (int i = inicio; i <= fin; i++) {
            if (esPrimo(i)) {
                suma += i; // Si el número es primo, lo sumamos
            }
        }
        return suma;
    }
}
