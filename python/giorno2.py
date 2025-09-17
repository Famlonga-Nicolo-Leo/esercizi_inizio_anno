"""
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

Traduzione in Python: due funzioni, una che stampa gli elementi di un array
e una che restituisce il valore massimo (gestisce array vuoto restituendo None).
"""

from typing import List, Optional


def print_array(arr: List[object]) -> None:
    """Stampa ogni elemento dell'array su una nuova riga."""
    for item in arr:
        print(item)


def max_in_array(arr: List[float]) -> Optional[float]:
    """Restituisce il valore massimo in arr.

    Se l'array è vuoto, restituisce None (il pseudocodice mostrava
    l'uso di una variabile VAL inizializzata, qui non assumiamo un valore
    di default che potrebbe essere errato per array con numeri negativi).
    """
    if not arr:
        return None
    max_val = arr[0]
    for v in arr[1:]:
        if v > max_val:
            max_val = v
    return max_val


if __name__ == "__main__":
    # Esempio d'uso (puoi sostituire con input reale o test):
    sample = [3, 7, 2, 9, 4]
    print("Stampa array:")
    print_array(sample)
    print("Valore massimo:", max_in_array(sample))
