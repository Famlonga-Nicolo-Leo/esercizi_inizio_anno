"""
Trascrizione (best-effort) dall'immagine 1:

GIORNO 3 (CALCOLA IL FATTORIALE)
X = numero
FAT = 1
FOR i FROM 1 TO X
    FAT = FAT * i
PRINT(FAT)

Traduzione: funzione factorial(n) iterativa, gestisce n>=0.
"""

from typing import Optional


def factorial(n: int) -> Optional[int]:
    """Calcola il fattoriale di n (n >= 0). Restituisce None per n < 0."""
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    for n in (0, 1, 5):
        print(f"{n}! = {factorial(n)}")
