class NPC:
    var name: String

    func _init(name):
        self.name = name

    func greet():
        print("Hola, soy", name)

var npc_instance = NPC.new("Pedro")
npc_instance.greet()  # Salida: Hola, soy Pedro
