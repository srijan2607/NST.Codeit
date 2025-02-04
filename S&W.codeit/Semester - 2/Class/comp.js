let name1 = "Vishal";
let name2 = "Pooja";
let c_score = 0;

if (name1.length == name2.length) {
  c_score += 10;
}
for (let i = 0; i < name1.length; i++) {
  for (let j = 0; j < name2.length; j++) {
    if (name1[i] == name2[j]) {
      c_score += 10;
    }
  }
}
if (c_score > 50){
    console.log("Congratulations! Both Are compatable");
}
else{
    console.log("Sorry! Both are not compatable");
}

console.log(c_score);
