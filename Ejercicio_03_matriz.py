# Ejercicio 3 Suma de filas y columnas de una matriz 3x3
 
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 
filas = len(matriz)      # número de filas -> 3
cols = len(matriz[0])    # número de columnas -> 3
 
# Suma de cada fila (ciclos anidados)
for i in range(filas):
    suma_fila = 0
    for j in range(cols):
        suma_fila = suma_fila + matriz[i][j]
    print(f"Suma fila {i}: {suma_fila}")
 
# Suma de cada columna (ahora el ciclo de afuera recorre las columnas)
for j in range(cols):
    suma_col = 0
    for i in range(filas):
        suma_col = suma_col + matriz[i][j]
    print(f"Suma col {j}: {suma_col}")