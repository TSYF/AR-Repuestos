import { showCarrito } from "./utils/carrito.js";


const btnCarrito = document.querySelector("[data-toggle-carrito]");

btnCarrito.addEventListener("click", e => {
    e.preventDefault();

    showCarrito();
});