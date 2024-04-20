//GML en GameMaker se utiliza principalmente en el contexto de eventos.
//Por ejemplo, puedes tener un evento "Create" para inicializar objetos, un evento "Step" para actualizar en cada fotograma y un evento "Collision" para manejar colisiones.

// Evento "Create" de un objeto
score = 0;

// Evento "Step" de un objeto
if (keyboard_check_pressed(vk_space)) {
    score += 10;
}

// Evento "Collision" de un objeto
if (other.name == "Enemigo") {
    health -= 10;
}