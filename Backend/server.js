const pool = require('./db');
const express = require('express');
require('nodemon');
const app =  express();








app.get("/students" ,async (req,res)=> {
   console.log('server alive')
   const {rows}  = await pool.query('SELECT * FROM public.students;');
   res.json(rows);
});




app.listen(3000 , ()=> {
  console.log(' server is runing on http://localhost:3000')
})