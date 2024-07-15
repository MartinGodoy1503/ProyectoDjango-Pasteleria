$(document).ready(function () {
    $('#form-contact').submit(function (event) {
        event.preventDefault();
        
        // Clear previous validation messages
        $('.msg-valid-nom').text('');
        $('.msg-valid-em').text('');
        $('.msg-valid-cel').text('');
        $('.msg-valid-msg').text('');

        let nombre = $('#id_nombre').val();
        let email = $('#id_email').val();
        let celular = $('#id_celular').val();
        let mensaje = $('#id_mensaje').val();

        let isValid = true;

        if (nombre === "") {
            $('.msg-valid-nom').css({color: 'red'}).text('El nombre no puede ir vacío.').insertAfter('#id_nombre');
            isValid = false;
        }

        if (email === "") {
            $('.msg-valid-em').css({color: 'red'}).text('El correo electrónico no puede estar vacío').insertAfter('#id_email');
            isValid = false;
        } else if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email)) {
            $('.msg-valid-em').css({color: 'red'}).text('El correo electrónico no es válido').insertAfter('#id_email');
            isValid = false;
        }

        if (celular === "") {
            $('.msg-valid-cel').css({color: 'red'}).text('El número de celular está vacío.').insertAfter('#id_celular');
            isValid = false;
        } else if (!/^[9]\d{8}$/.test(celular)) {
            $('.msg-valid-cel').css({color: 'red'}).text('El número de celular no es válido.').insertAfter('#id_celular');
            isValid = false;
        }

        if (mensaje === "") {
            $('.msg-valid-msg').css({color: 'red'}).text('El mensaje está vacío.').insertAfter('#id_mensaje');
            isValid = false;
        } else {
            let words = mensaje.match(/\S+/g).length;
            if (words < 10) {
                $('.msg-valid-msg').css({color: 'red'}).text('El mensaje debe tener al menos 10 palabras.').insertAfter('#id_mensaje');
                isValid = false;
            }
        }

        if (isValid) {
            alert('Formulario válido. Procesando...');
            this.submit();
        }
    });
});
