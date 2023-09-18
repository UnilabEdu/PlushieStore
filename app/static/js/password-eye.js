var password = document.getElementById('passcode');
var password2 = document.getElementById('passcode2');
var toggler = document.getElementById('toggler');
var toggler2 = document.getElementById('toggler2');
showHidePassword = () => {
    if (password.type == 'password') {
        password.setAttribute('type', 'text');
        toggler.classList.add('fa-eye-slash');
        password2.setAttribute('type', 'text');
        toggler2.classList.add('fa-eye-slash');
    } else {
        toggler.classList.remove('fa-eye-slash');
        password.setAttribute('type', 'password');
        toggler2.classList.remove('fa-eye-slash');
        password2.setAttribute('type', 'password');
    }
};
toggler.addEventListener('click', showHidePassword);
toggler2.addEventListener('click', showHidePassword);
