import csv
import json
# import pandas as pd # Requiere: pip install pandas openpyxl

# --- 1. EJEMPLO CSV ---
def ejemplo_csv():
    data = [
        {"id": "001", "nombre": "laptop", "precio": 450.0},
        {"id": "002", "nombre": "mouse", "precio": 15.0}
    ]

    # Guardar CSV
    with open('inventario.csv', 'w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=data[0].keys())
        escritor.writeheader()
        escritor.writerows(data)

    # Cargar CSV
    with open('inventario.csv', 'r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        inventario = list(lector)
        print("CSV Cargado:", inventario)

# --- 2. EJEMPLO JSON ---
def ejemplo_json():
    config = {
        "tienda": "Walmart",
        "sucursal": 102,
        "productos": ["laptop", "mouse"]
    }

    # Guardar JSON
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)

    # Cargar JSON
    with open('config.json', 'r', encoding='utf-8') as f:
        config_cargada = json.load(f)
        print("JSON Cargado:", config_cargada)

# --- 3. EJEMPLO EXCEL (PANDAS) ---
# def ejemplo_excel():
#     data = [
#         {"id": "001", "nombre": "laptop", "precio": 450.0},
#         {"id": "002", "nombre": "mouse", "precio": 15.0}
#     ]

#     # Guardar Excel
#     df = pd.DataFrame(data)
#     df.to_excel('inventario.xlsx', index=False)

#     # Cargar Excel
#     df_leido = pd.read_excel('inventario.xlsx')
#     lista_productos = df_leido.to_dict(orient='records')
#     print("Excel Cargado:", lista_productos)

if __name__ == "__main__":
    ejemplo_csv()
    ejemplo_json()
    # ejemplo_excel() # Descomentar si tienes pandas instalado