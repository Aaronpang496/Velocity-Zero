import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Velocity Zero", layout="wide")

components.iframe(
    "https://YOUR_USERNAME.github.io/YOUR_REPOSITORY/",
    height=750,
    scrolling=False,
)
