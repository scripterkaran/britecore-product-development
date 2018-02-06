import Vue from 'vue'
import App from './App.vue'
import router from './router/index'

import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/en'
import axios from 'axios'
import './styles/main.scss'

axios.defaults.baseURL = window.apiOrigin ?  window.apiOrigin :'/api'

Vue.use(ElementUI,{ locale })


new Vue({
  el: '#app',
  render: h => h(App),
  router,
})

