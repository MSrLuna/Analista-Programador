document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Evitar el envío del formulario

    // Obtener los valores de usuario y contraseña
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Verificar si el usuario y la contraseña son válidos
    if (username === "Franco" && password === "esbello") {
        // Si son válidos, redireccionar a la página deseada
        window.location.href = "pagina.html";
    } else {
        // Si no son válidos, mostrar un mensaje de error
        alert("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.");
    }
});
