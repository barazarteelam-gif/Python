ventas = [ 
 {"cliente": "C001", "boleto": "VIP", "cantidad": 2, "precio": 500, "tipo": "VIP"}, 
 {"cliente": "C002", "boleto": "General", "cantidad": 3, "precio": 120, "tipo": "NORMAL"}, 
 {"cliente": "C003", "boleto": "Preferencial", "cantidad": 1, "precio": 300, "tipo": "NORMAL"}, 
 {"cliente": "C001", "boleto": "General", "cantidad": 2, "precio": 120, "tipo": "VIP"}, 
 {"cliente": "C004", "boleto": "VIP", "cantidad": 1, "precio": 500, "tipo": "NORMAL"}, 
 {"cliente": "C005", "boleto": "General", "cantidad": 5, "precio": 120, "tipo": "VIP"}, 
 {"cliente": "C006", "boleto": "Preferencial", "cantidad": 2, "precio": 300, "tipo": "NORMAL"}, 
 {"cliente": "C002", "boleto": "General", "cantidad": 1, "precio": 120, "tipo": "NORMAL"}, 
 {"cliente": "C007", "boleto": "VIP", "cantidad": 2, "precio": 500, "tipo": "VIP"},  
 {"cliente": "C008", "boleto": "General", "cantidad": 4, "precio": 120, "tipo": "NORMAL"} 
] 

def procesar_ventas_concierto(lista_ventas):
    # Estructuras para acumular los resultados finales
    reporte_clientes = {}
    recaudacion_total = 0.0
    
    for operacion in lista_ventas:
        # 1. Extraemos los datos de la operación actual
        id_cliente = operacion["cliente"]
        cantidad = operacion["cantidad"]
        precio = operacion["precio"]
        tipo_cliente = operacion["tipo"]
        
        # 2. Aplicamos la matemática del enunciado para esta operación
        subtotal = cantidad * precio
        
        if tipo_cliente == "VIP":
            descuento = subtotal * 0.50
        else:
            descuento = 0.0
            
        monto_con_descuento = subtotal - descuento
        iva = monto_con_descuento * 0.16
        total_operacion = monto_con_descuento + iva
        
        # 3. Acumulamos en la recaudación general del concierto
        recaudacion_total += total_operacion
        
        # 4. Guardamos o actualizamos los datos del cliente en el reporte
        if id_cliente not in reporte_clientes:
            # Si es la primera vez que vemos al cliente, lo creamos con sus datos iniciales
            reporte_clientes[id_cliente] = {
                "total_pagado": total_operacion,
                "total_boletos": cantidad
            }
        else:
            # Si ya existía, le SUMAMOS el dinero y los boletos nuevos a lo anterior
            reporte_clientes[id_cliente]["total_pagado"] += total_operacion
            reporte_clientes[id_cliente]["total_boletos"] += cantidad
            
    # Mostramos los resultados consolidados
    print("--- REPORTES POR CLIENTE ---")
    for cliente, datos in reporte_clientes.items():
        print(f"Cliente {cliente} -> Total Pagado: ${datos['total_pagado']:.2f} | Boletos Comprados: {datos['total_boletos']}")
        
    print("\n--- RECAUDACIÓN GENERAL ---")
    print(f"Monto total recaudado por el concierto: ${recaudacion_total:.2f}")

# Corremos la función pasándole la lista del ejercicio
procesar_ventas_concierto(ventas)
asistencias = ["Luis", "Maria", "Luis", "Carlos", "Maria"]
reporte_asistencias = {}

for alumno in asistencias:
    nombre_alumno = alumno  # ej. "Luis"
    
    # 1. Si el alumno NO ESTÁ en nuestra hoja todavía
    if nombre_alumno not in reporte_asistencias:
        # Lo registramos por primera vez y su asistencia arranca en 1
        reporte_asistencias[nombre_alumno] = {
            "Veces que asistio a clase": 1
        }
    # 2. Si el alumno SÍ ESTÁ (ya lo habíamos registrado antes)
    else:
        # Buscamos su carpeta usando su nombre, y le sumamos 1 a sus asistencias
        reporte_asistencias[nombre_alumno]["Veces que asistio a clase"] += 1

print(reporte_asistencias)

#Formula clave para el examen
# LA PLANTILLA UNIVERSAL DE REPORTES

def generar_reporte(lista_de_datos):
    # PASO 1: Tu hoja en blanco (siempre es un diccionario vacío)
    reporte = {}
    
    # PASO 2: El bucle para revisar la lista
    for elemento in lista_de_datos:
        
        # PASO 3: Sacar las variables que necesitas
        clave = elemento["llave_que_se_repite"] # Ej: el cliente o el alumno
        dato_numerico = elemento["un_numero"]  # Ej: el precio o las asistencias
        
        # PASO 4: La estructura fija de decisión
        if clave not in reporte:
            # SI ES NUEVO: Creas la estructura y la arrancas con el dato actual
            reporte[clave] = {
                "total_acumulado": dato_numerico
            }
        else:
            # SI YA EXISTE: Buscas la casilla interna y le SUMAS el dato nuevo
            reporte[clave]["total_acumulado"] += dato_numerico
            
    # PASO 5: Devolver el resultado
    return reporte

reporte_rutas = [ 
    {"unidad": "TRUCK-01", "paquetes": ["PX-100", "PX-102", "PX-105"]}, 
    {"unidad": "TRUCK-02", "paquetes": ["PX-101", "PX-103", "PX-999"]},  
    {"unidad": "VAN-03", "paquetes": ["PX-104"]} 
]

maestro_paquetes = { 
    "PX-100": {"desc": "Laptops", "peso": 15.5, "valor": 3500}, 
    "PX-101": {"desc": "Muebles", "peso": 45.0, "valor": 1200}, 
    "PX-102": {"desc": "Smartphone", "peso": 0.5, "valor": 800}, 
    "PX-103": {"desc": "Monitor 4K", "peso": 8.2, "valor": 600}, 
    "PX-104": {"desc": "Cámara DSLR", "peso": 1.2, "valor": 1500}, 
    "PX-105": {"desc": "Teclados Mecánicos", "peso": 3.0, "valor": 450} 
}

# Iteración básica sobre rutas
# Forma anidada tradicional
for ruta in reporte_rutas:
    for paquete in ruta["paquetes"]:
        print(paquete)