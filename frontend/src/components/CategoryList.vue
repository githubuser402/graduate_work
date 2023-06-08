<template>
    <div>
        <div class="control-panel">
            <h1>Categories</h1>
            <button v-if="$store.getters.loggedIn" class="btn btn-primary" @click="showForm = true">Add category</button>
        </div>

        <div v-if="showForm === true" class="floating-window rounded rounded-3 p-5 m-3">
            <form v-on:submit.prevent="">
                <div class="mb-3">
                    <label for="titleInput" class="form-label">Category title</label>
                    <input type="text" v-model="formData.title" class="form-control" id="titleInput"
                        aria-describedby="titleHelp">
                </div>
                <div class="mb-3">
                    <label for="imageInput">Image</label>
                    <input class="form-control" @change="handleFileChange" type="file" accept="image/*" id="imageInput">
                </div>
                <div class="d-flex flex-row">
                    <button class="btn btn-primary m-2" style="background-color: white;  color: blue;"
                        @click="showForm = false">Cancel</button>
                    <button type="submit" @click="submitForm" class="btn btn-primary m-2">Create</button>
                </div>
            </form>
        </div>

        <div v-if="getCategories().length !== 0" class="border border-2 border-success rounded-4 m-3 flex-direction row">
            <div v-for="category in getCategories()" :key="category.id"
                class="card  border min-height-200 p-3 m-3 border-primary border-2"
                style="width: 18rem; border-color: greenyellow">
                <div class="card-body">
                    <img :src="$store.state.urls.API_DOMAIN + category.image" class="card-img-top rounded overflow-hidden"
                        style="width: 100%; height: 150px;" alt="">
                    <router-link :to="{
                        name: 'admin-category',
                        params: {
                            restaurantId: $route.params.restaurantId,
                            menuId: $route.params.menuId,
                            categoryId: encodeURIComponent(category.id)
                        }
                    }">
                        <h5 class="card-title m-4">{{ category.title }}</h5>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';

export default {
    name: 'CategoryList',
    data() {
        return {
            showForm: false,
            formData: {
                title: '',
                image: null,
            },
        }
    },
    mounted() {
        this.fetchCategories({ restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId });
    },
    components: {
    },
    methods: {
        ...mapActions('category', ['fetchCategories',]),
        ...mapGetters('category', ['getCategories',]),
        handleFileChange(e) {
            this.formData.image = e.target.files[0];
            console.log('file loaded')
        },
        submitForm() {
            // console.log("submitForm")
            this.$store.dispatch('category/createCategory', {
                restaurantId: this.$route.params.restaurantId,
                menuId: this.$route.params.menuId,
                title: this.formData.title,
                image: this.formData.image,
            });
            this.showForm = false;
        },
    },
    computed: {
    },
};
</script>

<style scoped>
/* .control-panel {
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

.floating-window {
    position: absolute;
    transform: translate(-50%, -50%);
    top: 30%;
    left: 50%;
    min-width: 600px;
    background-color: #fff;
    border: 1px solid #ccc;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
} */
</style>