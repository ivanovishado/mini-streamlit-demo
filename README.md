# Streamlit Mini-Curso: de Notebook a Dashboard de Bitcoin

> Parte del **Curso Intensivo: Python para la Innovación — CUGDL x GDG Guadalajara 2026**.

Repo para un mini-curso de **2 horas** sobre Streamlit. Toma el dataset limpio de Bitcoin de la Semana 3 y lo convierte en un dashboard local con filtros, métricas, gráficas y descarga de datos.

## Qué incluye

- Una app Streamlit completa en `streamlit_app.py` con 5 páginas de navegación.
- Dataset de Bitcoin en `data/btc_diario_limpio.csv` (5,285 filas diarias, 2012-01-01 → 2026-06-23).
- Helpers de Pandas en `src/streamlit_course/data_utils.py`.
- Tests en `tests/`.
- Una presentación interactiva en `slides/open-slide/` (deck React con open-slide).

## Páginas de la app

1. **Qué es Streamlit** — introducción y modelo mental del rerun.
2. **Componentes UI** — `st.slider`, `st.selectbox`, `st.button`, `st.code` en acción.
3. **Pandas interactivo** — widgets conectados a filtros de Pandas sobre el dataset real.
4. **Dashboard Bitcoin** — sidebar con filtros, seis métricas, tres gráficas, tabla y descarga CSV.
5. **Despliegue** — vista previa de cómo publicar en Streamlit Community Cloud.

## Dashboard Bitcoin

**Filtros (sidebar):**

- Rango de fechas (mín/máx del dataset).
- Multiselect de años (opcional).
- Multiselect de meses (opcional).

**Métricas:**

- Días.
- Último cierre.
- Máximo cierre.
- Retorno diario prom.
- Volatilidad.
- Volumen total.

**Gráficas:**

- Precio de cierre por `Date` (línea).
- Cierre promedio por `Year` (barras).
- Retorno promedio por `Month_Name` (barras).

**Tabla:**

- DataFrame filtrado con botón `st.download_button` para exportar CSV.

## Dataset

`data/btc_diario_limpio.csv` — columnas:

| Columna        | Descripción                          |
| -------------- | ------------------------------------ |
| `Date`         | Fecha diaria.                        |
| `Open`         | Precio de apertura (USD).            |
| `High`         | Precio máximo del día (USD).         |
| `Low`          | Precio mínimo del día (USD).         |
| `Close`        | Precio de cierre (USD).              |
| `Volume`       | Volumen negociado (BTC).             |
| `Year`         | Año derivado de `Date`.              |
| `Month`        | Mes derivado de `Date` (1-12).       |
| `Daily_Return` | Retorno porcentual diario (1 NaN).   |

`Month_Name` se deriva al cargar (`Ene`, `Feb`, …, `Dic`).

## Setup local

Requisitos: Python 3.10 a 3.14.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
streamlit run streamlit_app.py
```

Si usas Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements-dev.txt
streamlit run streamlit_app.py
```

Si tienes `uv` instalado:

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements-dev.txt
streamlit run streamlit_app.py
```

## Flujo sugerido de 2 horas

| Tiempo      | Bloque                                    |
| ----------- | ----------------------------------------- |
| 0:00–0:10   | Intro, setup y objetivo.                  |
| 0:10–0:35   | Modelo mental + primitivas de UI.         |
| 0:35–1:05   | Widgets conectados a filtros de Pandas.   |
| 1:05–1:40   | Dashboard Bitcoin (métricas, gráficas).   |
| 1:40–1:55   | Vista previa de despliegue.               |
| 1:55–2:00   | Cierre y preguntas.                       |

Cada bloque se acompaña de la app en vivo en `http://localhost:8501`.

## Presentación

Las slides viven en `slides/open-slide/` como un deck de React con el framework [open-slide](https://open-slide.dev/). Para editarlas o presentarlas:

```bash
cd slides/open-slide
npm run dev      # servidor de desarrollo
npm run build    # build de producción
```

El deck acompaña a la app: cubre el modelo mental de Streamlit, el dataset de Bitcoin, el patrón widget → filtro → DataFrame, el layout del dashboard y el despliegue.

## VS Code

Extensiones recomendadas:

- Python.
- Jupyter, si los estudiantes traen notebooks de Pandas.
- Streamlit Runner, opcional para correr apps desde VS Code.

También se incluye `.devcontainer/devcontainer.json` para usar Codespaces como fallback si alguien no logra configurar Python localmente.

## Comandos útiles

```bash
streamlit run streamlit_app.py    # correr la app
pytest                             # tests
cd slides/open-slide && npm run dev  # presentar las slides
```

## Estructura

```text
streamlit_app.py                  # Punto de entrada de la app
src/streamlit_course/             # Lógica reutilizable y páginas
data/btc_diario_limpio.csv        # Dataset de Bitcoin (Semana 3)
solution/                         # Notas de solución
slides/open-slide/                # Presentación interactiva (open-slide)
tests/                            # Pruebas automatizadas
```
