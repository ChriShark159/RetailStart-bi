import os
import sqlite3
import pandas as pd

# ==================================
# CONFIGURACIÓN
# ==================================

DB_PATH = "database/retail_dw.db"

RUTA_CLIENTES = "data/clientes.csv"
RUTA_PRODUCTOS = "data/productos.csv"
RUTA_TIEMPO = "data/tiempo.csv"
RUTA_CANALES = "data/canales.csv"
RUTA_TIENDAS = "data/tiendas.csv"
RUTA_VENTAS = "data/ventas.csv"

RUTA_EXPORT = "export"

# ==================================
# CONEXIÓN SQLITE
# ==================================

def conectar():

    if not os.path.exists(DB_PATH):

        raise FileNotFoundError(
            f"No existe la base de datos: {DB_PATH}\n"
            "Primero ejecuta 02_crear_dw.py"
        )

    return sqlite3.connect(DB_PATH)

# ==================================
# CARGAR CSV
# ==================================

def cargar_csv():

    clientes = pd.read_csv(RUTA_CLIENTES)

    productos = pd.read_csv(RUTA_PRODUCTOS)

    tiempo = pd.read_csv(RUTA_TIEMPO)

    canales = pd.read_csv(RUTA_CANALES)

    tiendas = pd.read_csv(RUTA_TIENDAS)

    ventas = pd.read_csv(RUTA_VENTAS)

    return (
        clientes,
        productos,
        tiempo,
        canales,
        tiendas,
        ventas
    )
    
# ==================================
# CARGAR DIMCLIENTE
# ==================================

def cargar_dim_cliente(conn, df_clientes):

    cursor = conn.cursor()

    print("Cargando DimCliente...")

    for _, row in df_clientes.iterrows():

        cursor.execute("""

        INSERT INTO DimCliente
        (
            id_cliente,
            nombre,
            apellido,
            email,
            segmento,
            ciudad
        )

        VALUES (?, ?, ?, ?, ?, ?)

        """,

        (
            int(row["id_cliente"]),
            row["nombre"],
            row["apellido"],
            row["email"],
            row["segmento"],
            row["ciudad"]
        ))

    conn.commit()

    clientes_map = {}

    cursor.execute("""

        SELECT
            cliente_key,
            id_cliente
        FROM DimCliente

    """)

    for cliente_key, id_cliente in cursor.fetchall():

        clientes_map[id_cliente] = cliente_key

    print(f"✔ DimCliente cargada ({len(clientes_map)} registros)")

    return clientes_map

# ==================================
# CARGAR DIMPRODUCTO
# ==================================

def cargar_dim_producto(conn, df_productos):

    cursor = conn.cursor()

    print("Cargando DimProducto...")

    for _, row in df_productos.iterrows():

        cursor.execute("""

        INSERT INTO DimProducto
        (
            id_producto,
            nombre_producto,
            categoria,
            proveedor,
            precio_base
        )

        VALUES (?, ?, ?, ?, ?)

        """,

        (
            int(row["id_producto"]),
            row["nombre_producto"],
            row["categoria"],
            row["proveedor"],
            float(row["precio_base"])
        ))

    conn.commit()

    productos_map = {}

    cursor.execute("""

        SELECT
            producto_key,
            id_producto
        FROM DimProducto

    """)

    for producto_key, id_producto in cursor.fetchall():

        productos_map[id_producto] = producto_key

    print(f"✔ DimProducto cargada ({len(productos_map)} registros)")

    return productos_map

# ==================================
# CARGAR DIMTIEMPO
# ==================================

def cargar_dim_tiempo(conn, df_tiempo):

    cursor = conn.cursor()

    print("Cargando DimTiempo...")

    for _, row in df_tiempo.iterrows():

        cursor.execute("""

        INSERT INTO DimTiempo
        (
            fecha,
            dia,
            mes,
            nombre_mes,
            trimestre,
            anio,
            dia_semana,
            fin_semana
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)

        """,

        (
            row["fecha"],
            int(row["dia"]),
            int(row["mes"]),
            row["nombre_mes"],
            int(row["trimestre"]),
            int(row["anio"]),
            row["dia_semana"],
            row["fin_semana"]
        ))

    conn.commit()

    tiempo_map = {}

    cursor.execute("""

        SELECT
            fecha_key,
            fecha
        FROM DimTiempo

    """)

    for fecha_key, fecha in cursor.fetchall():

        tiempo_map[fecha] = fecha_key

    print(f"✔ DimTiempo cargada ({len(tiempo_map)} registros)")

    return tiempo_map

# ==================================
# DIM CANAL
# ==================================

def cargar_dim_canal(conn, df_canales):

    cursor = conn.cursor()

    for _, row in df_canales.iterrows():

        cursor.execute("""

        INSERT INTO DimCanal
        (
            canal,
            tipo_canal
        )

        VALUES (?, ?)

        """,

        (
            row["canal"],
            row["tipo_canal"]
        ))

    conn.commit()

    canales_map = {}

    cursor.execute("""

    SELECT
        canal_key,
        canal
    FROM DimCanal

    """)

    for canal_key, canal in cursor.fetchall():

        canales_map[canal] = canal_key

    print(f"Canales cargados: {len(canales_map)}")

    return canales_map

