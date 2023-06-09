import { createStore } from 'vuex';
import restaurant from './restaurant';
import menu from './menu';
import category from './category';
import dish from './dish';
import publicMenu from './publicMenu';

const REST_API = 'http://127.0.0.1:8000/menu/v1';

const store = createStore({
    modules: {
        restaurant,
        menu,
        category,
        dish,
        publicMenu,
    },
    state: {
        urls: {
            REST_API: 'http://localhost:8000/menu/v1',
            API_DOMAIN: 'http://localhost:8000',
        },
        user: {
            loggedIn: false,
            loginData: {
                email: '',
                password: ''
            },
            registerData: {
                firstName: '',
                lastName: '',
                email: '',
                password: ''
            },
        },
    },
    mutations: {
        logOut(state, payload) {
            console.log('logOut called');
            console.log(payload);
            state.user.loggedIn = false;
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            // set user data to empty
        },
        clearUserFields(state) {
            state.user.loginData.email = '';
            state.user.loginData.password = '';
            state.user.registerData.firstName = '';
            state.user.registerData.lastName = '';
            state.user.registerData.email = '';
            state.user.registerData.password = '';
        },
        logIn(state, payload) {
            console.log('logIn called');
            //payload must contain access token and refresh token
            //tokens must be saved in local storage
            console.log(payload)
            try {
                localStorage.setItem('access_token', payload.access);
                console.log(payload.access_token);
                localStorage.setItem('refresh_token', payload.refresh);
                state.user.loggedIn = true;
            }
            catch (error) {
                alert('error occured while logging in');
            }

        },
        saveRefisterData(state, payload) {
            state.user.registerData.firstName = payload.firstName;
            state.user.registerData.lastName = payload.lastName;
            state.user.registerData.email = payload.email;
            state.user.registerData.password = payload.password;
        },
        setLoginEmail(state, payload) {
            state.user.loginData.email = payload;
        },
        setLoginPassword(state, payload) {
            state.user.loginData.password = payload;
        },
        setRegisterFirstName(state, payload) {
            state.user.registerData.firstName = payload;
        },
        setRegisterLastName(state, payload) {
            state.user.registerData.lastName = payload;
        },
        setRegisterEmail(state, payload) {
            state.user.registerData.email = payload;
        },
        setRegisterPassword(state, payload) {
            state.user.registerData.password = payload;
        },
    },
    actions: {
        async sendLoginRequest(store) {
            // console.log('sendLoginRequest called');
            // console.log(JSON.stringify({ email: store.state.user.loginData.email, password: store.state.user.loginData.password }));
            await fetch(`${REST_API}/token/`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email: store.state.user.loginData.email, password: store.state.user.loginData.password })
                }).then(response => {
                    if (response.ok) {
                        //if success response must contain access token and refresh token
                        // it must be saved in local storage
                        // save may be done in a separate function or in logIn
                        return response.json()
                    } else {
                        throw new Error('Some error occured');
                    }
                }).then(data => {
                    store.commit('logIn', data);
                }).catch(error => {
                    console.log(error);
                });
        },
        async sendRegisterRequest(store) {
            return new Promise((resolve, reject) => {
                fetch(`${REST_API}/u/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(
                        {
                            email: store.state.user.registerData.email,
                            password: store.state.user.registerData.password,
                            first_name: store.state.user.registerData.firstName,
                            last_name: store.state.user.registerData.lastName
                        }),
                }).then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    resolve(data);
                }).catch(error => {
                    reject(error);
                });
            })
        },
        async checkLogin(state) {
            const token = localStorage.getItem('access_token');
            const refreshToken = localStorage.getItem('refresh_token');
            // console.log(token);
            // console.log(refreshToken);
            // console.log(token != null && refreshToken != null);

            if (token != null) {
                await fetch(`${REST_API}/token/verify/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ token: token })
                }).then(response => {
                    console.log(response.status)
                    if (response.status >= 200 && response.status < 300) {
                        store.state.user.loggedIn = true;
                        return;
                    }
                    else {
                        state.user.loggedIn = false;
                        throw new Error(response.status);
                    }
                }).catch(error => {
                    alert('token has expired, please log in again');
                });
            }
            else {
                state.user.loggedIn = false;
            }
        },
    },
    getters: {
        loggedIn(state) {
            console.log(state.user.loggedIn)
            return state.user.loggedIn;
        },
        getDomain(state) {
            return state.urls.API_DOMAIN;
        },
        getAPIURL(state) {
            return state.urls.REST_API;
        },
    }
});

export default store; 