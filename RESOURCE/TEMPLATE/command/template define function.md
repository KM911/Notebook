<%* 
let input = await tp.system.prompt("输入会议标题：")
let templateName = tp.file.find_tfile("Metting-work")
let today = tp.date.now("YYYY-MM-DD")
let titleName = today+" - " + input
const child_process = require("child_process");


child_process.exec("o " +input, (error, stdout, stderr) => {
  if (error) {
    console.error(error);  
  } else {
    console.log(stdout);
  }
});
-%>
