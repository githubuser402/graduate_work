<template>
    <div>
        <div class="d-flex column justify-content-between gap-4">
            <div class="border border-1 m-1">
            <router-link class="btn" :to="{name: 'home'}">Домашня сторінка</router-link>
            <router-link class="btn" :to="{name: 'admin'}">Ресторани</router-link>
            <router-link class="btn" :to="{name: 'admin-restaurant', params: { id: $route.params.restaurantId }}">Меню</router-link>
            <router-link class="btn" :to="{name: 'admin-menu', params: { restaurantId: $route.params.restaurantId, menuId: $route.params.menuId }}">Страви</router-link>
        </div>
        <button type="button" class="btn btn-outline-secondary m-1 rounded-0" @click='deleteDish()' style="width:100px;">Видалити</button>
        </div>
        <div>
            <center>
                <h1 contenteditable="true">{{ getDish().name }}</h1>
                <h4 contenteditable="true">{{ getDish().price }} грн</h4>
            </center>
            <center>
                <img class="m-2 border border-5" style="border-color: black;width: 300px;" :src="$store.state.urls.API_DOMAIN + getDish().image" alt=""> 
            </center>
            <div class="border border-primary border-2 rounded-2 m-3 p-3">
                <h3>Опис</h3>
                <p contenteditable="true">{{ getDish().description }}</p>
            </div>
            <div class="border border-primary border-2 rounded-2 m-3 p-3">
                <h3>Рецепт</h3>
                <p contenteditable="true">{{ getDish().recipe }}</p>
            </div>
        </div>

    </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';

export default {
    name: 'AdminDishView',
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
        this.fetchDish({ restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId, dishId: this.$route.params.dishId });
    },
    methods: {
        ...mapActions('dish', ['fetchDish']),
        ...mapGetters('dish', ['getDish']),
        deleteDish(){
            this.$store.dispatch('dish/deleteDish', { restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId, dishId: this.$route.params.dishId });
            this.$router.push({ name: 'admin-menu', params: { restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId } });
        }
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
