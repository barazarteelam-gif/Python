aire_actual = 100
i = 0
while aire_actual > 0:
    try:
        bomba_de_vacio = float(input("Ingrese la cantidad de aire consumida en el ultimo segundo, cabe aclarar que la presion actual es de 100 pascales, no puedes ingresar un numero negativo o un numero mayor a 100"))
    except ValueError:
        print("caracteres invalidos")
        i += 1
        aire_actual = aire_actual - bomba_de_vacio
print(f"El sistema le tomo {i} segundos alcanzar el vacio absoluto")
"""
señal = input("Hay señal? S/N").upper()
intentos_fallidos = 0
while señal == "n":
    señal = input("Hay señal? S/N").upper()
    intentos_fallidos += 1
print("Sincronización Establecida")
print(f"Ha intentado {intentos_fallidos} veces para sincronizar la señal sin éxito")

meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
for mes in range(meses):
    for dias in range(1,31):
        print(f"{dias} de {meses} de 2026")
        """