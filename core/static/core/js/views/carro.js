const deleteCartItem = async(id) => {
    const carro = await fetch(`/carro/delete/${id}`, {
        method: "DELETE",
        headers: {
            "Accept": "application/json"
        }
    }).then(res => res.json());

    location.reload();
    
    return carro;
}

const updateCartItem = async(id) => {
    const cantidad = +prompt("¿Cuantos productos quiere?");

    const carro = await fetch(`/carro/update/${id}`, {
        method: "PATCH",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json "
        },
        body: JSON.stringify({cantidad})
    }).then(res => res.json());

    location.reload();
    
    return carro;
}
