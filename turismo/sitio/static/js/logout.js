function redirect_to_home() {
    $.ajax({url: '/'});
}

function on_load_logout() {
    setInterval(redirect_to_home, 2000);
}

$(on_load_logout)