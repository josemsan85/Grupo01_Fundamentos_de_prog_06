#Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
#Escribir un programa que calcule: promedio, nota más alta, nota más baja y cuántos aprobaron (nota ≥ 11)

notas = [15, 18, 12, 9, 17, 14, 20, 10, 16, 13]
alumnoAprobado = 0

def promedio (notas):
    return sum(notas)/len(notas)

def notaAlta (notas):
    return max(notas)

def notaBaja (notas):
    return min(notas)

def alumnosAprobados (notas):

    for i in range (0, len (notas)):
      if (notas[i]>= 11):
          global alumnoAprobado
          alumnoAprobado += 1 
    return alumnoAprobado

print ("el promedio es " + str (promedio(notas)) +
       ", Nota mas alta " + str (notaAlta(notas)) + 
       ", nota mas baja " + str (notaBaja (notas)) + 
       ", alumnos aprobados " + str (alumnosAprobados(notas)) )
