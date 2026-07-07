import os
import random
import pandas as pd
from datetime import datetime, timedelta


# ==================================
# CONFIGURACIÓN
# ==================================

RUTA_DATA = "data"

NUM_CLIENTES = 20
NUM_PRODUCTOS = 15
NUM_VENTAS = 100
NUM_DIAS = 10

random.seed(42)


# ==================================
# NOMBRES
# ==================================

NOMBRES = [

    "Juan",
    "Ana",
    "Carlos",
    "María",
    "Pedro",
    "Laura",
    "Diego",
    "Sofía",
    "Andrés",
    "Camila",

    "Javier",
    "Valentina",
    "Tomás",
    "Fernanda",
    "Ignacio",
    "Paula",
    "Felipe",
    "Daniela",
    "Matías",
    "Constanza"

]


APELLIDOS = [

    "Pérez",
    "Gómez",
    "Rojas",
    "López",
    "Díaz",
    "Martínez",
    "Soto",
    "Reyes",
    "Castro",
    "Vega",

    "Muñoz",
    "Silva",
    "Torres",
    "Navarro",
    "Herrera",
    "Morales",
    "Fuentes",
    "Vargas",
    "Araya",
    "Cortés"

]


# ==================================
# SEGMENTOS
# ==================================

SEGMENTOS = (

    ["Premium"] * 6 +
    ["Regular"] * 8 +
    ["Nuevo"] * 6

)

random.shuffle(SEGMENTOS)
# ==================================
# CIUDADES
# ==================================

CIUDADES = [

    "Santiago",
    "Valparaíso",
    "Concepción",
    "Antofagasta",
    "Temuco",
    "La Serena",
    "Rancagua",
    "Puerto Montt"

]


# ==================================
# PRODUCTOS
# ==================================

PRODUCTOS = [

    (2001, "Notebook Lenovo", "Tecnología", "Lenovo", 140000),
    (2002, "Smartphone Samsung", "Tecnología", "Samsung", 280000),
    (2003, "Tablet Huawei", "Tecnología", "Huawei", 180000),
    (2004, "Monitor Dell", "Tecnología", "Dell", 160000),
    (2005, "Audífonos Sony", "Tecnología", "Sony", 70000),
    (2006, "Mouse Logitech", "Tecnología", "Logitech", 25000),
    (2007, "Teclado Mecánico", "Tecnología", "Redragon", 60000),

    (2008, "Silla Oficina", "Hogar", "Ikea", 90000),
    (2009, "Escritorio", "Hogar", "Ikea", 150000),
    (2010, "Microondas", "Hogar", "LG", 85000),
    (2011, "Lámpara LED", "Hogar", "Philips", 35000),

    (2012, "Polera Hombre", "Vestuario", "Nike", 30000),
    (2013, "Jeans Mujer", "Vestuario", "Levis", 45000),
    (2014, "Chaqueta", "Vestuario", "Columbia", 95000),
    (2015, "Zapatillas Running", "Vestuario", "Adidas", 120000)

]


# ==================================
# CANALES
# ==================================

CANALES = [

    ("WEB", "Online"),
    ("APP", "Online"),
    ("POS", "Presencial")

]


# ==================================
# TIENDAS
# ==================================

TIENDAS = {

    "Las Condes": "Metropolitana",

    "Providencia": "Metropolitana",

    "Santiago Centro": "Metropolitana",

    "Maipú": "Metropolitana",

    "Concepción Centro": "Biobío",

    "Temuco Portal": "La Araucanía",

    "Antofagasta Mall": "Antofagasta"

}


# ==================================
# CREAR CARPETA DATA
# ==================================

def crear_directorio():

    os.makedirs(
        RUTA_DATA,
        exist_ok=True
    )

# ==================================
# GENERAR CLIENTES
# ==================================

def generar_clientes():

    clientes = []

    segmentos = SEGMENTOS.copy()
    random.shuffle(segmentos)

    for i in range(NUM_CLIENTES):

        id_cliente = 101 + i

        nombre = NOMBRES[i]
        apellido = APELLIDOS[i]

        email = (
            nombre.lower()
            + "."
            + apellido.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            + "@email.com"
        )

        segmento = segmentos[i]

        ciudad = random.choice(CIUDADES)

        clientes.append({

            "id_cliente": id_cliente,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "segmento": segmento,
            "ciudad": ciudad

        })

    return pd.DataFrame(clientes)


# ==================================
# GENERAR PRODUCTOS
# ==================================

def generar_productos():

    productos = []

    for producto in PRODUCTOS:

        productos.append({

            "id_producto": producto[0],
            "nombre_producto": producto[1],
            "categoria": producto[2],
            "proveedor": producto[3],
            "precio_base": producto[4]

        })

    return pd.DataFrame(productos)

