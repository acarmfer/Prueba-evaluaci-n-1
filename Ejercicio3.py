def palabras_comunes(lista1, lista2):
    # Convertir las listas en conjuntos para eliminar duplicados y hacer las operaciones de intersección
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    # Encontrar la intersección de los conjuntos y la devuelve
    return conjunto1 & conjunto2

# Ejemplo de uso:
lista1 = ["manzana", "pera", "naranja", "plátano"]
lista2 = ["pera", "uva", "sandía", "manzana"]

resultado = palabras_comunes(lista1, lista2)
print("Palabras comunes:", resultado)