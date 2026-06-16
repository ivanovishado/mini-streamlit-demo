# Streamlit Mini-Curso: Datos a Web Apps

Repo para un mini-curso de 4 horas sobre Streamlit para estudiantes de ingenieria que ya vieron Pandas. El objetivo es construir una app local donde una persona pueda filtrar datos dinamicamente con sliders y dropdowns.

## Que incluye

- Una app Streamlit completa en `streamlit_app.py`.
- Datos de ejemplo en `data/estudiantes_ai.csv`.
- Helpers de Pandas en `src/streamlit_course/data_utils.py`.
- Ejercicios guiados en `exercises/`.
- Tests basicos en `tests/`.
- Una presentacion HTML editable en `slides/streamlit-mini-curso.html`.

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

## Flujo sugerido de 4 horas

### Dia 1

1. Que es Streamlit y por que sirve para prototipos de datos.
2. Crear y correr una primera app.
3. Usar textos, botones, sliders y selectbox.
4. Entender el modelo de rerun: el script se ejecuta de arriba hacia abajo.
5. Checkpoint: crear un filtro simple conectado a una variable.

### Dia 2

1. Recap de Pandas con el dataset de ejemplo.
2. Conectar widgets con filtros de dataframe.
3. Crear metricas, tabla filtrada y grafica.
4. Completar el capstone.
5. Bonus: discutir como Streamlit puede envolver flujos de IA.

## Reemplazar con materiales de Semana 3

Cuando tengas el material de Pandas de la semana anterior:

1. Copia el CSV real a `data/`.
2. Actualiza `DATA_PATH` en `src/streamlit_course/app_pages.py`.
3. Ajusta `REQUIRED_COLUMNS` en `src/streamlit_course/data_utils.py`.
4. Cambia los filtros de `filter_students` para usar las columnas reales.
5. Corre `pytest` y `streamlit run streamlit_app.py`.

La idea es reemplazar el dataset y los filtros, no reescribir toda la interfaz.

## VS Code

Extensiones recomendadas:

- Python.
- Jupyter, si los estudiantes traen notebooks de Pandas.
- Streamlit Runner, opcional para correr apps desde VS Code.

Tambien se incluye `.devcontainer/devcontainer.json` para usar Codespaces como fallback si alguien no logra configurar Python localmente.

## Comandos utiles

```bash
streamlit run streamlit_app.py
pytest
```

## Estructura

```text
streamlit_app.py                  # Punto de entrada de la app
src/streamlit_course/             # Logica reutilizable y paginas
data/                             # Datos de ejemplo o Semana 3
exercises/                        # Laboratorios guiados
solution/                         # Notas de solucion
slides/                           # Presentacion HTML
tests/                            # Pruebas automatizadas
```
