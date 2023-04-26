import { createApp } from "vue";
import App from "./App.vue";

import { Inkline, components } from "@inkline/inkline";
import "@inkline/inkline/inkline.scss";

import "./styles/global.scss";

const app = createApp(App);

app.use(Inkline, {
  colorMode: "light",
  components,
});

app.mount("#app");
