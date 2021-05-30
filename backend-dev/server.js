const express = require('express')
const {router} = require('./config/router')

const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: true}))

const port = 8000;

app.use('/', router)

app.listen(port, () => {
  console.log(`Example app listening on port ${port}!`)
});

// import express from 'express';
// import {router} from './config/router';
// const app = express();
// const port = 8000;

// // app.get('/', (req, res) => {
// //   res.send('Hello World!')
// // });
// app.use('/', router)

// app.listen(port, () => {
//   console.log(`Example app listening on port ${port}!`)
// });