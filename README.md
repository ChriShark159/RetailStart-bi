# RetailStart Business Intelligence

Proyecto desarrollado para la asignatura **Arquitectura y Almacenamiento de Datos**.

El objetivo del proyecto consiste en construir un Data Warehouse y una solución de Business Intelligence utilizando **Python**, **SQLite** y **Power BI**, permitiendo analizar las ventas de RetailStart Chile S.A.

---

# Tecnologías utilizadas

- Python 3
- SQLite
- Pandas
- Power BI Desktop
- SQL
- Modelo Estrella (Star Schema)

---

# Arquitectura

CRM
ERP
POS
WEB
APP

↓

ELT / ETL (Python)

↓

Data Warehouse (SQLite)

↓

Power BI

---

# Modelo del Data Warehouse

Tabla de hechos

- FactVentas

Dimensiones

- DimCliente
- DimProducto
- DimTiempo
- DimCanal
- DimTienda

Modelo implementado mediante Star Schema.

---

# Dashboards

El proyecto incorpora dos dashboards principales.

## Dashboard Ejecutivo

Incluye:

- Ventas Totales
- Cantidad de Ventas
- Venta Promedio
- Clientes Activos
- Ventas por Canal
- Ventas por Región
- Ventas por Tienda
- Ventas por Mes
- Ventas por Trimestre

---

## Dashboard Comercial

Incluye:

- Top 10 Productos
- Ventas por Categoría
- Ventas por Ciudad
- Ventas por Segmento
- Comparación de Canales

---

# KPIs Implementados

- Ventas Totales
- Cantidad de Ventas
- Venta Promedio
- Clientes Activos
- Participación Canal Online
- Participación Canal Presencial

---

# Estructura del proyecto

```
RetailStart-BI
│
├── data/
├── database/
├── export/
├── scripts/
├── powerbi/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Instalación y ejecución

## 1. Clonar el repositorio

```bash
git clone https://github.com/ChriShark159/RetailStart-bi.git
```

## 2. Ingresar al proyecto

```bash
cd RetailStart-bi
```

## 3. Crear un entorno virtual

```bash
python -m venv .venv
```

## 4. Activar el entorno virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## 6. Ejecutar la ingesta de datos

Este proceso genera los archivos CSV que serán utilizados durante la carga del Data Warehouse.

```bash
python scripts/01_generar_datos.py
```

## 7. Revisar la base de datos (Opcional)

El proyecto ya incluye la base de datos SQLite ubicada en:

```text
database/retail_dw.db
```

## 7.1. Crear el Data Warehouse pero si falta un dato o da error borra la base de datos

Este script crea la base de datos SQLite (`retail_dw.db`) y la estructura del modelo estrella.

```bash
python scripts/02_crear_dw.py
```


Puede abrirse con **DB Browser for SQLite** para revisar su estructura antes o después de ejecutar el proceso ETL.

## 8. Ejecutar el proceso ETL

Este proceso carga las dimensiones y la tabla de hechos en el Data Warehouse y genera los archivos CSV utilizados por Power BI.

```bash
python scripts/03_etl_dw.py
```

Al finalizar se obtendrán:

- Base de datos SQLite poblada (`database/retail_dw.db`).
- Archivos CSV para Power BI en la carpeta `export/`.

## 9. Abrir el proyecto de Power BI

Abrir el archivo `.pbix` incluido en el proyecto y actualizar los orígenes de datos si fuese necesario para utilizar los archivos de la carpeta `export/`.
# Resultados

El proyecto genera:

- Data Warehouse SQLite
- Archivos CSV para Power BI
- Dashboard Ejecutivo
- Dashboard Comercial

---
