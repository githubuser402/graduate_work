<template>
    <div id="admin-view">
        <RouterLink :to="{name: 'home'}">Home</RouterLink>
        <Login v-if="!$store.getters.loggedIn"></Login> 
        <Admin v-else></Admin>
    </div>
</template>

<script>
import Login from '@/components/Login.vue';
import Admin from '@/components/Admin.vue';

export default {
    name: 'AdminView',
    data() {
        return {
        }
    },
    components: {
        Login,
        Admin,
    },
    methods: {

    },
    computed: {

    },
};
</script>

<style>
#admin-view {
    display: flex;
    justify-content: center;
}
</style>