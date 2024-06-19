$(document).ready(function () {
    $('#form-contact').submit(function (event) {
        event.preventDefault();
        
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
            $('.msg-valid-nom').css({color: 'red'});
            $('.msg-valid-nom').text('El nombre no puede ir vacío.');
            isValid = false;
        }

        if (email === "") {
            $('.msg-valid-em').css({color: 'red'});
            $('.msg-valid-em').text('El correo electrónico no puede estar vacío');
            isValid = false;
        } else if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email)) {
            $('.msg-valid-em').css({color: 'red'});
            $('.msg-valid-em').text('El correo electrónico no es válido');
            isValid = false;
        }

        if (celular === "") {
            $('.msg-valid-cel').css({color: 'red'});
            $('.msg-valid-cel').text('El número de celular está vacío.');
            isValid = false;
        } else if (!/^[9]\d{8}$/.test(celular)) {
            $('.msg-valid-cel').css({color: 'red'});
            $('.msg-valid-cel').text('El número de celular no es válido.');
            isValid = false;
        }

        if (mensaje === "") {
            $('.msg-valid-msg').css({color: 'red'});
            $('.msg-valid-msg').text('El mensaje está vacío.');
            isValid = false;
        } else {
            let words = mensaje.match(/\S+/g).length;
            if (words < 10) {
                $('.msg-valid-msg').css({color: 'red'});
                $('.msg-valid-msg').text('El mensaje debe tener al menos 10 palabras.');
                isValid = false;
            }
        }

        if (isValid) {
            alert('Formulario válido. Procesando...');
            this.submit();
        }
    });
});