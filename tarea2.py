#Tienes la agenda: ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
#Realiza: (1) Agregar "Pedro Ruiz", (2) Buscar "Carlos Díaz" y mostrar posición, 
# (3) Modificar "Luis Torres" por "Luis Mendoza", (4) Eliminar "Ana
 #Garcia".

nombre = input ("Agregar ")

agenda = ["Ana Garcia", "Luis Torres", "Carlos Diaz", "Maria Lopez"]

agenda.append(nombre)

def buscarNombre (name, nombre):

   # name.remove ("Ana Garcia")
    for i in range(0, len (name)):

        if (name[i]== nombre):
            return i 

def reemplazo (name, rem, reemplaPor):

      for i in range(0, len (name)):

          if (name[i] == rem):
          
           name[i] = reemplaPor

def recorreLista (name):
    return name   

def elimina (name, elimina):
    name.remove(elimina)
#print(recorreLista(agenda))

reemplazo(agenda, "Luis Torres", "Luis Mendoza")
print ("indice es " + str (buscarNombre(agenda, "Carlos Diaz")) )
elimina(agenda, "Ana Garcia")
print(recorreLista(agenda))
