
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {

    // Función que retorna un mensaje como String, en lugar de booleano
    public static String verificarNumeroPerfecto(int n) {
        int suma = IntStream.range(1, n)
                .filter(i -> n % i == 0)
                .sum();

        return (n > 1 && suma == n) ?
                "Es un número perfecto." :
                "No es un número perfecto.";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingresa un número: ");
        int numero = sc.nextInt();

        // Mostrar resultado directamente
        System.out.println(numero + ": " + verificarNumeroPerfecto(numero));
    }
}