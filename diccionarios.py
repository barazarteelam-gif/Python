"""dic1 = {
    "anarcoide":"Que tiende al desorden"
}
dic2 = {
    "enjuiciar":"Instruir, juzgar o sentenciar una causa"
}
print(dic1|dic2)

conjunto = {1,2,3,4,5,6,7,8,9,10}

beatles = set(["Mccartney","Lennon","Harrison","Starr"])
beatles.add("Best")
sorted(beatles)
print(beatles)

def decir_hola():
    print("Hello!")
decir_hola()
def one():
    return 1

value = one()
print(value)

negas = {"Pinchimono","Checker","Ñoñostacio","Paulo","Negas","Poppa","Niño Rata","Veto","Enrike","Lataman","Negas"}
for personajes in negas:
    print(personajes)
#Los elementos de un conjunto no se pueden repetir, el sistema solo imprimirá uno

def ficha_tecnica(**info):
    print("-"*10)
    print("--DETALLES PRODUCTO--")
    for marca,descripcion in info.items():
        print(f"{marca}: {descripcion}")

if __name__ =="__main__":
    ficha_tecnica(marca = "Ipad", Descripcion = "Tablet", Precio = 300)
"""

def num():
    return 1,2,3,4
result = num()
print(type(num))
#CRUD
#CREAR
#LEER
#ELIMINAR
#OBTENER
#ACTUALIZAR

def portero(edad):
  if edad >=18:
     print("Puede Pasar")
  else:
     print("solo puede pasar si esta con un acompañante")
portero(17)