# CHEAT SHEET PYTHON - PRINCIPIANTE

# Operaciones aritméticas
suma = 5 + 3          
resta = 5 - 3          
multiplicacion = 5 * 3  
division = 5 / 3   
division_entera = 5 // 3
modulo = 5 % 3
potencia = 5 ** 3

# Operaciones de comparación
# (devuelven True o False)
igual = 5 == 3          
distinto = 5 != 3       
mayor = 5 > 3          
menor = 5 < 3           
mayor_igual = 5 >= 3  
menor_igual = 5 <= 3

# Operaciones lógicas
and_logico = (True) and (True)   # True
# and sera verdad solo si los dos valores son verdad

or_logico = (False) or (False)    # False
# or sera verdad si tienes al menos una verdad

not_logico = not (False)         # True
# not cambia de verdad a falso, y de falso a verdad

# FUNCIONES BASICAS
print("mensaje") # muestra por pantalla
nombre = input("mensaje") # entrada de datos
longitud = len("texto") # tamanio del item
tipo = type(5) # tipo de dato
texto = str(123) # conversion a string
numero = int("456") # conversion a entero
decimal = float("7.89") # conversion a float
maximo = max([1, 5, 3]) # maximo: 5
minimo = min([1, 5, 3]) # minimo: 1
suma = sum([1, 2, 3]) # suma: 6
ordenado = sorted([3, 1, 2]) # [1, 2, 3]
secuencia = list(range(5)) # [0, 1, 2, 3, 4]

# STRINGS
texto = "hola mundo"
nombre = "Juan"
f_string = f"Hola {nombre}"
print(texto[0]) # primer caracter
print(texto[-1]) # ultimo caracter
print(texto[0:4]) # slicing [inicio:fin:paso]
print(texto[::-1]) # recorre todo hacia atras
print(texto.lower()) # minusculas
print(texto.upper()) # mayusculas
print("  hola  ".strip()) # elimina espacios
print(texto.split()) # divide en lista
print(texto.replace("hola", "adios")) # reemplazar
print(" ".join(["hola", "mundo"])) # unir lista con texto
print(texto.find("mundo")) # 5 - buscar posicion

# DECISIONES
edad = 18
if edad >= 18:
    print("Mayor de edad")
elif edad >= 13:
    print("Adolescente")
else:
    print("Nino")

# bucle while
contador = 3
while contador > 0:
    print(contador)
    contador -= 1
    if contador == 1:
        break  # salir del ciclo completo

# bucle for
for i in range(30):
    if i == 13:
        continue # saltar a la siguiente iteracion del ciclo
    print(f"Numero: {i}")

# ciclos para recorrer contenedores (strings, listas, tuplas, etc)
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(f"{fruta}")

# enumerate en ciclos
for indice, fruta in enumerate(frutas):
    print(f"Indice {indice}: {fruta}")

# LISTAS
lista_vacia = [] # lista vacia
lista_vacia2 = list() # lista vacia usando constructor
lista = [1, 2, 3] # lista con elementos

# Slicing listas - ejemplos practicos
numeros = [0, 1, 2, 3, 4, 5]
print(numeros[1:4]) # [1, 2, 3] - posiciones 1 a 3
print(numeros[2:]) # [2, 3, 4, 5] - desde posicion 2 hasta final
print(numeros[:3]) # [0, 1, 2] - desde inicio hasta posicion 2
print(numeros[::2]) # [0, 2, 4] - cada 2 elementos
print(numeros[::-1]) # [5, 4, 3, 2, 1, 0] - lista invertida

# CRUD LISTAS
# Create
lista = []
lista.append(10) # anade al final: [10]
lista.insert(0, 5) # inserta en posicion: [5, 10]
lista.extend([15, 20]) # anade multiples: [5, 10, 15, 20]

# Read
print(lista[0]) # 5 - acceder por indice
print(lista[1:3]) # [10, 15] - slicing
print(lista.index(10)) # 1 - encuentra indice
print(15 in lista) # True - verifica existencia

# Update
lista[0] = 25 # modificar elemento: [25, 10, 15, 20]
lista.sort() # ordena la lista: [10, 15, 20, 25]
lista.reverse() # invertir orden: [25, 20, 15, 10]

# Delete
ultimo = lista.pop() # elimina y retorna ultimo: 10, lista: [25, 20, 15]
elemento = lista.pop(1) # elimina por indice: 20, lista: [25, 15]
lista.remove(15) # elimina primera ocurrencia: lista: [25]
del lista[0] # elimina por indice: lista: []
lista.clear() # vacia la lista: []

# TUPLAS
tupla_vacia = () # tupla vacia
tupla_vacia2 = tuple() # tupla vacia con constructor
tupla = (1, 2, 3) # tupla con elementos

# Slicing tuplas - ejemplos practicos
mi_tupla = (0, 1, 2, 3, 4, 5)
print(mi_tupla[1:4]) # (1, 2, 3) - posiciones 1 a 3
print(mi_tupla[2:]) # (2, 3, 4, 5) - desde posicion 2 hasta final
print(mi_tupla[:3]) # (0, 1, 2) - desde inicio hasta posicion 2
print(mi_tupla[::2]) # (0, 2, 4) - cada 2 elementos
print(mi_tupla[::-1]) # (5, 4, 3, 2, 1, 0) - tupla invertida

# CRUD TUPLAS (inmutables - crear nuevas)
# Create
tupla = (1, 2, 3)
nueva_tupla = tupla + (4,) # crear nueva tupla: (1, 2, 3, 4)

# Read
print(tupla[0]) # 1 - acceder por indice
print(tupla[1:3]) # (2, 3) - slicing
print(2 in tupla) # True - verifica existencia

# Update (creando nuevas)
nueva_tupla = tupla[:1] + (99,) + tupla[2:] # (1, 99, 3)

# Delete (creando nuevas)
nueva_tupla = tupla[:1] + tupla[2:] # elimina posicion 1: (1, 3)

# EMPAQUETAR/DESEMPAQUETAR
# Listas/Tuplas
a, b, c = [1, 2, 3] # desempaquetar
tupla_empaquetada = (1, 2, 3)   # empaquetar
tupla_empaquetada = 1, 2, 3     # empaquetar