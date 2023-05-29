<template>
    <div>
        <div v-for="restaurant in ">

        </div>
    </div>
</template>

<script>
import {mapMutations, mapActions} from 'vuex';

export default {
    name: 'RestaurantList',
    data() {
        return {
        }
    },
    components: {
    },
    methods: {
        ...mapActions('restaurant', ['fetchRestaurants']),
    },
    mounted() {
        this.fetchRestaurants();
        // alert(this.$store.getters['restaurant/getRestaurants'].length);
    },
    computed: {
    },
};
</script>

<style scoped>
</style>