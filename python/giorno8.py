# giorno8.py - Correzione esercizio Studente
class Studente:
    def __init__(self, nome: str, matricola: str):
        self.nome = nome
        self.matricola = matricola
        self.voti = []

    def aggiungi_voto(self, voto):
        try:
            voto = float(voto)
        except Exception:
            raise TypeError("Il voto deve essere un numero")
        self.voti.append(voto)

    def calcola_media(self):
        if not self.voti:
            return 0.0
        return sum(self.voti) / len(self.voti)

    def __str__(self):
        return f"{self.nome} ({self.matricola}) - media: {self.calcola_media():.2f}"


def main():
    studenti = [
        Studente("Alice", "S001"),
        Studente("Bruno", "S002"),
        Studente("Carla", "S003"),
    ]

    # Aggiungi voti
    studenti[0].aggiungi_voto(7)
    studenti[0].aggiungi_voto(8)
    studenti[0].aggiungi_voto(6)

    studenti[1].aggiungi_voto(5)
    studenti[1].aggiungi_voto(6)

    studenti[2].aggiungi_voto(9)
    studenti[2].aggiungi_voto(10)
    studenti[2].aggiungi_voto(8)
    studenti[2].aggiungi_voto(7)

    # Stampa
    for s in studenti:
        print(s)


if __name__ == "__main__":
    main()
