import { createApp } from "vue";
import App from "./app/App.vue";

import { Inkline, components,  } from "@inkline/inkline";
import "@inkline/inkline/inkline.scss";


import "./styles/global.scss";
import "./styles/style.scss";
import router from './app/router/router';

const app = createApp(App);

app.use(Inkline, {
  colorMode: "light",
  components,
  
});

app.use(router)

app.mount("#app");
