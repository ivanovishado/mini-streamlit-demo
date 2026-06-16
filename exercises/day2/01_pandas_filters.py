from pathlib import Path

import pandas as pd
import streamlit as st


DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "estudiantes_ai.csv"

st.title("Filtros con Pandas")

data = pd.read_csv(DATA_PATH)

min_grade = st.slider("Calificacion minima", 0, 100, 80)

# TODO: crea filtered usando data["calificacion"] >= min_grade.

# TODO: muestra filtered con st.dataframe.
