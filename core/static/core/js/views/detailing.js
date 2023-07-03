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

    if (!validaRut(rut)) {
        return alert("El RUT no es válido");
    }

    if (!validaEmail(email)) {
        return alert("El E-Mail no es válido");
    }

    if (!validaTelefono(telefono)) {
        return alert("El número de Teléfono no es válido")
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
        const res = await fetch("/contacto-detailing/store", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfmiddlewaretoken
            },
            body: JSON.stringify(data)
        }).then(res => res.json());

    } catch (error) {
        console.error(error);
    }    
});