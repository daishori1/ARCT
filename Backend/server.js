const express = require('express').config(); 
require('nodemon').config();
const app =  express();


app.listen(3000 , ()=> {
  console.log(' server is runing on http://localhost:3000')
})











