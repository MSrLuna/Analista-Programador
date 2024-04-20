// Obtenemos una referencia al encabezado
const header = document.querySelector('header');

// Función para cambiar el color de fondo del encabezado
function changeHeaderColor() {
    // Generamos un color aleatorio en formato hexadecimal
    const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    
    // Aplicamos el color aleatorio al fondo del encabezado
    header.style.backgroundColor = randomColor;
}

// Agregamos un evento de clic al encabezado que llamará a la función para cambiar el color de fondo
header.addEventListener('click', changeHeaderColor);
