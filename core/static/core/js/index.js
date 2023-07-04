import state from "./utils/state.js";
import userUtils from './utils/user.js';


$(() => {
	userUtils.currentUser()
        .then(user => {
            if (user.status !== 401) {
                
                state.user.loadUser();
                userUtils.loadUserUI(user);
                return
            }

            userUtils.unloadUserUI();
        });

    $("[data-toggle-user]").click(e => {
        $("#manageUser").toggleClass("d-none");
    });

    $("[data-signout]").click(e => {
        userUtils.userSignOut()
            .then(res => {
                userUtils.unloadUserUI();
            });       
            
    });

    
    $("[data-toggle-carro]").click(e => state.cart.showCarro() );

    state.cart.get();
});