const {connection} = require('../config/database');
const Sequelize = require('sequelize');

// const User = require('../models')(connection, Sequelize.DataTypes);
const Users = require('../models').Users;
// console.log(User.Users);

// router.get('/', async (req, res) => {
//     users = await User.findAll();
//     console.log(users);
//     // res.send('Users Home Page');
// })

exports.users_all_get = async(req, res) => {
    users = await Users.findAll();
    res.send(users);
}

exports.users_id_get = async(req, res) => {
    user = await Users.findOne({
        where: {
            id: req.params.i
        }
    })
    // console.log(user.length)
    if (user.length == 0){
        res.send("User Not Found")
    }
    res.send(user);
}

exports.users_create_post = async(req, res) => {
    const user = await Users.create(req.body);
    res.send(user.dataValues);
    // res.json(`User Created! User Details: ${user.dataValues}`)
}

exports.users_update_post = async(req,res) => {
    const user = await Users.update(req.body, {
        where: {
            id: req.params.i
        }
    })
    user_details = await Users.findOne({
        where: {
            id: req.params.i
        }
    })
    res.send(user_details);
}

// router.post('/create', async (req, res) => {
//     console.log(req.body);
//     const user = await User.create(req.body);
//     res.send(`User Created! User Details: ${user}`)
// })