import { validaEmail } from "../utils/detailing.js";
import userUtils from "../utils/user.js";

const form = document.getElementById("form_signup");

form.addEventListener("submit", e => {
    e.preventDefault();

    const { usernameSignIn, registerUser, loadUserUI } = userUtils;

    const username = $("#username").val();
    const email = $("#email").val();
    const password = $("#password").val();
    const confirmPassword = $("#confirm").val();

    if (!validaEmail(email)) {
        return alert("Email Inválido");
    }
    
    if (password !== confirmPassword) {
        return alert("Contraseñas no Coinciden");
    }
    
    registerUser(username, email, password)
        .then(user => {

            const { username: name } = user;

            usernameSignIn(name, password)
                .then(signedUser => {
                    $("#username").val("");
                    $("#email").val("");
                    $("#password").val("");
                    $("#confirm").val("");
                    loadUserUI(signedUser);
                    // open("/", "_self");
                }).catch(error => {
                    error.code && alert(error.message);
                });
        }).catch(error => {
            error.code && alert(error.message);
        });
});