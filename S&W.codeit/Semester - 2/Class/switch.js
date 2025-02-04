// const percentage = 80;
// switch (true) {
//   case percentage >= 90:
//     console.log("A");
//     break;
//   case percentage >= 70:
//     console.log("B");
//     break;
//   case percentage >= 60:
//     console.log("C");
//     break;
//   case percentage >= 50:
//     console.log("D");
//     break;
//   case percentage >= 40:
//     console.log("E");
// }

// console.log("Hello, world!".indexOf("world"));

// const num = 12;
// const message = num % 2 === 0 ? "Even" : "Odd";
// const message2 =
//   num % 2 === 0 && num % 5 === 0
//     ? "Divisiable by 2 & 5"
//     : num % 3 === 0 && num % 2 === 0
//     ? "Divisiable by 2 & 3"
//     : "odd";

// for (let i = 0; i < 5; i++) {
//   console.log(i);
//   if (i === 3) {
//     break;
//   }
// }

let count = 0;
while (count < 10) {
  console.log(count);
  count++;
  if (count === 5) {
    continue;
  }
}
