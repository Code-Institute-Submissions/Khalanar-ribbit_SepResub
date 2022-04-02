document.addEventListener('DOMContentLoaded', function() {
    var navbar = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(navbar);
    var select = document.querySelectorAll('select');
    var instances = M.FormSelect.init(select);
});

setTimeout( () => {
    document.getElementById('message-container').innerHTML = "";
}, 3000 )

