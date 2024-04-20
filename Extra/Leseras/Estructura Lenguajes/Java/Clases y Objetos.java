public class Persona {
    private String nombre;
    private int edad;

    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public void saludar() {
        System.out.println("Hola, soy " + this.nombre);
    }

    public static void main(String[] args) {
        Persona persona1 = new Persona("Ana", 25);
        persona1.saludar();
    }
}

//Las clases en Java se utilizan para definir objetos y sus propiedades.
//El constructor se llama cuando se crea un nuevo objeto a partir de la clase.
//Los métodos definidos en la clase pueden usarse para realizar acciones relacionadas con el objeto.