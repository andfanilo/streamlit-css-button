import "./index.css";

import jss from "jss";
import preset from "jss-preset-default";
import { Streamlit, RenderData } from "streamlit-component-lib";

jss.setup(preset());

const button = document.body.appendChild(document.createElement("button"));
let state = "idle";

button.onclick = () => {
  Streamlit.setComponentValue(true);
  state = "clicked";
};

const onRender = (event: Event) => {
  const data = (event as CustomEvent<RenderData>).detail;

  button.disabled = data.disabled;

  let label = data.args["label"];
  button.textContent = label;

  let style = {
    button: {
      ...data.args["style"],
      "&:hover": data.args["hover_style"],
      "&:focus": data.args["focus_style"],
      "&:active": data.args["active_style"],
    },
  };
  const { classes } = jss.createStyleSheet(style).attach();
  button.className = classes.button;

  Streamlit.setFrameHeight();

  if (state === "clicked") {
    state = "reset";
  } else if (state === "reset") {
    Streamlit.setComponentValue(false);
    state = "idle";
  }
  
};

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
Streamlit.setComponentReady();
Streamlit.setFrameHeight();
