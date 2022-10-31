//  Função tradicional sem nenhum parâmetro;
function cuidado() {
  console.log('Cuidado!')
}
cuidado()

//  Função tradicional com parâmetros e retorno;
function ola(nome) {
  console.log('Olá', nome)
}
ola('Gustavo')

//  Arrow function;
const outro_ola = (nome) => {
  return console.log('Olá', nome)
}
outro_ola('Gustavo!')
