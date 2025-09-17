/*
Trascrizione (best-effort) - valore massimo in array
*/

function maxInArray(arr) {
  if (!Array.isArray(arr) || arr.length === 0) return null;
  let m = arr[0];
  for (let i = 1; i < arr.length; i++) if (arr[i] > m) m = arr[i];
  return m;
}

if (require && require.main === module) {
  console.log(maxInArray([5, 1, 8, 3]));
}
