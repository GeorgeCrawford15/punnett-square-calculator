const monoSection = document.querySelector('.mono-cross');
const diSection = document.querySelector('.di-cross');

function toggleDiCross() {
    monoSection.style.display = 'none';
    diSection.style.display = 'block';
}

function toggleMonoCross() {
    diSection.style.display = 'none';
    monoSection.style.display = 'block';
}


const button = document.getElementById('calculate');

const parent1GenoDescription = document.querySelector('.parent1-geno');
const parent2GenoDescription = document.querySelector('.parent2-geno');

const parent1Gamete1 = document.getElementById('parent1-gamete1');
const parent1Gamete2 = document.getElementById('parent1-gamete2');
const parent2Gamete1 = document.getElementById('parent2-gamete1');
const parent2Gamete2 = document.getElementById('parent2-gamete2');

const offspring1Mono = document.getElementById('offspring1-mono');
const offspring2Mono = document.getElementById('offspring2-mono');
const offspring3Mono = document.getElementById('offspring3-mono');
const offspring4Mono = document.getElementById('offspring4-mono');

button.addEventListener('click', function() {
    const parent1Input = document.getElementById('parent1-mono').value;
    const parent2Input = document.getElementById('parent2-mono').value;

    parent1Gamete1.innerText = parent1Input.charAt(0);
    parent1Gamete2.innerText = parent1Input.charAt(1);
    parent2Gamete1.innerText = parent2Input.charAt(0);
    parent2Gamete2.innerText = parent2Input.charAt(1);

    document.querySelector('caption').style.visibility = 'visible';
    parent1GenoDescription.innerText = parent1Input;
    parent2GenoDescription.innerText = parent2Input;

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            parent1: parent1Input,
            parent2: parent2Input
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Response from server:', data);

        offspring1Mono.innerText = data.offspring1;
        offspring2Mono.innerText = data.offspring2;
        offspring3Mono.innerText = data.offspring3;
        offspring4Mono.innerText = data.offspring4;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

/*
These parameters are determined by the fetch API's promise chain:
The first .then() receives the Response object from the fetch promise.
The second .then() receives the result of the response.json() promise.
The .catch() block receives any error that occurs during the fetch request or subsequent promise resolution.
*/
