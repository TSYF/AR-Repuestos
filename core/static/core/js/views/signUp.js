import { validaEmail } from "../utils/detailing.js";
import userUtils from "../utils/user.js";

const form = document.getElementById("form_signup");

form.addEventListener("submit", e => {
    e.preventDefault();

    const { usernameSignIn: emailSignIn, registerUser } = userUtils;

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

            const { username } = user;

            emailSignIn(username, password)
                .then(signedUser => {
                    $("#email").val("");
                    $("#password").val("");
                    $("#confirm").val("");
                    loadUserUI(signedUser);
                    // open("/", "_self");
                }).catch(error => {
                    error.code && alert(userUtils.state.errorMessages[error.code]);
                });
        }).catch(error => {
            error.code && alert(userUtils.state.errorMessages[error.code]);
        });
});