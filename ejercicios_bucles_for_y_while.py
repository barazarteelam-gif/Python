password = input("Ingresa tu Contraseña")
while password != "Mittens" :
    password = input("ERROR, Vuelve a Intentarlo")
print("Correcto")


pasword = "mittens"
correcto = 1
while correcto != 0:
    intento = input("Contraseña: ")
    if intento == pasword:
        correcto = 0
    else:
        print("ERROR, vuelve a intentar. ")

print("correcto bb")

op = 2
contador = 1
while op < 500:
    op = op + op
print(op)

positivo = int(input("Ingresa un numero:"))
while positivo < 0 :
    positivo = int(input("ERROR, Vuelve a Intentarlo"))
print("Correcto")

for n in range (2,21,2):
    print(n)
contador = 0
for tabla in range (5,51,5):
    contador += 1
    print(f"5 x {contador} = {tabla} ")

