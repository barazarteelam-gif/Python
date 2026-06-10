#Como comparar listas (buscar)
#Como iterar una lista y una tupla (buscar)
matriz = [
    [5,10],
    [15,20]
]
suma_total = 0
for i in range(len(matriz)):
    for j in range(len(matriz[1])):
        valor = matriz[i][j]
        suma_total += valor
        print(f"Iteracion: Fila {i}, columna {j}| Valor encontrado: {valor}| Suma Actual: {suma_total}")
cursos = [
    ["Ana","Luis"],#Seccion A
    ["Marta","Pedro"],#Seccion B
    ["Juan","Sofia"]#Seccion C
]
#El primer for elige el grupo (la lista interna)
for lista_curso in cursos:
    print("---Iniciando nuevo curso---")
    #El segundo for recorre cada nombre dentro de una lista elegida
    for alumno in lista_curso:
        print(f"Alumno: {alumno}")
import time
ruta_entregas = (
    (10.5,20.1)
    ,(15.2,12.8),
    (30.0,45.5)
)
for punto in ruta_entregas:
    print("Analizando punto geografico...")
    time.sleep(3)

    for coordenada in punto:#Punto:Variable para recorrer la matriz
        print(f"Valor: {coordenada}")

velocidad_100km = []
lista_placas = [
    ("PLK-456", (90,95)),
    ("ABC-123",(80,110)),
    ("XYZ-789",(105,105))
                ]
for placa,velo in lista_placas:
    v1,v2 = velo
    for velocidades in velo:
        if velocidades > 100:
            velocidad_100km.append(placa)
            break
print(velocidad_100km)

matriz = [[1, 2], [3, 4], [5, 6]]

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    print(fila[2]) # Accedemos directamente al tercer elemento de cada fila



matriz_tuplas = [
    [("A", 3), ("B", 6)],
    [("C", 9), ("D", 12)]
]
for elemento in matriz_tuplas:
    for letra,numero in elemento:
        print(numero)

datos = [
    [("A", 10, "Activo"), ("B", 20, "Inactivo")],
    [("C", 30, "Activo"), ("D", 40, "Activo")]
]
for estado in datos:
    for letra,numero,actividad in estado:
        if actividad == "Activo":
            print(letra)
       
