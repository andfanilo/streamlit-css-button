import "./index.css";

import jss from "jss";
import preset from "jss-preset-default";
import { Streamlit, RenderData } from "streamlit-component-lib";

jss.setup(preset());

const button = document.body.appendChild(document.createElement("button"));

button.onclick = () => {
  Streamlit.setComponentValue(true);
};

const onRender = (event: Event) => {
  const data = (event as CustomEvent<RenderData>).detail;

  // Disable our button while rendering
  button.disabled = data.disabled;

  let label = data.args["label"];
  button.textContent = label;

  let style = { button: data.args["style"] };
  const { classes } = jss.createStyleSheet(style).attach();
  button.className = classes.button;

  Streamlit.setFrameHeight();
};

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
Streamlit.setComponentReady();
Streamlit.setFrameHeight();
