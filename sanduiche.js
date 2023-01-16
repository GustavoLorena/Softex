class Sanduíche {
    constructor() {        
      this.cost = 0;
    }
  }

  const addPepperon = function(sanduíche) {
    const cost = sanduíche.cost + 0.99;
    return {...sanduíche, hasPeperoni: true, cost};
  };

  const addFrangoAssado = function(sanduíche) {
    const cost = sanduíche.cost + 4.5;
    return {...sanduíche, hasFrango: true, cost};
  };

  const addQueijoMussarelaRalado = function(sanduíche) {
    const cost = sanduíche.cost + 2;
    return {...sanduíche, hasQueijo: true, cost};
  };

const completo = new Sanduíche();
const pepperon = addPepperon(completo);
const frango = addFrangoAssado(completo);
const queijo = addQueijoMussarelaRalado(completo);
const total = pepperon.cost + frango.cost + queijo.cost
console.log("O Sanduíche de Frango, Pepperoni, Queijo Mussarela Ralado custa:", total )
