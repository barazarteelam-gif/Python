numero=int(input("Ingresa un numero"))#Numero negativo, positivo, o cero
if numero<0:
    print("Negativo")
elif numero>0:
    print("Positivo")
else:
    print("Cero")

#¿Es mayor de edad?
edad=int(input("Edad?"))
if edad<18:
    print("Menor de Edad")
elif edad>=18 and edad<65:
    print("Adulto")
elif edad>=65:
    print("Adulto Mayor")

#Par o Impar
m=int(input("Ingresa un numero"))
if m%2==0:
    print("Par")
else:
    print("Impar")

#Rango de Numeros
n=int(input("Numero puto, quiero un numero"))
if n<=20 and n>=10:
    print("Esta en el rango")
else:
    print("No esta en el rango")

#Vocal o consonante
l=input("Letra").lower()
if l=="a" or l=="e" or l=="i" or l=="o" or l=="u":
    print("Vocal")
else:
    print("Consonante")

#Año bisiesto
ano=int(input("Año?"))
if (ano%4==0 and ano%400!=0) or (ano%400==0):
   print(f'El año {ano} fue un año bisiesto')
#else:
   print(f'El año {ano} es un año invalido')

#Calculadora de calificaciones
nota = int(input("Nota (0-20): "))

if nota < 0 or nota > 20:
    print("Nota inválida")
elif nota >= 18:
    print(f'Sacaste {nota} - SUPEREXCELENTE')
elif nota >= 16:  # 16-17
    print(f'Sacaste {nota} - Ta bien, felicidades')
elif nota >= 14:  # 14-15
    print(f'Sacaste {nota} - Más o menos, por lo menos pasaste')
elif nota >= 11:  # 11-13
    print(f'Sacaste {nota} - Pasaste, pero échale más ganas')
else:  # 0-10
    print(f'Sacaste {nota} - Reprobaste')

#Dias del mes
mes=input("Elige un mes")
if mes=="enero" or mes=="marzo" or mes=="mayo" or mes=="julio" or mes=="agosto" or mes=="octubre" or mes=="diciembre":
    print(f'{mes} tiene 31 dias')
elif mes=="abril" or mes=="junio" or mes=="septiembre" or mes=="noviembre":
    print(f'{mes} tiene 30 dias')
elif mes=="febrero":
    print(f'{mes} tiene 28 dias')
else:
    print("error")

#Login simple
usuario_correcto="admin"
pass_correcto=1234
pin=input("nombre de usuario?")
password=int(input("Contraseña"))


if pin==usuario_correcto and password==pass_correcto:
    print("Acceso Concedido")
elif pin!=usuario_correcto and password==pass_correcto:
    print("Usuario Incorrecto")
elif pin==usuario_correcto and password!=pass_correcto:
    print("Contraseña incorrecta")
else:
    print("TODO MAL")

#IMC
peso=float(input("Peso?"))
altura=float(input("Altura?"))
IMC=peso/(altura*altura)
if IMC<18.5:
    print("Estas muy flaquito")
elif IMC>=18.5 and IMC<=24.9:
    print("Peso Normal")
elif IMC>=25 and IMC<=29.9:
    print("Sobrepeso")
elif IMC>=30:
    print("Obesidad Morbida, sal a correr y deja los mcdonalds, a la gran puta, estas demasiado gordo/a pinche golem de elixir, tanque de guerra, bola de boliche")

#Calculadora de descuentos
compra = float(input("¿De cuánto fue tu compra? "))
vip = input("¿Eres miembro VIP? (s/n): ")


descuento_vip = 0.05 if vip == "s" else 0 

if compra >= 100 and compra <= 500:
    descuento_monto = 0.10
elif compra >= 501 and compra <= 1000:
    descuento_monto = 0.15
elif compra > 1000:
    descuento_monto = 0.20
else:
    descuento_monto = 0


descuento_final = max(descuento_vip, descuento_monto)
monto_descuento = compra * descuento_final
total = compra - monto_descuento

print(f"Compra: {compra} Soles")
print(f"Descuento aplicado: {descuento_final*100}%")
print(f"Descuento final: {monto_descuento} Soles")
print(f"Monto total: {total} Soles")

