const boton = document.getElementById('boton');
let posicion = window.scrollY;

function cambiarPosicion() {
  if (window.scrollY < posicion) {
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
  } else {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  posicion = window.scrollY;
}

boton.addEventListener('click', cambiarPosicion);



document.getElementById("toastbtn").onclick = function() {
  var toastElList = [].slice.call(document.querySelectorAll('.toast'))
  var toastList = toastElList.map(function(toastEl) {
    return new bootstrap.Toast(toastEl)
  })
  toastList.forEach(toast => toast.show())
}



function buscarPais() {
  var input = document.getElementById("pais-busqueda");
  var filtro = input.value.toLowerCase();
  var paises = document.querySelectorAll("#paiss");
  for (var i = 0; i < paises.length; i++) {
    var nombre = paises[i].innerHTML.toLowerCase();
    if (nombre.indexOf(filtro) > -1) {
      paises[i].style.display = "";
    } else {
      paises[i].style.display = "none";
    }
  }
}

  



  // Obtener los inputs del formulario
const emailInput = document.querySelector('input[name="email"]');
const dniInput = document.querySelector('input[name="dni"]');
const telefonoInput = document.querySelector('input[name="telefono"]');

// Expresiones regulares para validar el formato de cada campo
const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const dniRegex = /^[0-9]{7,8}$/;
const telefonoRegex = /^[0-9]{7,}$/;

// Función para validar el email
function validarEmail() {
  const email = emailInput.value.trim();
  if (!emailRegex.test(email)) {
    emailInput.setCustomValidity('Por favor, ingrese un correo electrónico válido');
  } else {
    emailInput.setCustomValidity('');
  }
}

// Función para validar el DNI
function validarDni() {
  const dni = dniInput.value.trim();
  if (!dniRegex.test(dni)) {
    dniInput.setCustomValidity('Por favor, ingrese un número de DNI válido');
  } else {
    dniInput.setCustomValidity('');
  }
}

// Función para validar el teléfono
function validarTelefono() {
  const telefono = telefonoInput.value.trim();
  if (!telefonoRegex.test(telefono)) {
    telefonoInput.setCustomValidity('Por favor, ingrese un número de teléfono válido');
  } else {
    telefonoInput.setCustomValidity('');
  }
}

// Añadir eventos a los inputs para validarlos cada vez que el usuario escribe algo en ellos
emailInput.addEventListener('input', validarEmail);
dniInput.addEventListener('input', validarDni);
telefonoInput.addEventListener('input', validarTelefono);

// Añadir un evento al formulario para enviarlo solo si todos los campos son válidos
document.querySelector('form.form-empresarial').addEventListener('submit', function(event) {
  if (!emailInput.checkValidity() || !dniInput.checkValidity() || !telefonoInput.checkValidity()) {
    event.preventDefault();
  }
});





function search() {
var input, filter, table, tr, td, i, j, txtValue;
input = document.getElementById("myInput");
filter = input.value.toUpperCase();
table = document.getElementsByTagName("table")[0];
tr = table.getElementsByTagName("tr");

for (i = 0; i < tr.length; i++) {
  for (j = 0; j < 4; j++) { // Cambiar 4 por el número de columnas de tu tabla
    td = tr[i].getElementsByTagName("td")[j];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
        break; // Si se encuentra la búsqueda en una celda, se muestra la fila completa y se pasa a la siguiente fila
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
}



function buscarCiudades() {
    var input = document.getElementById("ciudad-busqueda");
    var filtro = input.value.toLowerCase();
    var paises = document.querySelectorAll("#paisss");
    for (var i = 0; i < paises.length; i++) {
      var nombre = paises[i].innerHTML.toLowerCase();
      if (nombre.indexOf(filtro) > -1) {
        paises[i].style.display = "";
      } else {
        paises[i].style.display = "none";
      }
    }
}




function buscarCalles() {
    var input = document.getElementById("calles-busqueda");
    var filtro = input.value.toLowerCase();
    var paises = document.querySelectorAll("#paissss");
    for (var i = 0; i < paises.length; i++) {
      var nombre = paises[i].innerHTML.toLowerCase();
      if (nombre.indexOf(filtro) > -1) {
        paises[i].style.display = "";
      } else {
        paises[i].style.display = "none";
      }
    }
  }



