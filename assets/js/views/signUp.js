import { validaEmail } from "../utils/detailing.js";
import userUtils from "../utils/user.js";

const form = document.getElementById("form_signup");

form.addEventListener("submit", e => {
    e.preventDefault();

    const { emailSignIn, registerUser } = userUtils;

    const email = $("#email").val();
    const password = $("#password").val();
    const confirmPassword = $("#confirm").val();

    if (!validaEmail(email)) {
        return alert("Email Inválido");
    }
    
    if (password !== confirmPassword) {
        return alert("Contraseñas no Coinciden");
    }
    
    registerUser(email, password)
        .then(user => {

            const { email: userEmail } = user;

            emailSignIn(userEmail, password)
                .then(signedUser => {
                    $("#email").val("");
                    $("#password").val("");
                    $("#confirm").val("");
                    $("#displayUser").text("@" + signedUser.email.split("@")[0]);
                    open("index.html", "_self");
                }).catch(error => {
                    error.code && alert(userUtils.state.errorMessages[error.code]);
                });
        }).catch(error => {
            error.code && alert(userUtils.state.errorMessages[error.code]);
        });
});