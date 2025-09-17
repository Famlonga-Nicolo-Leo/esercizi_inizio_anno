"""
Trascrizione (best-effort) - funzione che trova il valore massimo in un array

VAL = 0 (o primo valore)
FOR elem IN ARRAY
  IF elem > VAL
    VAL = elem
PRINT(VAL)

Traduzione: implementazione robusta che restituisce None per array vuoto.
"""

from typing import List, Optional


def max_in_array(arr: List[float]) -> Optional[float]:
    if not arr:
        return None
    m = arr[0]
    for x in arr[1:]:
        if x > m:
            m = x
    return m


if __name__ == "__main__":
    print(max_in_array([5, 1, 8, 3]))
