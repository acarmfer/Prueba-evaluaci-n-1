

from collections import deque

# Definir las misiones con sus respectivos niveles de dificultad
misiones = [
    ("Misión 1", 3),
    ("Misión 2", 1),
    ("Misión 3", 2),
    ("Misión 4", 5),
    ("Misión 5", 4)
]

# Ordenar las misiones por dificultad
misiones_ordenadas = sorted(misiones, key=lambda x: x[1])

# Crear una cola para almacenar las misiones ordenadas
cola_misiones = deque(m[0] for m in misiones_ordenadas)

# Mostrar las misiones sin los números de dificultad
print("Misiones ordenadas por dificultad:")
for mision in cola_misiones:
    print(mision)
