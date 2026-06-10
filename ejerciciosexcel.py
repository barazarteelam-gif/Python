import pandas as pd

# Datos para tu nueva tabla
datos = {
    "Jugador": ["Simeone", "Griezmann", "Koke", "De Paul"],
    "Estado": ["Cucaracha", "Crack", "Capitán", "Motor"],
    "Goles": [0, 15, 5, 3]
}

df = pd.DataFrame(datos)

# Guardamos como CSV (formato universal que LibreOffice lee perfecto)
nombre_archivo = "reporte_atleti.csv"
df.to_csv(nombre_archivo, index=False)

print(f"¡Archivo '{nombre_archivo}' creado! Ve a tu carpeta y ábrelo con LibreOffice.")