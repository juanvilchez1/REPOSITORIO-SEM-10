#Inicio de codigo

#matriz
matriz = [
    [9, 4, 6],
    [3, 7, 1],
    [5, 2, 8]
]

def ordenar_burbuja(fila):
    n = len(fila)
    # Iteramos sobre toda la fila
    for i in range(n):
        # Últimos i elementos ya están en su posición correcta
        for j in range(0, n-i-1):
            # Intercambiamos si el elemento actual es mayor que el siguiente
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


# Mostramos la matriz original
print("Matriz original:")
mostrar_matriz(matriz)

# Ordenamos la segunda fila (fila índice 1) en orden ascendente utilizando Bubble Sort
fila_a_ordenar = matriz[1]
ordenar_burbuja(fila_a_ordenar)

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la segunda fila ordenada:")
mostrar_matriz(matriz)