#Cedula: 32.308.107 Ejercicio 1
tanque = 500
horas = 0
    
while tanque > 0:
    consumo = input("Ingrese la cantidad de litros que se ha gastado en una hora:")
    if consumo.isalpha():
        print("ERROR")
    if consumo.isnumeric():
        horas += 1
        tanque = tanque - int(consumo)
        if int(consumo) > 500 or int(consumo) < 0:
            print("ERROR")
       


print("Alerta: Tanque Vacio")
print(f"La nave logrò resistir un total de {horas} horas")

peso = 0 
for lote in range(8):
    peso = input("Ingrese el peso del objeto")
if peso.isalpha():
    print("ERROR")
elif peso.isnumeric():
    peso_total = peso + peso

print(f"Peso Total: {peso}")

