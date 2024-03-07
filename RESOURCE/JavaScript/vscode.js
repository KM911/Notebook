function vscode (){
  // 启动vscode 然后start 一个目录 不是吗? 

  const python_function_path = "D:\\GITHUB\\KM911\\static-html\\blogs\\_posts\\RESOURCE\\Function\\"
  const child_process = require("child_process");
  child_process.exec("code " + python_function_path  ,(error, stdout, stderr) => {
    if (error) {
      console.error(error);  
      return error.msg
    }else{
      // var env = window ? "browser" : "node"
      // console.log(env)
      // 重定向 stdout 
      console.log(stdout)
    }
  });
  return ""
}
module.exports =vscode
