const randomNumber = Math.floor(Math.random() * 10) + 1;
let tries = 3;

function checkGuess() {
    const guess = parseInt(document.getElementById('guess').value);

    if (guess === randomNumber) {
        document.getElementById('message').innerHTML = '¡Correcto! Has adivinado el número.';
    } else {
        tries--;
        if (tries === 0) {
            document.getElementById('message').innerHTML = '¡Perdiste! El número era ' + randomNumber + '.';
            document.getElementById('guess').disabled = true;
        } else {
            document.getElementById('message').innerHTML = 'Incorrecto. Te quedan ' + tries + ' intentos.';
        }
    }
}
