export default {
    namespaced: true,
    state: {
        dishes: [],
        showOrder: false,
    },
    mutations: {
        addDish(state, dish) {
            let found = false;
            state.dishes.forEach(element => {

                if (element.id == dish.id) {
                    element.quantity += 1;
                    found = true;
                    return;
                }
            });

            if (!found) {
                dish.quantity = 1;
                state.dishes.push(dish);
            }
        },
        removeDish(state, dish) {
            state.dishes.forEach(element => {
                if (element.id == dish.id) {
                    element.quantity -= 1;
                    if (element.quantity == 0) {
                        state.dishes.splice(state.dishes.indexOf(element), 1);
                    }
                    return;
                }
            });
        },
    },
    actions: {
        sendOrder(store, { tableNumber, restaurantId, menuId }) {
            const dishes = store.state.dishes.map(element => {
                return {
                    name: element.name,
                    quantity: element.quantity
                }});

                const time = new Date();

                fetch('http://localhost:8000/public/v1/order/', 
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        table_number: tableNumber,
                        restaurant_id: restaurantId,
                        menu_id: menuId,
                        dishes: dishes,
                        time: time.toJSON(),
                        price: store.getters.price,
                    })

                }).then(response => {
                    if (response.ok) {
                        return response;
                    }
                    else {
                        throw new Error();
                    }
                }).then(data => {
                    alert('Ваше замовлення прийнято');
                }).catch(error => {
                    console.log(error);
                    alert('На жаль, сталася помилка при замовленні');
                });
                

        },
    },
    getters: {
        price(state) {
            let price = 0;
            state.dishes.forEach(element => {
                price += element.price * element.quantity;
            });
            return price;
        },
        dishes(state) {
            return state.dishes;
        },
        quantity(state) {
            return function (id) {
                const dish = state.dishes.find(element => element.id == id);
                return dish ? dish.quantity : 0
            }
        },
    }
};