# ==================================
# GENERAR DIM TIEMPO
# ==================================

def generar_tiempo():

    tiempo = []

    fechas = [

        ("2026-04-01", 1, 4, "Abril", 2, 2026, "Miércoles", "No"),
        ("2026-04-02", 2, 4, "Abril", 2, 2026, "Jueves", "No"),
        ("2026-04-03", 3, 4, "Abril", 2, 2026, "Viernes", "No"),
        ("2026-04-04", 4, 4, "Abril", 2, 2026, "Sábado", "Sí"),
        ("2026-04-05", 5, 4, "Abril", 2, 2026, "Domingo", "Sí"),
        ("2026-04-06", 6, 4, "Abril", 2, 2026, "Lunes", "No"),
        ("2026-04-07", 7, 4, "Abril", 2, 2026, "Martes", "No"),
        ("2026-04-08", 8, 4, "Abril", 2, 2026, "Miércoles", "No"),
        ("2026-04-09", 9, 4, "Abril", 2, 2026, "Jueves", "No"),
        ("2026-04-10", 10, 4, "Abril", 2, 2026, "Viernes", "No")
    ]

    for fila in fechas:

        tiempo.append({

            "fecha": fila[0],
            "dia": fila[1],
            "mes": fila[2],
            "nombre_mes": fila[3],
            "trimestre": fila[4],
            "anio": fila[5],
            "dia_semana": fila[6],
            "fin_semana": fila[7]

        })

    return pd.DataFrame(tiempo)

# ==================================
# GENERAR DIM CANAL
# ==================================

def generar_canales():

    canales = []

    for canal in CANALES:

        canales.append({

            "canal": canal[0],
            "tipo_canal": canal[1]

        })

    return pd.DataFrame(canales)

# ==================================
# GENERAR DIM TIENDA
# ==================================

def generar_tiendas():

    tiendas = [

        {
            "nombre_tienda": "Las Condes",
            "region": "Metropolitana",
            "tipo_tienda": "Mall"
        },

        {
            "nombre_tienda": "Providencia",
            "region": "Metropolitana",
            "tipo_tienda": "Mall"
        },

        {
            "nombre_tienda": "Santiago Centro",
            "region": "Metropolitana",
            "tipo_tienda": "Centro"
        },

        {
            "nombre_tienda": "Maipú",
            "region": "Metropolitana",
            "tipo_tienda": "Sucursal"
        },

        {
            "nombre_tienda": "Concepción Centro",
            "region": "Biobío",
            "tipo_tienda": "Centro"
        },

        {
            "nombre_tienda": "Temuco Portal",
            "region": "La Araucanía",
            "tipo_tienda": "Mall"
        },

        {
            "nombre_tienda": "Antofagasta Mall",
            "region": "Antofagasta",
            "tipo_tienda": "Mall"
        },
        


    ]

    return pd.DataFrame(tiendas)
# ==================================
# GUARDAR CSV
# ==================================

def guardar_csv(df, nombre_archivo):

    ruta = os.path.join(
        RUTA_DATA,
        nombre_archivo
    )

    df.to_csv(
        ruta,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"✔ Archivo generado: {ruta}")

# ==================================
# FUNCIONES AUXILIARES
# ==================================

def obtener_fecha(numero_venta):

    ventas_por_dia = [7, 8, 9, 9, 10, 11, 11, 11, 12, 12]

    fecha_inicio = datetime(2026, 4, 1)

    acumulado = 0

    for dia, cantidad in enumerate(ventas_por_dia):

        acumulado += cantidad

        if numero_venta <= acumulado:

            return (
                fecha_inicio +
                timedelta(days=dia)
            ).strftime("%Y-%m-%d")

    return (
        fecha_inicio +
        timedelta(days=9)
    ).strftime("%Y-%m-%d")


# ==================================

def obtener_cliente(df_clientes):

    return df_clientes.sample(
        1,
        random_state=random.randint(1, 999999)
    ).iloc[0]


# ==================================

def obtener_producto(df_productos):

    pesos = []

    for _, producto in df_productos.iterrows():

        categoria = producto["categoria"]

        if categoria == "Tecnología":

            pesos.append(55)

        elif categoria == "Vestuario":

            pesos.append(25)

        else:

            pesos.append(20)

    indice = random.choices(

        population=list(df_productos.index),

        weights=pesos,

        k=1

    )[0]

    return df_productos.loc[indice]


# ==================================

def obtener_canal():

    return random.choices(

        ["WEB", "APP", "POS"],

        weights=[45, 20, 35],

        k=1

    )[0]


