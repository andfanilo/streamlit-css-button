import os

import streamlit.components.v1 as components


_RELEASE = False

if not _RELEASE:
    _st_css_button = components.declare_component(
        "streamlit_css_button", url="http://localhost:1234",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _st_css_button = components.declare_component("streamlit_css_button", path=build_dir)


def st_css_button(
    label: str,
    key=None,
):
    """Create a button. Pimp with CSS.

    Behaves like Streamlit's native button. Click on it, it returns True.
    """
    return _st_css_button(
        label=label,
        key=key,
        default=False,
    )
