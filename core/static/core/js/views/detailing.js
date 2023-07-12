import { validaEmail, validaRut, validaTelefono } from '../utils/detailing.js';

const form = document.getElementById("form_contacto");

form.addEventListener("submit", async e => {
    e.preventDefault();

    const csrf = document.querySelector('[name="csrfmiddlewaretoken"]');
    const nombreInput = document.getElementById("nombre");
    const rutInput = document.getElementById("rut");
    const emailInput = document.getElementById("email");
    const telefonoInput = document.getElementById("telefono"); 
    const servicioInput = document.getElementById("servicio"); 

    const csrfmiddlewaretoken = csrf.value;
    const rut = rutInput.value;
    const nombre = nombreInput.value;
    const email = emailInput.value;
    const telefono = telefonoInput.value;
    const servicio = servicioInput.value;


    if (telefono.substring(0, 2) = "+56") {
        telefono = telefono.replace(" ", "");
        telefono = telefono.substring(3, -1);
    }
    
    if (!validaRut(rut)) {
        return alert("El RUT no es válido");
    }

    if (!validaEmail(email)) {
        return alert("El E-Mail no es válido");
    }

    if (!validaTelefono(telefono)) {
        return alert("El número de Teléfono no es válido");
    }

    // return alert("Muchas gracias! Lo contactaremos a la brevedad");

    const data = {
        rut,
        nombre,
        email,
        telefono,
        servicio
    };

    try {
        const res = await fetch("/api/detailing/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfmiddlewaretoken
            },
            body: JSON.stringify(data)
        }).then(res => res.json());

        if (res.OK) {

            csrf.value = null;
            nombreInput.value = null;
            rutInput.value = null;
            emailInput.value = null;
            telefonoInput.value = null;
            servicioInput.value = null;
            return;
        }

        alert("Ha ocurrido un error. Por favor intente más tarde.");

    } catch (error) {
        console.error(error);
    }    
});