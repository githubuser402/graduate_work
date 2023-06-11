<template>
    <div>
        <div class="control-panel">
            <h1>Страви</h1>
            <button v-if="$store.getters.loggedIn" class="btn btn-primary" @click="showForm=true">Додати страву</button>
        </div>

        <div v-if="showForm === true" style="transform: translate('-50%', '-50%'); top: 50%; background-color: antiquewhite;" class="floating-window rounded rounded-3 p-5 m-3">
            <form v-on:submit.prevent="">
                <div class="mb-3">
                    <label for="nameInput" class="form-label">Назва страви</label>
                    <input type="text" v-model="formData.name" class="form-control" id="nameInput"
                        aria-describedby="titleHelp">
                </div>
                <div class="mb-3">
                    <label for="descriptionTextarea">Опис</label>
                    <textarea class="form-control" style="resize: vertical" v-model="formData.description" id="descriptionTextarea"
                        rows="3"></textarea>
                </div>
                <div class="mb-3">
                    <label for="recipeTextarea">Рецепт</label>
                    <textarea class="form-control" v-model="formData.recipe" id="recipeTextarea"
                        rows="3"></textarea>
                </div>
                <div class="mb-3">
                </div>
                <div class="mb-3">
                    <label for="priceInput" class="form-label">Ціна</label>
                    <input type="number" v-model="formData.price" class="form-control" id="priceInput"
                        aria-describedby="titleHelp">
                </div>
                <div class="mb-3">
                    <label for="imageInput">Фото</label>
                    <input class="form-control" @change="handleFileChange" type="file" accept="image/*" id="imageInput">
                </div>
                <div class="mb-3">
                    <label for="categoryInput">Категорія</label>
                    <select id="categoryInput" v-model="formData.category">
                        <option v-for="category in getCategories()" :key="category.id" :value="category.id">{{ category.title }}</option>
                    </select>
                </div>
                <div class="d-flex flex-row">
                    <button class="btn btn-primary m-2" style="background-color: white;  color: blue;" @click="showForm = false">Cancel</button>
                    <button type="submit" @click="submitForm" class="btn btn-primary m-2">Create</button>
                </div>
            </form>
        </div>

        <div v-if="getDishes().length !== 0" class="border border-2 border-success rounded-4 m-3 d-flex row">
            <div v-for="dish in getDishes()" :key="dish.id" class="card border min-height-200 p-3 m-3 border-primary border-2"
                style="width: 18rem; border-color: greenyellow">
                <img :src="$store.getters.getDomain + dish.image" class="card-img-top" alt="">
                <router-link :to="{
                    name: 'admin-dish',
                    params: {
                        restaurantId: $route.params.restaurantId,
                        menuId: $route.params.menuId,
                        dishId: encodeURIComponent(dish.id)
                    }
                }">
                    <h5 class="card-title m-4">{{ dish.name }}</h5>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';

export default {
    name: 'DishList',
    data() {
        return {
            showForm: false,
            formData: {
                name: '',
                description: '',
                recipe: '',
                price: '',
                image: null,
                category: {
                    type: Number,
                    required: true,
                },
            },
        }
    },
    components: {
    },
    methods: {
        ...mapActions('dish', ['fetchDishes', 'createDish']),
        ...mapGetters('dish', ['getDishes']),
        ...mapGetters('category', ['getCategories']),
        submitForm() {
            this.createDish({
                restaurantId: this.$route.params.restaurantId,
                menuId: this.$route.params.menuId,
                dish: this.formData,
            });
            this.showForm = false;
        },
        handleFileChange(e) {
            this.formData.image = e.target.files[0];
        },
    },
    mounted() {
        this.fetchDishes({ restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId });
    },
    computed: {
    },
};
</script>

<style scoped>
.control-panel {
    background-color: #f8f9fa;
    padding-left: 40px;
    padding-right: 40px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 10px;
}

.control-panel * {
    margin: 10px;
}
</style>