// giorno8.js - Correzione esercizio Studente
class Studente {
  constructor(nome, matricola) {
    this.nome = nome;
    this.matricola = matricola;
    this.voti = [];
  }

  aggiungiVoto(voto) {
    if (typeof voto !== 'number' || isNaN(voto)) {
      throw new TypeError('Il voto deve essere un numero');
    }
    this.voti.push(voto);
  }

  calcolaMedia() {
    if (this.voti.length === 0) return 0;
    const somma = this.voti.reduce((a, b) => a + b, 0);
    return somma / this.voti.length;
  }

  toString() {
    return `${this.nome} (${this.matricola}) - media: ${this.calcolaMedia().toFixed(2)}`;
  }
}

// Esempio d'uso
const studenti = [];
studenti.push(new Studente('Alice', 'S001'));
studenti.push(new Studente('Bruno', 'S002'));
studenti.push(new Studente('Carla', 'S003'));

// Aggiungi alcuni voti
studenti[0].aggiungiVoto(7);
studenti[0].aggiungiVoto(8);
studenti[0].aggiungiVoto(6);

studenti[1].aggiungiVoto(5);
studenti[1].aggiungiVoto(6);

studenti[2].aggiungiVoto(9);
studenti[2].aggiungiVoto(10);
studenti[2].aggiungiVoto(8);
studenti[2].aggiungiVoto(7);

// Stampa nome e media per ciascuno
for (const s of studenti) {
  console.log(s.toString());
}
