require('dotenv').config('ARCT/.env');
const {Pool} = require('pg');

const pool = new Pool({
  user : process.env.PGUSER,
  port : Number(process.env.PGPORT || 14152) ,
  host : process.env.PGHOST,
  database : process.env.PGDBNAME,
  password : process.env.PGPASSWORD, 

  ssl : {
    rejectUnauthorized : false ,  
  }
});





