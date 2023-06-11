
const REST_API = 'http://127.0.0.1:8000/public/v1';

export default ({
    namespaced: true,
    state: {
        menuNotFound: false,
        selectedCategory: null,
        category: {
            type: Object,
            default: null,
        },
        menu: {
        },
    },
    mutations: {
        setCategory(state, payload) {
            state.selectedCategory = payload;
        },
    },
    actions: {
        async fetchMenu(store, { restaurantId, menuId }) {
            fetch(`${REST_API}/r/${restaurantId}/m/${menuId}/`,
                {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                }).then(response => {
                    if (response.ok) {
                        return response;
                    }
                    else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    store.state.menuNotFound = false;
                    return data.json();

                }).then(json => {
                    store.state.menu = json;
                }).catch(error => {
                    store.state.menuNotFound = true;
                });

        },
        async fetchCategory(store, { restaurantId, menuId, categoryId }) {
            // use fetch, by curl example: curl -X GET http://localhost:8000/public/v1/r/2/m/8/c/13/
            fetch(`${REST_API}/r/${restaurantId}/m/${menuId}/c/${categoryId}/`,
                {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                }).then(response => {
                    if (response.ok) {
                        return response;
                    }
                    else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    store.state.menuNotFound = false;
                    return data.json();

                }).then(json => {
                    store.state.category = json;
                }).catch(error => {
                    store.state.menuNotFound = true;
                });
        },
    },
    getters: {
        menu(state) {
            return {
                id: state.menu.id,
                title: state.menu.title,
                image: state.menu.image,
            };
        },
        restaurant(state) {
            return state.menu.restaurant;
        },
        categories(state) {
            return state.menu.categories;
        },
        category(state) {
            return state.category
        }
    },
});