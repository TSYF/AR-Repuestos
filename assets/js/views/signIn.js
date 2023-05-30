import userUtils from "../utils/user.js";

const form = document.getElementById("form_login");

form.addEventListener("submit", e => {
    e.preventDefault();

    const { emailSignIn } = userUtils;

    const email = $("#email").val();
    const password = $("#password").val();
    
    emailSignIn(email, password)
        .then(res => {
            $("#email").val("");
            $("#password").val("");
            $("#displayUser").text("@" + res.email.split("@")[0]);
            open("index.html", "_self");
        }).catch(error => {
            if (error.code === "auth/user-not-found") {
                alert("Usuario No Existe");
            }
        });
});