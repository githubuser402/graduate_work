import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AdminView from '../views/AdminView.vue'
import AdminRestaurantView from '../views/AdminRestaurantView.vue';
import AdminMenuView from '../views/AdminMenuView.vue';
import AdminDishView from '../views/AdminDishView.vue';
import AdminCategoryView from '../views/AdminCategoryView.vue';
import MenuView from '../views/MenuView.vue';
import CategoryView from '../views/CategoryView.vue';

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
    {
      path: '/admin/r/:id/',
      name: 'admin-restaurant',
      component: AdminRestaurantView,
    },
    {
      path: '/admin/r/:restaurantId/m/:menuId/',
      name: 'admin-menu',
      component: AdminMenuView,
    },
    {
      path: '/admin/r/:restaurantId/m/:menuId/d/:dishId/',
      name: 'admin-dish',
      component: AdminDishView,
    },
    {
      path: '/admin/r/:restaurantId/m/:menuId/c/:categoryId/',
      name: 'admin-category',
      component: AdminCategoryView,
    },
    {
      path: '/r/:restaurantId/m/:menuId/',
      name: 'public-menu',
      component: MenuView,
    },
    {
      path: '/r/:restaurantId/m/:menuId/c/:categoryId/',
      name: 'public-category',
      component: CategoryView,
    }
  ]
})

export default router
