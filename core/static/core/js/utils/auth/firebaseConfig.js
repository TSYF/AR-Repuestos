// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-auth.js";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCj1kpCtp7Savmr9MNwpq4hZUJhTFeipPs",
    authDomain: "arrepuestos-ed87a.firebaseapp.com",
    projectId: "arrepuestos-ed87a",
    storageBucket: "arrepuestos-ed87a.appspot.com",
    messagingSenderId: "294356422497",
    appId: "1:294356422497:web:9806d71656f063764cbf20"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { app, auth };
