<template>
    <div>
        <nav class="navbar menu-nav" style="justify-content: flex-end;">
            <button class="order-btn" @click="$store.state.order.showOrder=!$store.state.order.showOrder">Рахунок</button>
        </nav>
        
        <Order v-if="$store.state.order.showOrder"/>
        <div class="row p-0 m-0">
            <center style="position:fixed; left: 0px; top: 0px; z-index: -1;">
                <img :src="$store.state.urls.API_DOMAIN + menu.image" style="width: 100%;" alt="Menu Image"
                    class="img-fluid">
            </center>
        </div>
        <div class="border border-3 jumbotron text-center m-3 p-2" style="background-color: rgba(183, 184, 209, 0.63);">
            <h1>{{ restaurant.name }}</h1>
            <p>{{ restaurant.address }}</p>
            <p>{{ restaurant.description }}</p>
            <p>Contact: {{ restaurant.email.work }}</p>
        </div>
        <div class="container border border-3" style="width: 100%;background-color: rgba(183, 184, 209, 0.63);">
            <div class="row">
                <div class="col-md-12">
                    <h2>Menu Categories</h2>
                </div>
            </div>

            <div class="row d-flex justify-content-center">
                <div v-for="category in categories" :key="category.id" @click="goToCategory(category.id)"
                    class="card mb-3 d-flex flex-column align-items-center justify-content-center p-4 m-5" style="max-width: 400px;;">
                    <img :src="$store.state.urls.API_DOMAIN + category.image" class="card-img-top"
                        style="width: 300px; height: 300px;" alt="Category Image">
                    <div class="card-body">
                        <h5 class="card-title">{{ category.title }}</h5>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>
  
<script>
import { mapGetters, mapActions, mapMutations, mapState } from 'vuex';
import Order from '@/components/Order.vue';

export default {
    name: 'MenuView',
    data() {
        return {
        }
    },
    components: {
        Order,
    },
    computed: {
        ...mapGetters('publicMenu', ['menu', 'categories', 'restaurant']),
        ...mapState('order', ['showOrder']),
    },
    methods: {
        ...mapActions('publicMenu', ['fetchMenu']),
        ...mapMutations('publicMenu', ['setCategory']),
        // ...mapMutations('order', ['changeOrderView']),

        goToCategory(categoryId) {
            this.$router.push({ name: 'public-category', params: { restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId, categoryId: categoryId } });
            this.setCategory(categoryId);
        },  
    },
    beforeMount() {
        this.fetchMenu({ restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId });
    },
};
</script>
  
<style>

</style>