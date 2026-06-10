saldo:int=1000
cajero=0
while cajero != 3:
    cajero=int(input("1.Ingresar Saldo, 2.Retirar Saldo, 3.Salir"))
    if cajero==1:
        ingreso=int(input("Cuanto deseas ingresar?"))
        saldo_total=saldo+ingreso
        print(f'Tu Saldo ahora es de {saldo_total}')
    elif cajero==2:
        retiro=int(input("Ingresa Cuanto deseas retirar?"))
        saldo_retirado=saldo-retiro
        if retiro>1000:
            print("No puedes retirar mas de lo que ya tienes")
        else:
            print(f'Retiraste {retiro}, Tenias {saldo}, Ahora Tienes {saldo_retirado}')
    elif cajero==3:
        print("Has Salido del Programa")


"""""contraseña:int=1234
intentos=0
acceso=False
while intentos<3 and not acceso:
    pin=int(input("Cual es tu contraseña"))
    if pin!=contraseña:
        print("I")
        print("N")
        print("C")
        print("O")
        print("R")
        print("R")
        print("E")
        print("C")
        print("T")
        print("O")
        intentos+=1
    else:
        print("Contraseña correcta, bienvenido")
        acceso=True"""""

num=int(input("Ingresa un numero pene"))
postivos=0
while num>0:
    num=int(input("Ingresa otro numero pene"))
    postivos+=1
    if num<0:
        print("Se acabo el programa pene")
        prom=(postivos+postivos//num)
        print(f'El promedio de todos lo numeros positivos: {prom}')

   