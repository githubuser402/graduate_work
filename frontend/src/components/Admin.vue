<template>
    <div>
        <nav>
            <RouterLink :to="{name: 'home'}">Home</RouterLink>
            <button @click="logOut">Log out</button>
        </nav>
        <div>
           <RestaurantList/>
        </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex';
import Menu from '@/components/Menu.vue';
import RestaurantList from '@/components/RestaurantList.vue';

export default {
    name: 'Admin',
    data() {
        return {
        }
    },
    components: {
        RestaurantList
    },
    methods: {
        ...mapMutations(['logOut']),
    },
    computed: {
    },
};
</script>

<style scoped>
nav {
    display: flex;
    justify-content: space-between;
    border-bottom: 3px solid #e5e5e5;
    flex-direction: row;
}

nav a {
    margin: 10px;
    text-decoration: none;
    color: #000;
}

nav button {
    margin: 10px;
    padding: 5px;
    background-color: #4caf50;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

nav *{
    padding-left: 10px;
    padding-right: 10px;
    max-width: 100px;
}
</style>