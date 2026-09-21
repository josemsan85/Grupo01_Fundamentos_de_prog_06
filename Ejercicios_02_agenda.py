# Ejercicio 2 Operaciones CRUD en agenda de contactos
 
agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
 
# (1) Agregar "Pedro Ruiz" al final
agenda.append("Pedro Ruiz")
 
# (2) Buscar "Carlos Díaz" y mostrar su posición
if "Carlos Díaz" in agenda:
    posicion = agenda.index("Carlos Díaz")
    print(f"Carlos Díaz está en la posición: {posicion}")
else:
    print("Carlos Díaz no está en la agenda")
 
# (3) Modificar "Luis Torres" por "Luis Mendoza"
pos_luis = agenda.index("Luis Torres")   # buscamos dónde está
agenda[pos_luis] = "Luis Mendoza"        # lo reemplazamos por índice
 
# (4) Eliminar "Ana García"
agenda.remove("Ana García")
 
# Resultado final
print(agenda)