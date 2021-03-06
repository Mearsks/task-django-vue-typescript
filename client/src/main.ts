import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueCompositionAPI from '@vue/composition-api'
import VueSweetalert2 from "vue-sweetalert2";
import 'sweetalert2/dist/sweetalert2.min.css'
// eslint-disable-next-line @typescript-eslint/ban-ts-ignore
// @ts-ignore
import VueSession from 'vue-session'
import axios from "axios";

Vue.config.productionTip = false
Vue.use(VueCompositionAPI);
Vue.use(VueSession)
Vue.use(VueSweetalert2)

axios.defaults.baseURL = 'http://localhost:8000/';


new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
console.log(Vue);
