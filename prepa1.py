#Iterador: Variable que va a tomar los valores en cada ciclo
#for i in range(10):
#    print(i)
"""cadena = "esto es un str"
print(cadena[3:6])
print(cadena[::-1])
c = "Hola "+ "Mundo"
print(c.lower())
print(c.upper())
print(c.split())"""
texto = "holas mundo"
print(texto.replace("hola","adios"))
print(" EL BARCELONA PASARA A SEMIFINALES HIJUEPUTA ".join(["hola","Mundo"]))

#bucle while
contador = 3
while contador > 0:
    print(contador)
    contador -= 1
    if contador == 0:
        break #Salir del ciclo si la condicion funciona (en este caso)

for i in range(30):
    if i == 15:
        print("Feliz cumpleaños")
        continue
    print(f"dia: {i} de abril")

frutas = ["manzana","banana","naranja"]
for indice, fruta in enumerate(frutas):
    print(f"Indice {indice +1}: {fruta}")


#LISTAS,TUPLAS: Contenedores de elementos
a = [1,2]
a.append(3)
print(a[0:4])
b = (1,2)
b = (3,4)
print(b)

inv = [("Manzana",10),("Piña",7),("Banana",30),("Pera",45),("Naranja",20)]
mayor = (inv[0])
print(inv[1][1])
for f,p in inv:
    print(p)
    if p > mayor[1]:
        mayor =(f,p)
print(mayor)

#Inventario del Heroe (ejercicio) hacer una lista con tuplas en la cual se muestren el nombre de los objetos, la categoria y la cantidad
#IMprimir un resumen eleGANte del inventario.Si tengo 0 cantidad no lo muestro
#Calcular cuantos elementos hay por categoria (arma,armadura o defensa,pociones)
# El ejercicio No esta completo
categoria_arma = 0
categoria_pocion = 0
categoria_armadura = 0 
cantidad = 0
resumen = []
inventario = [("Pocion de vida",5,"pocion"),("Espada de Hierro",1,"arma"),("Espada de Acero",2,"arma"),("Pocion de mana",3,"pocion"),("Pechera de Diamante",2,"Armadura"),("cota de malla",1,"Armadura"),("antidoto",6,"pocion")]
for obj,cantidades,inventarios in inventario:
    cantidad = inventario[1]
    if inventarios == "pocion":
        categoria_pocion += 1
        resumen.append(obj)    
    elif inventarios == "arma":
        categoria_arma += 1
        resumen.append(obj)  
    elif inventarios == "Armadura":
        categoria_armadura += 1
        resumen.append(obj) 
        
print(f"Cantidad de pociones : {categoria_pocion}")                    
print(f"Cantidad de arma : {categoria_arma}")                    
print(f"Cantidad de armadura : {categoria_armadura}")   
print(resumen)
             


   
  
