var inventory = ["sword", "shield", "potion"]
inventory.append("armor")  # Agregar un elemento a la lista
inventory.remove("potion")  # Eliminar un elemento de la lista
print(inventory)  # Salida: ["sword", "shield", "armor"]

var player_info = {
    "name": "Carol",
    "health": 95,
    "items": ["key", "map"]
}
print(player_info["name"])  # Salida: Carol
player_info["health"] += 5