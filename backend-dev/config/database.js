const { Sequelize, DataTypes, Model } = require('sequelize');

// const connection = new Sequelize({
//     dialect: 'mysql',
//     host: '127.0.0.1',
//     port: 3306,
//     username: 'root',
//     password: 'password',
//     database: 'database_development'
// })

const env = process.env.NODE_ENV || 'development';
const config = require('./config.json')[env];

let sequelize;
if (config.use_env_variable) {
  sequelize = new Sequelize(process.env[config.use_env_variable], config);
} else {
  sequelize = new Sequelize(config.database, config.username, config.password, config);
}

exports.connection = sequelize