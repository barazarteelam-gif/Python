edad=int(input("Edad?"))#El Portero del Club: Un club privado solo permite la entrada a personas mayores de 18 años. Crea un programa que pida la edad y diga si puede pasar 
if edad>=18:
    print("Puede Pasar")
else:
    print("No puedes pasar por ser menor de edad")
 #Control de Temperatura: Si la temperatura de un tanque es mayor a 100°C, mostrar "Alarma: Sobrecalentamiento". 
temperatura=float(input("Temperatura del tanque"))
if temperatura>100:
    print("Alerta: Sobrecalentamiento")
else:
    print("Temperatura Estandar")
#Número Par o Impar: El usuario ingresa un número entero. Determina si el número es par. 
numero=int(input("Ingresa un numero"))
if numero%2==0:
    print(f'{numero} es par')
else:
    print(f'{numero} es impar')
#Validación de Saldo: Un cajero quiere retirar una cantidad X. Si el retiro es menor o igual al saldo, aprobar; si no, rechazar. 
saldo=500
retiro=int(input("Cuanto desea retirar?"))
if retiro<=saldo:
    print("Retiro exitoso")
else:
    print("No puedes retirar mas de lo que ya tienes, saldo insuficiente, retiro rechazado")
#Aprobación de Examen: En la ULA, se aprueba con 10 o más puntos. Crea el validador. 
nota=float(input("Nota del semestre?"))
validacion=True if nota>=10 and nota<=20 else False
if nota>=10 and nota<=20:
    print("Aprobaste el semestre")
    print(validacion)
elif nota<10:
    print("Reprobaste el semestre")
    print(validacion)
else:
    print("Nota Invalida")
# Semáforo Inteligente: Pide un color (rojo, amarillo, verde) y da la instrucción (Pare, Precaución, Siga). 
color=input("Semaforo, un color, rojo, amarillo o verde")
if color=="rojo":
    print("Pare")
elif color=="amarillo":
    print("Precaución")
elif color=="verde":
    print("Siga Avanzando")
else:
    print("Color invalido")
#Categoría de Edad: Clasiffca: 0-12 (Niño), 13-17 (Adolescente), 18-64 (Adulto), 65+ (Anciano). 
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
#Calculadora de Descuento: Si compras más de 10 artículos, tienes 10% de descuento. Si compras más de 20, tienes 20%. Menos de 10, no hay 
#descuento
articulos=int(input("Cuantos articulos vas a comprar?"))
if articulos>=10 and articulos<20:
    print("Tienes 10% de descuento")
elif articulos>=20:
    print("Tienes 20% de descuento")
else:
    print("No hay descuento")
#Tipo de Triángulo: Pide tres lados. Si los tres son iguales: Equilátero. Si dos son iguales: Isósceles. Si todos son diferentes: Escaleno. 
ladoA=float(input("Cuanto mide el primer lado de tu triangulo?"))
ladoB=float(input("Cuanto mide el segundo lado?"))
ladoc=float(input("Cuanto mide el tercer lado?"))
if ladoA == ladoB==ladoc:
    print("Tu triangulo es equilatero")
elif (ladoA!=ladoB or ladoA!=ladoc or ladoB!=ladoc) and ladoA==ladoB or ladoA==ladoc or ladoB==ladoc:
    print("Tu triangulo es Isosceles")
else:
    print("Tu triangulo es escaleno")
#Estaciones del Año: Pide el número de mes (1-12) y devuelve la estación (suponiendo cambios trimestrales). 
mes=int(input("Dame el numero de un mes (1-12)"))
if mes==12 or mes==1 or mes==2:
    print("Invierno")
elif mes==3 or mes==4 or mes==5:
    print("Primavera")
elif mes==6 or mes==7 or mes==8:
    print("Verano")
elif mes==9 or mes==10 or mes==11:
    print("Otoño")
else:
    print("Mes Invalido")
# Beca Universitaria: Un estudiante califfca si su promedio es mayor a 16 Y sus ingresos familiares son menores a $500. 
promedio=int(input("Cual es tu promedio?"))
ingresos=int(input("Ingresos Familiares"))
if promedio>16 and ingresos>500:
    print("Has calificado para conseguir tu beca universitaria")
else:
    print("No has logrado clasificar")

vip=input("Tienes invitacion?")
socio=input("Eres socio Platino?")
# Acceso VIP: Se entra a la zona VIP si se tiene "Invitación" O si se es "Socio Platino". 
if vip=="S" or socio=="S":
    print("Acceso Concedido a VIP")
else:
    print("Acceso Denegado")
#Login de Usuario: Validar que el usuario sea "admin" Y la clave sea "12345". 
usuario="admin"
contraseña=1234
pin=input("Nombre de Usuario?")
password=int(input("Contraseña"))
if pin==usuario and password==contraseña:
    print("Acceso Concedido")
else:
    print("Acceso Denegado")
#Rango de Califfcación: Determinar si una nota ingresada es válida (debe estar entre 0 Y 20). 
rango=float(input("Nota"))
if rango>=0 and rango<=20:
    print("Nota Valida")
else:
    print("Nota Invalida")
#Día Laboral: Pide el nombre del día. Si es "Sábado" O "Domingo", es "Descanso", de lo contrario es "Trabajo". 
dia_laboral=input("Que dia es hoy?").lower
if dia_laboral=="Sabado" or dia_laboral=="Domingo":
    print("Descanso")
elif dia_laboral=="Lunes" or dia_laboral=="Martes" or dia_laboral=="Miercoles" or dia_laboral=="Jueves" or dia_laboral=="Viernes":
    print("Trabajo")
else:
    print("Dia Invalido")
    #Clasificación de Año Bisiesto: Un año es bisiesto si es divisible por 4. Pero si es divisible por 100, no lo es, a menos que también sea divisible por 400. 
año=int(input("Ingresa un año"))
if (año%4==0 or año%400==0) and año%100!=0:
    print(f'{año} es bisiesto')
else:
    print(f'{año} no es bisiesto')
# Triaje Médico: Si el paciente tiene ffebre, preguntar si tiene tos. Si tiene ambos: "Protocolo Respiratorio". Si tiene ffebre pero no tos: "Chequeo General". Si no tiene nada: "Alta". 
fiebre=input("Tienes fiebre?")
if fiebre=="no":
      tos=input("tienes tos?")
      if tos=="no":
           print("Alta")
elif fiebre=="si":
    tos=input("tienes tos?")
    if fiebre=="si" and tos=="si":
        print("Protocolo Respiratorio")
    elif fiebre=="si" and tos=="no":
         print("Chequeo General")
#Impuestos por País y Edad: Si la persona vive en Venezuela y es mayor de 60, no paga impuestos. Si vive en Venezuela y es menor de 60, paga 10%. Si vive en el extranjero, paga 20% sin importar la edad. 
pais=input("Cual es tu pais de origen?")
edad=int(input("Cuantos años tienes?"))
if pais=="venezuela" and edad>60:
    print("No pagaras impuestos")
elif pais=="venezuela" and edad<60:
    print("Pagar 10% de impuestos")
elif pais!="venezuela":
    print("Pagas 20% de impuestos, no importa la edad")
else:
    print("error")
# Juego de Piedra, Papel o Tijera (Lógica de 1 Jugador): Dados los valores de dos jugadores, determina quién gana. (Requiere anidar todas las posibilidades). 
import random
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
    print("empate")

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
