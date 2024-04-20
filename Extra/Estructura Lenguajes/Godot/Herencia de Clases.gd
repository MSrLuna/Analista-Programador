class Character:
    var name: String

    func _init(name):
        self.name = name

class Player(Character):
    var health: int

    func _init(name, health):
        super._init(name)  # Llamar al constructor de la clase padre
        self.health = health

var player_instance = Player.new("Alex", 90)
print(player_instance.name)  # Salida: Alex