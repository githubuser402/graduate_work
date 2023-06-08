const REST_API = 'http://localhost:8000/menu/v1';

export default {
    namespaced: true,
    state: {
        categories: {
            type: Array,
            default: [],
        },
        category: {
            type: Object,
            default: {},
        },
    },

    mutations: {

    },
    actions: {
        fetchCategories(state, { restaurantId, menuId }) {
            fetch(`${REST_API}/r/${restaurantId}/m/${menuId}/c/`,
                {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
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
                    state.state.categories = json;
                }).catch(error => {
                    console.log(error);
                    alert('error getting categories');
                });
        },
        fetchCategory(store, { restaurantId, menuId, categoryId }) {
            fetch(`${REST_API}/r/${restaurantId}/m/${menuId}/c/?id=${categoryId}`,
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
                    store.state.category = json;
                }).catch(error => {
                    console.log(error);
                    alert('error getting category');
                });
        },
        createCategory(store, { restaurantId, menuId, title, image }) {
            const formData = new FormData();
            formData.append('json', JSON.stringify({ title: title }));
            formData.append('image', image);

            fetch(`${REST_API}/r/${restaurantId}/m/${menuId}/c/`,
                {
                    method: 'POST',
                    headers: { 'Authorization': `Bearer ${localStorage.getItem('access_token')}` },
                    body: formData,
                }).then(response => {
                    if (response.ok) {
                        return response;
                    } else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    return data.json();
                }).then(json => {
                    store.state.categories.push(json);
                }).catch(error => {
                    console.log(error);
                    alert('error creating category');
                });
        },
        deleteCategory(store, { restaurantId, menuId, categoryId }) {
            fetch(`${REST_API}/r/${restaurantId}/m/${menuId}/c/?id=${categoryId}`,
                {
                    method: 'DELETE',
                    headers: { 'Authorization': `Bearer ${localStorage.getItem('access_token')}` },
                }).then(response => {
                    if (response.ok) {
                        return response;
                    } else {
                        throw new Error(response.json());
                    }
                }).then(data => {
                    store.state.categories = store.state.categories.filter(category => category.id !== categoryId);
                }).catch(error => {
                    console.log(error);
                    alert('error deleting category');
                });
        },
    },
    getters: {
        getCategories(state) {
            return state.categories;
        },
        getCategory(state) {
            return state.category;
        },
    },
};