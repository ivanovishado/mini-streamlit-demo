from pathlib import Path

import pandas as pd
import streamlit as st

from .data_utils import filter_students, load_students, summarize_students


DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "estudiantes_ai.csv"


@st.cache_data
def get_students() -> pd.DataFrame:
    return load_students(DATA_PATH)


def apply_theme() -> None:
    st.markdown(
        """
        <style>
        :root {
            --udg-red: #8f1018;
            --udg-gold: #f4b400;
            --gdg-blue: #4285f4;
            --gdg-green: #0f9d58;
            --ink: #171717;
        }
        .main .block-container {
            padding-top: 2rem;
            max-width: 1080px;
        }
        div[data-testid="stMetric"] {
            border-left: 5px solid var(--udg-red);
            background: #fff8ea;
            padding: 1rem;
            border-radius: 0.5rem;
        }
        .course-callout {
            border-left: 6px solid var(--gdg-blue);
            background: #f6f9ff;
            padding: 1rem 1.2rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_intro() -> None:
    apply_theme()
    st.title("Streamlit: de script a web app")
    st.caption("Mini-curso para estudiantes de ingenieria con enfoque en datos e IA.")

    st.markdown(
        """
        Streamlit permite convertir un script de Python en una interfaz web local en minutos.
        La idea central de este curso es sencilla: si ya puedes analizar datos con Pandas,
        puedes agregar controles visuales para que otra persona explore ese analisis.
        """
    )

    st.markdown(
        """
        <div class="course-callout">
        <strong>Modelo mental:</strong> cada vez que una persona cambia un widget,
        Streamlit vuelve a ejecutar el script de arriba hacia abajo con los nuevos valores.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Objetivo del capstone")
    st.write(
        "Construir una app local donde el usuario filtre datos de estudiantes por "
        "programa, nivel de Pandas y calificacion minima."
    )


def render_components() -> None:
    apply_theme()
    st.title("Componentes UI")
    st.write("Estos son los bloques basicos que usaremos para crear interactividad.")

    name = st.text_input("Nombre", "Equipo Streamlit")
    min_grade = st.slider("Calificacion minima", 0, 100, 80)
    program = st.selectbox("Programa", ["Computacion", "Datos", "Electronica", "Industrial"])

    if st.button("Generar mensaje"):
        st.success(
            f"{name}: el filtro actual busca estudiantes de {program} "
            f"con calificacion mayor o igual a {min_grade}."
        )

    st.subheader("Codigo mental")
    st.code(
        """min_grade = st.slider("Calificacion minima", 0, 100, 80)
program = st.selectbox("Programa", programas)
filtered = data[data["calificacion"] >= min_grade]""",
        language="python",
    )


def render_filters() -> None:
    apply_theme()
    st.title("Interactividad con Pandas")
    data = get_students()

    st.write(
        "Los widgets regresan valores normales de Python. Esos valores se conectan "
        "directamente con filtros de Pandas."
    )

    min_grade = st.slider("Calificacion minima", 0, 100, 80, key="filters_min_grade")
    program = st.selectbox(
        "Programa",
        ["Todos", *sorted(data["programa"].unique())],
        key="filters_program",
    )
    pandas_level = st.selectbox(
        "Nivel de Pandas",
        ["Todos", *sorted(data["uso_pandas"].unique())],
        key="filters_pandas_level",
    )

    filtered = filter_students(data, min_grade, program, pandas_level)
    st.dataframe(filtered, use_container_width=True)

    st.code(
        """filtered = filter_students(
    data,
    min_grade=min_grade,
    program=program,
    pandas_level=pandas_level,
)""",
        language="python",
    )


def render_capstone() -> None:
    apply_theme()
    st.title("Capstone: dashboard local")
    data = get_students()

    with st.sidebar:
        st.header("Filtros")
        min_grade = st.slider("Calificacion minima", 0, 100, 75)
        program = st.selectbox("Programa", ["Todos", *sorted(data["programa"].unique())])
        pandas_level = st.selectbox("Nivel de Pandas", ["Todos", *sorted(data["uso_pandas"].unique())])

    filtered = filter_students(data, min_grade, program, pandas_level)
    summary = summarize_students(filtered)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Estudiantes", summary["students"])
    col2.metric("Promedio", summary["average_grade"])
    col3.metric("Asistencia", f"{summary['average_attendance']}%")
    col4.metric("En riesgo", summary["at_risk"])

    st.subheader("Distribucion por proyecto")
    project_counts = filtered["proyecto_ai"].value_counts()
    st.bar_chart(project_counts)

    st.subheader("Datos filtrados")
    st.dataframe(filtered, use_container_width=True)

    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Descargar datos filtrados",
        data=csv,
        file_name="estudiantes_filtrados.csv",
        mime="text/csv",
    )


def render_bonus_ai() -> None:
    apply_theme()
    st.title("Bonus: donde entra IA")
    st.write(
        "Esta pagina no requiere API keys. Sirve para discutir como una app Streamlit "
        "puede envolver un flujo de IA despues de dominar datos, widgets y estado."
    )

    question = st.text_area(
        "Pregunta que un usuario podria hacerle a un asistente de analisis",
        "Que patrones ves en estudiantes en riesgo?",
    )

    if st.button("Simular respuesta"):
        st.info(
            "Respuesta simulada: revisaria asistencia, horas de estudio y nivel de Pandas "
            "para explicar el riesgo y proponer una accion concreta."
        )

    st.markdown(
        """
        Para convertir esto en una app real de IA, se agregaria:

        - Un proveedor de modelo.
        - Manejo seguro de secretos.
        - Validacion de entradas.
        - Observabilidad de costos y errores.
        """
    )
