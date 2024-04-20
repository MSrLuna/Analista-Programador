try {
    val resultado = 10 / 0
} catch (e: ArithmeticException) {
    println("No puedes dividir entre cero.")
}

//Los bloques try y catch se utilizan para manejar errores en tiempo de ejecución.
//Si ocurre un error en el bloque try, el control se traslada al bloque catch correspondiente.