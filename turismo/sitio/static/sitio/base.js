function pedir_contadores() {
    $.ajax({url: '/contador_usuarios_ajax/'}).done(actualizar_contadores).error(error_actualizar_contadores);
}


function actualizar_contadores(data, options) {
    $('#cantidad-usuarios-online').text(data.cantidad_usuarios_online);
}


function error_actualizar_contadores() {

}


function al_cargar_base() {
    setInterval(pedir_contadores, 3000);
}


$(al_cargar_base)