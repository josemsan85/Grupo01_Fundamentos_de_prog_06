# Matriz 3x3 dada
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

filas = len(matriz)
cols = len(matriz[0])

# 1. Calcular suma de cada fila
textos_filas = []
for i in range(filas):
    suma_fila = sum(matriz[i])
    textos_filas.append(f"fila {i}: {suma_fila}")

# 2. Calcular suma de cada columna
textos_cols = []
for j in range(cols):
    suma_col = 0
    for i in range(filas):
        suma_col += matriz[i][j]
    textos_cols.append(f"col {j}: {suma_col}")

# 3. Formatear y mostrar el resultado exacto
salida_filas = " | ".join(textos_filas)
salida_cols = " | ".join(textos_cols)

print(f"Suma {salida_filas} || Suma {salida_cols}")