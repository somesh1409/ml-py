import * as express from "express";

const router = express.Router();
import {connection} from './database';
import {User} from '../models/user';

router.get('/', (req, res) => {
    res.send('Hello World!')
});

router.get('/test', async (req, res) => {
    // res.send('Testing 1.. 2.. 3...')
    try {
        await User.sync({alter: true});
        console.log('Connection has been established successfully.');
        res.send('Connection has been established successfully.')
      } catch (error) {
        console.error('Unable to connect to the database:', error);
      }
});

router.get('/login', (req,res) => {
    res.send('Login Page')
});

export {router};