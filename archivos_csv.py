import pandas as pd
import os

FILE = "inventario.csv"

def cargar_datos():
    if not os.path.exists(FILE):
        # Creamos el archivo con cabeceras si no existe
        df = pd.DataFrame(columns=['ID', 'Producto', 'Precio', 'Stock'])
        df.to_csv(FILE, index=False, encoding='utf-8')
        return df
    # Leemos el CSV
    return pd.read_csv(FILE)

# --- 1. CREATE ---
def crear_producto(id_prod, nombre, precio, stock):
    try:
        df = cargar_datos()
        nueva_fila = pd.DataFrame([{'ID': id_prod, 'Producto': nombre, 'Precio': precio, 'Stock': stock}])
        df = pd.concat([df, nueva_fila], ignore_index=True)
        # index=False evita que se guarde una columna extra con los números de fila
        df.to_csv(FILE, index=False, encoding='utf-8')
        print(f"Guardado en CSV: {nombre}")
    except Exception as Error:
        print(f"Error {Error}")
    

# --- 2. READ ---
def leer_productos():
    df = cargar_datos()
    print("\n--- CONTENIDO DEL CSV ---")
    print(df if not df.empty else "Archivo vacío")
    print("-------------------------\n")

# --- 2.1 READ COL(Leer/Consultar) ---
def leer_productos_por_col(col_name):
    df = cargar_datos()
    if df.empty:
        print("El inventario está vacío.")
    else:
        print(F"\n--- INVENTARIO ACTUAL POR COL {col_name.upper()} ---")
        print(df[col_name])
        print("-------------------------\n") 

# --- 3. UPDATE ---
def actualizar_stock(id_prod, nuevo_stock):
    df = cargar_datos()
    if id_prod in df['ID'].values:
        df.loc[df['ID'] == id_prod, 'Stock'] = nuevo_stock
        df.to_csv(FILE, index=False, encoding='utf-8')
        print(f"Stock del ID {id_prod} actualizado.")
    else:
        print("ID no encontrado.")

# --- 4. DELETE ---
def borrar_producto(id_prod):
    df = cargar_datos()
    df = df[df['ID'] != id_prod]
    df.to_csv(FILE, index=False, encoding='utf-8')
    print(f"ID {id_prod} eliminado del CSV.")

# --- PRUEBA ---
if __name__ == "__main__":
    crear_producto(1, "Teclado", 50, 10)
    crear_producto(2, "Monitor", 200, 5)
    leer_productos()
    leer_productos_por_col("ID")
    leer_productos_por_col("Producto")
    leer_productos_por_col("Precio")
    leer_productos_por_col("Stock")
    actualizar_stock(1, 15)
    borrar_producto(2)
    leer_productos()
import pandas as pd

print("###############################")
print("SI PUEDES LEER ESTO, EL PRINT SIRVE")
print("###############################")

file = "inventario_total.csv"

try:
    df = pd.read_csv(file)
    print("Contenido del archivo:")
    print(df)
except Exception as e:
    print(f"Error al leer: {e}")