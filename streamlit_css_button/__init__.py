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
    display: str = None
    alignItems: str = None
    justifyContent: str = None
    lineHeight: str = None
    color: str = None
    backgroundImage: str = None
    backgroundColor: str = None
    border: str = None
    outline: str = None
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


def __asdict(o, skip_empty=True):
    return (
        {}
        if o is None
        else {k: v for k, v in o.__dict__.items() if not (skip_empty and v is None)}
    )


st_button_style = css_properties(
    width="auto",
    display="inline-flex",
    alignItems="center",
    justifyContent="center",
    lineHeight="1.6",
    color="inherit",
    backgroundColor="rgb(255, 255, 255)",
    border="1px solid rgba(38, 39, 48, 0.1)",
    borderRadius="0.25em",
    cursor="pointer",
    fontFamily="Arial",
    fontWeight="400",
    margin="0.2rem",
    padding="0.25rem 0.75rem",
)

st_button_style_hover = css_properties(
    border="1px solid rgb(246, 51, 102)", color="rgb(246, 51, 102)",
)

st_button_style_focus = css_properties(
    margin="0 0 0 0.2rem",
    boxShadow="rgba(246, 51, 102, 0.5) 0px 0px 0px 0.2rem",
    outline="currentcolor none medium",
    border="1px solid rgb(246, 51, 102)",
    color="rgb(246, 51, 102)",
)

st_button_style_active = css_properties(
    border="1px solid rgb(246, 51, 102)",
    backgroundColor="rgb(246, 51, 102)",
    color="white",
)


def st_css_button(
    label: str,
    css_properties: css_properties,
    hover_properties: css_properties = None,
    focus_properties: css_properties = None,
    active_properties: css_properties = None,
    key=None,
):
    """Create a button. Pimp with CSS.

    Behaves like Streamlit's native button. Click on it, it returns True.
    """
    return _st_css_button(
        label=label,
        style=__asdict(css_properties),
        hover_style=__asdict(hover_properties),
        focus_style=__asdict(focus_properties),
        active_style=__asdict(active_properties),
        key=key,
        default=False,
    )
