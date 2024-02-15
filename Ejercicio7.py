def agregar_item(inventario, item):
    if item in inventario:
        raise ValueError("El ítem ya está en el inventario.")
    else:
        inventario.append(item)

# Ejemplo de uso:
inventario = ["espada", "poción", "armadura"]
nuevo_item = "poción"  # Intentaremos agregar un ítem que ya está en el inventario

try:
    agregar_item(inventario, nuevo_item)
    print("Ítem agregado con éxito.")
except ValueError as e:
    print("Error:", e)

print("Inventario actualizado:", inventario)
