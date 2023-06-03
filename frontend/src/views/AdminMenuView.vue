<template>
    <div>
        <div class="border border-1 m-1">
            <router-link class="btn" :to="{name: 'home'}">Home</router-link>
            <router-link class="btn" :to="{name: 'admin'}">Restaurants</router-link>
            <router-link class="btn" :to="{name: 'admin-restaurant', params: { id: $route.params.restaurantId }}">Menus</router-link>
        </div>
        <!-- <img :src="$store.getters.getDomain + getMenu().image" alt="Background Image"> -->
        <div class="d-flex justify-content-center">
            <h1>{{ getMenu().title }}</h1>
        </div>
        <DishList />
        <CategoryList />
    </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';
import DishList from '@/components/DishList.vue';
import CategoryList from '@/components/CategoryList.vue';

export default {
    name: 'AdminMenuView',
    data() {
        return {
        }
    },
    components: {
        DishList,
        CategoryList,
    },
    beforeMount() {
        this.$store.dispatch('checkLogin');
        if (!this.$store.getters.loggedIn) {
            this.$router.push({ name: 'admin' });
            this.$store.state.user.loggedIn = false;
        }
    },
    mounted() {
        // console.log('manu id: ', this.$route.params.menuId)
        this.fetchMenu({ restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId });
        // console.log('menu:', this.getMenu());
    },
    methods: {
        ...mapActions('menu', ['fetchMenu']),
        ...mapGetters('menu', ['getMenu']),
    },
    computed: {
        setBackground() {
            return {
                'background-image': `url(${this.$store.state.urls.API_DOMAIN}${this.getMenu().image})`,
                'background-repeat': 'no-repeat',
                'background-size': 'cover',
                'background-position': 'center',
                'height': '100vh',
            }
        },
    },
};
</script>

<style scoped></style>