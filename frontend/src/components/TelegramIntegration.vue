<template>
    <div>
        <div class="window">
            <h2>Інтеграція з Telegram</h2>
            <label for="token"></label>
            <textarea id="token" type="text" cols="5" readonly>{{ accessToken }}</textarea>
            <p class="p-3 ">Для отримання оновлень меню в чаті вам необхідно додати телеграм бота <b>@menu_management_bot</b> в вашу групу, скопіювати токен, та відпривати котанду '/login ваш токен' в чат</p>
        </div>
    </div>
</template>

<script>
export default{
    name: 'TelegramIntegration',
    data() {
        return {
        }
    },
    methods: {
    },
    computed: {
        accessToken(){
            return '/login ' + localStorage.getItem('access_token');
        }
    },
}
</script>

<style scoped>
.window{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 600px;
    max-height: 600px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
    padding: 20px 60px 20px 60px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
</style>