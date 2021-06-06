const express = require('express')

const router = express.Router();
const user_controller = require('../controller/user-controller')

const {connection} = require('./database');

// import {User} from '../models/user';

router.get('/', (req, res) => {
    res.send('Hello World!')
});

// User Routes

router.get('/user/all', user_controller.users_all_get);
router.get('/user/:i', user_controller.users_id_get);
router.post('/user/create', user_controller.users_create_post);
router.post('/user/edit/:i', user_controller.users_update_post);

// Testing Routes

router.get('/test', async (req, res) => {
    // res.send('Testing 1.. 2.. 3...')
    try {
        // await User.sync({alter: true});
        await connection.authenticate();
        console.log('Connection has been established successfully.');
        res.send('Connection has been established successfully.')
      } catch (error) {
        console.error('Unable to connect to the database:', error);
      }
});

router.get('/login', (req,res) => {
    res.send('Login Page')
});

exports.router = router