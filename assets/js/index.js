import state from "./utils/state.js";
import userUtils from './utils/user.js';


$(() => {
	userUtils.currentUser()
        .then(res => {
            state.user.loadUser();
            $("#displayUser").text("@" + res.email.split("@")[0]);
            $("#displayUserManagement").text("@" + res.email.split("@")[0]);
            $("#sign_in").addClass("d-none");
            $("#sign_up").addClass("d-none");
            $("[data-signout]").removeClass("d-none");
        });

    $("[data-toggle-user]").click(e => {
        $("#manageUser").toggleClass("d-none");
    });

    $("[data-signout]").click(e => {
        userUtils.userSignOut()
            .then(res => {
                $("#displayUser").text("");
                $("#displayUserManagement").text("");
                $("#sign_in").removeClass("d-none");
                $("#sign_up").removeClass("d-none");
                $("[data-signout]").addClass("d-none");
            });       
            
    });

    
});