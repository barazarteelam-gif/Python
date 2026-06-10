lenguajes = ["c","java"]
lenguajes.append("Python")
lenguajes.insert(1,"Rust")
print(lenguajes)

colores = ["Rojo", "Verde","Amarillo","Azul","Gris"]
print(colores[2])
frutas = ["Fresa","Sandia","Manzana","Pera"]
frutas[1] = "uva"
print(frutas)

numeros = []
numeros.append(10)
numeros.append(20)
numeros.append(30)
numeros.insert(0,5)
numeros.remove(20)
print(numeros)

letras = ["a","b","c","d","e","f","g"]
print(letras[0:3])
print(letras[5:7])
print(letras[::-1])

suma = [13,6,7,8,7]
print(sum(suma))
print(min(suma))
print(max(suma))

edades = [18, 25, 40, 12, 33, 55, 7]
print(min(edades))

need = 10
cont = 0
notas = [10,6,9,7,6,9,10]
print(notas.count(10))
for num in notas:
    if need==num:
        cont+=1
print(cont)

mx = [10, "python", 20 ,"codigo",30]
num = []
for mn in mx:
    if type(mn)==int:
        num.append(mn)
print(num)
print(type(mx))