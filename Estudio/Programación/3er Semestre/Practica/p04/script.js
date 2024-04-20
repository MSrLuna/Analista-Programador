document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Evitar que el formulario se envíe

    // Obtener valores de los campos de entrada
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Verificar las credenciales (esto es solo un ejemplo básico)
    if (username === "usuario" && password === "contraseña") {
        // Redirigir al usuario a la página en blanco
        window.location.href = "pagina.html";
    } else {
        // Mostrar mensaje de error
        alert("Credenciales incorrectas.");
    }
});
