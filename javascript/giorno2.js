/*
Trascrizione (best-effort) dal pseudocodice nell'immagine 2:

GIORNO 5 (FUNZIONE)
STAMP(A) ARRAY (IN ARRAY)
FOR i IN ARRAY
    PRINT(i)

FUNZIONE CHE TROVA VAL_MAX DI UN ARRAY
VAL = ??? (nell'immagine era impostato a 0 o primo valore)
FOR elem IN ARRAY
    IF elem > VAL
        VAL = elem
PRINT(VAL)

Traduzione in JavaScript: due funzioni, una che stampa gli elementi di un array
e una che restituisce il valore massimo (gestisce array vuoto restituendo null).
*/


function printArray(arr) {
  arr.forEach(item => console.log(item));
}


function maxInArray(arr) {
  if (!Array.isArray(arr) || arr.length === 0) return null;
  let maxVal = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > maxVal) maxVal = arr[i];
  }
  return maxVal;
}


// Esempio d'uso
if (require && require.main === module) {
  const sample = [3, 7, 2, 9, 4];
  console.log('Stampa array:');
  printArray(sample);
  console.log('Valore massimo:', maxInArray(sample));
}
