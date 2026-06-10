import os
import pandas as pd

# 1. Definir el nombre del archivo
file = "inventario.csv"

# 2. Cargar o crear el DataFrame (df)
if not os.path.exists(file):
    df = pd.DataFrame(columns=["Precio", "Stock"])
else:
    df = pd.read_csv(file, encoding="utf-8")

# 3. Agregar datos (Asegúrate de asignar el resultado a df)
nueva_fila = pd.DataFrame({"Precio": [500], "Stock": [50]})
df = pd.concat([df, nueva_fila], ignore_index=True)

# 4. Guardar (Es df.to_csv, NO pd.to_csv)
df.to_csv(file, index=False, encoding="utf-8")

# --- FUNCIONES CORREGIDAS ---
def imprimir_precio():
    print("\n--- Contenido de columna Precio ---")
    print(df["Precio"]) # Usamos df, no pd

def imprimir_stock():
    print("\n--- Contenido de columna Stock ---")
    print(df["Stock"])

# --- EJECUCIÓN ---
# El print de abajo ES LA PRUEBA de que el programa corre
print(">>> INICIANDO REPORTE DE INVENTARIO <<<")

total = 500 * 50
imprimir_precio()
imprimir_stock()
print(f"\nTOTAL CALCULADO: {total}")