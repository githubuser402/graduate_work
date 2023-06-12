
const REST_API = 'http://127.0.0.1:8000/menu/v1';

export default {
    namespaced: true,
    state: {
        menus: {
            type: Array,
            default: [],
        },
        menu: {
            type: Object,
            default: {},

        },
        qrcode: {
            type: Object,
            default: {},
        },
    },
    mutations: {
        menuPageUrl(store, { restaurantId, menuId }) {
            return window.location.protocol + '//' + window.location.host + '/r/' + restaurantId + '/m/' + menuId + '/';
        },
    },
    actions: {
        fetchMenus(store, restaurantId) {
            fetch(`${REST_API}/r/${restaurantId}/m/`,
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
                    // console.log(json);
                    store.state.menus = json;
                }).catch(error => {
                    console.log(error);
                    alert('error getting menus');
                });
        },
        fetchMenu(store, { restaurantId, menuId }) {
            fetch(`${REST_API}/r/${restaurantId}/m/?id=${menuId}`,
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
                    store.state.menu = json;
                }).catch(error => {
                    console.log(error);
                    alert('error getting menu');
                });
        },
        createMenu(store, { restaurantId, menu }) {
            const formData = new FormData();
            formData.append('json', JSON.stringify({ title: menu.title }));
            formData.append('image', menu.image);

            fetch(`${REST_API}/r/${restaurantId}/m/`,
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
                    store.state.menus.push(json);
                }).catch(error => {
                    console.log(error);
                    alert('error creating menu');
                });
        },
        deleteMenu(store, { restaurantId, menuId }) {
            fetch(`${REST_API}/r/${restaurantId}/m/?id=${menuId}`,
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
                    store.state.menus = store.state.menus.filter(menu => menu.id !== menuId);
                }).catch(error => {
                    console.log(error);
                    alert('error deleting menu');
                });
        },
        generateQRCode(store, { restaurantId, menuId }) {
            const fullDomain = window.location.protocol + '//' + window.location.host + '/r/' + restaurantId + '/m/' + menuId + '/';
            // console.log(fullDomain);
            fetch(`https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=${fullDomain}`, 
            {
                method: 'GET',
            }).then(response => {
                if (response.ok) {
                    return response;
                }
                else {
                    throw new Error();
                }
            }).then(data => {
                return data.blob();
            }).then(blob => {
                store.state.qrcode = URL.createObjectURL(blob);
            }).catch(error => {
                alert('error generating QRCode');
            });
            
        },
    },
    getters: {
        getMenus(state) {
            return state.menus;
        },
        getMenu(state) {
            return state.menu;
        },
        getQRCode(state) {
            return state.qrcode;
        }
    },
};