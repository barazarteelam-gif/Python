total_compras= float(input("Ingrese el monto de compra"))
if total_compras>=100:
    descuento=(15/total_compras)
    print(f'Se te ha aplicado un descuento del 15%')
    print(f'Ganancia por descuento : {descuento}')
    print(f'Monto total:{total_compras}')
elif total_compras>=50:
    descuento=(10/total_compras)
    print(f'Se te ha aplicado un descuento del 10%')
    print(f'Ganancia por descuento: {descuento}')
    print(f'Monto total: {total_compras}')
else:
    print(f'No has conseguido descuento')
    print(f'Monto Total: {total_compras} $')