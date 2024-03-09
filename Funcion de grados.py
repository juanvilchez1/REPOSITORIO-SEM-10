def convertir_centigrados(centigrados):
    # Esta función convierte grados centígrados a Fahrenheit y Kelvin.

    # Parámetros:
    # centigrados (float): La temperatura en grados centígrados.

    # Retorno:
    # Un diccionario con las temperaturas en Fahrenheit y Kelvin.

    fahrenheit = (centigrados * 9 / 5) + 32
    kelvin = centigrados + 273.15

    return {
        "fahrenheit": fahrenheit,
        "kelvin": kelvin
    }


# Ejemplo de uso
temperatura_centigrados = 20

conversiones = convertir_centigrados(temperatura_centigrados)

print(f"Temperatura en Fahrenheit: {conversiones['fahrenheit']}")
print(f"Temperatura en Kelvin: {conversiones['kelvin']}")
