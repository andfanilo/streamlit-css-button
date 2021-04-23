import streamlit as st
from streamlit_css_button import css_properties
from streamlit_css_button import st_css_button

st.title("Pimp my button!")

with st.echo("below"):
    if st_css_button(
        "Launch balloons!",
        css_properties=css_properties(
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
            boxShadow="7px 10px 0px 0px #3dc21b",
            textShadow="0px 1px 0px #2f6627",
            transition="width 2s, height 2s, transform 2s",
        ),
        hover_properties=css_properties(
            backgroundImage="linear-gradient(to bottom, #3498db, #2980b9)",
            fontWeight="bold",
            width="300px",
        ),
        active_properties=css_properties(backgroundColor="green",),
    ):
        st.balloons()
