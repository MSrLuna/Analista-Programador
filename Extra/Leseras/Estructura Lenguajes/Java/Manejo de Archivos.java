//En Java, el manejo de archivos es bastante flexible.
//Aquí tienes un ejemplo simplificado:

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ManejoArchivos {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("archivo.txt"))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                System.out.println(linea);
            }
        } catch (IOException e) {
            System.out.println("Error al leer el archivo.");
        }
    }
}

//En Java, se utiliza un bloque try-with-resources para asegurarse de que los recursos (en este caso, el archivo) se cierren automáticamente después de su uso.