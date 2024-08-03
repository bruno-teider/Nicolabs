// TOGGLE NAV BAR ----------------------------------------------------------------------------------------------------------
const navHeader = document.querySelector('.sideBar');
const navLogo = document.querySelector('.sideBar--logo');
const navLogoIcon = document.querySelector('.sideBar--logoIcon');
const navToggleIconCircle = document.querySelector('.sideBar--toggleIcon');
const navToggleIcon = document.querySelector('.sideBar--toggleIcon .material-icons');

navToggleIconCircle.addEventListener('click', () => {
    navHeader.classList.toggle('sideBar--collapsed');
    navToggleIconCircle.title = (navToggleIconCircle.title === 'Expandir menu') ?'Recolher menu' :'Expandir menu';
    navToggleIcon.textContent = (navToggleIcon.textContent === 'chevron_left') ?'chevron_right' :'chevron_left';
});
navLogo.addEventListener('click', () => {
  navHeader.classList.toggle('sideBar--collapsed');
});
navLogoIcon.addEventListener('click', () => {
  navHeader.classList.toggle('sideBar--collapsed');
});

// TOGGLE POPUP ADD USUARIO ----------------------------------------------------------------------------------------------------------
const popupAddUser = document.getElementById('modal--addUsuario');

function open_popupAddUser(){
  popupAddUser.showModal();
}
function closeModal_popupAddUser(){
  popupAddUser.close();
}

// TOGGLE POPUP EDITAR USUARIO ----------------------------------------------------------------------------------------------------------
const popupEditarUser = document.getElementById('modal--editarUsuario');
function open_popupEditarUser(id, email, nome, senha, admin, operador) {
  popupEditarUser.showModal();
  document.getElementById("idEditarUser").value = id;
  document.getElementById("emailEditarUser").value = email;
  document.getElementById("nomeEditarUser").value = nome;
  document.getElementById("senhaEditarUser").value = senha;
  document.getElementById("adminEditarUser").value = admin;
  document.getElementById("operadorEditarUser").value = operador;
}
function closeModal_popupEditarUser(){
  popupEditarUser.close();
}

// TOGGLE POPUP ADD SENSOR ----------------------------------------------------------------------------------------------------------
const popupAddSensor = document.getElementById('modal--addSensor');

function open_popupAddSensor(){
  popupAddSensor.showModal();
}
function closeModal_popupAddSensor(){
  popupAddSensor.close();
}

// TOGGLE POPUP EDITAR SENSOR ----------------------------------------------------------------------------------------------------------
const popupEditarSensor = document.getElementById('modal--editarSensor');
function open_popupEditarSensor(id, nome, medicao, ativo) {
  popupEditarSensor.showModal();
  document.getElementById("idEditarSensor").value = id;
  document.getElementById("nomeEditarSensor").value = nome;
  document.getElementById("medicaoEditarSensor").value = medicao;
  document.getElementById("ativoEditarSensor").value = ativo;
}
function closeModal_popupEditarSensor(){
  popupEditarSensor.close();
}

// TOGGLE POPUP ADD ATUADOR ----------------------------------------------------------------------------------------------------------
const popupAddAtuador = document.getElementById('modal--addAtuador');

function open_popupAddAtuador(){
  popupAddAtuador.showModal();
}
function closeModal_popupAddAtuador(){
  popupAddAtuador.close();
}

// TOGGLE POPUP EDITAR ATUADOR ----------------------------------------------------------------------------------------------------------
const popupEditarAtuador = document.getElementById('modal--editarAtuador');
function open_popupEditarAtuador(id, nome, ativo) {
  popupEditarAtuador.showModal();
  document.getElementById("idEditarAtuador").value = id;
  document.getElementById("nomeEditarAtuador").value = nome;
  document.getElementById("ativoEditarAtuador").value = ativo;
}
function closeModal_popupEditarAtuador(){
  popupEditarAtuador.close();
}

