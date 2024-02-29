# Definir nombres de ciudades, días de la semana y semanas
import random


ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Crear matriz 3D de temperaturas
#En esta lista vacia se van almacenar todos los datos del bucle for1
temperaturas = []
#Inicio del bucle for1
for ciudad in range(len(ciudades)):
    #en esta lista se almacenan datos de semana_temperatura
    ciudad_temperaturas = []
    for dia in range(len(dias_semana)):
        #en esta lista vacia se almacenan datos que se generaron aleatoriamente
        semana_temperaturas = []
        #Cuidad_temperaturas esta conectado con for semana
        for semana in range(semanas):
            #este comando random.randint(0, 40) sirve para generar numeros aleatorios
            semana_temperaturas.append(random.randint(0, 40))
        ciudad_temperaturas.append(semana_temperaturas)
    temperaturas.append(ciudad_temperaturas)

# Calcular el promedio de temperaturas por ciudad y semana
#ciudad_idx representa el índice numérico de la ciudad actual en la lista ciudades, y ciudad representa el nombre de la ciudad.
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas para {ciudad}:")
    # Este bucle for analiza sobre cada semana, donde semanas es el número total de semanas.
    for semana in range(semanas):
        #Se inicializa una variable temp_semana para almacenar la suma de las temperaturas de todos los días de la semana actual.
        temp_semana = 0
        #Esto significa que dia_idx representa el índice numérico del día de la semana actual en la lista dias_semana, y dia representa el nombre del día de la semana.
        for dia_idx, dia in enumerate(dias_semana):
            # Suma la temperatura del día actual de la semana actual para la ciudad actual a la variable temp_semana
            temp_semana += temperaturas[ciudad_idx][dia_idx][semana]
            #Calcula el promedio de temperatura para la semana actual dividiendo la suma total de las temperaturas diarias entre el número de días en la semana.
        promedio_semana = temp_semana / len(dias_semana)
        #mprime el promedio de temperatura para la semana actual, mostrando el número de semana (semana + 1) y el promedio de temperatura formateado con dos decimales ({promedio_semana:.2f})
        #seguido de "°C" para indicar que es en grados Celsius.
        print(f"Semana {semana + 1}: {promedio_semana:.2f}°C")
        #Imprime una línea en blanco para separar los resultados de las diferentes ciudades.
    print()
