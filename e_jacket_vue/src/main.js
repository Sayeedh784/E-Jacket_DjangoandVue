import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import axios from 'axios'



createApp(App).use(router, axios).mount('#app')


import 'bootstrap/dist/js/bootstrap.js'