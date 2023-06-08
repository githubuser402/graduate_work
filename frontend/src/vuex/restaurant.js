const REST_API = 'http://127.0.0.1:8000/menu/v1';


export default {
    namespaced: true,
    state: {
        restaurants: {
            type: Array,
            default: [],
        },
        restaurant: {
            type: Object,
            default: {},
        },
    },
    mutations: {
    },
    actions: {
        fetchRestaurants(store) {
            fetch(`${REST_API}/r/`,
                {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                    },
                }).then(response => {
                    if (response.ok) {
                        return response;
                    } else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    return data.json();
                }).then(json => {
                    store.state.restaurants = json;
                }).catch(error => {
                    console.log(error);
                    alert('error getting restaurants');
                })
        },
        fetchRestaurant(store, id) {
            fetch(`${REST_API}/r/?id=${id}`,
                {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                    },
                }).then(response => {
                    if (response.ok) {
                        return response;
                    } else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    return data.json();
                }).then(json => {
                    store.state.restaurant = json;
                })
        },
        createRestaurant(store, payload) {
            fetch(`${REST_API}/r/`,
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                    },
                    body: JSON.stringify({
                        'name': payload.name,
                        'description': payload.description,
                        'address': payload.address,
                        'contact_number': payload.contact_number,
                        'email': payload.email,
                    }),
                }).then(response => {
                    if (response.ok) {
                        return response;
                    } else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    return data.json();
                }).then(json => {
                    store.state.restaurants.push(json);
                }).catch(error => {
                    console.log(error);
                    alert('error creating restaurant');
                });
        },
        deleteRestaurant(store, {restaurantId}) {
            fetch(`${REST_API}/r/?id=${restaurantId}`,
                {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                    },
                }).then(response => {
                    if (response.ok) {
                        return response;
                    } else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    store.state.restaurants = store.state.restaurants.filter(restaurant => restaurant.id !== restaurantId);
                }).catch(error => {
                    console.log(error);
                    alert('error deleting restaurant');
                });
        },
    },
    getters: {
        getRestaurants(state) {
            console.log('in getter: ', state.restaurants)
            return state.restaurants;
        },
        getRestaurant(state) {
            return state.restaurant;
        },
    },
}
