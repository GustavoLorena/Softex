const express = require('express');
const app = express();
const students = [];

app.use(express.json());

// Cria um novo aluno
app.post('/students', (req, res) => {
  const student = req.body;
  students.push(student);
  res.status(201).send(student);
});

// Obtém uma lista de todos os alunos
app.get('/students', (req, res) => {
  res.send(students);
});

// Obtém um aluno específico pelo ID
app.get('/students/:id', (req, res) => {
  const id = req.params.id;
  const student = students[id];
  if (!student) {
    return res.status(404).send('Aluno não encontrado');
  }
  res.send(student);
});

// Atualiza um aluno específico pelo ID
app.put('/students/:id', (req, res) => {
  const id = req.params.id;
  const student = students[id];
  if (!student) {
    return res.status(404).send('Aluno não encontrado');
  }
  students[id] = req.body;
  res.send(student);
});

// Exclui um aluno específico pelo ID
app.delete('/students/:id', (req, res) => {
  const id = req.params.id;
  const student = students[id];
  if (!student) {
    return res.status(404).send('Aluno não encontrado');
  }
  students.splice(id, 1);
  res.send(student);
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Servidor iniciado na porta ${port}`);
});
