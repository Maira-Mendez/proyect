// script.js

// Función para mostrar el formulario de registro
function showRegister() {
    document.getElementById("login-form").classList.add("hidden");
    document.getElementById("register-form").classList.remove("hidden");
}

// Función para mostrar el formulario de login
function showLogin() {
    document.getElementById("register-form").classList.add("hidden");
    document.getElementById("login-form").classList.remove("hidden");
}

// Función para registrar un nuevo usuario
function register() {
    const username = document.getElementById("register-username").value;
    const password = document.getElementById("register-password").value;

    if (username && password) {
        // Guardar usuario en localStorage (inseguro para producción)
        localStorage.setItem(username, password);
        alert("Registro exitoso. Ahora puedes iniciar sesión.");
        showLogin();
    } else {
        alert("Por favor, ingresa todos los campos.");
    }
}

// Función para iniciar sesión
function login() {
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;

    // Verificar el usuario y la contraseña almacenada
    const storedPassword = localStorage.getItem(username);

    if (storedPassword === password) {
        alert("Inicio de sesión exitoso.");
        window.location.href= "file:///C:/Users/MAIRA%20MENDEZ/Desktop/cinematch/Cine%20Match.html#"
        // Aquí podrías redirigir a otra página o mostrar contenido restringido
        
    } else {
        alert("Nombre de usuario o contraseña incorrecta.");
    }
}