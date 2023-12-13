import random

# Función para calcular la propina y el total a pagar
def calcular_propina_y_total(monto):
    propina = monto * 0.15
    total = monto + propina
    return propina, total

# Generar montos aleatorios para las facturas de tres clientes
factura_cliente1 = round(random.uniform(20, 100), 2)
factura_cliente2 = round(random.uniform(20, 100), 2)
factura_cliente3 = round(random.uniform(20, 100), 2)

# Mostrar las facturas al usuario
print(f"Facturas generadas para los clientes:")
print(f"Cliente 1: ${factura_cliente1}")
print(f"Cliente 2: ${factura_cliente2}")
print(f"Cliente 3: ${factura_cliente3}")

# Solicitar al usuario que elija una factura
seleccion = int(input("Seleccione el número de cliente (1, 2 o 3) para ver detalles de la factura: "))

# Verificar la validez de la factura seleccionada
if seleccion == 1:
    monto_factura = factura_cliente1
elif seleccion == 2:
    monto_factura = factura_cliente2
elif seleccion == 3:
    monto_factura = factura_cliente3
else:
    print("Selección inválida. El programa ha finalizado.")
    exit()

# Calcular la propina y el total
propina, total = calcular_propina_y_total(monto_factura)

# Mostrar detalles de la factura, propina y total
print(f"\nDetalles de la factura seleccionada:")
print(f"Monto de la factura: ${monto_factura}")
print(f"Propina (15%): ${propina}")
print(f"Total a pagar: ${total}")

# Verificar condiciones para oferta especial
if total > 50 and propina < 20:
    print("\n¡Oferta especial disponible para este cliente!")
    print("Detalles de la oferta especial:")
    print(f"Propina: ${propina}")
    print(f"Total: ${total}")
