import streamlit as st
from streamlit_css_button import css_properties
from streamlit_css_button import st_button_style
from streamlit_css_button import st_button_style_active
from streamlit_css_button import st_button_style_focus
from streamlit_css_button import st_button_style_hover
from streamlit_css_button import st_css_button

st.set_page_config(page_title="Pimp my button!", page_icon=":art:")

st.title("Pimp my button!")
st.markdown("Here are 3 style examples, build your own in the sidebar!")

c1, c2, c3 = st.beta_columns(3)

with c1:
    st_css_button(
        "This button does nothing", css_properties(),
    )


with c2:
    if st_css_button(
        "Write something nice!",
        st_button_style,
        hover_properties=st_button_style_hover,
        focus_properties=st_button_style_focus,
        active_properties=st_button_style_active,
    ):
        st.markdown("Happy Streamlitin' :balloon:")

with c3:
    if st_css_button(
        "Launch balloons!",
        css_properties=css_properties(
            height="50px",
            width="150px",
            color="red",
            backgroundColor="yellow",
            border="1px solid blue",
            borderRadius="1em",
            cursor="pointer",
            fontFamily="Arial",
            fontSize="18px",
            padding="6px 13px",
            margin="0 0 12px 0",
            textDecoration="none",
            boxShadow="7px 10px 0px 0px #3dc21b",
            textShadow="0px 1px 0px #2f6627",
            transition="width 2s, height 2s, transform 2s",
        ),
        hover_properties=css_properties(
            backgroundImage="linear-gradient(to bottom, #3498db, #2980b9)",
            fontWeight="bold",
            width="200px",
        ),
        active_properties=css_properties(backgroundColor="green",),
    ):
        st.balloons()
