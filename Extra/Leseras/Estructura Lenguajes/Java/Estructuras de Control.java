//Condicionales:

int edad = 18;

if (edad >= 18) {
    System.out.println("Eres mayor de edad.");
} else {
    System.out.println("Eres menor de edad.");
}

//Las estructuras condicionales en Java, como if, se utilizan para tomar decisiones en función de una condición.
//El código dentro del bloque if se ejecutará si la condición es verdadera; de lo contrario, se ejecutará el bloque else.

//Bucles:

// Bucle for para iterar sobre una lista
int[] numeros = {1, 2, 3, 4, 5};
for (int num : numeros) {
    System.out.println(num);
}

// Bucle while
int contador = 0;
while (contador < 5) {
    System.out.println("Contador: " + contador);
    contador++;
}

//Los bucles permiten repetir un conjunto de instrucciones. 
//For-each se utiliza para iterar sobre una secuencia (como una lista en este caso), y while se utiliza para repetir un bloque de código mientras se cumple una condición.
