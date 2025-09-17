"""
Trascrizione (best-effort) dall'immagine per esercizio 5:
 - Funzione che stampa un array
 - Funzione che trova il massimo di un array

Queste funzioni sono analoghe a quelle di giorno2 e giorno4;
qui le riporto in un file separato come richiesto.
"""

from typing import List, Optional


def print_array(arr: List[object]) -> None:
    for e in arr:
        print(e)


def max_in_array(arr: List[float]) -> Optional[float]:
    if not arr:
        return None
    m = arr[0]
    for v in arr[1:]:
        if v > m:
            m = v
    return m


if __name__ == "__main__":
    a = [10, 20, 5]
    print_array(a)
    print('Max:', max_in_array(a))
