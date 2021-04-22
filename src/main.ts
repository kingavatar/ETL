import "@babel/polyfill";
import "mutationobserver-shim";
import Vue from "vue";
import "./plugins/bootstrap-vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import VueSocketIO from "vue-socket.io";
// socket io
import * as io from "socket.io-client";
import SocketIO from "socket.io-client";

Vue.config.productionTip = false;

/* Establish Connection */
const socketConnection = SocketIO("http://localhost:5000");

Vue.use(
  new VueSocketIO({
    debug: true,
    connection: socketConnection,
    vuex: {
      store,
      actionPrefix: "SOCKET_",
      mutationPrefix: "SOCKET_"
    }
  })
);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
