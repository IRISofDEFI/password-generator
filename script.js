const lowercaseLetters = "abcdefghijklmnopqrstuvwxyz";
const uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numbers = "0123456789";
const symbols = "!@#$%^&*()_+-=[]{}\\|;':\",./?<>~`";

const lengthEl = document.getElementById("length");

const lowercaseEl = document.getElementById("lowercase");

const uppercaseEl = document.getElementById("uppercase");

const numbersEl = document.getElementById("numbers");

const symbolsEl = document.getElementById("symbols");

const generateBtn = document.getElementById("generate");

const passwordEl = document.getElementById("password");

generateBtn.addEventListener("click", function () {

    const length = lengthEl.value;
    let characters = "";
    let password = "";

    if (lowercaseEl.checked) {
        characters += lowercaseLetters;
    }

    if (uppercaseEl.checked) {
        characters += uppercaseLetters;
    }

    if (numbersEl.checked) {
        characters += numbers;
    }

    if (symbolsEl.checked) {
        characters += symbols;
    }

    if (characters === "") {
        alert("Please select at least one character type!");
        return;
    }

    for (i = 0; i < length; i++) {
        password += characters.charAt(Math.floor(Math.random() * characters.length))

    }
    passwordEl.value = password;

});


const copyBtn = document.getElementById("copy");

copyBtn.addEventListener("click", function () {
    const password = passwordEl.value;

    if (!password) {
        alert("No password to copy!");
        return;
    }

    // Copy to clipboard
    navigator.clipboard.writeText(password).then(() => {
        alert("Password copied to clipboard! ✅");
    }).catch(err => {
        console.error("Failed to copy: ", err);
    });
});
