#Dada la matriz 3×3: [[1,2,3],[4,5,6],[7,8,9]] — 
# Calcular y mostrar la suma de cada fila y la suma de cada columna.

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9],
          [1,1,1]]

listaFila =[]
listColumna  =[]

#se agregan los valores a la lista horizontal, filas 
def sumaFilas (matriz):

    #fila 1 
    #matriz [0][0] + matriz [0][1] + matriz [0][2]
    #matriz [1][0] + matriz [1][1] + matriz [1][2]
    #matriz [2][0] + matriz [2][1] + matriz [2][2]

    suma = 0
    #en este caso la longitud de la matriz es 3
    for a in range (0, len( matriz)):

        for i in range (0, len(matriz[a])):
                     
            suma += matriz[a][i]
         
            if (i== len(matriz[a])-1):
                listaFila.append(suma)
                suma = 0

    """suma = 0
    for i in range (0, len(matriz[0])):
            
            suma += matriz[0][i]

            if (i== len(matriz[0])-1):
             listaFila.append(suma)

    suma = 0
    for i in range (0, len(matriz[1])):
            
            suma += matriz[1][i] 

            if (i== len(matriz[1])-1):
                listaFila.append(suma)

    suma = 0
    for i in range (0, len(matriz[2])):
            suma += matriz[2][i] 

            if (i== len(matriz[2])-1):
                listaFila.append(suma)"""

# columna 
#la primera componentes es el numero de elementos
#la segunda componenete es el numero de sub-elementos
# matriz [0][0] + matriz[1][0] + matriz [2][0] + matriz [3][0]
# matriz [0][1] + matriz[1][1] + matriz [2][1]
# matriz [0][2] + matriz[1][2] + matriz [2][2]
#se agregan los valores a la lista vertical, columnas
def sumaColumnas (matriz):

   
    #los valores de i son 0 1 2 hasta matriz - 1
    #si es 4 es 0 1 2 3
    #for i in range (0, len(matriz)):
   

    for i in range (0, len(matriz[0])):
         suma = 0 
         for a in range (0 , len (matriz)):
            #en ese caso a es 0 1 2 3 
            suma +=matriz[a][i]
            print (str (suma))
            if (a == len(matriz)-1):
               listColumna.append(suma)
              

    """suma = 0
    for i in range (0, len(matriz)):
        suma +=matriz[i][0]
        if (i == len(matriz)-1):
           listColumna.append(suma)

    suma = 0
    for i in range (0, len(matriz)):
        suma +=matriz[i][1]
        if (i == len(matriz)-1):
            listColumna.append(suma)

    suma = 0
    for i in range (0, len(matriz)):
        suma +=matriz[i][2]
        if (i == len(matriz)-1):
            listColumna.append(suma)"""

     
sumaFilas(matriz)
sumaColumnas(matriz)

def imprimecoluma (listVera):
     for i in range (0, len(listVera)):
          print("Suma columa " + str( i + 1 ) + ": " + str (listVera[i]))

def imprimeFila (listHora):
     for i in range (0, len(listHora)):
               print("Suma fila " + str(i+1) + " : " + str(listHora[i]))

imprimeFila(listaFila)
imprimecoluma(listColumna)
