import { createApp } from 'vue'
import { ref } from 'vue'
import './assets/styles.css'
import App from './App.vue'
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap/dist/js/bootstrap.js"
import 'bootstrap-icons/font/bootstrap-icons.css';
import './plugins/axios.js'
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import 'slick-carousel';
import $ from 'jquery'
import 'jquery-mask-plugin'
import router from './router' 


window.$ = window.jQuery = $  // Isso deixa o $ disponível globalmente


createApp(App)
.use(router)
.mount('#app')