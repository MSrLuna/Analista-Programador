//Condicionales:

val edad: Int = 18

if (edad >= 18) {
    println("Eres mayor de edad.")
} else {
    println("Eres menor de edad.")
}

//Las estructuras condicionales en Kotlin, como if, se utilizan para tomar decisiones en función de una condición.
//El código dentro del bloque if se ejecutará si la condición es verdadera; de lo contrario, se ejecutará el bloque else.

//Bucles:

// Bucle for para iterar sobre una lista
val numeros = listOf(1, 2, 3, 4, 5)
for (num in numeros) {
    println(num)
}

// Bucle while
var contador = 0
while (contador < 5) {
    println("Contador: $contador")
    contador++
}

//¡Por supuesto! Aquí están los mismos ejemplos con explicaciones detalladas en el contexto de Kotlin:

Variables y Tipos de Datos:

kotlin

// Números enteros
val entero: Int = 42

// Números decimales
val decimal: Double = 3.14

// Cadena de caracteres
val cadena: String = "Hola, mundo!"

// Booleanos
val verdadero: Boolean = true
val falso: Boolean = false

En Kotlin, las variables se utilizan para almacenar datos. Los tipos de datos incluyen enteros (Int), números decimales (Double), cadenas de caracteres (String) y valores booleanos (Boolean).

    Estructuras de Control:

    Condicionales:

kotlin

val edad: Int = 18

if (edad >= 18) {
    println("Eres mayor de edad.")
} else {
    println("Eres menor de edad.")
}

Las estructuras condicionales en Kotlin, como if, se utilizan para tomar decisiones en función de una condición. El código dentro del bloque if se ejecutará si la condición es verdadera; de lo contrario, se ejecutará el bloque else.

    Bucles:

kotlin

// Bucle for para iterar sobre una lista
val numeros = listOf(1, 2, 3, 4, 5)
for (num in numeros) {
    println(num)
}

// Bucle while
var contador = 0
while (contador < 5) {
    println("Contador: $contador")
    contador++
}

//Los bucles permiten repetir un conjunto de instrucciones.
//En Kotlin, for se utiliza para iterar sobre una secuencia (como una lista en este caso), y while se utiliza para repetir un bloque de código mientras se cumple una condición.