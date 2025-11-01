var a="你好",b=13,c=true,d=null,e=true;
var animal=new Array("cat","bear","pig","dog");
var score=new Array(7);
var str="我命,由我,不由天.!";
var arrSu=str.split(",");
var outStr=arrSu.join("-");
var namber =new Array("e123","d123","a123","c123");
var fruit=new Array("apple","pear","orange","grape");
document.write(a+"<br>")
document.write(b+"<br>")
document.write(c+"<br>")
document.write(d+"<br>")
document.write(e+"<br>")
document.write(animal[0]+"<br>")
document.write(animal[1]+"<br>")
document.write(animal[2]+"<br>")
document.write(animal[3]+"<br>")
document.write(score.length+"<br>")
document.write("分割前："+str+"<br>")
document.write("使用\"-\"重新连接后"+outStr+"<br>")
document.write(namber.sort()+"<br>")
document.write(fruit.push("banana")+"<br>")