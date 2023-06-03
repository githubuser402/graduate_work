import { createApp, provide } from 'vue'
import 'bootstrap/dist/css/bootstrap.css'
import App from './App.vue'
import router from './router'
import store from './vuex'

import './assets/main.css'

const app = createApp(App)

app.use(router)
app.use(store)

app.mount('#app')

import 'bootstrap/dist/js/bootstrap.js'
export default app
