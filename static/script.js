const fondos = [
    "static/img/fondo1.jpg",
    "static/img/fondo2.jpg",
    "static/img/fondo3.jpg",
    "static/img/fondo4.jpg",
    "static/img/fondo5.jpg",
    "static/img/fondo6.jpg",
    "static/img/fondo7.jpg",
    "static/img/fondo8.jpg",
    "static/img/fondo9.jpg",
    "static/img/fondo10.jpg",
    "static/img/fondo11.jpg",
    "static/img/fondo12.jpg",
    "static/img/fondo13.jpg",
    "static/img/fondo14.jpg",
    "static/img/fondo1.jpg",
    "static/img/fondo2.jpg"
];

let i = 0;
setInterval(() => {
    document.body.style.backgroundImage = `url(${fondos[i]})`;
    i = (i + 1) % fondos.length;
}, 5000); // cambia cada 5 segundos
