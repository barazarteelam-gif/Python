# PARCIAL PRE-EVALUATIVO: BUCLES, LISTAS Y TUPLAS

**Profesor:** Jesus Diaz
**Tiempo Máximo:** 1 hora y 30 minutos  
**Puntuación:** Nota Base: 20 pts 

---

## INSTRUCCIONES DE ENTREGA
1. **Organización:** Cree una carpeta principal nombrada con su cédula de identidad: `V-XXXXXXXX`.
2. **Archivos:** Guarde la solución de cada ejercicio en archivos Python separados: `ejercicio_1.py`, `ejercicio_2.py` y `ejercicio_3.py`.
3. **Código Limpio:** Es estrictamente obligatorio el uso de nombres de variables descriptivos. Se debe comentar cada bloque de código indicando qué requerimiento resuelve.
4. **Independencia:** La mayoría de los requerimientos están diseñados para resolverse de forma aislada. Si no logra resolver un punto, coméntelo y continúe con el siguiente.
5. **Evaluación:** Cada requerimiento resuelto correctamente suma **1 punto** a la nota final. 
6. **Puntos Extra:** * **Por Perfección:** Se otorgará **1 punto adicional por cada ejercicio** si el estudiante logra cumplir la totalidad de sus requerimientos de manera óptima.
   * **Bono por Rapidez:** El primer estudiante en entregar el examen obtendrá **2 puntos extra**, y el segundo en entregar obtendrá **1 punto extra**. *Nota obligatoria:* Para validar este bono, la entrega debe contar con al menos 5 requerimientos completados correctamente.
7. **Penalización:** El incumplimiento de las normativas de *Organización (1)*, *Archivos (2)* o *Código Limpio (3)* conllevará una deducción de **hasta 5 puntos** sobre la nota final. Esta resta se aplicará después de haber calculado la suma total de puntos obtenidos.

---

## EJERCICIO 1: Procesamiento de Pedidos

**Contexto:** Extracción y cálculo sobre una estructura de datos de comandas de restaurante.

**Requerimientos:**
1. Determinar y almacenar en una variable la cantidad total de pedidos registrados en la lista.
2. Crear una nueva lista que contenga únicamente los nombres de los clientes, omitiendo cualquier otro dato.
3. Extraer a una nueva lista llamada `pedidos_merida` las tuplas completas, de forma intacta, exclusivas de aquellos clientes cuya ciudad sea `"Merida"`.
4. Iterar sobre la lista original e imprimir los datos del cliente y su ciudad. **Es obligatorio imprimir la información siguiendo estrictamente la estructura del siguiente ejemplo:** `El cliente Ana Garcia realizó un pedido desde Merida.`
5. Recorrer la estructura y calcular el costo total (suma de precios) exclusivamente de los platos cuya categoría sea `"Bebida"` en toda la lista de pedidos.
6. Localizar el pedido con `ID: 4` y extraer mediante índices el **nombre del segundo plato** pedido ("Vino"), almacenándolo en una variable de texto.
7. Imprimir el resultado numérico obtenido en el requerimiento 5 bajo el título exacto: `TOTAL RECAUDADO EN BEBIDAS: $ [Monto]`.

**Datos:**
```python
# Estructura: (ID, (Cliente, Ciudad), [(Plato, Precio, Categoria), ...])
pedidos = [
    (1, ("Ana Garcia", "Merida"), [("Pizza", 12.0, "Principal"), ("Soda", 2.5, "Bebida")]),
    (2, ("Luis Perez", "Ejido"), [("Hamburguesa", 8.0, "Principal"), ("Papas", 3.0, "Entrada")]),
    (3, ("Maria Sosa", "Merida"), [("Ensalada", 10.0, "Principal"), ("Agua", 1.5, "Bebida")]),
    (4, ("Jose Rivas", "Tabay"), [("Pasta", 15.0, "Principal"), ("Vino", 20.0, "Bebida")])
]
```

---

## EJERCICIO 2: Gestión de Inventario Automotriz

**Contexto:** Manejo de un inventario dinámico con eliminación y agregación de elementos.

**Requerimientos:**
1. Validar mediante un bucle si existe algún producto en la lista cuyo `Stock` sea exactamente `0`. Retornar e imprimir un booleano (`True` o `False`).
2. Insertar al final de la estructura el siguiente nuevo registro: `(505, "Alternador", [3, 250.0], False)`.
3. Construir una lista nueva que almacene únicamente los **nombres** de los productos cuyo estatus de venta (`Vendido_Status`) sea `True`.
4. Calcular el **Valor Total del Inventario**, multiplicando el `Stock` por el `Precio_Unitario` de cada uno de los ítems existentes, acumulando la suma total.
5. Identificar y almacenar en una variable el **nombre** del producto más costoso según su precio unitario.
6. Buscar y eliminar de la lista original el registro completo correspondiente al `ID: 502`.
7. Imprimir un reporte concatenando los resultados de los requerimientos 4 y 5.

**Datos:**
```python
# Estructura: (ID, Nombre, [Stock, Precio_Unitario], Vendido_Status)
inventario = [
    (501, "Filtro Aceite", [20, 15.0], True),
    (502, "Pastillas Freno", [15, 45.0], False),
    (503, "Bateria 12V", [5, 120.0], True),
    (504, "Bujias x4", [50, 25.0], False),
    (506, "Correa Tiempo", [0, 60.0], False)
]
```

---

## EJERCICIO 3: Análisis de Datos Tecnológicos

**Contexto:** Manipulación de listas mutables anidadas, cálculos de agrupación y ordenamiento.

**Requerimientos:**
1. Generar una lista de tuplas independiente que contenga exclusivamente el par `(Marca, Modelo)` de todos los registros de la lista.
2. Localizar el producto con el modelo `"Redmi Note 12"` y actualizar directamente en la estructura original su `Cantidad_Vendida`, sumándole 5 unidades a su valor actual.
3. Calcular el ingreso proyectado (`Precio * Cantidad_Vendida`) agrupado por **Marca**. El resultado final debe ser una lista de listas o tuplas, por ejemplo: `[("Apple", 7400.0), ("Samsung", 2700.0), ...]`.
4. Recorrer la lista y aplicar un **descuento permanente del 10%** sobre el precio a aquellos productos cuyo valor original sea estrictamente mayor a `$850.0`. Modifique la lista `ventas_tech` de forma directa.
5. Implementar un algoritmo (o función built-in) para **ordenar** la lista completa de mayor a menor basándose en la `Cantidad_Vendida` actual de cada ítem.
6. Imprimir el estado final de los productos iterando la lista resultante. **La salida impresa por cada ciclo debe acatar de forma exacta la sintaxis del siguiente ejemplo:** `[Samsung] S23 Ultra - Unidades Vendidas: 3 - Precio Final: $900.0`

**Datos:**
```python
# Estructura: [(ID, (Marca, Modelo)), Precio, Cantidad_Vendida]
ventas_tech = [
    [(201, ("Apple", "iPhone 15")), 1000.0, 5],
    [(202, ("Samsung", "S23 Ultra")), 900.0, 3],
    [(203, ("Xiaomi", "Redmi Note 12")), 200.0, 10],
    [(204, ("Apple", "MacBook Air")), 1200.0, 2]
]
```