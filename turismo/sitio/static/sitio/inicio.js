function click_actualizar_usuarios() {
    $.ajax({url: '/lista_usuarios_ajax/'}).done(actualizar_usuarios).error(error_actualizar_usuarios);
}


function actualizar_usuarios(data, options) {
    $('#lista-usuarios').html(data);
}


function error_actualizar_usuarios() {
    $('#lista-usuarios').html('Error al cargar las usuarios');
}


function al_cargar_inicio() {
    $('#actualizar-usuarios').on('click', click_actualizar_usuarios);    
}


$(al_cargar_inicio)