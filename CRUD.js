const express = require('express');
const app = express();
const books = [];

app.use(express.json());

app.post('/books', (req, res) => {
  const book = req.body;
  books.push(book);
  res.status(201).send(book);
});

app.get('/books/:id', (req, res) => {
  const id = req.params.id;
  const book = books[id];
  if (!book) {
    return res.status(404).send('Livro não encontrado');
  }
  res.send(book);
});

app.put('/books/:id', (req, res) => {
  const id = req.params.id;
  const book = books[id];
  if (!book) {
    return res.status(404).send('Livro não encontrado');
  }
  books[id] = req.body;
  res.send(book);
});

app.delete('/books/:id', (req, res) => {
  const id = req.params.id;
  const book = books[id];
  if (!book) {
    return res.status(404).send('Livro não encontrado');
  }
  books.splice(id, 1);
  res.send(book);
});
