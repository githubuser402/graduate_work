import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AdminView from '../views/AdminView.vue'
// import store from '../vuex';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/admin/',
      name: 'admin',
      component: AdminView,
    },
  ]
})

// router.beforeEach((to, from, next) => {
//   console.log(`${to.fullPath}, ${from.fullPath}`);
//   console.log(router.resolve({name: 'admin'}));
//   if (from.fullPath === router.resolve({name: 'admin'}).fullPath && to.fullPath !== router.resolve({name: 'admin'}).fullPath) {
//     store.commit('logOut');
//     console.log('logged out because of page change')
//     next();
//   }
//   next();
// })

export default router
