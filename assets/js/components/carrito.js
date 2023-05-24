const showCarrito = () => {
    const carrito = document.getElementById("carrito");
    
    carrito.style.display = (carrito.style.display === "none") ? "" : "none";
}

const logShit = _ => {
    
    console.log("%cShit %chas been %clogged!", "color:#FFFF00", "color:#FFFFFF", "color:#0000FF");
}

console.log("carrito.js %cImported", "color:#00FF00");

export { showCarrito, logShit };
