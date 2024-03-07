// 与函数名无关,只与文件名有关
function TemplateFunction_NoMatter_Its_Name  (PyFunctionName,CurrentFilePath) {
  // 我们这里可以将python的执行结果stdout作为模板的内容
  const python_function_path = "D:\\GITHUB\\KM911\\static-html\\blogs\\_posts\\RESOURCE\\Function\\" + PyFunctionName + ".py "
  const child_process = require("child_process");
  // 这是一个回调函数
  // child_process.execSync("python " + python_function_path + CurrentFilePath ,(error, stdout, stderr) => {
  //   if (error) {
  //     console.error(error);  
  //     return error.msg
  //   }else{
  //     console.log(stdout)
  //   }
  // });
  
  // 这里的返回值应该是stdout
  // 将stdout做utf-8编码
  return child_process.execSync("python " + python_function_path + CurrentFilePath)
  // return   child_process.execSync("python " + python_function_path + CurrentFilePath);
  
}
module.exports =TemplateFunction_NoMatter_Its_Name
