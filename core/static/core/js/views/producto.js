import state from '../utils/state.js';

$("#addToCarro").submit(async (e) => {
    state.cart.get();
})