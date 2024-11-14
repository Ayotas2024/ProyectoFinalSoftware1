// Referencias del HTML
const pomodoroBtn = document.getElementById('pomodoro-btn');
const descansoCortoBtn = document.getElementById('descanso-corto-btn');
const descansoLargoBtn = document.getElementById('descanso-largo-btn');
const iniciarBtn = document.querySelector('.iniciar-button');
const timeDisplay = document.querySelector('.time-display');
const nuevaTareaInput = document.getElementById('nuevaTarea');
const tareasLista = document.getElementById('tareasLista');
const añadirTarea = document.querySelector('.añadir-tarea-button'); 

let timerInterval;
let currentTimerDuration = 25 * 60; 
let isTimerRunning = false;

// Función para actualizar la pantalla del temporizador
function updateTimerDisplay() {
  const minutes = Math.floor(currentTimerDuration / 60);
  const seconds = currentTimerDuration % 60;
  timeDisplay.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

// Función para iniciar/pausar el temporizador
function toggleTimer() {
  if (isTimerRunning) {
    clearInterval(timerInterval);
    iniciarBtn.textContent = 'Iniciar';
  } else {
    timerInterval = setInterval(() => {
      currentTimerDuration--;
      updateTimerDisplay();
      if (currentTimerDuration <= 0) {
        clearInterval(timerInterval);
        iniciarBtn.textContent = 'Iniciar';
        isTimerRunning = false;
        alert('Tiempo terminado')
      }
    }, 1000);
    iniciarBtn.textContent = 'Pausar';
  }
  isTimerRunning = !isTimerRunning;
}

// Botones de navegación
pomodoroBtn.addEventListener('click', () => {
  currentTimerDuration = 25 * 60;
  updateTimerDisplay();
});

descansoCortoBtn.addEventListener('click', () => {
  currentTimerDuration = 5 * 60;
  updateTimerDisplay();
});

descansoLargoBtn.addEventListener('click', () => {
  currentTimerDuration = 15 * 60;
  updateTimerDisplay();
});

// Botón iniciar/pausar
iniciarBtn.addEventListener('click', toggleTimer);

// Agregar una tarea
añadirTarea.addEventListener('click', () => {
  const taskText = nuevaTareaInput.value.trim();
  if (taskText) {
    const nuevaTarea = document.createElement('li');
    nuevaTarea.textContent = taskText;

    // Botón de eliminar
    const borrarBtn = document.createElement('img');
    borrarBtn.src= "{% static 'img/basura.png' %}";
    borrarBtn.alt= 'Eliminar';
    borrarBtn.classList.add('btn-eliminar');

    borrarBtn.addEventListener('click', () => {
      tareasLista.removeChild(nuevaTarea);
    });

    nuevaTarea.appendChild(borrarBtn);
    tareasLista.appendChild(nuevaTarea);
    nuevaTareaInput.value = '';
  }
});


//Menú
const menuButton = document.querySelector('.menu-button');
const menuNav = document.getElementById('menu');

menuButton.addEventListener('click', () => {
  menuNav.classList.toggle('active');
});