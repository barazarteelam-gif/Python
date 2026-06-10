pin:int =1234
num_int:int =0
acceso=False
while num_int< 3 and not acceso:
    pin_usuar: int = int(input("Ingresa tu PIN de usuario"))
if pin_usuar == pin:
    acceso=True
    print("Contraseña corrrecta")    
else:
    print("Clave Invalida")
    pin_usuar: int = int(input("Ingresa tu PIN de usuario"))
num_int+=1

if not acceso:
    print("Cuenta Bloqueada")

piso:int=1
destino:int =int(input("Que piso quieres ir"))
while piso !=destino:
    if piso < destino:
        piso+=1
    print(f'Piso Actual: {piso}')
else:
 piso-=1
print(f'Piso Actual: {piso}')
print(f'Llegaste a tu piso, el piso: {piso}')

p1=0
p2=0
while p1<20 and p2<20:
 p1=int(input("Ingresa un numero del 1 al 6 p1"))
 p2=int(input("Ingresa un numero del 1 al 6 p2"))





