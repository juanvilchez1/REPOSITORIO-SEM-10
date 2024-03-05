#Este importa el módulo random, que se utiliza para generar números aleatorios. Será útil para simular datos de temperatura en este caso.
import random
#Define una función llamada calcular_promedio_temperaturas que toma tres parámetros: ciudades, dias_semana y semanas.
def calcular_promedio_temperaturas(ciudades, dias_semana, semanas):
    # Crear matriz 3D de temperaturas
    #Este bloque de código crea una matriz 3D de temperaturas para todas las ciudades, días de la semana y semanas.
    temperaturas = []
    for ciudad in range(len(ciudades)):
        ciudad_temperaturas = []
        for dia in range(len(dias_semana)):
            semana_temperaturas = []
            for semana in range(semanas):
                #Se utiliza un bucle anidado para recorrer cada ciudad, cada día de la semana y cada semana, generando una temperatura aleatoria entre 0 y 40 grados Celsius para cada día de cada semana de cada ciudad.
                semana_temperaturas.append(random.randint(0, 40))
            ciudad_temperaturas.append(semana_temperaturas)
        temperaturas.append(ciudad_temperaturas)

    # Calcular el promedio de temperaturas por ciudad y semana
    #Este bloque de código calcula el promedio de temperaturas por ciudad y semana e imprime los resultados.
    for ciudad_idx, ciudad in enumerate(ciudades):
        print(f"Promedio de temperaturas para {ciudad}:")
        for semana in range(semanas):
            temp_semana = 0
            #En cada iteración, suma las temperaturas de cada día de la semana y calcula el promedio dividiendo esta suma por el número de días en la semana.
            for dia_idx, dia in enumerate(dias_semana):
                temp_semana += temperaturas[ciudad_idx][dia_idx][semana]
            promedio_semana = temp_semana / len(dias_semana)
            print(f"Semana {semana + 1}: {promedio_semana:.2f}°C")
        print()

# Ejemplo uso de la funcion con datos diferentes datos proporcionados
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

calcular_promedio_temperaturas(ciudades, dias_semana, semanas)