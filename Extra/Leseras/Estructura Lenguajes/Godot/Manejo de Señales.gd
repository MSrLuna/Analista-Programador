class ButtonPress:
    signal pressed

    func _ready():
        emit_signal("pressed")

class Game:
    func _init():
        var button = ButtonPress.new()
        button.connect("pressed", self, "_on_button_pressed")

    func _on_button_pressed():
        print("¡Botón presionado!")

var game_instance = Game.new()  # Salida: ¡Botón presionado!