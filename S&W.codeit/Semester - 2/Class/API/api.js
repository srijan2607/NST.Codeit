// fetch("https://jsonplaceholder.typicode.com/users")
//     .then(response => response.json())
//     .then(data => console.log(data))
//     .catch(error => console.error('Error:', error));

const response = fetch("https://jsonplaceholder.typicode.com/users");

function successCallback(response) {
  console.log("Fetch Value",response);
  response.json().then(data => console.log(data));
  console.log("Fetch Value",response);
}
