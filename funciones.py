"""def nombre(nombre):
    print(nombre + " es una cucaracha")
nombre("El cholo Simeone")
def risa(pendejos):
    print(pendejos + " Perdio un titulo JAJAJAJAJA, Que imbeciles idiotas de mierda")
risa(pendejos = "El Atletico de Madrid")"""
#Las funciones son como una caja donde guardas codigo
#  y lo que haces con ellas es llamarlas en el momento preciso para usarlas

def agregar_cosas(objeto, cantidad):
    # El modo "a" crea el archivo si no existe, así que no necesita try aquí
    with open("mochila.txt", "a") as inventario_actualizado:
        inventario_actualizado.write(f"Item: {objeto}, cantidad: {cantidad}|\n")

def leer_inventario():
    try:
        with open("mochila.txt", "r") as archivo:
            return archivo.read()
    except FileNotFoundError:
        # Aquí es donde el escudo es útil
        return "⚠️ El Cholo se robó la mochila (Aún no hay archivo de inventario)."

def escribir_inventario():
    # Simplificamos: esta función solo llama a la lectura
    return leer_inventario()

cantidad_total = 0

try:
    while True:
        print("\n1. Agregar al Inventario")
        print("2. Ver la mochila")
        print("3. Salir")
        
        opcion = int(input("Ingrese qué opción desea: "))
        
        if opcion == 1:
            objeto = input("Objeto: ")
            cantidad = int(input("Cantidad: "))
            cantidad_total += cantidad
            agregar_cosas(objeto, cantidad)
        elif opcion == 2:
            print(leer_inventario())
        elif opcion == 3:
            break
        else:
            print("Esa opción no existe.")

except ValueError:
    print("❌ Caracteres inválidos. El programa se cerró por tu culpa.")

print("Has salido del programa.")
    

        
