<template>
  <div id="login-form">
    
    <h2>{{ isRegister ? 'Реєстрація' : 'Вхід' }}</h2>
    <form v-if="!isRegister" @submit.prevent="login">
      <label for="email">Емейл:</label>
      <input type="email" id="email" v-model="email" required>

      <label for="password">Пароль:</label>
      <input type="password" id="password" v-model="password" required>

      <button type="submit">Увійти</button>
    </form>

    <form v-if="isRegister" @submit.prevent="register">
      <label for="firstName">Ім'я:</label>
      <input type="text" id="firstName" v-model="firstName" required>

      <label for="lastName">Прізвище:</label>
      <input type="text" id="lastName" v-model="lastName" required>

      <label for="email">Емейл:</label>
      <input type="email" id="email" v-model="emailRegister" required>

      <label for="password">Пароль:</label>
      <input type="password" id="password" v-model="passwordRegister" required>

      <button type="submit">Зареєструватись</button>
    </form>

    <p v-if="isRegister">
      Вже є акаунт? <a href="#" @click="toggleForm">Увійти</a>
    </p>
    <p v-else>
      Ще немає акаунту? <a href="#" @click="toggleForm">Зареєструватись</a>
    </p>
  </div>
</template>
  
<script>
import Message from '@/components/Message.vue'

export default {
  name: 'Login',
  data() {
    return {
      isRegister: false,
      // loginData: {
      //   email: '',
      //   password: ''
      // },
      // registerData: {
      //   firstName: '',
      //   lastName: '',
      //   email: '',
      //   password: ''
      // }
    };
  },
  components: {
    Message,
  },
  methods: {
    login() {
      this.$store.dispatch('sendLoginRequest');
    },
    register() {
      this.$store.dispatch('sendRegisterRequest')
        .then((response) => {
          this.$store.commit('setLoginEmail', this.$store.state.user.registerData.email);
          this.$store.commit('setLoginPassword', this.$store.state.user.registerData.password);
          this.$store.dispatch('sendLoginRequest');
          this.$store.commit('clearUserFields');
        }), error => {
          console.log('Error', error);
        };
    },
    toggleForm() {
      this.isRegister = !this.isRegister;
      this.$store.state.loggedIn = true;
    },
  },
  computed: {
    email: {
      get() {
        return this.$store.state.user.loginData.email;
      },
      set(value) {
        this.$store.commit('setLoginEmail', value);
      },
    },
    password: {
      get() {
        return this.$store.state.user.loginData.password;
      },
      set(value) {
        console.log('Setting password', value);
        this.$store.commit('setLoginPassword', value);
      },
    },
    firstName: {
      get() {
        return this.$store.state.user.registerData.firstName;
      },
      set(value) {
        this.$store.commit('setRegisterFirstName', value);
      },
    },
    lastName: {
      get() {
        return this.$store.state.user.registerData.lastName;
      },
      set(value) {
        this.$store.commit('setRegisterLastName', value);
      },
    },
    emailRegister: {
      get() {
        return this.$store.state.user.registerData.email;
      },
      set(value) {
        this.$store.commit('setRegisterEmail', value);
      },
    },
    passwordRegister: {
      get() {
        return this.$store.state.user.registerData.password;
      },
      set(value) {
        this.$store.commit('setRegisterPassword', value);
      },
    },
  }
};
</script>
  
<style>
#login-form {
  max-width: 300px;
}

.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f4f4f4;
  border-radius: 5px;
}

h2 {
  text-align: center;
}

form {
  margin-top: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #4caf50;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.form-toggle-text {
  margin-top: 20px;
  text-align: center;
}
</style>
