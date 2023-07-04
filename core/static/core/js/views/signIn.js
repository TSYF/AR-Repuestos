import userUtils from "../utils/user.js";

const form = document.getElementById("form_login");

form.addEventListener("submit", e => {
    e.preventDefault();

    const { usernameSignIn: usernameSignIn, loadUserUI } = userUtils;

    const username = $("#username").val();
    const password = $("#password").val();
    
    usernameSignIn(username, password)
        .then(user => {
            $("#username").val("");
            $("#password").val("");
            loadUserUI(user);
            // open("/", "_self");
        }).catch(error => {
            console.log(error);
        });
});