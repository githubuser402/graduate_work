import { createApp, provide } from 'vue'
import App from './App.vue'
import router from './router'
import store from './vuex'

import './assets/main.css'

const app = createApp(App)

app.use(router)
app.use(store)
//store api url in app config

app.mount('#app')

export default app
