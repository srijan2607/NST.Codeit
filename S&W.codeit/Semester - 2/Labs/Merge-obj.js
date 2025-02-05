const obj1 = {
  name: "John",
  age: 30,
  city: "New York",
};
const obj2 = {
  name: "Angel",
  age: 40,
  city: "Los Angeles",
};

// const mergedObj = { ...obj1, ...obj2 };

// console.log(mergedObj);

// Sort
// function mergeAndSortStudentMarks(obj1, obj2) {
//     let mergedObj = {...obj1,...obj2}
//     let objectit = Object.entries()
//     objectit.sort((a, b) => b[1] - a[1])
//     return objectit
//   }
//

// Deep copy without inbuilt function
return function deepClone(object) {
    if (typeof object!== 'object' || object === null) {
      return object;
    }
    let clone = Array.isArray(object)? [] : {};
    for (let key in object) {
      clone[key] = deepClone(object[key]);
    }
    return clone;
    
};