# ==================================

def obtener_tienda():

    return random.choices(

        [

            "Las Condes",

            "Santiago Centro",

            "Providencia",

            "Concepción Centro",

            "Antofagasta Mall",

            "Maipú",

            "Temuco Portal"

        ],

        weights=[25, 20, 15, 12, 10, 10, 8],

        k=1

    )[0]


# ==================================

def calcular_precio(precio_base):

    variacion = random.uniform(

        -0.05,

        0.10

    )

    return round(

        precio_base * (1 + variacion),

        0

    )


# ==================================

def obtener_cantidad():

    return random.choices(

        [1, 2, 3],

        weights=[60, 30, 10],

        k=1

    )[0]
    
# ==================================
# GENERAR VENTAS
# ==================================

def generar_ventas(df_clientes, df_productos):

    ventas = []

    for id_venta in range(1, NUM_VENTAS + 1):

        cliente = obtener_cliente(df_clientes)

        segmento = cliente["segmento"]

        # ----------------------------
        # PRODUCTOS SEGÚN SEGMENTO
        # ----------------------------

        if segmento == "Premium":

            pesos = []

            for _, producto in df_productos.iterrows():

                categoria = producto["categoria"]

                if categoria == "Tecnología":
                    pesos.append(70)

                elif categoria == "Hogar":
                    pesos.append(20)

                else:
                    pesos.append(10)

        elif segmento == "Regular":

            pesos = []

            for _, producto in df_productos.iterrows():

                categoria = producto["categoria"]

                if categoria == "Tecnología":
                    pesos.append(50)

                elif categoria == "Vestuario":
                    pesos.append(30)

                else:
                    pesos.append(20)

        else:

            pesos = []

            for _, producto in df_productos.iterrows():

                categoria = producto["categoria"]

                if categoria == "Vestuario":
                    pesos.append(45)

                elif categoria == "Tecnología":
                    pesos.append(35)

                else:
                    pesos.append(20)

        indice = random.choices(

            population=list(df_productos.index),

            weights=pesos,

            k=1

        )[0]

        producto = df_productos.loc[indice]

        # ----------------------------
        # CANTIDAD
        # ----------------------------

        cantidad = obtener_cantidad()

        # ----------------------------
        # PRECIO
        # ----------------------------

        precio_unitario = calcular_precio(

            producto["precio_base"]

        )

        # Premium suele comprar productos más caros

        if segmento == "Premium":

            precio_unitario *= 1.05

        elif segmento == "Nuevo":

            precio_unitario *= 0.95

        precio_unitario = round(precio_unitario, 0)

        # ----------------------------
        # FECHA
        # ----------------------------

        fecha = obtener_fecha(id_venta)

        # ----------------------------
        # CANAL
        # ----------------------------

        canal = obtener_canal()

        # ----------------------------
        # TIENDA
        # ----------------------------

        tienda = obtener_tienda()

        if canal == "POS":

            tipo_venta = "Presencial"

        else:

            tipo_venta = "Online"
        # ----------------------------
        # REGISTRO
        # ----------------------------

        ventas.append({

            "id_venta": id_venta,

            "fecha": fecha,

            "id_cliente": cliente["id_cliente"],

            "id_producto": producto["id_producto"],

            "cantidad": cantidad,

            "precio_unitario": precio_unitario,

            "canal": canal,

            "tienda": tienda,

            "tipo_venta": tipo_venta

        })

    return pd.DataFrame(ventas)


# ==================================
# MAIN
# ==================================

def main():

    print("=" * 50)
    print("GENERADOR DE DATOS RETAILSTART")
    print("=" * 50)

    crear_directorio()

    print("\nGenerando clientes...")

    df_clientes = generar_clientes()

    guardar_csv(
        df_clientes,
        "clientes.csv"
    )

    print("\nGenerando productos...")

    df_productos = generar_productos()

    guardar_csv(
        df_productos,
        "productos.csv"
    )

    print("\nGenerando tiempo...")

    df_tiempo = generar_tiempo()

    guardar_csv(
        df_tiempo,
        "tiempo.csv"
    )

    print("\nGenerando canales...")

    df_canales = generar_canales()

    guardar_csv(
        df_canales,
        "canales.csv"
    )

    print("\nGenerando tiendas...")

    df_tiendas = generar_tiendas()

    guardar_csv(
        df_tiendas,
        "tiendas.csv"
    )

    
    print("\nGenerando ventas...")

    df_ventas = generar_ventas(
        df_clientes,
        df_productos
    )

    guardar_csv(
        df_ventas,
        "ventas.csv"
    )    
    
    print("\nProceso finalizado correctamente.")

if __name__ == "__main__":
    main()