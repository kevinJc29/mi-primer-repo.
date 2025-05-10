
import java.util.Scanner;

public class Main {
    public static boolean esPalindromo(String texto) {
        // Eliminamos espacios, signos de puntuación y pasamos a minúsculas
        texto = texto.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        // Invertimos el texto usando StringBuilder
        String textoInvertido = new StringBuilder(texto).reverse().toString();

        // Comparamos el texto original con el invertido
        return texto.equals(textoInvertido);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pedimos entrada al usuario
        System.out.print("Escribe una palabra o frase para verificar si es un palíndromo: ");
        String entrada = scanner.nextLine();

        // Verificamos si es palíndromo con la funcio if y elseOSO
        if (esPalindromo(entrada)) {
            System.out.println("¡Sí! Es un palíndromo.");
        } else {
            System.out.println("No, no es un palíndromo.");
        }

        scanner.close();
    }
}
