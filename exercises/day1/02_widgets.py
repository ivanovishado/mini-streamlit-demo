import streamlit as st


st.title("Widgets basicos")

min_grade = st.slider("Calificacion minima", 0, 100, 80)
program = st.selectbox("Programa", ["Computacion", "Datos", "Electronica", "Industrial"])

# TODO: muestra una frase que use min_grade y program.

# TODO: agrega un segundo widget y conecta su valor con st.write.
