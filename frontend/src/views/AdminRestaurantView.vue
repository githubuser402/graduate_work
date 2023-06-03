<template>
    <div>
        <div class="border border-1 m-1">
            <router-link class="btn" :to="{name: 'home'}">Home</router-link>
            <router-link class="btn" :to="{name: 'admin'}">Restaurants</router-link>
        </div>
        <!-- <Breadcrumbs /> -->
        <!-- <router-link :to="{ name: 'admin-restaurant-edit', params: { id: getRestaurant().id } }">Edit</router-link> -->
        <center>
            <h1>{{ getRestaurant().name }}</h1>
        </center>
        <MenuList />
    </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';
import MenuList from '@/components/MenuList.vue';
import Breadcrumbs from '../components/Breadcrumbs.vue';

export default {
    name: 'AdminRestaurantView',
    data() {
        return {
        }
    },
    components: {
        MenuList,
        Breadcrumbs,
    },
    beforeMount() {
        this.$store.dispatch('checkLogin');
        if (!this.$store.getters.loggedIn) {
            this.$router.push({ name: 'admin' });
            this.$store.state.user.loggedIn = false;
        }
    },
    methods: {
        ...mapActions('restaurant', ['fetchRestaurant']),
        ...mapGetters('restaurant', ['getRestaurant']),
    },
    mounted() {
        this.fetchRestaurant(this.$route.params.id);
        console.log('restaurant:', this.getRestaurant());
    },
    computed: {
    },
};
</script>

<style scoped></style>