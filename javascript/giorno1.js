/*
Trascrizione (best-effort) dall'immagine 1:

GIORNO 3 (CALCOLA IL FATTORIALE)
X = numero
FAT = 1
FOR i FROM 1 TO X
    FAT = FAT * i
PRINT(FAT)

Traduzione: funzione factorial(n) iterativa, gestisce n>=0.
*/


function factorial(n) {
  if (n < 0) return null;
  let res = 1;
  for (let i = 1; i <= n; i++) res *= i;
  return res;
}


if (require && require.main === module) {
  [0, 1, 5].forEach(n => console.log(`${n}! = ${factorial(n)}`));
}
