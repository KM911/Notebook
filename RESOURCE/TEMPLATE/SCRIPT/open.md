<%* 
let input = await tp.system.prompt("op：")
const child_process = require("child_process");
child_process.exec("o " +input, (error, stdout, stderr) => {
  if (error) {
    console.error("argv error")
  } else {
    console.log(stdout);
  }
});
-%>