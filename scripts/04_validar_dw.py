import sqlite3

# ==================================
# CONFIGURACIÓN
# ==================================

DB_PATH = "database/retail_dw.db"


# ==================================
# CONEXIÓN
# ==================================

def conectar():

    conn = sqlite3.connect(DB_PATH)

    conn.execute("PRAGMA foreign_keys = ON")

    return conn


# ==================================
# CONTAR REGISTROS
# ==================================

def contar_registros(conn):

    print("\n" + "=" * 50)
    print("REGISTROS DEL DATA WAREHOUSE")
    print("=" * 50)

    tablas = [

        "DimCliente",
        "DimProducto",
        "DimTiempo",
        "DimCanal",
        "DimTienda",
        "FactVentas"

    ]

    for tabla in tablas:

        cursor = conn.execute(

            f"SELECT COUNT(*) FROM {tabla}"

        )

        total = cursor.fetchone()[0]

        print(f"{tabla:<15}: {total}")


# ==================================
# VALIDAR NULOS
# ==================================

def validar_nulos(conn):

    print("\n" + "=" * 50)
    print("VALIDACIÓN DE VALORES NULOS")
    print("=" * 50)

    cursor = conn.execute("""

    SELECT COUNT(*)

    FROM FactVentas

    WHERE

        fecha_key IS NULL
        OR cliente_key IS NULL
        OR producto_key IS NULL
        OR canal_key IS NULL
        OR tienda_key IS NULL
        OR cantidad IS NULL
        OR precio_unitario IS NULL
        OR total_venta IS NULL
        OR tipo_venta IS NULL

    """)

    nulos = cursor.fetchone()[0]

    if nulos == 0:

        print("FactVentas ............. OK")

    else:

        print(f"FactVentas ............. {nulos} registros con valores nulos")


# ==================================
# VALIDAR INTEGRIDAD REFERENCIAL
# ==================================

def validar_integridad(conn):

    print("\n" + "=" * 50)
    print("VALIDACIÓN REFERENCIAL")
    print("=" * 50)

    consultas = {

        "Clientes":

        """
        SELECT COUNT(*)
        FROM FactVentas f
        LEFT JOIN DimCliente d
        ON f.cliente_key = d.cliente_key
        WHERE d.cliente_key IS NULL
        """,

        "Productos":

        """
        SELECT COUNT(*)
        FROM FactVentas f
        LEFT JOIN DimProducto d
        ON f.producto_key = d.producto_key
        WHERE d.producto_key IS NULL
        """,

        "Tiempo":

        """
        SELECT COUNT(*)
        FROM FactVentas f
        LEFT JOIN DimTiempo d
        ON f.fecha_key = d.fecha_key
        WHERE d.fecha_key IS NULL
        """,

        "Canales":

        """
        SELECT COUNT(*)
        FROM FactVentas f
        LEFT JOIN DimCanal d
        ON f.canal_key = d.canal_key
        WHERE d.canal_key IS NULL
        """,

        "Tiendas":

        """
        SELECT COUNT(*)
        FROM FactVentas f
        LEFT JOIN DimTienda d
        ON f.tienda_key = d.tienda_key
        WHERE d.tienda_key IS NULL
        """

    }

    for nombre, consulta in consultas.items():

        cursor = conn.execute(consulta)

        errores = cursor.fetchone()[0]

        if errores == 0:

            print(f"{nombre:<10}: OK")

        else:

            print(f"{nombre:<10}: {errores} errores")


# ==================================
# RESUMEN DE VENTAS
# ==================================

def resumen_ventas(conn):

    print("\n" + "=" * 50)
    print("RESUMEN GENERAL")
    print("=" * 50)

    cursor = conn.execute("""

    SELECT

        COUNT(*),
        SUM(total_venta),
        AVG(total_venta)

    FROM FactVentas

    """)

    cantidad, total, promedio = cursor.fetchone()

    if total is None:
        total = 0

    if promedio is None:
        promedio = 0

    print(f"Cantidad de ventas : {cantidad}")
    print(f"Ventas totales     : ${total:,.0f}")
    print(f"Venta promedio     : ${promedio:,.0f}")

# ==================================
# MAIN
# ==================================

def main():

    print("=" * 50)
    print("VALIDACIÓN DEL DATA WAREHOUSE")
    print("=" * 50)

    conn = conectar()

    contar_registros(conn)

    validar_nulos(conn)

    validar_integridad(conn)

    resumen_ventas(conn)

    conn.close()

    print("\n" + "=" * 50)
    print("VALIDACIÓN FINALIZADA")
    print("=" * 50)


if __name__ == "__main__":

    main()