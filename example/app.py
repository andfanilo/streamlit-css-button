import streamlit as st
from streamlit_css_button import css_properties
from streamlit_css_button import st_css_button

st.title("Pimp my button!")

with st.echo("below"):
    if st_css_button(
        "Hello world", css_properties(color="red", backgroundColor="yellow")
    ):
        st.balloons()
