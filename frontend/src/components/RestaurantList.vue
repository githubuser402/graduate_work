<template>
    <div>
        <div>
            <div class="control-panel">
                    <h1>Restaurants</h1>
                <button type="button" v-if="$store.getters.loggedIn" @click="showForm=true" class="btn btn-sm btn-primary"><h5>Create restaurant</h5></button>
            </div>

            <div>
                <div v-if="showForm===true" class="floating-window rounded rounded-3 p-5 m-3">
                    <form v-on:submit.prevent="">
                        <div class="mb-3">
                            <label for="nameInput" class="form-label">Restaurant name</label>
                            <input type="text" v-model="formData.name" class="form-control" id="nameInput">
                        </div>
                        <div class="mb-3">
                            <label for="addressInput">Address</label>
                            <input v-model="formData.address" id="addressInput" class="form-control">
                        </div>
                        <div class="mb-3">
                            <label for="descriprionInput">Descripiton</label>
                            <input v-model="formData.description" id="descriprionInput" class="form-control">
                        </div>
                        <div class="mb-3">
                            <label for="email">Email</label>
                            <input type="email" v-model="formData.email.work" id="email" class="form-control">
                        </div>
                        <div class="mb-3">
                            <label for="phone">Phone</label>
                            <input type="text" v-model="formData.contactNumber.work" id="email" class="form-control">
                        </div>
                        <div class="d-flex flex-row">
                            <button class="btn btn-primary m-2" style="background-color: white;  color: blue;" @click="showForm = false">Cancel</button>
                            <button type="submit" @click="submitForm" class="btn btn-primary m-2">Create</button>
                        </div>
                    </form>
                </div>
            </div>

            <div v-show="getRestaurants().length !== 0" class="border border-2 border-success rounded-4 m-3">
                <div v-for="restaurant in getRestaurants()" :key="restaurant.id" class="card border p-1 m-3"
                    style="width: 18rem;">
                    <div class="card-body">
                        <router-link :to="{ name: 'admin-restaurant', params: { id: encodeURIComponent(restaurant.id) } }">
                            <h5 class="card-title">{{ restaurant.name }}</h5>
                        </router-link>
                        <p class="card-text">{{ restaurant.description }}</p>
                        <p class="card-text"><strong>{{ restaurant.address }}</strong></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations, mapActions, mapGetters } from 'vuex';

export default {
    name: 'RestaurantList',
    data() {
        return {
            showForm: false,
            formData: {
                name: '',
                address: '',
                description: '',
                contactNumber: {work: ''},
                email: {work: ''},
            },
        }
    },
    components: {
    },
    methods: {
        ...mapActions('restaurant', ['fetchRestaurants', 'createRestaurant']),
        ...mapGetters('restaurant', ['getRestaurants']),

        submitForm() {
            this.createRestaurant(this.formData);
            this.showForm = false;
            this.name = '';
            this.address = '';
            this.description = '';
            this.contactNumber = {work: ''};
            this.email = {work: ''};
        },
    },
    mounted() {
        this.fetchRestaurants();
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