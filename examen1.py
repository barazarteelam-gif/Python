
contador = 0
while contador < 10:
    contador = contador + 1
    print(contador)
contador = -11
while contador < -1:
   contador = contador + 1
print(contador)


for i in range(-11,-1,1):
   i+=1
print(i)

for h in range(-1,4,1):
   h+=1
   print(h)
print("¡Hecho!")

n = int(input("Ingresa un numero papi"))
for n in range(1,n+1):
   print(n)

#Take input from user and convert to integer
n = int(input("Enter number: "))

# Variable to store the sum
s = 0
n=0
#Loop from 1 to n (n+1 is used because range is exclusive)
for i in range(1, n + 1):
    s += i

print("Sum is:", s)

pts = float(input("Ingrese el precio del producto"))
puntaje = 0
while pts != 0:
    pts = float(input("Ingrese el precio del producto"))
    puntaje += 1
print(f"Puntaje Total Obtenido: {puntaje}")
for piso in [1, 2]:
    print(f"Subiendo al piso {piso}")
    for habitacion in [1, 2, 3]:
        print(f"   Limpiando habitación {habitacion}")

especies = ["Perro","Gato","Loro","Hamsters"]
Tiempo = ["Mañana","Tarde","Noche"]
for animal in especies:
      if animal != "Gato":
         continue
      print(animal)
      for momento in Tiempo:
           if momento != "Noche" :
            continue
    
      print(f"Servir comida en la {momento}")
    
      print("-" * 10)
      #Rectangulo
for i in range(5):
    for j in range(10):
        print("*",end="")
    print()
#Tabla de multiplicar
for i in range(1,11):
    for j in range(1,11):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()
#Los relojes comienzan desde 0
import time
for horas in range(1,25):
   for minutos in range(0,60):
      for segundos in range(0,60):
         time.sleep(1)
         print(f'Horas: {horas} Minuto: {minutos} Segundo: {segundos}')


tanque = 500
i = 0
while tanque > 0:
    consumo = input("Cuanto combustible se ha consumido en una hora?")
    if not consumo.replace(".","",1).isdigit():
        print("Error: no texto solo numero")
        continue
    consumo = float(consumo)
    if consumo < 0:
        print("Error: Datos numericos invalidos")
        continue 
    tanque = tanque - consumo
    i += 1
print(f"Alerta de tanque vacio")
print("-" * 10)
print(f"Horas Totales de resistencia del tanque : {i}")
