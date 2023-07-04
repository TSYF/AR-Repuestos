import state from "./state.js";

const userUtils = {
    state: {
        errorMessages: {
        }
    },
    async registerUser(username, email, password) {
        try {
            const user = await fetch(
                "/auth/signUp",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({username, email, password})
                }
            ).then(res => res.json());
            
            return user;
        } catch (error) {
            console.trace(error.code);
            throw error;
        }
    },
    async usernameSignIn(username, password) {
        try {
            const { id, username: name, email } = await fetch(
                "/auth/signIn",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        username,
                        password
                    })
                }
            ).then(res => res.json());

            const user = {
                id,
                username: name,
                email
            };
            
            state.user.setUser(user);

            return user;
        } catch (error) {
            console.trace(error.code);
            throw error;
        }
    },
    async userSignOut() {
        try {
            await fetch("/auth/signOut");
            state.user.setUser({});
        } catch (error) {
            console.trace(error.code);
        }
    },
    currentUser() {
        const response = fetch("/auth").then(res => res.json())

        return response;
    },
    loadUserUI(user) {
        $("#displayUser").text("@" + user.username);
        $("#displayUserManagement").text("@" + user.username);
        
        $("#sign_in").addClass("d-none");
        $("#sign_up").addClass("d-none");
        $("[data-signout]").removeClass("d-none");
    },
    unloadUserUI() {
        $("#displayUser").text("");
        $("#displayUserManagement").text("");
        $("#sign_in").removeClass("d-none");
        $("#sign_up").removeClass("d-none");
        $("[data-signout]").addClass("d-none");
    }
};

export default userUtils;