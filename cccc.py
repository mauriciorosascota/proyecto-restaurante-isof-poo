import random

# Función para generar montos aleatorios de facturas para tres clientes
def generar_facturas():
    return [round(random.uniform(20, 100), 2) for _ in range(3)]

# Función para calcular la propina y el total a pagar
def calcular_propina_y_total(monto_factura):
    propina = monto_factura * 0.15
    total = monto_factura + propina
    return propina, total

# Función para mostrar los detalles de la factura
def mostrar_detalles_factura(monto_factura, propina, total):
    print(f"Detalle de la factura:")
    print(f"Monto de la factura: ${monto_factura}")
    print(f"Propina (15%): ${propina}")
    print(f"Total a pagar: ${total}")

def main():
    facturas_clientes = generar_facturas()
    print("Facturas generadas para los clientes:", facturas_clientes)

    while True:
        try:
            factura_seleccionada = int(input("Ingrese el número de la factura seleccionada (1, 2 o 3): "))
            if factura_seleccionada not in [1, 2, 3]:
                raise ValueError("Ingrese un número válido de factura (1, 2 o 3)")
            break
        except ValueError as e:
            print(e)

    monto_factura_seleccionada = facturas_clientes[factura_seleccionada - 1]

    propina, total = calcular_propina_y_total(monto_factura_seleccionada)
    mostrar_detalles_factura(monto_factura_seleccionada, propina, total)

    if total > 50 and propina < 20:
        print("¡Oferta especial disponible para este cliente!")
        print(f"Propina: ${propina}")
        print(f"Total con oferta especial: ${total - 10}")  # Se aplica un descuento de $10 en el total
    else:
        print("Este cliente no cumple con los requisitos para la oferta especial.")

if __name__ == "__main__":
    main()
