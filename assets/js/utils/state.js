const state = {
    user: {
        data: {},
        setUser(data) {
            this.data = data;

            if (Object.keys(data)) {
                return localStorage.setItem("userData", JSON.stringify(data));
            }
            return localStorage.removeItem("userData");
        },
        getUser() {
            return this.data;
        },
        loadUser() {
            if (!Object.keys(this.data)) {
                this.data = JSON.parse(localStorage.getItem("userData"));
            }
        }
    }
};

export default state;