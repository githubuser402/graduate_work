<template>
    <div>
        <div class="control-panel">
            <h1>Menus</h1>
            <button v-if="$store.getters.loggedIn" type="button" @click="showForm=true" class="btn btn-sm btn-primary"><h5>Create menu</h5></button>
        </div>

        <div v-if="showForm === true" class="floating-window rounded rounded-3 p-5 m-3">
            <form v-on:submit.prevent="">
                <div class="mb-3">
                    <label for="titleInput" class="form-label">Menu title</label>
                    <input type="text" v-model="formData.title" class="form-control" id="titleInput"
                        aria-describedby="titleHelp">
                </div>
                <div class="mb-3">
                    <label for="imageInput">Image</label>
                    <input class="form-control" @change="handleFileChange" type="file" accept="image/*" id="imageInput">
                </div>
                <div class="d-flex flex-row">
                    <button class="btn btn-primary m-2" style="background-color: white;  color: blue;" @click="showForm = false">Cancel</button>
                    <button type="submit" @click="submitForm" class="btn btn-primary m-2">Create</button>
                </div>
            </form>
        </div>

        <div class="border border-2 border-success rounded-4 m-3 d-flex row">
            <div v-for="menu in getMenus()" :key="menu.id" class="card border p-3 m-3 border-primary border-2" style="width: 18rem; border-color: greenyellow">
                <img :src="$store.getters.getDomain + menu.image" class="card-img-top" alt="...">
                <router-link :to="{ name: 'admin-menu', params: { restaurantId: encodeURIComponent($route.params.id), menuId: encodeURIComponent(menu.id) } }">
                    <h5 class="card-title m-4">{{ menu.title }}</h5>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';

export default {
    name: 'MenuList',
    data() {
        return {
            showForm: false,
            formData: {
                title: '',
                image: null,
            },
        }
    },
    components: {
    },
    methods: {
        ...mapActions('menu', ['fetchMenus', 'createMenu']),
        ...mapGetters('menu', ['getMenus']),
        handleFileChange(e) {
            this.formData.image = e.target.files[0];
        },
        submitForm() {
            this.createMenu({
                restaurantId: this.$route.params.id,
                menu: this.formData,
            });
            this.showForm = false;
        },
    },
    mounted() {
        this.fetchMenus(this.$route.params.id);
        // console.log('menus: ', this.getMenus());
    },
    computed: {
    },
}
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