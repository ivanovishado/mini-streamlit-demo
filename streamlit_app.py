import streamlit as st

from src.streamlit_course.app_pages import (
    render_bonus_ai,
    render_capstone,
    render_components,
    render_filters,
    render_intro,
)


st.set_page_config(
    page_title="Streamlit Mini-Curso",
    page_icon="ST",
    layout="wide",
)

pages = [
    st.Page(render_intro, title="1. Que es Streamlit"),
    st.Page(render_components, title="2. Componentes UI"),
    st.Page(render_filters, title="3. Pandas interactivo"),
    st.Page(render_capstone, title="4. Capstone"),
    st.Page(render_bonus_ai, title="Bonus IA"),
]

st.navigation(pages).run()
