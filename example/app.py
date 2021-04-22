import streamlit as st
from streamlit_css_button import st_css_button

st.title("Pimp my button!")

if st_css_button("Hello world"):
    st.balloons()