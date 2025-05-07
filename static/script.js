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


const button = document.getElementById('hi');

button.addEventListener('click', function() {
    const parent1Input = document.getElementById('parent1-mono').value;
    const parent2Input = document.getElementById('parent2-mono').value;
    console.log('Parent 1 Input:', parent1Input);
});

