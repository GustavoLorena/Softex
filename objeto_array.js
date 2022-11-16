function Pessoa(Nome, idade, sexo) {
    this.nome = Nome
    this.idade = idade
    this.sexo = sexo
  }

var pessoa = new Pessoa("mMaria", 18, "F");

for (var prop in pessoa) {
    console.log("Pessoa." + prop + " = " + pessoa[prop]);
  }


const motos = ["Yamaha", "Honda", "Dafra", "Suzuki"]


for (const i of motos){
    console.log(i)
}
