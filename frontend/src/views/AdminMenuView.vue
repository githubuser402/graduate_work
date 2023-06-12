<template>
    <div>
        <div class="d-flex column justify-content-between gap-4">
            <div class="border border-1 m-1">
                <router-link class="btn" :to="{ name: 'home' }">Домашня сторінка</router-link>
                <router-link class="btn" :to="{ name: 'admin' }">Ресторани</router-link>
                <router-link class="btn"
                    :to="{ name: 'admin-restaurant', params: { id: $route.params.restaurantId } }">Меню</router-link>
            </div>
            <div>
                <button class="btn btn-outline-secondary m-1 rounded-0" @click="generateQRCode"
                    style="width: 200px;">Створити QR-код</button>
                <button type="button" class="btn btn-outline-secondary m-1 rounded-0" @click="deleteMenu"
                    style="width:100px;">Видалити</button>
            </div>
        </div>
        <div v-if='showQRCode' class="qrcode-window">
            <img :src="qrcode" alt="qr code" class="border border-1 p-2">
            
            <div style="display: flex; justify-content: center;flex-direction: column;">
                <input v-model="getUrl" style="max-width: 400px;" readonly> 
                <button class="btn btn-primary-inverted border" @click="showQRCode=false" style="width:100px">Закрити</button>
                <button class="btn btn-primary" @click="saveQRCode()"
                    style="width: 100px; text-align: center;font-weight: 600;">Скачати</button>
            </div>
            <a ref="downloadLink" style="display: none;"></a>
        </div>
        <div class="d-flex justify-content-center">
            <h1>{{ getMenu().title }}</h1>
        </div>
        <DishList />
        <CategoryList />
    </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';
import DishList from '@/components/DishList.vue';
import CategoryList from '@/components/CategoryList.vue';
import { normalizeStyle } from 'vue';

export default {
    name: 'AdminMenuView',
    data() {
        return {
            qrcode: null,
            showQRCode: false,
        }
    },
    components: {
        DishList,
        CategoryList,
    },
    beforeMount() {
        this.$store.dispatch('checkLogin');
        if (!this.$store.getters.loggedIn) {
            this.$router.push({ name: 'admin' });
            this.$store.state.user.loggedIn = false;
        }
    },
    mounted() {

        this.fetchMenu({ restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId });
        // console.log('menu:', this.getMenu());
    },
    methods: {
        ...mapActions('menu', ['fetchMenu', 'deleteMenu', 'generateQRCode']),
        ...mapGetters('menu', ['getMenu', 'getQRCode']),
        ...mapMutations('menu', ['menuPageUrl']),
        deleteMenu() {
            this.$store.dispatch('menu/deleteMenu', { restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId });
            this.$router.push({ name: 'admin-restaurant', params: { id: this.$route.params.restaurantId } });
        },
        generateQRCode() {
            this.$store.dispatch('menu/generateQRCode', { restaurantId: this.$route.params.restaurantId, menuId: this.$route.params.menuId });
            this.qrcode = this.getQRCode();
            this.showQRCode = true;
        },
        saveQRCode() {
            const link = this.$refs.downloadLink;
            link.href = this.qrcode;
            link.download = 'qrcode.png'; // Specify the desired filename here

            // Programmatically click the link to trigger the download
            link.click();
            this.showQRCode = false;
        },
    },
    computed: {
        setBackground() {
            return {
                'background-image': `url(${this.$store.state.urls.API_DOMAIN}${this.getMenu().image})`,
                'background-repeat': 'no-repeat',
                'background-size': 'cover',
                'background-position': 'center',
                'height': '100vh',
            }
        },
        getUrl(){
            return  window.location.protocol + '//' + window.location.host + '/r/' + this.$route.params.restaurantId + '/m/' + this.$route.params.menuId + '/';
        }
    },
};
</script>

<style scoped>
.qrcode-window * {
    /* position: relative;  */
    display: flex;
    margin: auto;
    z-index: 3;
    top: 10%;
    /* width: 100px; */
    padding: 10px;
    text-align: center;
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