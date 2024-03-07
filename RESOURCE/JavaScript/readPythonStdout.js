// 与函数名无关,只与文件名有关
function TemplateFunction_NoMatter_Its_Name  (PyFunctionName) {
  // 我们这里可以将python的执行结果stdout作为模板的内容
  const python_function_path = "D:\\GITHUB\\KM911\\static-html\\blogs\\_posts\\RESOURCE\\Function\\" + PyFunctionName + ".py "
  const child_process = require("child_process");
  // 非常好
  return   child_process.execSync("python " + python_function_path).toString();
  
}
module.exports =TemplateFunction_NoMatter_Its_Name
