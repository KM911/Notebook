// function 这里好像是浏览器环境
// 因为是 commonjs的

function PyFunction (PyFunctionName,CurrentFilePath) {
  const python_function_path = "D:\\GITHUB\\KM911\\static-html\\blogs\\_posts\\RESOURCE\\Function\\" + PyFunctionName + ".py "
  const child_process = require("child_process");
  const command = "python " + python_function_path + CurrentFilePath
  console.log("command is " + command)
  child_process.exec(command ,(error, stdout, stderr) => {
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
  // 这里的返回值应该是stdout
  return ""
}
module.exports = PyFunction;
