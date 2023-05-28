import { validaEmail, validaRut, validaTelefono } from '../utils/detailing.js';

const form = document.getElementById("form_contacto");

form.addEventListener("submit", e => {
    e.preventDefault();

    const rutInput = document.getElementById("rut");
    const emailInput = document.getElementById("email");
    const telefonoInput = document.getElementById("telefono"); 

    const rut = rutInput.value;
    const email = emailInput.value;
    const telefono = telefonoInput.value;

    if (!validaRut(rut)) {
        return alert("El RUT no es válido");
    }

    if (!validaEmail(email)) {
        return alert("El E-Mail no es válido");
    }

    if (!validaTelefono(telefono)) {
        return alert("El número de Teléfono no es válido")
    }

    return alert("Muchas gracias! Lo contactaremos a la brevedad");
});