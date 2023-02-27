const database = require('../database');

class CRUDController {
  async create(req, res) {
    const { name, email, age } = req.body;
    const query = `INSERT INTO users (name, email, age) VALUES ('${name}', '${email}', ${age})`;

    try {
      const result = await database.query(query);
      res.status(201).send({ message: 'User created successfully' });
    } catch (error) {
      res.status(500).send({ message: error.message });
    }
  }

  async read(req, res) {
    const query = 'SELECT * FROM users';

    try {
      const result = await database.query(query);
      res.status(200).send(result);
    } catch (error) {
      res.status(500).send({ message: error.message });
    }
  }

  async update(req, res) {
    const { id } = req.params;
    const { name, email, age } = req.body;
    const query = `UPDATE users SET name = '${name}', email = '${email}', age = ${age} WHERE id = ${id}`;

    try {
      const result = await database.query(query);
      res.status(200).send({ message: 'User updated successfully' });
    } catch (error) {
      res.status(500).send({ message: error.message });
    }
  }

  async delete(req, res) {
    const { id } = req.params;
    const query = `DELETE FROM users WHERE id = ${id}`;

    try {
      const result = await database.query(query);
      res.status(200).send({ message: 'User deleted successfully' });
    } catch (error) {
      res.status(500).send({ message: error.message });
    }
  }
}

module.exports = new CRUDController();
