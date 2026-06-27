import streamlit as st

from src.streamlit_course.app_pages import (
    render_capstone,
    render_components,
    render_deployment,
    render_filters,
    render_intro,
    render_openrouter_chat,
    render_sqlite_dashboard,
    render_upload_state,
)


st.set_page_config(
    page_title="Streamlit Mini-curso",
    page_icon="ST",
    layout="wide",
)

pages = [
    st.Page(render_intro, title="1. ¿Qué es Streamlit?"),
    st.Page(render_components, title="2. Componentes de UI"),
    st.Page(render_filters, title="3. Pandas interactivo"),
    st.Page(render_capstone, title="4. Dashboard de Bitcoin"),
    st.Page(render_sqlite_dashboard, title="5. Dashboard SQLite"),
    st.Page(render_openrouter_chat, title="6. OpenRouter chat"),
    st.Page(render_upload_state, title="7. Upload + session state"),
    st.Page(render_deployment, title="8. Despliegue"),
]

st.navigation(pages).run()
