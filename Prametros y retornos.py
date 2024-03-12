
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicando un porcentaje al monto total de la compra.

    Args:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar. Por defecto es 10%.

    Returns:
    float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función proporcionando solo el monto total de la compra
monto_compra1 = 1000
descuento_calculado1 = calcular_descuento(monto_compra1)
print("Descuento 1:", descuento_calculado1)

# Llamada a la función proporcionando tanto el monto total de la compra como el porcentaje de descuento
monto_compra2 = 1500
porcentaje_descuento2 = 15
descuento_calculado2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
print("Descuento 2:", descuento_calculado2)
