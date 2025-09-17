/*
Esercizio 5: stampa array e trova massimo
*/

function printArray(arr) {
  arr.forEach(x => console.log(x));
}

function maxInArray(arr) {
  if (!Array.isArray(arr) || arr.length === 0) return null;
  return arr.reduce((acc, x) => (x > acc ? x : acc), arr[0]);
}

if (require && require.main === module) {
  const a = [10, 20, 5];
  printArray(a);
  console.log('Max:', maxInArray(a));
}
