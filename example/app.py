import streamlit as st
from streamlit_css_button import css_properties
from streamlit_css_button import st_css_button

st.title("Pimp my button!")

with st.echo("below"):
    if st_css_button(
        "Launch balloons!",
        css_properties(
            height="50px",
            width="200px",
            color="red",
            backgroundColor="yellow",
            border="1px solid blue",
            borderRadius="1em",
            cursor="pointer",
            fontFamily="Arial",
            fontSize="18px",
            padding="6px 13px",
            margin="0.1em",
            textDecoration="none",
            textShadow="0px 1px 0px #2f6627",
        ),
        css_properties(backgroundImage="linear-gradient(to bottom, #3498db, #2980b9)",),
    ):
        st.balloons()
