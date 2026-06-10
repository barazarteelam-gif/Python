"""
dicc = {"a":10,"b":15,"c":20}
print(dicc.get("c"),"no existe")
dicc.update({"c":30})
for k, v in dicc.items():
    print(f"Clave: {k}, Valor: {v}")
for v in dicc.values():
    print(f"Valores: {v}")
for k in dicc.keys():
    print(f"Claves:{k}")


a = {2,3,5,7}
b = {7,3,2,4,6,8}
c = set()
for i in b:
    if i not in a:
        c.add(i)
print(c)

def agregar_marcas_porno(x):
    for i,j in x.items():
        if j == "Porno":
            porno.add(i)
def agregar_cosas_santas(x):
        for i,j in x.items():
            if not j == "Porno":
                Cosas_santas.add(i) 


x = {"XNXX":"Porno","Asus":"Laptops","Brazzers":"Porno","Tecno":"Celulares","Nintendo":"Videojuegos","Minalba":"Agua","Harina Pan":"Comida","Pornhub":"Porno"}
porno = set()
Cosas_santas = set()
for r in x.values():
    if r == "Porno":
        agregar_marcas_porno(x)
    else:
        agregar_cosas_santas(x)
print(f"Cosas Pervertidas y del diablo {porno}")
print(f"Cosas no Pervertidas {Cosas_santas}")


def papas(*args):
    return args
print(papas("Carne","Queso","Arroz","Pollo"))

def sal(**kwargs):
    return kwargs


try:
    a = int(input("Ingresa Un numero"))
    b = int(input("Ingresa un numero"))
    print(a//b)
    
except Exception as error:
    print(f"Error de: {error}")"""
