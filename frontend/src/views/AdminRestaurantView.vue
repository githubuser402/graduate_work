<template>
    <div>
        <div class="d-flex column justify-content-between gap-4">
            <div class="border border-1 m-1">
                <router-link class="btn" :to="{ name: 'home' }">Домашня сторінка</router-link>
                <router-link class="btn" :to="{ name: 'admin' }">Ресторани</router-link>
            </div>
            <div>
                <button type="button" class="btn btn-outline-secondary m-1 rounded-0" @click="deleteRestaurant()" style="width:100px;">Видалити</button>
            </div>
        </div>
        <div class="d-flex justify-content-center column">
            <h1>{{ getRestaurant().name }}</h1>
        </div>
        <div class="border border-3 m-3 p-2 rounded-4">
            <p>Адреса: {{ getRestaurant().address }}</p>
            <p>Опис: {{ getRestaurant().description }}</p>
        </div>
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
        deleteRestaurant() {
            this.$store.dispatch('restaurant/deleteRestaurant', { restaurantId: this.$route.params.id });
            this.$router.push({ name: 'admin' });
        },
    },
    mounted() {
        this.fetchRestaurant(this.$route.params.id);
        console.log('restaurant:', this.getRestaurant());
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