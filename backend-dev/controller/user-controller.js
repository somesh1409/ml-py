const express = require('express');
const router = express.Router();
const {connection} = require('../config/database');
const Sequelize = require('sequelize');

const User = require('../models/users')(connection, Sequelize.DataTypes);

router.get('/', async (req, res) => {
    users = await User.findAll();
    console.log(users);
    // res.send('Users Home Page');
})

router.post('/create', async (req, res) => {
    console.log(req.body);
    const user = await User.create(req.body);
    res.send(`User Created! User Details: ${user}`)
})

exports.UserController = router