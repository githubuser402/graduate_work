<template>
    <div id="admin-view">
        <Login class="login-style" v-if="!$store.getters.loggedIn"></Login>
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
    beforeMount() {
        this.$store.dispatch('checkLogin');
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

<style scoped>
#admin-view {
    margin: 0 auto;
}
.login-style {
    margin: 0 auto;
    width: 50%;
}
</style>