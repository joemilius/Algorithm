import fetch from "node-fetch";
// const x = 2
// let y = 4

// function update(arg){
//     return Math.random() + y * arg
// }
// y = 2
// y = 3
// const result = update(x)
// console.log(result)

// console.log("1"+2+"3"+4)

// console.log(4 + 3+ 2+ "1")
// 'Hello There'
// for (char of 'Hello There'){
//     if(char !== ' '){
//         console.log(char.toLowerCase())
//     }
// }

// fetch('https://api.themoviedb.org/3/search/movie?query=John&api_key=af4b08f18f8cad0dde782175d569446e')
// .then(resp => resp.json())
// .then(data => console.log(data))

fetch(`https://www.googleapis.com/books/v1/volumes?q=rye&key=AIzaSyAFot0f1lMbwAY9D91JMfxO4tEzDWflnSU`)
.then(resp => resp.json())
.then(data => console.log(data.items))

//.forEach(book => console.log(book.volumeInfo))