edad=int(input("Edad?"))
if edad>=18:
    print("Puede Pasar")
else:
    print("No puedes pasar por ser menor de edad")
 
temperatura=float(input("Temperatura del tanque"))
if temperatura>100:
    print("Alerta: Sobrecalentamiento")
else:
    print("Temperatura Estandar")
numero=int(input("Ingresa un numero"))
if numero%2==0:
    print(f'{numero} es par')
else:
    print(f'{numero} es impar')

saldo=500
retiro=int(input("Cuanto desea retirar?"))
if retiro<=saldo:
    print("Retiro exitoso")
else:
    print("No puedes retirar mas de lo que ya tienes, saldo insuficiente, retiro rechazado")

nota=float(input("Nota del semestre?"))
validacion=True if nota>=10 and nota<=20 else False
if nota>=10 and nota<=20:
    print("Aprobaste el semestre")
elif nota<10:
    print("Reprobaste el semestre")
else:
    print("Nota Invalida")

color=input("Semaforo, un color, rojo, amarillo o verde")
if color=="rojo":
    print("Pare")
elif color=="amarillo":
    print("Precaución")
elif color=="verde":
    print("Siga Avanzando")
else:
    print("Color invalido")

edad=int(input("Cuantos Años tienes?"))
if edad>=0 and edad<=12:
    print("Niño/a")
elif edad>12 and edad<18:
    print("Adolescente")
elif edad>=18 and edad<=64:
    print("Adulto")
elif edad>=65:
    print("Anciano")
else:
    print("Edad Invalida")

articulos=int(input("Cuantos articulos vas a comprar?"))
if articulos>=10 and articulos<20:
    print("Tienes 10% de descuento")
elif articulos>=20:
    print("Tienes 20% de descuento")
else:
    print("No hay descuento")

"""ladoA=float(input("Cuanto mide el primer lado de tu triangulo?"))
ladoB=float(input("Cuanto mide el segundo lado?"))
ladoc=float(input("Cuanto mide el tercer lado?"))
if ladoA==ladoB and ladoA==ladoc and ladoB==ladoc:
    print("Tu triangulo es equilatero")
elif (ladoA!=ladoB or ladoA!=ladoc or ladoB!=ladoc) and ladoA==ladoB or ladoA==ladoc or ladoB==ladoc:
    print("Tu triangulo es Isosceles")
else:
    print("Tu triangulo es escaleno")"""

"""mes=int(input("Dame el numero de un mes (1-12)"))
if mes==12 or mes==1 or mes==2:
    print("Invierno")
elif mes==3 or mes==4 or mes==5:
    print("Primavera")
elif mes==6 or mes==7 or mes==8:
    print("Verano")
elif mes==9 or mes==10 or mes==11:
    print("Otoño")
else:
    print("Mes Invalido")"""

"""promedio=int(input("Cual es tu promedio?"))
ingresos=int(input("Ingresos Familiares"))
if promedio>16 and ingresos>500:
    print("Has calificado para conseguir tu beca universitaria")
else:
    print("No has logrado clasificar")"""

"""vip=input("Tienes invitacion?")
socio=input("Eres socio Platino?")

if vip=="S" or socio=="S":
    print("Acceso Concedido")
else:
    print("Acceso Denegado")"""

"""usuario="admin"
contraseña=1234
pin=input("Nombre de Usuario?")
password=int(input("Contraseña"))
if pin==usuario and password==contraseña:
    print("Acceso Concedido")
else:
    print("Acceso Denegado")"""

"""rango=float(input("Nota"))
if rango>=0 and rango<=20:
    print("Nota Valida")
else:
    print("Nota Invalida")"""

""""año=int(input("Ingresa un año"))
if (año%4==0 or año%400==0) and año%100!=0:
    print(f'{año} es bisiesto')
else:
    print(f'{año} no es bisiesto')"""

"""fiebre=input("Tienes fiebre?")
if fiebre=="no":
      tos=input("tienes tos?")
      if tos=="no":
           print("Alta")
elif fiebre=="si":
    tos=input("tienes tos?")
    if fiebre=="si" and tos=="si":
        print("Protocolo Respiratorio")
    elif fiebre=="si" and tos=="no":
         print("Chequeo General")"""

"""pais=input("Cual es tu pais de origen?")
edad=int(input("Cuantos años tienes?"))
if pais=="venezuela" and edad>60:
    print("No pagaras impuestos")
elif pais=="venezuela" and edad<60:
    print("Pagar 10% de impuestos")
elif pais!="venezuela":
    print("Pagas 20% de impuestos, no importa la edad")
else:
    print("error")"""

"""import random
ia=("piedra","papel","tijera")   
ia=random.choice(ia)
jugador=input("piedra, papel o tijera?")
if ia=="piedra" and jugador=="tijera":
    print(f'LA IA utilizo {ia}')
    print(f'EL JUGADOR utilizo {jugador}')
    print("GANA LA IA") 
elif ia=="tijera" and jugador=="piedra":
    print(f'LA IA utilizo {ia}')
    print(f'EL JUGADOR utilizo {jugador}')
    print("GANA EL JUGADOR")
elif ia=="papel" and jugador=="piedra":
    print(f'LA IA utilizo {ia}')
    print(f'EL JUGADOR utilizo {jugador}')
    print("GANA LA IA")
elif ia=="piedra" and jugador=="papel":
    print(f'LA IA utilizo {ia}')
    print(f'EL JUGADOR utilizo {jugador}')
    print("GANA EL JUGADOR")
elif ia=="tijera" and jugador=="papel":
    print(f'LA IA utilizo {ia}')
    print(f'EL JUGADOR utilizo {jugador}')
    print("GANA LA IA")  
elif jugador=="tijera" and ia=="papel":
    print(f'LA IA utilizo {ia}')
    print(f'EL JUGADOR utilizo {jugador}')
    print("GANA EL JUGADOR")  
else:
    print(f'LA IA utilizo {ia}')
    print(f'EL JUGADOR utilizo {jugador}')
    print("empate")"""

import random
ia=("piedra","papel","tijera")
ia=random.choice(ia)
jugador=input("piedra, papel o tijera?")
if (ia=="piedra" and jugador=="tijera") or (ia=="papel" and jugador=="piedra") or (ia=="tijera" and jugador=="papel")  :
    print(f'LA IA utilizo {ia}')
    print(f'EL JUGADOR utilizo {jugador}')
    print("GANA LA IA")
elif (ia=="tijera" and jugador=="piedra") or (ia=="piedra" and jugador=="papel") or (jugador=="tijera" and ia=="papel"):
    print(f'LA IA utilizo {ia}')
    print(f'EL JUGADOR utilizo {jugador}')
    print("GANA EL JUGADOR") 
else:
    print(f'LA IA utilizo {ia}')
    print(f'EL JUGADOR utilizo {jugador}')
    print("empate")
