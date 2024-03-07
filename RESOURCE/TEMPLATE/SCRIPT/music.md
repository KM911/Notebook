<%*
let command  = await tp.system.suggester(["play", "pause", "next","previous"],["play", "pause", "next","previous"]) 
const child_process = require("child_process");
child_process.exec("playerctl -p spotify " +command, (error, stdout, stderr) => {
  if (error) {
    console.error("argv error")
  } else {
    console.log(stdout);
  }
});
-%>