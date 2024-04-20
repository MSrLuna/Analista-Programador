import java.util.Scanner;

// Entrada de datos desde el usuario
Scanner scanner = new Scanner(System.in);
System.out.print("Ingrese su nombre: ");
String nombre = scanner.nextLine();
System.out.println("Hola, " + nombre);

// Salida formateada
int edad = 28;
System.out.printf("Tengo %d años.", edad);

//La clase Scanner se utiliza para obtener datos del usuario desde la consola.
//System.out.println() y System.out.printf() se utilizan para mostrar información en la consola.