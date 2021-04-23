import os
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
    _st_css_button = components.declare_component(
        "streamlit_css_button", path=build_dir
    )


@dataclass
class css_properties:
    height: str = None
    width: str = None
    color: str = None
    backgroundImage: str = None
    backgroundColor: str = None
    border: str = None
    borderRadius: str = None
    cursor: str = None
    fontFamily: str = None
    fontSize: str = None
    fontWeight: str = None
    margin: str = None
    padding: str = None
    textDecoration: str = None
    boxShadow: str = None
    textShadow: str = None
    transition: str = None


def asdict(o, skip_empty=True):
    return {k: v for k, v in o.__dict__.items() if not (skip_empty and v is None)}


def st_css_button(
    label: str,
    css_properties: css_properties,
    hover_properties: css_properties,
    active_properties: css_properties,
    key=None,
):
    """Create a button. Pimp with CSS.

    Behaves like Streamlit's native button. Click on it, it returns True.
    """
    return _st_css_button(
        label=label,
        style=asdict(css_properties),
        hover_style=asdict(hover_properties),
        active_style=asdict(active_properties),
        key=key,
        default=False,
    )
