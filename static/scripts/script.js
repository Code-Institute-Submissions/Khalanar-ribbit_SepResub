document.addEventListener('DOMContentLoaded', function() {
    var navbar = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(navbar);
    var select = document.querySelectorAll('select');
    var instances = M.FormSelect.init(select);
    var modal = document.querySelectorAll('.modal');
    var instances = M.Modal.init(modal);
});

setTimeout( () => {
    document.getElementById('message-container').innerHTML = "";
}, 3000 );
