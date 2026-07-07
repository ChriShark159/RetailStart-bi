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

# Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/ChriShark159/RetailStart-bi
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

## 6. Ejecutar el proceso ETL

```bash
python scripts/03_etl_dw.py
```

Los archivos CSV para Power BI serán exportados automáticamente a la carpeta `export/`.

---

# Resultados

El proyecto genera:

- Data Warehouse SQLite
- Archivos CSV para Power BI
- Dashboard Ejecutivo
- Dashboard Comercial

---