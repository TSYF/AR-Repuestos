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
    },
    cart: {
        showCarro() {
            const carro = document.getElementById("carro");
            
            carro.classList.toggle("d-none");
        },
        async get() {
            const listaCarro = document.querySelector("[data-carro-lista]");
            const totalCarro = document.querySelector("[data-carro-total]");
        
            try {
                const productos = await fetch("/carro/index", {
                    method: "GET",
                    headers: {
                        "Accept": "application/json"
                    }
                }).then(res => res.json());

                console.log(productos);
        
                productos.forEach((producto, i, arr) => {
                    
                    listaCarro.insertAdjacentHTML(
                        "beforeend",
                        `<li
                            key="${producto.id}"
                            class="
                                carro__item
                                d-flex
                                align-items-center
                                justify-content-between
                            "
                        >
                            ${producto.nombre} <span class="carro__item-count w-50">$${producto.precio}<br>Cantidad: ${producto.cantidad}</span>
                        </li>`
                    );
                });
        
                totalCarro.innerHTML = "Total: $" + productos.reduce((total, producto) => {
                    return total + producto.precio * producto.cantidad;
                }, 0);
        
            } catch (error) {
                console.trace(error);
            }
        },
        async delete(id) {
            const producto = await fetch("/carro/index", {
                method: "DELETE",
                headers: {
                    "Accept": "application/json"
                }
            }).then(res => res.json());

            console.log(producto);

            location.reload();
            
            return producto;
        }
    }
};

export default state;