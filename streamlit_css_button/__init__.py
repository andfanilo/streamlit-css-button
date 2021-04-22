import os
from dataclasses import asdict
from dataclasses import dataclass

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


@dataclass
class css_properties:
    color: str = "black"
    backgroundColor: str = "green"


def st_css_button(
    label: str,
    css_properties: css_properties,
    key=None,
):
    """Create a button. Pimp with CSS.

    Behaves like Streamlit's native button. Click on it, it returns True.
    """
    return _st_css_button(
        label=label,
        style=asdict(css_properties),
        key=key,
        default=False,
    )
