import state from "./state.js";
import { auth } from "./auth/firebaseConfig.js";
import {
	createUserWithEmailAndPassword,
	signInWithEmailAndPassword,
	signOut,
    onAuthStateChanged
} from "https://www.gstatic.com/firebasejs/9.22.1/firebase-auth.js";

const userUtils = {
    state: {
        errorMessages: {
            "auth/missing-password": "Falta Contraseña",
            "auth/invalid-email": "Email Inválido",
            "auth/user-not-found": "Usuario no Existe",
            "auth/wrong-password": "Contraseña Incorrecta",
            "auth/email-already-in-use": "Email ya está en uso",
            "auth/operation-not-allowed": "Operación no Permitida",
            "auth/weak-password": "Contraseña Débil"
        }
    },
    async registerUser(email, password) {
        try {
            const { user } = await createUserWithEmailAndPassword(
                auth,
                email,
                password
            );
            return user;
        } catch (error) {
            console.trace(error.code);
            throw error;
        }
    },
    async emailSignIn(email, password) {
        try {
            const { user } = await signInWithEmailAndPassword(
                auth,
                email,
                password
            );

            const userData = {
                uid: user.uid,
                email: user.email
            };
            
            state.user.setUser(userData);
            return userData;
        } catch (error) {
            console.trace(error.code);
            throw error;
        }
    },
    async userSignOut() {
        try {
            await signOut(auth);
            state.user.setUser({});
        } catch (error) {
            console.trace(error.code);
        }
    },
    currentUser() {
        return new Promise((resolve, reject) => {
            const unsuscribe = onAuthStateChanged(
                auth,
                async (user) => {
                    if (user) {
                        state.user.setUser({
                            uid: user.uid,
                            email: user.email
                        });
                    } else {
                        state.user.setUser({});
                    }
                    resolve(user);
                },
                (e) => reject(e)
            );
            unsuscribe();
        });
    },
};

export default userUtils;