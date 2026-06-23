from pathlib import Path

import pandas as pd
import streamlit as st

from .data_utils import MONTH_NAMES, filter_bitcoin_data, load_bitcoin_data, summarize_bitcoin_data


DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "btc_diario_limpio.csv"


@st.cache_data
def get_bitcoin_data() -> pd.DataFrame:
    return load_bitcoin_data(DATA_PATH)


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
    st.title("Streamlit: del notebook al dashboard")
    st.caption("Mini-curso de 2 horas para convertir el análisis de Bitcoin de la Semana 3 en una app local.")

    st.markdown(
        """
        Streamlit permite convertir un script de Python en una interfaz web local en minutos.
        En esta sesión tomaremos el dataset limpio de Bitcoin de la Semana 3 y lo convertiremos
        en un dashboard con filtros, métricas, gráficas y descarga de datos.
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

    st.subheader("Objetivo del dashboard")
    st.write(
        "Construir una app local donde el usuario explore el precio histórico de Bitcoin "
        "por rango de fechas, año y mes."
    )


def render_components() -> None:
    apply_theme()
    st.title("Componentes de UI")
    st.write("Estos son los bloques básicos que usaremos para crear interactividad.")

    analyst = st.text_input("Analista", "Ivan")
    min_price = st.slider("Precio mínimo de cierre (USD)", 0, 130000, 30000, step=1000)
    year = st.selectbox("Año", list(range(2012, 2027)))

    if st.button("Generar mensaje"):
        st.success(
            f"{analyst}: el filtro actual busca días de {year} "
            f"con precio de cierre mayor o igual a ${min_price:,.0f}."
        )

    st.subheader("Código mental")
    st.code(
        """min_price = st.slider(\"Precio mínimo de cierre\", 0, 130000, 30000)
year = st.selectbox(\"Año\", sorted(data[\"Year\"].unique()))
filtered = data[(data[\"Close\"] >= min_price) & (data[\"Year\"] == year)]""",
        language="python",
    )


def render_filters() -> None:
    apply_theme()
    st.title("Interactividad con Pandas")
    data = get_bitcoin_data()

    st.write(
        "Los widgets devuelven valores normales de Python. Esos valores se conectan "
        "directamente con filtros de Pandas."
    )

    min_date = data["Date"].min().date()
    max_date = data["Date"].max().date()
    date_range = st.date_input(
        "Rango de fechas",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        key="filters_date_range",
    )
    start_date, end_date = date_range if len(date_range) == 2 else (min_date, max_date)

    years = st.multiselect(
        "Años",
        sorted(data["Year"].unique()),
        default=[],
        key="filters_years",
    )
    months = st.multiselect(
        "Meses",
        options=list(MONTH_NAMES.keys()),
        format_func=lambda month: MONTH_NAMES[month],
        default=[],
        key="filters_months",
    )

    filtered = filter_bitcoin_data(data, start_date, end_date, years, months)
    st.dataframe(filtered, width="stretch")

    st.code(
        """filtered = filter_bitcoin_data(
    data,
    start_date=start_date,
    end_date=end_date,
    years=years,
    months=months,
)""",
        language="python",
    )


def render_capstone() -> None:
    apply_theme()
    st.title("Dashboard de Bitcoin")
    data = get_bitcoin_data()

    min_date = data["Date"].min().date()
    max_date = data["Date"].max().date()

    with st.sidebar:
        st.header("Filtros")
        date_range = st.date_input(
            "Rango de fechas",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
        )
        start_date, end_date = date_range if len(date_range) == 2 else (min_date, max_date)
        years = st.multiselect("Años", sorted(data["Year"].unique()), default=[])
        months = st.multiselect(
            "Meses",
            options=list(MONTH_NAMES.keys()),
            format_func=lambda month: MONTH_NAMES[month],
            default=[],
        )

    filtered = filter_bitcoin_data(data, start_date, end_date, years, months)
    summary = summarize_bitcoin_data(filtered)

    col1, col2, col3 = st.columns(3)
    col1.metric("Días", f"{summary['days']:,}")
    col2.metric("Último cierre", f"${summary['latest_close']:,.2f}")
    col3.metric("Máximo cierre", f"${summary['max_close']:,.2f}")

    col4, col5, col6 = st.columns(3)
    col4.metric("Retorno diario promedio", f"{summary['average_return']:.3f}%")
    col5.metric("Volatilidad", f"{summary['volatility']:.3f}%")
    col6.metric("Volumen total", f"{summary['total_volume']:,.0f} BTC")

    st.subheader("Precio de cierre")
    if filtered.empty:
        st.info("No hay datos para los filtros seleccionados.")
    else:
        st.line_chart(filtered.set_index("Date")["Close"])

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Cierre promedio por año")
        yearly_close = filtered.groupby("Year")["Close"].mean() if not filtered.empty else pd.Series(dtype=float)
        st.bar_chart(yearly_close)

    with col_b:
        st.subheader("Retorno promedio por mes")
        monthly_return = filtered.groupby("Month_Name")["Daily_Return"].mean() if not filtered.empty else pd.Series(dtype=float)
        st.bar_chart(monthly_return)

    st.subheader("Datos filtrados")
    st.dataframe(filtered, width="stretch")

    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Descargar datos filtrados",
        data=csv,
        file_name="bitcoin_filtrado.csv",
        mime="text/csv",
    )


def render_deployment() -> None:
    apply_theme()
    st.title("Vista previa del despliegue")
    st.write(
        "Cuando la app funciona localmente, el siguiente paso es publicarla desde un repositorio "
        "con sus dependencias y datos preparados."
    )
    st.markdown(
        """
        - Sube el proyecto a GitHub.
        - Mantén `requirements.txt` actualizado.
        - Evita depender del CSV crudo de millones de filas si ya tienes `btc_diario_limpio.csv`.
        - En Streamlit Community Cloud, selecciona el archivo `streamlit_app.py`.
        """
    )
