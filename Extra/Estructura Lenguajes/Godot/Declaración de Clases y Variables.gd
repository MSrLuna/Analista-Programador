class Player:
    var name: String  # Variable para el nombre del jugador
    var health: int   # Variable para la salud del jugador

    # Constructor
    func _init(name, health):
        self.name = name
        self.health = health

var player_instance = Player.new("Alice", 100)  # Crear una instancia de jugador
print(player_instance.name)  # Salida: Alice
