/*
Scambia A e B usando aritmetica (senza variabile temporanea)
*/

function swapArithmetic(a, b) {
  a = a + b;
  b = a - b;
  a = a - b;
  return [a, b];
}

if (require && require.main === module) {
  let [A, B] = swapArithmetic(5, 7);
  console.log(A);
  console.log(B);
}
