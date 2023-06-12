<template>
    <div>
        <div class="window">
            <h2>Замовлення</h2>
            <div v-for="dish in dishes">
                <p>{{ dish.name }} {{ dish.price }} x {{ dish.quantity }}={{ dish.price * dish.quantity }} грн</p>
            </div>
            <p>Загальна сума: {{ price }} грн</p>
            <div v-show="showTableInput">
                <label for="tableInput">Номер столику</label>
                <input v-model="tableNumber" type="number" />
            </div>
            <div class="d-flex column">
                <button class="m-2 btn btn-outline-secondary" @click="$store.state.order.showOrder = false">Закрити</button>
                <button :disabled="isOrderDisabled" class="m-2 btn btn-success" @click="makeOrder()">{{ orderButton
                }}</button>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions, mapState } from "vuex";

export default {
    name: "Order",
    data() {
        return {
            tableNumber: null,
            showTableInput: false,
        }
    },
    computed: {
        ...mapGetters("order", ["price", "dishes"]),
        ...mapState('order', ['showOrder',]),
        orderButton() {
            if (this.showTableInput) {
                return "Замовити"
            } else {
                return "Виберіть столик"
            }
        },
        isOrderDisabled() {
            if (this.dishes.length > 0) {
                return false
            }
            return true
        }
    },
    methods: {
        ...mapActions("order", ["sendOrder"]),
        makeOrder() {
            if (!this.showTableInput) {
                this.showTableInput = true;
            } else {
                if (!this.tableNumber) {
                    return
                }
                this.sendOrder({
                    tableNumber: this.tableNumber,
                    restaurantId: this.$route.params.restaurantId,
                    menuId: this.$route.params.menuId,
                });

                this.showTableInput = false;
                this.$store.state.order.showOrder = false;
            }
        },
    },
};
</script>

<style scoped>
.window {
    position: fixed;
    z-index: 3;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 600px;
    max-height: 600px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    padding: 20px 60px 20px 60px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
</style>