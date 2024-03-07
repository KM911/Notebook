<%* 
let input = await tp.system.prompt("google：")
if (input.length <= 2){
    return
}
const child_process = require("child_process");
let google_search_url = "https://www.google.com/search?q=" + input
child_process.exec("start " +google_search_url, (error, stdout, stderr) => {
  if (error) {
    console.error(error);  
  } else {
    console.log(stdout);
  }
});
-%>

