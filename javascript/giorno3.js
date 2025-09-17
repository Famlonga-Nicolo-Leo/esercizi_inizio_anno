/*
Trascrizione (best-effort) - somma lista

SOMMA = 0
FOR elem IN LISTA
  SOMMA = SOMMA + elem
PRINT(SOMMA)
*/

function sumList(nums) {
  let total = 0;
  for (const n of nums) total += n;
  return total;
}

if (require && require.main === module) {
  console.log(sumList([1, 2, 3]));
}
