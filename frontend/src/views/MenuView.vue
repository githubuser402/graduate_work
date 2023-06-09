<template>
    <div>
        <img :src="$store.getters.getDomain + getMenu().image" class="background-image" alt="Responsive image">
        <div class="content">
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'MenuView',
    data() {
        return {

        }
    },
    methods: {
        ...mapActions('publicMenu', ['fetchMenu']),
        ...mapGetters('publicMenu', ['getMenu']),
    },
    mounted() {
        this.fetchMenu({ restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId })
        console.log(this.$route.params.restaurantId, this.$route.params.menuId)
        // this.$store.dispatch('publicMenu/fetchMenu', { restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId })
    },
}
</script>

<style scoped>
.background-image {
    top: 0;
    left: 0;
    width: 400px;
    z-index: 1;
    border-radius: 12px;
}
.content {
  z-index: 2;
  width: 100%;
  height: 90%;
  background-color: aliceblue;
  background-color: white;
}
</style>