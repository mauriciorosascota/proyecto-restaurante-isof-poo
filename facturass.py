import random
factura1 = round(random.uniform(20, 100), 2)
factura2 = round(random.uniform(20, 100), 2)
factura3 = round(random.uniform(20, 100), 2)
print(f"Factura 1: ${factura1}")
print(f"Factura 2: ${factura2}")
print(f"Factura 3: ${factura3}")
opcion = input('seleccione una factura(factura1, factura2, factura3): ')
if opcion == factura1:
    propina = (15 / 100) * factura1
total = factura1 + propina
print(f"Detalle de la factura:")
print(f"Monto de la factura: ${factura1}")
print(f"Propina (15%): ${propina}")
print(f"Total a pagar: ${total}")
if total > 50 and propina < 20:
        print("¡Oferta especial disponible para este cliente!")
        print(f"Propina: ${propina}")
        print(f"Total con oferta especial: ${total - 10}")
else:
        print("Este cliente no cumple con los requisitos para la oferta especial.")



