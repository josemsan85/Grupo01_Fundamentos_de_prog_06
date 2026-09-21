# Ejercicio 1 estadísticas de una lista de notas
 
notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
 
# Variables para ir acumulando resultados
suma = 0
maxima = notas[0]   # empezamos con la primera nota
minima = notas[0]
aprobados = 0
 
# Recorremos la lista con for...in
for nota in notas:
    suma = suma + nota
 
    if nota > maxima:
        maxima = nota
 
    if nota < minima:
        minima = nota
 
    if nota >= 11:
        aprobados = aprobados + 1
 
promedio = suma / len(notas)
 
print(f"Promedio: {promedio}  Máx: {maxima}  Mín: {minima}  Aprobados: {aprobados}")