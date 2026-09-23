"""Assegna i partecipanti a prodotto o placebo, in cieco.

Uso:
    python3 randomizza.py partecipanti.csv --seme 2026 [--crossover]

Il file partecipanti.csv deve avere almeno la colonna "id" e, facoltativa,
la colonna "strato" (es. "M-under40", "F-over40") per bilanciare i gruppi.

Produce due file:
- codici_confezioni.csv  -> da dare a chi allena e misura (solo codici A/B, nessun nome del prodotto)
- chiave_segreta.csv     -> da tenere chiuso (es. dal farmacista o dal medico) fino alla fine dello studio
"""

import argparse
import csv
import random
from collections import defaultdict


def assegna_parallelo(partecipanti, rng):
    """Randomizzazione a blocchi di 4 dentro ogni strato: gruppi sempre bilanciati."""
    per_strato = defaultdict(list)
    for p in partecipanti:
        per_strato[p.get("strato") or "unico"].append(p)

    assegnazioni = {}
    for membri in per_strato.values():
        rng.shuffle(membri)
        for inizio in range(0, len(membri), 4):
            blocco = ["prodotto", "prodotto", "placebo", "placebo"]
            rng.shuffle(blocco)
            for p, braccio in zip(membri[inizio:inizio + 4], blocco):
                assegnazioni[p["id"]] = braccio
    return assegnazioni


def assegna_crossover(partecipanti, rng):
    """Ognuno prova entrambi: metà inizia con il prodotto, metà con il placebo."""
    ids = [p["id"] for p in partecipanti]
    rng.shuffle(ids)
    meta = len(ids) // 2
    sequenze = {}
    for i, pid in enumerate(ids):
        sequenze[pid] = "prodotto-poi-placebo" if i < meta else "placebo-poi-prodotto"
    return sequenze


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("file_partecipanti")
    parser.add_argument("--seme", type=int, required=True, help="numero fisso per rendere l'assegnazione riproducibile")
    parser.add_argument("--crossover", action="store_true", help="disegno crossover invece che a gruppi paralleli")
    args = parser.parse_args()

    with open(args.file_partecipanti, newline="", encoding="utf-8") as f:
        partecipanti = list(csv.DictReader(f))
    if not partecipanti or "id" not in partecipanti[0]:
        raise SystemExit("Il file deve contenere una colonna 'id'.")

    rng = random.Random(args.seme)
    if args.crossover:
        assegnazioni = assegna_crossover(partecipanti, rng)
    else:
        assegnazioni = assegna_parallelo(partecipanti, rng)

    # I codici delle confezioni nascondono il contenuto: la lettera A/B è casuale per ogni studio.
    lettere = ["A", "B"]
    rng.shuffle(lettere)
    codice_di = {"prodotto": lettere[0], "placebo": lettere[1],
                 "prodotto-poi-placebo": f"{lettere[0]}-{lettere[1]}",
                 "placebo-poi-prodotto": f"{lettere[1]}-{lettere[0]}"}

    with open("codici_confezioni.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "codice_confezione"])
        for p in partecipanti:
            w.writerow([p["id"], codice_di[assegnazioni[p["id"]]]])

    with open("chiave_segreta.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "assegnazione", "codice_confezione"])
        for p in partecipanti:
            braccio = assegnazioni[p["id"]]
            w.writerow([p["id"], braccio, codice_di[braccio]])

    conteggio = defaultdict(int)
    for braccio in assegnazioni.values():
        conteggio[braccio] += 1
    print("Assegnazione completata:", dict(conteggio))
    print("-> codici_confezioni.csv (per lo staff) e chiave_segreta.csv (da custodire chiusa)")


if __name__ == "__main__":
    main()
