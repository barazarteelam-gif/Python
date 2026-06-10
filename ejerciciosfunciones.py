"""def suma(a, b): return a + b
def resta(a, b): return a - b
def multi(a, b): return a * b 
def div(a, b): return a / b



alumnos = [("Ana",10),("Luis",6),("Pedro",7)]
with open ("Reporte.txt","w",encoding= "utf-8") as f:
    f.write("REPORTE DE NOTAS")
    f.write("-"*20+"\n")
    for nombre,nota in alumnos:
        f.write(f"Alumnos:{nombre:<10}| Nota: {nota:>2}\n")
historial = [] 

try: 
    op = int(input("Operación (1:Suma, 2:Resta, 3:Multi, 4:Div): "))
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    
    res = 0
    nombre_op = ""

    if op == 1:
        res = suma(n1, n2)
        nombre_op = "Suma"
    elif op == 2:
        res = resta(n1, n2)
        nombre_op = "Resta"
    elif op == 3:
        res = multi(n1, n2)
        nombre_op = "Multiplicación"
    elif op == 4:
        res = div(n1, n2)
        nombre_op = "División"
    
    if nombre_op != "":
        # AGREGAMOS TODO AQUÍ (Una sola vez)
        historial.append({
            "operacion": nombre_op, 
            "n1": n1, 
            "n2": n2, 
            "resultado": res
        })
        print(f"✅ Resultado: {res}")

except ZeroDivisionError:
    print("❌ No puedes dividir entre cero")
except ValueError:
    print("❌ Caracteres inválidos")

# --- RESUMEN FINAL ---
# Ahora el bucle solo lee, no añade nada.
print("\n" + "="*30)
print("--- RESUMEN DE TU ACTIVIDAD ---")
for e in historial:
    print(f"Operación: {e['operacion']} -> {e['n1']} y {e['n2']} = {e['resultado']}")



inventario = [
    {"nombre": "Teclado", "precio": 50, "stock": 10},
    {"nombre": "Mouse", "precio": 20, "stock": 5},
    {"nombre": "Monitor", "precio": 200, "stock": 2}
]

def procesar_venta(lista_inventario):
    comprar_producto = input("¿Qué desea comprar? ").capitalize()
    
    for items in lista_inventario:
        # 1. Buscamos coincidencia exacta
        if items["nombre"] == comprar_producto:
            cantidad_deseada = int(input(f"¿Cuántos {comprar_producto} desea comprar? "))
            
            # 2. Verificamos stock
            if cantidad_deseada <= items["stock"]:
                # CALCULAMOS
                monto_total = items["precio"] * cantidad_deseada
                
                # ACTUALIZAMOS EL DICCIONARIO REAL (Esto es la clave)
                items["stock"] -= cantidad_deseada 
                
                print(f"✅ Venta exitosa. Total a cobrar: ${monto_total}")
                return items["stock"], monto_total # Salimos de la función con éxito
            else:
                print(f"❌ No tenemos esa cantidad. Solo quedan {items['stock']} unidades.")
                return None, 0 # Salimos porque no hubo venta
                
    # 3. Si el bucle termina y nunca entró al IF de coincidencia:
    print("❌ El producto no existe en el inventario.")
    return None, 0

# Ejecución
stock_actual, total_pago = procesar_venta(inventario)

print("-" * 30)
if stock_actual is not None:
    print(f"Stock restante del producto vendido: {stock_actual}")
print(f"Inventario completo actualizado: {inventario}")



estudiantes = [
    {"nombre": "Ana", "notas": [8, 9, 10], "asistencia": 95},
    {"nombre": "Luis", "notas": [4, 5, 3], "asistencia": 80},
    {"nombre": "Marta", "notas": [7, 8, 7], "asistencia": 60},
    {"nombre": "Juan", "notas": [10, 10, 9], "asistencia": 100}
]

def buscar_estudiante(lista):
    # 1. Pedimos el nombre una sola vez fuera del bucle
    busqueda = input("Ingrese el nombre del alumno: ").capitalize()
    
    # 2. Variable "bandera" para saber si lo encontramos
    encontrado = False

    for alumno in lista:
        if alumno["nombre"] == busqueda:
            print(f"✅ El/la estudiante {busqueda} tiene {alumno['asistencia']}% de asistencia.")
            encontrado = True
            break  # ¡Importante! Si ya lo encontramos, dejamos de buscar.
    
    # 3. Si después de revisar toda la lista, 'encontrado' sigue siendo False:
    if not encontrado:
        print(f"❌ El/la estudiante {busqueda} no existe en el registro.")

buscar_estudiante(estudiantes)
"""

"""personajes = [
    {"nombre": "Aragorn", "clase": "Guerrero", "nivel": 20},
    {"nombre": "Gandalf", "clase": "Mago", "nivel": 25},
    {"nombre": "Legolas", "clase": "Arquero", "nivel": 18},
    {"nombre": "Gimli", "clase": "Guerrero", "nivel": 19}
]
mayor_al_minimo = []
def filtrar_por_nivel(lista,nivel_minimo):
    for c in lista:
        k = c["nombre"]
        if c["nivel"] >= nivel_minimo:
            mayor_al_minimo.append(k)

    print(f"Los personajes mas fuertes son: {mayor_al_minimo}")
filtrar_por_nivel(personajes,20)"""


"""
while True:
    nombre = input("Dime tu nombre: ")
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"Nombre del Usuario: {nombre}" + "\n") 
    salida = input("Deseas Salir?").capitalize()
    if salida == "Si":
        break
print("Nombres guardados con éxito.")
"""
