// // objects
// const A = {
//   name: "Srijan",
//   id: 134,
// };

// function modifyObject(obj) {
//   obj.name = "yo";
//   obj.id = 4;
// }

// modifyObject(A);
// console.log(A);

// const D = A
// D.name = "no"

// console.log(A);

// Shallow Copy
// const B = Object.assign({}, A);
// const B = { ...A };
// B.name = "no";
// console.log(A);
// console.log(B);

// const B = { ...A };
// B.id = 33;
// B.nested.d.e = 20;
// console.log(B);
// console.log(A);
// const A = {
//   id: 1,
//   nested: {
//     d: { e: 15 },
//   },
// };

// Deep copy
// const ACopy = structuredClone(A);
// ACopy.nested.d.e = 33;
// console.log(ACopy);
// console.log(A);

// const ACopy = JSON.parse(JSON.stringify(A));
// ACopy.nested.d.e = 3344;
// console.log(ACopy);
// console.log(A);
