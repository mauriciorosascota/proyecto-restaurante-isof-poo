import random 
factura1 = round(random.uniform(20, 100), 2)
factura2 = round(random.uniform(20, 100), 2)
factura3 = round(random.uniform(20, 100), 2)

print(f'Facturas generadas para los clientes:')
print(f'Cliente 1: ${factura1}')
print(f'Cliente 2: ${factura2}')
print(f'Cliente 3: ${factura3}')

def calcular_propina_y_total(monto_factura):
    propina = monto_factura * 0.15
    total = monto_factura + propina
    return propina, total
seleccion = int(input('Seleccione el número de cliente (1, 2 o 3) para ver detalles de la factura: '))
if seleccion == 1:
    monto_factura = factura1
    print('la seleccion es valida.')
elif seleccion == 2:
    monto_factura = factura2
    print('la seleccion es valida.')
elif seleccion == 3:
    monto_factura = factura3
    print('la seleccion es valida.')
else:
    print('Selección invalida. El programa ha finalizado.')
    exit()
propina, total = calcular_propina_y_total(monto_factura)

print(f'Detalles de la factura seleccionada:')
print(f'Monto de la factura: ${monto_factura}')
print(f'Propina (15%): ${propina}')
print(f'Total a pagar: ${total}')
if total > 50 and propina < 20:
    print('¡Oferta especial disponible para este cliente!')
    print('Detalles adicionales:')
    print(f'Propina: ${propina}')
    print(f'Total: ${total}')
print('¡GRACIAS POR SU ATENCION!')
