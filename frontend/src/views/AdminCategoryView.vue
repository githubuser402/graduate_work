<template>
    <div>
        <div class="border border-1 m-1">
            <router-link class="btn" :to="{name: 'home'}">Home</router-link>
            <router-link class="btn" :to="{name: 'admin'}">Restaurants</router-link>
            <router-link class="btn" :to="{name: 'admin-restaurant', params: { id: $route.params.restaurantId }}">Menus</router-link>
            <router-link class="btn" :to="{name: 'admin-menu', params: { restaurantId: $route.params.restaurantId, menuId: $route.params.menuId }}">Categories</router-link>
        </div>
        <center>
            <h1>{{ getCategory().title }}</h1>
        </center>
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
    
        ...mapActions('category', ['fetchCategory']),
        ...mapGetters('category', ['getCategory']),
    },
    computed: {
    },
};
</script>