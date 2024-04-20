//En Kotlin, el manejo de archivos es similar a Java.
//Aquí tienes un ejemplo simplificado:

import java.io.File

fun main() {
    val archivo = File("archivo.txt")
    archivo.writeText("Hola, archivo!")

    val contenido = archivo.readText()
    println(contenido)
}