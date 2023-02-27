const express = require('express');
const app = express();

// Defina uma rota para o recurso "produto"
app.get('/produto', (req, res) => {
  const produto = {
    id: 1,
    nome: 'Notebook',
    preco: 4299.90
  };

  res.json(produto);
});

// Defina uma rota para o recurso "usuário"
app.get('/usuario', (req, res) => {
  const usuario = {
    id: 1,
    nome: 'Softex Recife',
    email: 'softex@email.com'
  };

  res.json(usuario);
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Web service rodando na porta ${port}`);
});
