<template>
    <div class="category">
        <nav class="navbar menu-nav">
            <router-link role="button" :to="{name: 'public-menu', params: {restaurantId: $route.params.restaurantId, menuId: $route.params.menuId }}" class="btn btn-primary" style="background-color: #ccc;">Назад</router-link>
            <button class="order-btn" @click="$store.state.order.showOrder=!$store.state.order.showOrder">Рахунок</button>
        </nav>
        
        <Order v-if="$store.state.order.showOrder"/>
        <h2 class="card-container">{{ category.title }}</h2>
        <img :src="$store.state.urls.API_DOMAIN + category.image" alt="Category Image" class="category-image">
        <div class="d-flex flex-wrap justify-content-center card-container">
            <div v-for="dish in category.dishes" :key="dish.id" class="dish-card">
                <img :src="$store.state.urls.API_DOMAIN + dish.image" alt="Dish Image" class="dish-image">
                <div class="dish-details">
                    <h4 class="dish-name">{{ dish.name }}</h4>
                    <p class="dish-description">{{ dish.description }}</p>
                    <p class="dish-price">{{ dish.price }} грн</p>
                    <!-- <button class="btn btn-primary">Order Now</button> -->
                    <div class="d-flex column">
                        <button @click="removeDish(dish)" class="card-btn"><h3>-</h3></button>
                        <span class="p-2"><h3>{{ quantity(dish.id) }}</h3></span>
                        <button @click="addDish(dish)" class="card-btn"><h3>+</h3></button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import { mapGetters, mapActions, mapMutations, mapState } from "vuex";
import Order from '@/components/Order.vue';

export default {
    name: "CategoryView",
    data() {
        return {
        }
    },
    components: {
        Order,
    },
    computed: {
        ...mapGetters("publicMenu", ["category"]),
        ...mapGetters("order", ["quantity"]),
    },
    methods: {
        ...mapActions("publicMenu", ["fetchCategory"]),
        ...mapMutations("order", ["addDish", "removeDish"]),
    },
    mounted() {
        this.fetchCategory({
            restaurantId: this.$route.params.restaurantId,
            menuId: this.$route.params.menuId,
            categoryId: this.$route.params.categoryId,
        });
    },
};
</script>
  
<style>
.category-image{
    position: fixed;
    left: 0px;
    top: 0px;
    z-index: -1;
    width: 100%;
}
.card-container{
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin: 10px;
    border: 1px solid black;
    border-radius: 10px;
    background-color: rgba(183, 184, 209, 0.63);
    height: 100%;
    margin: 40px 50px 0px 50px;
    padding: 30px;
}
.dish-card{
    margin: 10px;
    display: flex;
    justify-content: center;
    flex-direction: column;
    border: 1px solid black;
    background-color: aliceblue;
    padding: 15px;
    max-height: 500px;
}
.dish-image{
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
}
.card-btn{
    border: 1px solid blue;
    border-radius: 10px;
    background-color: rgb(146, 230, 241);
    padding: 4px;
    max-height: 500px;
    margin: 10px;
    color: black;
}
</style>
  