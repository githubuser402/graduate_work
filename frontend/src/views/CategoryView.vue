<template>
    <div class="category">
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
                        <button class="card-btn"><h3>-</h3></button>
                        <span class="p-2"><h3>0</h3></span>
                        <button class="card-btn"><h3>+</h3></button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import { mapGetters, mapActions } from "vuex";

export default {
    name: "CategoryView",
    computed: {
        ...mapGetters("publicMenu", ["category"]),
    },
    methods: {
        ...mapActions("publicMenu", ["fetchCategory"]),
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
  