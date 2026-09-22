agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
agenda.append("Pedro Ruiz")
for posicion, nombre in enumerate(agenda):
    if nombre == "Carlos Díaz":
        print(f"Carlos Díaz esta en la pocicion: {posicion}")
agenda[1] = "Luis Mendoza"
agenda.remove("Ana García")
print(f"Nueva Agenda: {agenda}")