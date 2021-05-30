import {Sequelize, DataTypes, Model} from 'sequelize'

const connection = new Sequelize({
    dialect: 'mysql',
    host: '127.0.0.1',
    port: 3306,
    username: 'root',
    password: 'password',
    database: 'project'
})

export {connection}