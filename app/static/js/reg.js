
// Register Validation
const fullName = document.getElementById('fullName');
let email = document.getElementById('email');
let password = document.getElementById('password');
let confirmPassword = document.getElementById('confirmPassword');
    
// REAL TIME VALIDATION
fullName.addEventListener('input', () => { checkName(fullName); });
email.addEventListener('input', () => { checkEmail(email); });
password.addEventListener('input', () => { checkPassword(password); });
confirmPassword.addEventListener('input', () => { checkConfirmPassword(confirmPassword); });

function setErrorFor(input, message) {
    const formControl = input.parentElement;
    const span = formControl.querySelector('span');
    const inputField = formControl.querySelector('input');


    // Change from hidden to visible and set the message
    inputField.style.border = '1px solid red';
    span.style.display = 'flex';
    span.innerText = message;    
}

function setSuccessFor(input) {
    const formControl = input.parentElement;
    const span = formControl.querySelector('span');
    const inputField = formControl.querySelector('input');

    // Change from visible to hidden
    inputField.style.border = '1px solid green';
    span.style.display = 'none';
}


function isEmail(emailValue) {
    return /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(emailValue);
}

function checkName(name) {
    let nameValue = name.value.trim();

    if(nameValue === '') {
        setErrorFor(name, 'Name cannot be blank');
    } else if (nameValue.length < 3) {
        setErrorFor(name, 'Name must be at least 3 characters');
    } else {
        setSuccessFor(name);
    }
}

function checkEmail(email) {
    let emailValue = email.value.trim();

    if(emailValue === '') {
        setErrorFor(email, 'Email cannot be blank');
    } else if(!isEmail(emailValue)) {
        setErrorFor(email, 'Email is not valid');
    } else {
        setSuccessFor(email);
    }
}

function checkPassword(password) {
    let passwordValue = password.value.trim();

    if(passwordValue === '') {
        setErrorFor(password, 'Password cannot be blank');
    } else if (passwordValue.length < 8) {
        setErrorFor(password, 'Password must be at least 8 characters');
    } else if (passwordValue.search(/[a-z]/) < 0) {
        setErrorFor(password, 'Password must contain at least one lowercase letter');
    } else if (passwordValue.search(/[A-Z]/) < 0) { 
        setErrorFor(password, 'Password must contain at least one uppercase letter');
    } else if (passwordValue.search(/[0-9]/) < 0) {
        setErrorFor(password, 'Password must contain at least one digit');
    } else if (passwordValue.search(/[!@#$%^&*/';.,\/]/) < 0) {
        setErrorFor(password, 'Password must contain at least one special character');
    } else {
        setSuccessFor(password);
    }
}

function checkConfirmPassword(confirmPassword) {
    let confirmPasswordValue = confirmPassword.value.trim();

    if(confirmPasswordValue === '') {
        setErrorFor(confirmPassword, 'Confirm Password cannot be blank');
    } else if(password.value !== confirmPasswordValue) {
        setErrorFor(confirmPassword, 'Passwords does not match');
    } else {
        setSuccessFor(confirmPassword);
    }
}
