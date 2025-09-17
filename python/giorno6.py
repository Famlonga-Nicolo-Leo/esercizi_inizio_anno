"""
Trascrizione (best-effort) dall'immagine per esercizio 6:

SCAMBIA (A, B)
A = A + B
B = A - B
A = A - B
PRINT(A)
PRINT(B)

Traduzione: funzione swap senza usare una variabile temporanea (aritmetica).
"""

from typing import Tuple


def swap_arithmetic(a: int, b: int) -> Tuple[int, int]:
    a = a + b
    b = a - b
    a = a - b
    return a, b


if __name__ == "__main__":
    A, B = 5, 7
    A, B = swap_arithmetic(A, B)
    print(A)
    print(B)
