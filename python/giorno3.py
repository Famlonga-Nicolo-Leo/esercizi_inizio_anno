"""
Trascrizione (best-effort) dall'immagine (esercizio somma/lista):

GIORNO 3 (SOMMA) LISTA 1,2,3
SOMMA = 0
FOR i IN LISTA
    SOMMA = SOMMA + i
PRINT(SOMMA)

Traduzione: funzione sum_list che calcola la somma degli elementi.
"""

from typing import List


def sum_list(nums: List[float]) -> float:
    total = 0
    for x in nums:
        total += x
    return total


if __name__ == "__main__":
    print(sum_list([1, 2, 3]))
