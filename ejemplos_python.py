"""
GUÍA MAESTRA DE PYTHON: REFERENCIA RÁPIDA EJECUTABLE
Este archivo contiene ejemplos de sintaxis para copiar y pegar.
"""

import json
import csv

# =============================================================================
# 1. DICCIONARIOS (dict)
# =============================================================================

def ejemplos_diccionarios():
    # Creación y acceso seguro
    usuario = {"id": 101, "nombre": "Ana", "rol": "Admin"}
    
    # .get() evita errores si la llave no existe
    puntos = usuario.get("puntos", 0) 
    
    # .setdefault() inicializa si no existe
    usuario.setdefault("login_count", 1)
    
    # .update() para fusionar datos
    usuario.update({"ultimo_acceso": "2023-10-27", "activo": True})
    
    # Iteración técnica
    for llave, valor in usuario.items():
        print(f"Propiedad: {llave} -> Valor: {valor}")


# =============================================================================
# 2. CONJUNTOS (set)
# =============================================================================

def ejemplos_sets():
    grupo_a = {"Python", "Java", "C++", "SQL"}
    grupo_b = {"SQL", "PHP", "JavaScript", "Python"}
    
    # Operaciones lógicas
    union = grupo_a | grupo_b             # Todos los lenguajes sin repetir
    interseccion = grupo_a & grupo_b      # Solo los que están en ambos
    diferencia = grupo_a - grupo_b        # En A pero no en B
    simetrica = grupo_a ^ grupo_b        # En uno o en otro, pero NO en ambos
    
    # Gestión de elementos
    grupo_a.add("Rust")
    grupo_a.discard("C++") # No da error si no existe


# =============================================================================
# 3. FUNCIONES Y JERARQUÍA DE PARÁMETROS
# =============================================================================

def funcion_maestra(pos1, pos2, *args, defecto="Valor", **kwargs):
    """
    JERARQUÍA OBLIGATORIA:
    1. Posicionales (pos1, pos2)
    2. *args (Tupla de extras posicionales)
    3. Keyword defaults (defecto)
    4. **kwargs (Diccionario de extras nombrados)
    """
    print(f"Obligatorios: {pos1}, {pos2}")
    print(f"Args (tupla): {args}")
    print(f"Default: {defecto}")
    print(f"Kwargs (dict): {kwargs}")

# Ejemplo de llamada:
# funcion_maestra("A", "B", 1, 2, 3, defecto="Nuevo", debug=True, log="si")


# =============================================================================
# 4. MANEJO DE ERRORES (TypeError)
# =============================================================================

def ejemplos_errores():
    try:
        # Intento de operación de tipos incompatibles
        total = "100" + 50
    except TypeError as e:
        print(f"Error capturado: {e}")
    except Exception as e:
        print(f"Otro error: {e}")
    else:
        print("Operación exitosa")
    finally:
        print("Finalización de bloque de control")

    # Lanzamiento manual de errores
    edad = "veinte"
    if not isinstance(edad, int):
        # raise TypeError("La edad debe ser un número entero")
        pass


# =============================================================================
# 5. FICHEROS (TXT, CSV, JSON)
# =============================================================================

def gestion_ficheros():
    # --- TEXTO PLANO ---
    with open("datos.txt", "w", encoding="utf-8") as f:
        f.write("Línea 1\nLínea 2")

    # --- CSV (con Diccionarios) ---
    datos_csv = [{"id": 1, "msg": "Hola"}, {"id": 2, "msg": "Mundo"}]
    with open("archivo.csv", "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["id", "msg"])
        escritor.writeheader()
        escritor.writerows(datos_csv)

    # --- JSON ---
    config = {"tema": "oscuro", "idioma": "es", "v": 1.2}
    # Guardar
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    
    # Leer
    # with open("config.json", "r") as f:
    #     data = json.load(f)

if __name__ == "__main__":
    print("Ejemplos listos para ser usados.")