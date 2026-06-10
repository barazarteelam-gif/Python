#Lista enumerada de asistencia de alumnos
lista_alumnos = ["Migdalia","Cesar","Amparo","Edgar","Juan","Lucero","Ana","Luis","Miguel","Fabiola","Karen","Sofia","Ruben"]
for numero,alumnos in enumerate(lista_alumnos, start=1):
    if numero % 2 == 0:
        print(f"{numero}.{alumnos}")
  

#Gestor de Inventario Dinámico: Crea un sistema que permita registrar productos con sus precios y cantidades. 
registro = [
    ("Leche",20,20),("Mantequilla",20,50),("Queso",30,20),
    ("Carne",30,40),("Pollo",20,50),("Cerdo",25,30),
    ("Arroz",70,20),("Harina",35,30),("Avena",30,25)        
]
precio_total = 0
for producto,precio,stock in registro:
    if stock < 30:
        continue
    precio_total += stock
    print(f"{producto} | {precio}$ | {stock}")
print(f"precio total: {precio_total}$")

#Inventario de stock productos electronicos 
productos = [
    (101, "Teclado", 25.50, 10),
    (102, "Mouse", 15.00, 0),
    (103, "Monitor", 150.00, 5)
]
total = 0
for id_producto,producto,precio,stock in productos:
    total += (precio * stock)
    print(f"{total}$")

#Registro de reabastecimiento de productos con stock menores a 10
inventario = [
    ("Cuadernos", (15, 8)),
    ("Lápices", (20, 25)),
    ("Borradores", (5, 12)),
    ("Marcadores", (3, 4)),
    ("Boligrafos",(5,6))
]
reabastecer = []
for producto, cantidad_en_tienda in inventario:
    for cantidad_en_deposito in cantidad_en_tienda:
       if cantidad_en_deposito < 10:
           reabastecer.append(producto)
           break
print("---------REGISTRO DE INVENTARIO---------")
print("-"*45)
for i in reabastecer:
    print(f"Necesitamos reabastecimiento de: {i}")

#Registro de alumnos con faltas
asistencia = [
    ("Ana", [1, 1, 1, 1, 1]),
    ("Pedro", [1, 0, 1, 1, 1]),
    ("Luis", [1, 1, 1, 0, 0]),
    ("Marta", [1, 1, 1, 1, 1])
]
alumnos_con_faltas = []
for alumno,dias in asistencia:
        for faltas in dias:
            if faltas == 0:
                alumnos_con_faltas.append(alumno)
                break
for i in alumnos_con_faltas:
    print(f"Alumno para bajar puntos por faltas: {i}")

#Alerta de temperatura alta y baja y normal
datos_clima = [
    ("Caracas", (22, 28, 20)),
    ("Maracaibo", (28, 38, 30)),
    ("Mérida", (4, 15, 8)),
    ("Valencia", (24, 30, 24))
]
clima_normal = []
alertas_clima_calor= []
alertas_clima_frio = []
for ciudad,temperatura in datos_clima:
    temp_mañana,temp_tarde,temp_noche = temperatura
    if temp_mañana > 35 or temp_tarde > 35 or temp_noche > 35:
        alertas_clima_calor.append(ciudad)
    elif temp_mañana < 5 or temp_tarde < 5 or temp_noche < 5:
        alertas_clima_frio.append(ciudad)
    else:
        clima_normal.append(ciudad)
print(f"Alerta, temperaturas altas detectadas en {alertas_clima_calor}")
print(f"Alerta, temperaturas bajas detectadas en {alertas_clima_frio}")
print(f"Ciudades con clima templado: {clima_normal}")

#Registro de edades de animales
refugio = [
    ("Max", "Perro", 2),
    ("Luna", "Gato", 1),
    ("Rocky", "Perro", 5),
    ("Toby", "Perro", 1),
    ("Simba", "Gato", 4),
    ("Rex","Perro",6),
    ("Moki","Gato",3),
    ("Bobi","Perro",6)
]
perros_jovenes = []
perros_adultos = []
for animales in refugio:
    nombre,especie,edad = animales
    if edad < 5 and especie == "Perro":
        perros_jovenes.append(nombre)
    elif edad >= 5 and especie == "Perro":
        perros_adultos.append(nombre)
for i in perros_jovenes:
    print(f"Perros con menos de 5 años de edad: {i}")
    print("-"*60)
    print("-"*60)
for j in perros_adultos:
    print(f"Perros con mas de 5 años de edad: {j}")
    print("-"*60)

#Registro de placas con velocidades mayores a 100
placa_100 = []
registro=[("plk-456 ",(90,95)),("ab-123 ",(80,110)),("xyz-789",(105,105)),("mki-345",(50,120)),("kja-675",(70,90)),("ghj-997",(55,95))]
for placa,velo in registro:
    v1,v2 = velo
    for velocidades in velo:
        if v1 > 100 or v2 > 100:
            placa_100.append(placa)
            break
print("\n --- REPORTE DE VELOCIDAD --- ")
print("-"*60)
for i in placa_100:
    print(f"Vehiculo que rebasó los 100 km/h: {i}")
            