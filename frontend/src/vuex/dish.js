const REST_API = 'http://localhost:8000/menu/v1';

export default {
    namespaced: true,
    state: {
        dishes: {
            type: Array,
            default: [],
        },
        dish: {
            type: Object,
            default: {},
        },
    },
    mutations: {},
    actions: {
        fetchDishes(store, { restaurantId, menuId }) {
            fetch(`${REST_API}/r/${restaurantId}/m/${menuId}/d/`,
                {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                    },
                }).then(response => {
                    if (response.ok) {
                        return response;
                    }
                    else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    return data.json();
                }).then(json => {
                    store.state.dishes = json;
                }).catch(error => {
                    console.log(error);
                    alert('error getting dishes');
                });
        },
        fetchDish(store, { restaurantId, menuId, dishId }) {
            fetch(`${REST_API}/r/${restaurantId}/m/${menuId}/d/?id=${dishId}`,
                {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                    },
                }).then(response => {
                    if (response.ok) {
                        return response;
                    }
                    else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    return data.json();
                }).then(json => {
                    store.state.dish = json;
                }).catch(error => {
                    console.log(error);
                    alert('error getting dish');
                });
        },
        createDish(store, { restaurantId, menuId, dish }) {
            const formData = new FormData();
            formData.append('json', JSON.stringify({ name: dish.name, description: dish.description, recipe: dish.recipe, price: dish.price, category_id: dish.category }));
            formData.append('image', dish.image);
            
            fetch(`${REST_API}/r/${restaurantId}/m/${menuId}/d/`,
                {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
                    },
                    body: formData,
                }).then(response => {
                    if (response.ok) {
                        return response;
                    }
                    else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    return data.json();
                }).then(json => {
                    store.state.dishes.push(json);
                }).catch(error => {
                    console.log(error);
                    alert('error creating dish');
                });
        },
        deleteDish(store, { restaurantId, menuId, dishId }) {
            fetch(`${REST_API}/r/${restaurantId}/m/${menuId}/d/?id=${dishId}`,
                {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
                    },
                }).then(response => {
                    if (response.ok) {
                        return response;
                    }
                    else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    store.state.dishes = store.state.dishes.filter(dish => dish.id !== dishId);
                }).catch(error => {
                    console.log(error);
                    alert('error deleting dish');
                });
        },
    },
    getters: {
        getDishes(state) {
            return state.dishes;
        },
        getDish(state) {
            return state.dish;
        }
    },
};