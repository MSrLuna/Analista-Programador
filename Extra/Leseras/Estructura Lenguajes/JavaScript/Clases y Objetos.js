class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    saludar() {
        console.log("Hola, soy", this.nombre);
    }
}

let persona1 = new Persona("Ana", 25);
persona1.saludar();

//Las clases en JavaScript se utilizan para definir objetos y sus propiedades.
//El constructor se llama cuando se crea un nuevo objeto a partir de la clase.
//Los métodos definidos en la clase pueden usarse para realizar acciones relacionadas con el objeto.