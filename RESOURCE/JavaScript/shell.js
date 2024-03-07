function shell (command){
  // 启动vscode 然后start 一个目录 不是吗? 
  const child_process = require("child_process");
  child_process.exec(command ,(error, stdout, stderr) => {
    if (error) {
      console.error(error);  
      return error.msg
    }else{
      console.log(stdout)
    }
  });
  return ""
}
module.exports =shell