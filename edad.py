edad=int(input("Cual es tu edad?"))
if edad >0 and edad <=5:
    print("Eres un bebe gugutata")
elif edad<=13 and edad>5:
    print("Eres un niño, estudie mijo")
elif edad<=18 and edad>5:
    print("Eres un adolescente, porfa no entres a la universidad, vas a sufrir")
elif edad<=65 and edad>18:
    print("Eres un adulto, ya no se te para verdad?, lo lamento mucho")
elif edad>65:
    print("Eres un Anciano, JAJA pinche fosil prehistòrico, hijo de tutankamon, le ganaste a la reina isabel en longevidad ya deberias estar muerto JAJAJA")
else:
    print("Opcion Ivalida")

# 1. Entrada de datos
p1 = float(input("Peso Saco 1: "))
t1 = float(input("Temp Saco 1: "))
h1 = float(input("Hum Saco 1: "))

p2 = float(input("Peso Saco 2: "))
t2 = float(input("Temp Saco 2: "))
h2 = float(input("Hum Saco 2: "))

p3 = float(input("Peso Saco 3: "))
t3 = float(input("Temp Saco 3: "))
h3 = float(input("Hum Saco 3: "))

# 2. Cálculos base (Uso de paréntesis obligatorio para el promedio)
peso_total = p1 + p2 + p3
temp_prom = (t1 + t2 + t3) / 3

# 3. Lógica de Decisión (Estructura de cascada if-elif-else)

# FILTRO DE SEGURIDAD 1: Temperatura (Cualquiera > 25.5)
if t1 > 25.5 or t2 > 25.5 or t3 > 25.5:
    print(f"RECHAZADO: Riesgo de germinación (Una temp > 25.5°C)")

# FILTRO DE SEGURIDAD 2: Humedad (Todas > 15.0)
elif h1 > 15.0 and h2 > 15.0 and h3 > 15.0:
    print(f"RECHAZADO: Riesgo de hongos (Todas las humedades > 15%)")

# Si pasó los filtros, evaluamos ZONAS
else:
    # Determinamos categoría de peso para el mensaje
    categoria_peso = "Pesado" if peso_total > 500 else "Estándar"
    
    # OPCIÓN A: Criogénica
    if peso_total <= 500 and temp_prom < 5.0:
        destino = "Zona A (Criogénica)"
    
    # OPCIÓN B: Estable (Al menos 2 de 3 con humedad < 10)
    # Aquí usamos las 3 combinaciones posibles: (1y2) o (2y3) o (1y3)
    elif (h1 < 10 and h2 < 10) or (h2 < 10 and h3 < 10) or (h1 < 10 and h3 < 10):
        destino = "Zona B (Estable)"
    
    # OPCIÓN C: General (Si no es A ni B)
    else:
        destino = "Zona C (General)"
    
    print(f"ADMITIDO | Peso Total: {peso_total}kg ({categoria_peso})")
    print(f"Promedio Temp: {temp_prom:.2f}°C | Destino: {destino}")



