const deleteCartItem = async(id) => {
    const { data: carro } = await fetch(`/api/carro/${id}/`, {
        method: "DELETE",
        headers: {
            "Accept": "application/json"
        }
    }).then(res => res.json());

    location.reload();
    
    return carro;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const updateCartItem = async(id) => {
    const csrftoken = getCookie('csrftoken');
    const cantidad = +prompt("¿Cuantos productos quiere?");

    const { data: carro } = await fetch(`/api/carro/${id}/`, {
        method: "PATCH",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({cantidad})
    }).then(res => res.json());

    location.reload();
    
    return carro;
}

const buyCart = async() => {
    

    const { data: carro } = await fetch(`/api/orden/buy/`, {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json "
        },
        body: JSON.stringify(cart)
    }).then(res => res.json());

    location.reload()

    return carro;
}