# ==================================
# CARGAR DIMTIENDA
# ==================================

def cargar_dim_tienda(conn, df_tiendas):

    cursor = conn.cursor()

    print("Cargando DimTienda...")

    for _, row in df_tiendas.iterrows():

        cursor.execute("""

        INSERT INTO DimTienda
        (
            nombre_tienda,
            region,
            tipo_tienda
        )

        VALUES (?, ?, ?)

        """,

        (
            row["nombre_tienda"],
            row["region"],
            row["tipo_tienda"]
        ))

    conn.commit()

    tiendas_map = {}

    cursor.execute("""

        SELECT
            tienda_key,
            nombre_tienda
        FROM DimTienda

    """)

    for tienda_key, nombre_tienda in cursor.fetchall():

        tiendas_map[nombre_tienda] = tienda_key

    print(f"✔ DimTienda cargada ({len(tiendas_map)} registros)")

    return tiendas_map

# ==================================
# CARGAR FACTVENTAS
# ==================================

def cargar_fact_ventas(
    conn,
    df_ventas,
    clientes_map,
    productos_map,
    tiempo_map,
    canales_map,
    tiendas_map
):

    cursor = conn.cursor()

    print("Cargando FactVentas...")

    total_insertadas = 0

    for _, row in df_ventas.iterrows():

        fecha_key = tiempo_map[row["fecha"]]

        cliente_key = clientes_map[int(row["id_cliente"])]

        producto_key = productos_map[int(row["id_producto"])]

        canal_key = canales_map[row["canal"]]

        tienda_key = tiendas_map[row["tienda"]]

        cantidad = int(row["cantidad"])

        precio_unitario = float(row["precio_unitario"])

        total_venta = cantidad * precio_unitario

        cursor.execute("""

        INSERT INTO FactVentas
        (
            fecha_key,
            cliente_key,
            producto_key,
            canal_key,
            tienda_key,
            cantidad,
            precio_unitario,
            total_venta,
            tipo_venta
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

        """,

        (

            fecha_key,

            cliente_key,

            producto_key,

            canal_key,

            tienda_key,

            cantidad,

            precio_unitario,

            total_venta,

            row["tipo_venta"]

        ))

        total_insertadas += 1

    conn.commit()

    print(f"✔ FactVentas cargada ({total_insertadas} registros)")
    
# ==================================
# EXPORTAR PARA POWER BI
# ==================================

def exportar_powerbi(conn):

    os.makedirs(RUTA_EXPORT, exist_ok=True)

    tablas = [

        "DimCliente",
        "DimProducto",
        "DimTiempo",
        "DimCanal",
        "DimTienda",
        "FactVentas"

    ]

    print("\nExportando tablas para Power BI...\n")

    for tabla in tablas:

        df = pd.read_sql_query(

            f"SELECT * FROM {tabla}",

            conn

        )

        # Convertir columnas numéricas enteras para que no exporten .0
        for columna in df.columns:

            if pd.api.types.is_float_dtype(df[columna]):

                if (df[columna] % 1 == 0).all():

                    df[columna] = df[columna].astype("Int64")

        ruta = os.path.join(

            RUTA_EXPORT,

            f"{tabla}.csv"

        )

        df.to_csv(

            ruta,

            index=False,
            encoding="utf-8-sig"

        )

        print(f"✔ {tabla}.csv ({len(df)} registros)")

# ==================================
# MAIN
# ==================================

def main():

    print("=" * 50)
    print("INICIANDO PROCESO ETL")
    print("=" * 50)

    # Conectar a SQLite
    conn = conectar()

    # Leer CSV
    (
        df_clientes,
        df_productos,
        df_tiempo,
        df_canales,
        df_tiendas,
        df_ventas
    ) = cargar_csv()

    # Cargar dimensiones
    clientes_map = cargar_dim_cliente(conn, df_clientes)

    productos_map = cargar_dim_producto(conn, df_productos)

    tiempo_map = cargar_dim_tiempo(conn, df_tiempo)

    canales_map = cargar_dim_canal(conn, df_canales)

    tiendas_map = cargar_dim_tienda(conn, df_tiendas)

    # Cargar tabla de hechos
    cargar_fact_ventas(
        conn,
        df_ventas,
        clientes_map,
        productos_map,
        tiempo_map,
        canales_map,
        tiendas_map
    )

    # Exportar CSV para Power BI
    exportar_powerbi(conn)

    # Cerrar conexión
    conn.close()

    print("\n" + "=" * 50)
    print("PROCESO ETL FINALIZADO")
    print("=" * 50)

    print(f"\nBase de datos: {DB_PATH}")
    print(f"Archivos exportados en: {RUTA_EXPORT}")


if __name__ == "__main__":
    main()
        