matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
filas = len(matriz)
cols = len(matriz[0])
for i in range(filas):
    suma_fila = 0
    for j in range(cols):
        suma_fila = suma_fila + matriz[i][j]
    print(f"Suma de la fila {i}: {suma_fila}")
for j in range(cols):
    suma_columna = 0
    for i in range(filas):
        suma_columna = suma_columna + matriz[i][j]
    print(f"Suma de la columna {j}: {suma_columna}")