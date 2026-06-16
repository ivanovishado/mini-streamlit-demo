from pathlib import Path

import pandas as pd
import streamlit as st


DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "estudiantes_ai.csv"

st.set_page_config(page_title="Capstone Streamlit", layout="wide")
st.title("Capstone: dashboard local")

data = pd.read_csv(DATA_PATH)

with st.sidebar:
    st.header("Filtros")
    min_grade = st.slider("Calificacion minima", 0, 100, 75)
    program = st.selectbox("Programa", ["Todos", *sorted(data["programa"].unique())])

filtered = data[data["calificacion"] >= min_grade]

# TODO: si program no es "Todos", filtra por programa.

# TODO: agrega tres metricas: estudiantes, promedio y asistencia.

# TODO: muestra una grafica por proyecto_ai.

st.dataframe(filtered, width="stretch")
