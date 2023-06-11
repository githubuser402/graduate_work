<template>
    <div>
        <nav>
            <RouterLink :to="{ name: 'home' }">Домашня сторінка</RouterLink>
            <TelegramIntegration v-if="showTelegramIntegration"/>
            <div class="d-flex column">
                <button @click="changeTelegramIntegrationView()">Інтеграція з Telegram</button>
                <button @click="logOut">Вийти з акаунту</button>
            </div>
        </nav>
        <div>
            <RestaurantList />
        </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex';
import RestaurantList from '@/components/RestaurantList.vue';
import TelegramIntegration from '@/components/TelegramIntegration.vue';

export default {
    name: 'Admin',
    data() {
        return {
            showTelegramIntegration: false,
        }
    },
    components: {
    RestaurantList,
    TelegramIntegration,
    TelegramIntegration
},
    methods: {
        ...mapMutations(['logOut']),
        changeTelegramIntegrationView(){
            this.showTelegramIntegration = !this.showTelegramIntegration;
            console.log('clicked')
        }
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

nav * {
    padding-left: 10px;
    padding-right: 10px;
    max-width: 400px;
}
</style>