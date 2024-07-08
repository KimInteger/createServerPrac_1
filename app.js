const http = require('http');
const PORT = process.env.PORT || 8080;

const server = http.createServer((req,res)=>{
  console.log('server Open!');
});

server.listen(PORT,(err)=>{
  if(err){
    throw new Error('아직도 에러가 나와여?')
  } else {
    console.log('와 서버 열림!');
    console.log(`http://localhost:${PORT}`);
  }
});