const REST_API = 'http://127.0.0.1:8000/menu/v1';

export default {
    namespaced: true,
    state: {
        restaurants: [],
        foo: 'bars',
    },
    mutations: {
    },
    actions: {
        fetchRestaurants(state) {
            fetch(`${REST_API}/r/`, 
            {
                method: 'GET',
                headers: {'Content-Type': 'application/json',},
            }).then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error(response.json());
                }
            }).then(data => {
                console.log(data);
                state.restaurants = data;
            }).catch(error => {
                console.log(error);
                alert('error getting restaurants');
            })
        },
    },
        getters: {
            getRestaurants(state) {
                return state.restaurants;
            },
        },
    }
