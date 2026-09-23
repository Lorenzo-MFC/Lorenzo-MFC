"""Confronta prodotto e placebo a fine studio.

Uso (gruppi paralleli):
    python3 analizza.py risultati.csv chiave_segreta.csv [--test salto_cm] [--permutazioni 20000]
    risultati.csv: colonne "id", "test", "prima", "dopo" (una riga per persona e per test).

Uso (crossover, ognuno prova entrambe le confezioni):
    python3 analizza.py risultati.csv chiave_segreta.csv --crossover
    risultati.csv: colonne "id", "test", "valore_A", "valore_B"
    (il valore misurato nella sessione con la confezione A e con la confezione B).

Il file chiave_segreta.csv è quello prodotto da randomizza.py: si apre solo a misure concluse.

Per ogni test calcola:
- variazione media (dopo - prima) nei due gruppi e la differenza tra i due
- dimensione dell'effetto (d di Cohen): ~0,2 piccolo, ~0,5 medio, ~0,8 grande
- valore p con test di permutazione (nessuna libreria esterna richiesta):
  sotto 0,05 la differenza difficilmente è dovuta al caso
"""

import argparse
import csv
import random
import statistics
from collections import defaultdict


def d_di_cohen(a, b):
    if len(a) < 2 or len(b) < 2:
        return float("nan")
    sd_comune = (((len(a) - 1) * statistics.variance(a) + (len(b) - 1) * statistics.variance(b))
                 / (len(a) + len(b) - 2)) ** 0.5
    return (statistics.mean(a) - statistics.mean(b)) / sd_comune if sd_comune else float("nan")


def p_permutazione(a, b, n, rng):
    """Quante volte, mescolando a caso le etichette, si ottiene una differenza almeno così grande."""
    osservata = abs(statistics.mean(a) - statistics.mean(b))
    tutti = a + b
    estremi = 0
    for _ in range(n):
        rng.shuffle(tutti)
        if abs(statistics.mean(tutti[:len(a)]) - statistics.mean(tutti[len(a):])) >= osservata:
            estremi += 1
    return (estremi + 1) / (n + 1)


def p_permutazione_appaiata(diff, n, rng):
    """Crossover: si inverte a caso il segno delle differenze individuali."""
    osservata = abs(statistics.mean(diff))
    estremi = 0
    for _ in range(n):
        if abs(statistics.mean([d if rng.random() < 0.5 else -d for d in diff])) >= osservata:
            estremi += 1
    return (estremi + 1) / (n + 1)


def analizza_crossover(args):
    """Differenza individuale (con prodotto - con placebo) per ogni persona e test."""
    lettera_prodotto = {}
    with open(args.file_chiave, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            prima, dopo = r["codice_confezione"].split("-")
            lettera_prodotto[r["id"]] = prima if r["assegnazione"] == "prodotto-poi-placebo" else dopo

    differenze = defaultdict(list)
    with open(args.file_risultati, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if args.test and r["test"] != args.test:
                continue
            lettera = lettera_prodotto.get(r["id"])
            if lettera is None or not r["valore_A"] or not r["valore_B"]:
                continue
            con_prodotto = float(r[f"valore_{lettera}"])
            con_placebo = float(r["valore_B" if lettera == "A" else "valore_A"])
            differenze[r["test"]].append(con_prodotto - con_placebo)

    rng = random.Random(0)
    print(f"{'test':<18}{'n':>5}{'diff media':>12}{'d':>7}{'p':>8}")
    for test, diff in differenze.items():
        if len(diff) < 2 or not statistics.stdev(diff):
            print(f"{test:<18} dati insufficienti")
            continue
        d = statistics.mean(diff) / statistics.stdev(diff)
        p = p_permutazione_appaiata(diff, args.permutazioni, rng)
        print(f"{test:<18}{len(diff):>5}{statistics.mean(diff):>12.2f}{d:>7.2f}{p:>8.3f}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("file_risultati")
    parser.add_argument("file_chiave")
    parser.add_argument("--test", help="analizza solo questo test")
    parser.add_argument("--permutazioni", type=int, default=20000)
    parser.add_argument("--crossover", action="store_true", help="disegno crossover (valore_A / valore_B)")
    args = parser.parse_args()
    if args.crossover:
        analizza_crossover(args)
        return

    with open(args.file_chiave, newline="", encoding="utf-8") as f:
        braccio_di = {r["id"]: r["assegnazione"] for r in csv.DictReader(f)}

    variazioni = defaultdict(lambda: {"prodotto": [], "placebo": []})
    with open(args.file_risultati, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if args.test and r["test"] != args.test:
                continue
            braccio = braccio_di.get(r["id"])
            if braccio not in ("prodotto", "placebo") or not r["prima"] or not r["dopo"]:
                continue  # abbandoni o dati mancanti: vengono esclusi e vanno riportati
            variazioni[r["test"]][braccio].append(float(r["dopo"]) - float(r["prima"]))

    rng = random.Random(0)
    print(f"{'test':<18}{'n prod':>7}{'n plac':>7}{'Δ prod':>9}{'Δ plac':>9}{'diff':>8}{'d':>7}{'p':>8}")
    for test, g in variazioni.items():
        a, b = g["prodotto"], g["placebo"]
        if len(a) < 2 or len(b) < 2:
            print(f"{test:<18} dati insufficienti")
            continue
        diff = statistics.mean(a) - statistics.mean(b)
        p = p_permutazione(a, b, args.permutazioni, rng)
        print(f"{test:<18}{len(a):>7}{len(b):>7}{statistics.mean(a):>9.2f}{statistics.mean(b):>9.2f}"
              f"{diff:>8.2f}{d_di_cohen(a, b):>7.2f}{p:>8.3f}")


if __name__ == "__main__":
    main()
