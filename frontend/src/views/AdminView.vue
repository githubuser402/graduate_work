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
        if (!this.$store.getters.loggedIn) {
            this.$router.push({ name: 'admin' });
            this.$store.state.user.loggedIn = false;
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
body {
  height: 100%;
  background: #ebf4f5;
  background: linear-gradient(90deg, #ebf4f5 0%, #b5c6e0  100%);
  background: -moz-linear-gradient(90deg, #ebf4f5 0%, #b5c6e0  100%);
  background: -webkit-linear-gradient(90deg, #ebf4f5 0%, #b5c6e0 100%);
  filter: progid: DXImageTransform.Microsoft.gradient(startColorstr="#F86CA7", endColorstr="#F4D444", GradientType=1);
}
</style>