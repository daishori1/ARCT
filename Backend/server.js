const pool = require('./db');
const express = require('express');
require('nodemon');
const app =  express();








app.get("/students" ,async (req,res)=> {
   try {
    const {rows}  = await pool.query('SELECT * FROM public.students;');
    
    if (rows.length === 0){
      res.status(400).send({error:"no data in the treaht"});
      return 
    }
    res.status(200).json(rows); 
  }catch(error){
     res.status(500).send({error:"internal server error"});
  }
     
});




app.listen(3000 , ()=> {
  console.log(' server is runing on http://localhost:3000')
})