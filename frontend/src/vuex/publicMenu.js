
const REST_API = 'http://127.0.0.1:8000/public/v1';

export default({
    namespaced: true,
    state: {
        menuNotFound: false,
        menu: {
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
    },
    getters: {
        getMenu(state) {
            return state.menu;
        },
    },
});