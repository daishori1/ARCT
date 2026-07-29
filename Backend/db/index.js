const {Pool} = require('pg');
require('dotenv').config();

const pool = new Pool({
    host : process.env.PGHOST,
    user : process.env.PGUSER,
    password : process.env.PGPASSWORD,
    port : Number(process.env.PGPORT || 14152),
    database : process.env.PGDATABASE,
    
    ssl : {
    rejectUnauthorized : false,
        
    }
});

module.exports = pool;