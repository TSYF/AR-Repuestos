import state from "./utils/state.js";
import userUtils from './utils/user.js';


$(() => {
    const { currentUser, loadUserUI, unloadUserUI, userSignOut } = userUtils;
    
	currentUser()
        .then(({ data: user, code }) => {
            if (code !== 401) {
                
                state.user.loadUser();
                loadUserUI(user);
                return
            }

            unloadUserUI();
        });

    $("[data-toggle-user]").click(e => {
        $("#manageUser").toggleClass("d-none");
    });

    $("[data-signout]").click(e => {
        userSignOut()
            .then(res => {
                unloadUserUI();
            });       
            
    });

    
    $("[data-toggle-carro]").click(e => state.cart.showCarro() );

    state.cart.get();
});