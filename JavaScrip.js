document.getElementById("btn__iniciar-sesion").addEventListener("click", iniciarSesion);
document.getElementById("btn__registrarse").addEventListener("click", register);
window.addEventListener("resize", anchoPage);


var contenedor_login_register = document.querySelector(".contenedor__login-register");
var caja_trasera_login = document.querySelector(".caja__trasera-login");
var caja_trasera_register = document.querySelector(".caja__trasera-register");
var formulario_login = document.querySelector(".formulario__login");
var formulario_register = document.querySelector(".formulario__register");


  

function anchoPage(){

        caja_trasera_register.style.display = "block";
        caja_trasera_login.style.display = "block";
}

anchoPage();


    function iniciarSesion(){

            contenedor_login_register.style.left = "10px";
            formulario_register.style.display = "none";
            caja_trasera_register.style.opacity = "1";
			formulario_login.style.display = "block";
            caja_trasera_login.style.opacity = "0";
    }

    function register(){
			caja_trasera_register.style.opacity = "0";
            caja_trasera_login.style.opacity = "1";
            formulario_register.style.display = "block";
            contenedor_login_register.style.left = "410px";
            formulario_login.style.display = "none";
            
    }