import {Sequelize, DataTypes, Model} from 'sequelize'
import {connection} from '../config/database'

const User = connection.define("User", {
    fname: {
        type: new DataTypes.STRING(128),
        allowNull: false
    },
    lname: {
        type: new DataTypes.STRING(128),
    },
    email: {
        type: new DataTypes.STRING(128),
        allowNull: false
    },
    phone: {
        type: new DataTypes.STRING(128),
        allowNull: false
    }
},
{
    tableName: 'users'
})

export {User};