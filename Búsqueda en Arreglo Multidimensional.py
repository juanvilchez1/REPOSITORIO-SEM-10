# Inicio de codigo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]

Fila = -1
columna = -1

def buscar_valor(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == valor:
                return True, (fila, columna)
    return False, None

3
# Valor de busqueda
Valor_busqueda= int(input("Ingrese el valor que desea buscar en la matriz: "))

# Buscar el valor en la matriz
encontrado, posicion = buscar_valor(matriz, Valor_busqueda)

# Mostrar el resultado
if encontrado:
    print(f"El valor {Valor_busqueda} se encontró en la posición {posicion}.")
else:
    print(f"El valor {Valor_busqueda} no se encontró en la matriz.")

