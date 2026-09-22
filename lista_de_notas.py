# Arreglo de notas inicial
notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

# Cálculos básicos
promedio = sum(notas) / len(notas)
maxima = max(notas)
minima = min(notas)

# Contador de aprobados (nota >= 11)
aprobados = 0
for nota in notas:
    if nota >= 11:
        aprobados += 1

# Impresión con el formato exacto de salida
print(
    f"Promedio: {promedio} | Máx: {maxima} | Mín: {minima} | Aprobados: {aprobados}"
)