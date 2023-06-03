<template>
    <div>
        <div class="border border-1 m-1">
            <router-link class="btn" :to="{name: 'home'}">Home</router-link>
            <router-link class="btn" :to="{name: 'admin'}">Restaurants</router-link>
            <router-link class="btn" :to="{name: 'admin-restaurant', params: { id: $route.params.restaurantId }}">Menus</router-link>
            <router-link class="btn" :to="{name: 'admin-menu', params: { restaurantId: $route.params.restaurantId, menuId: $route.params.menuId }}">Dishes</router-link>
        </div>
        <div>
            <center>
                <h1 contenteditable="true">{{ getDish().name }}</h1>
            </center>
            <div class="border border-primary border-2 rounded-2 m-3 p-3">
                <h3>Description</h3>
                <p contenteditable="true">{{ getDish().description }}</p>
            </div>
            <div class="border border-primary border-2 rounded-2 m-3 p-3">
                <h3>Recipe</h3>
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
    },
    computed: {
    },
};
</script>