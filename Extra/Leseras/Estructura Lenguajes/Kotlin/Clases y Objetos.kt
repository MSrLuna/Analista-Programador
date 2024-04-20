class Persona(val nombre: String, val edad: Int) {
    fun saludar() {
        println("Hola, soy $nombre")
    }
}

fun main() {
    val persona1 = Persona("Ana", 25)
    persona1.saludar()
}

//Las clases en Kotlin se utilizan para definir objetos y sus propiedades. El constructor se define directamente en la declaración de la clase.
//Los métodos definidos en la clase pueden usarse para realizar acciones relacionadas con el objeto.