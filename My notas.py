# Definicion de el nombre del archivo
file_name = "my_notes.txt"
# Abrir el archivo en modo escritura ("w")
with open(file_name, "w") as archivo:
    archivo.write("Esta es mi primera nota.\n")
    archivo.write("Hoy aprendí sobre la manipulación de archivos en Python.\n")
    archivo.write("Estoy emocionado por seguir aprendiendo y creando cosas nuevas.\n")
# Lectura del archivo my_notes.txt
with open("my_notes.txt", "r") as file:
    # Leer línea por línea y mostrar en la consola
    for line in file:
        print(line.strip())  # Eliminar el carácter de nueva línea y mostrar la línea

# El archivo se cierra automáticamente después de salir del bloque 'with'
