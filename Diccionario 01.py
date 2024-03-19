# Creamos el diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan Perez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Accedemos al valor asociado con la clave "ciudad" y lo modificamos
informacion_personal["ciudad"] = "Guayaquil"

# Agregamos una nueva clave-valor que represente la profesión de la persona
informacion_personal["profesion"] = "Desarrollador de software"

# Verificamos si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregamos la clave con un número de teléfono ficticio
    informacion_personal["telefono"] = "593-99 844 57507"

# Eliminamos la clave "edad" del diccionario, ya que no es necesaria
del informacion_personal["edad"]

# Imprimimos el diccionario resultante después de realizar todas las operaciones
print(informacion_personal)