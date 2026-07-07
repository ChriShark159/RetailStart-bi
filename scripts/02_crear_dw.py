import sqlite3
import os

# ==================================
# CONFIGURACIÓN
# ==================================

DB_PATH = "database/retail_dw.db"


# ==================================
# CREAR DIRECTORIO
# ==================================

def crear_directorio():

    os.makedirs(
        "database",
        exist_ok=True
    )


# ==================================
# CONEXIÓN
# ==================================

def conectar():

    conexion = sqlite3.connect(DB_PATH)

    conexion.execute("PRAGMA foreign_keys = ON")

    return conexion


# ==================================
# DIM CLIENTE
# ==================================

def crear_dim_cliente(cursor):

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS DimCliente (

        cliente_key INTEGER PRIMARY KEY AUTOINCREMENT,

        id_cliente INTEGER NOT NULL UNIQUE,

        nombre TEXT NOT NULL,

        apellido TEXT NOT NULL,

        email TEXT NOT NULL,

        segmento TEXT NOT NULL,

        ciudad TEXT NOT NULL

    )

    """)


# ==================================
# DIM PRODUCTO
# ==================================

def crear_dim_producto(cursor):

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS DimProducto (

        producto_key INTEGER PRIMARY KEY AUTOINCREMENT,

        id_producto INTEGER NOT NULL UNIQUE,

        nombre_producto TEXT NOT NULL,

        categoria TEXT NOT NULL,

        proveedor TEXT NOT NULL,

        precio_base REAL NOT NULL

    )

    """)

# ==================================
# DIM TIEMPO
# ==================================

def crear_dim_tiempo(cursor):

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS DimTiempo (

        fecha_key INTEGER PRIMARY KEY AUTOINCREMENT,

        fecha TEXT NOT NULL UNIQUE,

        dia INTEGER NOT NULL,

        mes INTEGER NOT NULL,

        nombre_mes TEXT NOT NULL,

        trimestre INTEGER NOT NULL,

        anio INTEGER NOT NULL,

        dia_semana TEXT NOT NULL,

        fin_semana TEXT NOT NULL

    )

    """)


# ==================================
# DIM CANAL
# ==================================

def crear_dim_canal(cursor):

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS DimCanal (

        canal_key INTEGER PRIMARY KEY AUTOINCREMENT,

        canal TEXT NOT NULL UNIQUE,

        tipo_canal TEXT NOT NULL

    )

    """)


# ==================================
# DIM TIENDA
# ==================================

def crear_dim_tienda(cursor):

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS DimTienda (

        tienda_key INTEGER PRIMARY KEY AUTOINCREMENT,

        nombre_tienda TEXT NOT NULL UNIQUE,

        region TEXT NOT NULL,

        tipo_tienda TEXT NOT NULL

    )

    """)

# ==================================
# FACT VENTAS
# ==================================

def crear_fact_ventas(cursor):

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS FactVentas (

        id_fact_venta INTEGER PRIMARY KEY AUTOINCREMENT,

        fecha_key INTEGER NOT NULL,

        cliente_key INTEGER NOT NULL,

        producto_key INTEGER NOT NULL,

        canal_key INTEGER NOT NULL,

        tienda_key INTEGER NOT NULL,

        cantidad INTEGER NOT NULL,

        precio_unitario REAL NOT NULL,

        total_venta REAL NOT NULL,

        tipo_venta TEXT NOT NULL,

        FOREIGN KEY (fecha_key)
            REFERENCES DimTiempo(fecha_key),

        FOREIGN KEY (cliente_key)
            REFERENCES DimCliente(cliente_key),

        FOREIGN KEY (producto_key)
            REFERENCES DimProducto(producto_key),

        FOREIGN KEY (canal_key)
            REFERENCES DimCanal(canal_key),

        FOREIGN KEY (tienda_key)
            REFERENCES DimTienda(tienda_key)

    )

    """)

# ==================================
# ÍNDICES
# ==================================

def crear_indices(cursor):

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_fact_fecha
        ON FactVentas(fecha_key)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_fact_cliente
        ON FactVentas(cliente_key)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_fact_producto
        ON FactVentas(producto_key)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_fact_canal
        ON FactVentas(canal_key)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_fact_tienda
        ON FactVentas(tienda_key)
    """)

# ==================================
# MAIN
# ==================================

def main():

    print("=" * 50)
    print("CREANDO DATA WAREHOUSE")
    print("=" * 50)

    crear_directorio()

    conexion = conectar()

    cursor = conexion.cursor()

    crear_dim_cliente(cursor)

    crear_dim_producto(cursor)

    crear_dim_tiempo(cursor)

    crear_dim_canal(cursor)

    crear_dim_tienda(cursor)

    crear_fact_ventas(cursor)

    crear_indices(cursor)

    conexion.commit()

    conexion.close()

    print("\nData Warehouse creado correctamente.")
    print(f"Base de datos: {DB_PATH}")


if __name__ == "__main__":
    main()