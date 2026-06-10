stock_estante = [45, -10,88,120,32,-5,0,110,95,25,-2,105,70,40,15]
stock_real = []
stock_faltante = []
stock_nan = []
for obj in stock_estante:
    if obj < 0:
        stock_real.append(0)
    elif obj > 100:
        stock_real.append(100)
    else:
        stock_real.append(obj)
        falt = 100 - obj
        stock_faltante += str(falt)
print(stock_real)
print(f"Unidades Faltantes {stock_faltante}")


for nan in stock_real:
   if nan <= 0:
        stock_faltante.append(0)
        stock_nan.append(nan)
   elif nan > 100:
        stock_faltante.append(100)
        stock_nan.append(nan)
   else:
       falta = 100 - nan
       stock_faltante.append(falta)
       if nan <= 20:
            stock_nan.append(nan)


print(f"Unidades Para Reponer {stock_faltante}")   

for i,val in enumerate(stock_real):
    if val <= 20:
        print(f"Cantidad Faltante  {val} + posicion {i}")       

      
#Tuplas
mi_tupla = ("pYthon",3.14,True)
mi = mi_tupla[0]
print(tuple(mi))
numeros = (1,2,3,4,5,6,7,8,9)
print(numeros[::-1])
marcas = ("Nike","Adidas","Puma")
for i, v in enumerate(marcas):
   print(f"{i+1}.{v}")


persona = ("Elam",18,"Corea del Norte")
#nombre,edad,pais = persona
#print(edad)

punto = (10,20,30)
print(punto[1])

pelicula = ("Inception",2010,"Christopher Nolan")
titulo,año,actor = pelicula
print(f"Titulo : {titulo}, año: {año}, actor: {actor}")

valores = int(input("INgrese Una Frase")).split(" ")
valor_1,valor_2,valor_3 = valores
print(valor_1,valor_2,valor_3)
tupla = (1,5,3,5,2,5,4,5)
print(tupla.count(5))
print(tupla.index(4))

for i,val in enumerate(tupla):
    if val== 3:
        print(i)
        break

tupla = ("rojo","azul","verde","amarillo")
colores = list(tupla)
colores.append("Naranja")
colores = tuple(colores)
print(colores)



    
 
      
