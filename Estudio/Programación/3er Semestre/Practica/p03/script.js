document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Evitar que se envíe el formulario

    // Aquí deberías agregar la lógica para verificar las credenciales del usuario
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Ejemplo de redirección si las credenciales son válidas
    if (username === "usuario" && password === "contraseña") {
        window.location.href = "dashboard.html";
    } else {
        alert("Usuario o contraseña incorrectos");
    }
});
