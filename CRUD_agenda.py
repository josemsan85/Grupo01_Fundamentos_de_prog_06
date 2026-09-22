# Agenda inicial
agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]

# (1) Agregar "Pedro Ruiz"
agenda.append("Pedro Ruiz")

# (2) Buscar "Carlos Díaz" y mostrar posición
posicion = agenda.index("Carlos Díaz")
print(f"Posición de Carlos Díaz: {posicion}")

# (3) Modificar "Luis Torres" por "Luis Mendoza"
pos_luis = agenda.index("Luis Torres")
agenda[pos_luis] = "Luis Mendoza"

# (4) Eliminar "Ana García"
agenda.remove("Ana García")

# Imprimir el estado final de la lista[cite: 2]
print(agenda)