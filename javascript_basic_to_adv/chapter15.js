let String1 = "Harry"

let String2 = "Potter"

console.log(String1 + " " + String2)
console.log(`${String1} = ${String1.length}`)
console.log(`${String2} = ${String2.length}`)

console.log(`${String1.replace("Har", "Per")} `)
console.log(`${String1.toUpperCase()} `)
console.log(`${String2.toLowerCase()} `)

console.log(`${String1.charAt(0)} `)

console.log(`${String1.charCodeAt(0)} `)


// In the following code, we are trying to change the first character of the string to "P". But it is not working. Why?

// Because strings are immutable in JavaScript. You can't change the value of a string once it is created. You can only create a new string with the desired value.

// har[0] = "P"
// console.log(har)

