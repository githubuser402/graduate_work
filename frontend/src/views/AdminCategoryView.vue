<template>
    <div>
        <div class="d-flex column justify-content-between gap-4">
            <div class="border border-1 m-1">
                <router-link class="btn" :to="{ name: 'home' }">Домашня сторінка</router-link>
                <router-link class="btn" :to="{ name: 'admin' }">Ресторани</router-link>
                <router-link class="btn"
                    :to="{ name: 'admin-restaurant', params: { id: $route.params.restaurantId } }">Меню</router-link>
                <router-link class="btn"
                    :to="{ name: 'admin-menu', params: { restaurantId: $route.params.restaurantId, menuId: $route.params.menuId } }">Categories</router-link>
            </div>
            <button type="button" class="btn btn-outline-secondary m-1 rounded-0" @click="deleteCategory()"
                style="width:100px;">Видалити</button>
        </div>
        <center>
            <h1>{{ getCategory().title }}</h1>
        </center>
        <div class="border border-2 border-success rounded-4 m-3 d-flex row">
            <div v-for="dish in getCategory().dishes" :key="dish.id"
                class="card border min-height-200 p-3 m-3 border-primary border-2"
                style="width: 18rem; border-color: greenyellow">
                <router-link :to="{
                    name: 'admin-dish',
                    params: {
                        restaurantId: $route.params.restaurantId,
                        menuId: $route.params.menuId,
                        dishId: encodeURIComponent(dish.id)
                    }
                }">
                    <h5 class="card-title m-4">{{ dish.name }}</h5>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';

export default {
    name: 'AdminCategoryView',
    data() {
        return {
        }
    },
    components: {
    },
    beforeMount() {
        this.$store.dispatch('checkLogin');
        if (!this.$store.getters.loggedIn) {
            this.$router.push({ name: 'admin' });
            this.$store.state.user.loggedIn = false;
        }
    },
    mounted() {
        this.fetchCategory({ restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId, categoryId: this.$route.params.categoryId });
    },
    methods: {

        ...mapActions('category', ['fetchCategory',]),
        ...mapGetters('category', ['getCategory']),

        deleteCategory() {
            this.$store.dispatch('category/deleteCategory', { restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId, categoryId: this.$route.params.categoryId });
            this.$router.push({ name: 'admin-menu', params: { restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId } });
        },
    },
    computed: {
    },
};
</script>

<style scoped>
body {
  height: 100%;
  background: #ebf4f5;
  background: linear-gradient(90deg, #ebf4f5 0%, #b5c6e0  100%);
  background: -moz-linear-gradient(90deg, #ebf4f5 0%, #b5c6e0  100%);
  background: -webkit-linear-gradient(90deg, #ebf4f5 0%, #b5c6e0 100%);
  filter: progid: DXImageTransform.Microsoft.gradient(startColorstr="#F86CA7", endColorstr="#F4D444", GradientType=1);
}
</style>