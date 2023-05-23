import { createStore } from 'vuex';

const REST_API = 'http://127.0.0.1:8000/menu/v1';

const store = createStore({
    state: {
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
            }
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
            state.user.loginData.email = '';
            state.user.loginData.password = '';
            state.user.registerData.firstName = '';
            state.user.registerData.lastName = '';
            state.user.registerData.email = '';
            state.user.registerData.password = '';
        },
        logIn(state, payload) {
            console.log('logIn called');
            state.user.loggedIn = true;
            //payload must contain access token and refresh token
            //tokens must be saved in local storage

            localStorage.setItem('access_token', payload.access_token);
            localStorage.setItem('refresh_token', payload.refresh_token);
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
        sendLoginRequest(store) {
            // console.log('sendLoginRequest called');
            // console.log(JSON.stringify({ email: store.state.user.loginData.email, password: store.state.user.loginData.password }));
            fetch(`${REST_API}/token/`,
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
            }
        },
        sendRegisterRequest(store) {
            return fetch(`${REST_API}/u/`, {
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
                    return response.json()
                } else {
                    throw new Error(response.json());
                }
            }).then(data => {
                store.commit('saveRegisterData', data);
                return data;
            }).catch(error => {
                throw error;
            });
        },
        getters: {
            loggedIn(state) {
                return state.user.loggedIn;
            }
        }
    });

export default store; 