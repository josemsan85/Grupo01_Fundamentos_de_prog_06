notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
contador_aprobados = 0
contador_desaprobados = 0
maxima = notas[0]
minima = notas[0]
suma_notas = 0
for i in range(len(notas)):
    print(notas[i])
    if notas[i] >= 11:
        contador_aprobados += 1
    else:
        contador_desaprobados +=1
    if notas [i] > maxima:
        maxima = notas [i]
    if notas [i] < minima:
        minima = notas [i]
    suma_notas += notas[i]
    promedio = suma_notas / len(notas)
print(f"La cantidad de aprobados es: {contador_aprobados}")
print(f"La cantidad de desaprovados fue: {contador_desaprobados}")
print(f"La mayor nota fue: {maxima}")
print(f"La menor nota fue: {minima}")
print(f"El promedio de la notas es: {promedio:.2f}")