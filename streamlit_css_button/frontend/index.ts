import "./index.css";

import { Streamlit, RenderData } from "streamlit-component-lib";

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

  Streamlit.setFrameHeight();
};

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
Streamlit.setComponentReady();
Streamlit.setFrameHeight();
