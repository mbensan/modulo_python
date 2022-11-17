// tags HTML
const input_num = document.querySelector('#num');

const nombre = document.querySelector('#nombre');
const peso = document.querySelector('#peso');
const altura = document.querySelector('#altura');

const planet = document.querySelector('#planet');
const orbital = document.querySelector('#orbital');
const rotation = document.querySelector('#rotation');


async function buscar () {
  // 1. Obtener el id del personaje
  const id = input_num.value;

  // 2. Voy a buscar los datos del personaje
  let persona = await fetch('https://swapi.py4e.com/api/people/' + id)

  // 3. Desempaqueto la información
  persona = await persona.json()
  
  // Una vez que llegué acá, puedo usar la información
  //  4. Finalmente completamos el DOM
  nombre.innerHTML = persona['name'];
  peso.innerHTML = persona.mass;
  altura.innerHTML = persona.height / 100;
  
  // 5. Vamos a buscar los datos del planeta
  let planeta = await fetch(persona.homeworld)
  
  // 6. Desempaqueto la información
  planeta = await planeta.json()
  console.log(planeta);

  // 7. Completamos el DOM con los datos del planeta
  planet.innerHTML = planeta.name;
  rotation.innerHTML = planeta.rotation_period
  orbital.innerHTML = planeta.orbital_period
}


$('#home').on('click', function (e) {
  e.preventDefault();

  $('.card').slideToggle(1500)
})
