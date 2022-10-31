var cliente = {
    nome: Gustavo,
    login: GustavoLorena,
    senha: 123456,
    conta: 13579,
    saldo: 1312.00
}

var saque = function (saque) {
    cliente.saque = cliente.saldo - saque;
}

var deposito = function (valor) {
    cliente.saldo = cliente.saldo + valor;
}

var extrato = function () {
    console.log('O saldo é: ' + cliente.saldo)
}

var dadosCliente = function () {
    console.log('Nome: ' + cliente.nome);
    console.log('Login: ' + cliente.login);
    console.log('Senha: ' + cliente.senha);
    console.log('Conta: ' + cliente.conta);
    console.log('Saldo: ' + cliente.saldo);
}

//  Consultar o cliente
consultar_cliente();
//  Despósito e depois consulta do extrato
deposito(100);
extrato();
//  Saque
saque(50);
