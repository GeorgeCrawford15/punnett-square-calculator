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
