# Trial di prodotti per la performance fisica: kit operativo per MFC

> Aggiornato a **settembre 2026**. Documento informativo, **non è consulenza medica o legale**.
> Prima di coinvolgere persone in uno studio vedere la sezione 6 (etica, consenso, assicurazione).

Obiettivo: permettere a MFC di **testare in modo serio** i prodotti per la performance,
sia per decidere **cosa vendere** ai clienti, sia come **servizio a pagamento per le
aziende** di integratori (vedi sezione 7).

Nella cartella [`strumenti-trial/`](strumenti-trial/) ci sono due programmi pronti:
- `randomizza.py`: assegna a caso prodotto o placebo, in cieco;
- `analizza.py`: a fine studio calcola se il prodotto ha funzionato davvero.

---

## 1. Le regole d'oro (senza queste il trial non vale niente)

1. **Placebo identico**: stessa forma, colore, gusto e confezione. Se il cliente capisce
   cosa sta prendendo, il risultato è falsato (l'effetto placebo nello sport vale spesso
   **2-5%**, cioè quanto molti integratori).
2. **Doppio cieco**: né il partecipante né l'istruttore che misura sanno chi prende cosa.
   Le confezioni riportano solo un codice (A/B); la chiave la custodisce una terza persona
   (medico, farmacista o il titolare non coinvolto nelle misure).
3. **Randomizzazione**: è il computer a decidere chi va in quale gruppo, non lo staff.
4. **Obiettivo scelto prima**: si decide **prima di iniziare** quale test conta di più
   (es. "1RM squat dopo 8 settimane"). Non si possono guardare 20 test e scegliere dopo
   quello che "è venuto bene".
5. **Stesse condizioni**: stesso orario, stesso riscaldamento, stesso strumento e,
   se possibile, stesso istruttore per le misure prima e dopo.
6. **Prodotti certificati**: solo lotti con certificazione antidoping (**Informed Sport**,
   **Cologne List**) e analisi del contenuto, per avere la certezza che la dose sia quella
   dichiarata e che non ci siano contaminanti.
7. **Registrare tutto**: abbandoni, effetti indesiderati, dosi saltate. Chi abbandona va
   riportato nei risultati, non nascosto.

---

## 2. Due disegni di studio

| Disegno | Come funziona | Quando usarlo | Persone necessarie |
|---|---|---|---|
| **Crossover** | Ognuno prova **sia** il prodotto **sia** il placebo in giorni diversi, in ordine casuale, con una pausa ("washout") tra i due | Prodotti ad **effetto acuto** (una dose prima dello sforzo): caffeina, nitrati, bicarbonato | **Poche**: 15-35 in totale |
| **Gruppi paralleli** | Metà prende il prodotto per settimane, metà il placebo, tutti con lo stesso allenamento | Prodotti ad **effetto cronico** (si accumulano): creatina, beta-alanina, urolitina A, NR | **Di più**: 25-65 per gruppo |

### Quante persone servono (stima)

Dipende da quanto è grande l'effetto atteso rispetto alla variabilità delle persone
(il "d di Cohen"). Valori per il 5% di errore e l'80% di probabilità di trovare l'effetto
se esiste:

| Effetto atteso | Gruppi paralleli (per gruppo) | Crossover (in totale) |
|---|---|---|
| Grande (d = 0,8) | ~26 | ~15 |
| Medio (d = 0,5) | ~64 | ~34 |
| Piccolo (d = 0,3) | ~175 | ~90 |

**Aggiungere il 15-20% per gli abbandoni.** Conseguenza pratica: con 20-30 iscritti una
palestra può fare **bene** trial crossover su prodotti acuti, mentre per effetti piccoli e
cronici (NR, urolitina A) serve collaborare con **più palestre** o con un'università.

---

## 3. Batteria di test consigliata

| Qualità | Test | Strumento | Variabilità tipica tra un giorno e l'altro* |
|---|---|---|---|
| **Forza massima** | 1RM o 3RM squat / panca / leg press | Bilanciere, macchine | ~2-5% |
| **Potenza** | Salto con contromovimento (CMJ) | Tappetino a contatto, pedana o app validata | ~3-5% |
| **Forza isometrica** | Forza di presa | Dinamometro | ~5% |
| **Resistenza muscolare** | Ripetizioni al 70% 1RM fino a cedimento | Bilanciere | ~5-10% |
| **Capacità anaerobica** | 30 secondi "all-out" su bike (tipo Wingate) o 500 m vogatore | Bike/vogatore con monitor | ~3-5% |
| **Resistenza aerobica** | 2 km vogatore, 5 km bike a tempo, test Cooper | Vogatore/bike, pista | ~2-4% |
| **Recupero** | Salto e forza 24-48 h dopo un allenamento pesante; dolore muscolare (scala 0-10) | Come sopra + questionario | Alta |
| **Composizione corporea** | Bioimpedenza (stesse condizioni: mattino, a digiuno, idratati) | Bilancia professionale | ~1-3% |
| **Percezione** | Sforzo percepito (RPE), fatica, sonno | Questionari | Alta |

\* *Valori indicativi dalla letteratura; conviene misurarli sulla propria popolazione con un
test ripetuto 2 volte a una settimana di distanza. Se un prodotto dà un miglioramento più
piccolo della variabilità del test, con pochi partecipanti non lo si vedrà.*

**Consiglio**: fare sempre **1-2 sessioni di familiarizzazione** con i test prima della misura
iniziale, altrimenti il miglioramento "da apprendimento" si confonde con quello del prodotto.

---

## 4. Protocolli pronti per prodotto

### A) Caffeina — crossover (il più semplice per iniziare)

| Voce | Dettaglio |
|---|---|
| Dose | 3 mg/kg in capsula, 60 minuti prima; placebo: capsula identica con cellulosa |
| Partecipanti | 30-40 adulti sani (con 20 il trial serve come collaudo, ma può non vedere un effetto medio-piccolo), **nessuna** condizione cardiaca, ansia, gravidanza |
| Regole | Niente caffè/energy drink nelle 24 h prima di ogni sessione |
| Sessioni | 2 sessioni a 3-7 giorni di distanza, stesso orario |
| Test principale | Ripetizioni al 70% 1RM su panca fino a cedimento, oppure 2 km vogatore |
| Test secondari | CMJ, RPE |
| Effetto atteso | +2-4% (d ~0,3-0,5) |
| Durata totale | 2-3 settimane |

### B) Nitrati (succo di barbabietola) — crossover

| Voce | Dettaglio |
|---|---|
| Dose | ~6-13 mmol di nitrati (1-2 shot da 70 mL di concentrato) 2,5 h prima; placebo: succo di barbabietola **privato dei nitrati** (disponibile in commercio per la ricerca) |
| Regole | Niente collutorio antibatterico (blocca l'effetto), niente gomme da masticare |
| Test principale | 5 km bike o 2 km vogatore a tempo |
| Effetto atteso | Più evidente nei **non atleti**: ~1-3% |
| Durata | 2-3 settimane |

### C) Creatina monoidrato — gruppi paralleli (il "riferimento")

| Voce | Dettaglio |
|---|---|
| Dose | 5 g/giorno (oppure carico 20 g/giorno per 5 giorni, poi 5 g); placebo: maltodestrine con stesso aspetto |
| Allenamento | Programma di forza identico per tutti, 3 volte/settimana |
| Durata | 8 settimane |
| Test principale | 1RM squat (o leg press) |
| Test secondari | 1RM panca, CMJ, ripetizioni al 70%, massa magra (bioimpedenza) |
| Effetto atteso | Di solito **medio-grande** sulla forza e sul peso corporeo (+1-2 kg, in parte acqua) |
| Utilità | Ottimo **trial "di prova"** per mettere a punto la procedura: se il sistema funziona, la creatina deve risultare efficace |

### D) Beta-alanina — gruppi paralleli

| Voce | Dettaglio |
|---|---|
| Dose | 3,2-6,4 g/giorno divisi in dosi da 0,8-1,6 g (limita il formicolio, detto *parestesia*) |
| Attenzione | Il formicolio può **rompere il cieco**: usare la forma a rilascio prolungato o dosi piccole |
| Durata | 6-8 settimane |
| Test principale | Sforzi di 1-4 minuti: 30 s all-out ripetuti, 500-1000 m vogatore |

### E) Urolitina A / NR / altri prodotti "longevity" — gruppi paralleli

| Voce | Dettaglio |
|---|---|
| Dose | Secondo i dosaggi degli studi (es. urolitina A 500-1000 mg/giorno; NR fino a 300 mg/giorno secondo i limiti UE) |
| Popolazione | Meglio **adulti over 40-45** o poco allenati (dove gli studi mostrano i segnali maggiori) |
| Durata | 12-16 settimane |
| Test principale | Resistenza muscolare (ripetizioni fino a cedimento), forza di presa |
| Persone | Effetti attesi piccoli → **50-100 per gruppo** → serve una **rete di palestre** o un'università |

### F) Bicarbonato di sodio — crossover (solo per atleti esperti)

Dose 0,2-0,3 g/kg 60-180 minuti prima; frequenti disturbi gastrointestinali → usare capsule
gastroresistenti e fare prima una prova di tolleranza. Test: sprint ripetuti o 4 × 30 s.

---

## 5. Calendario tipo (trial a gruppi paralleli di 8 settimane)

| Settimana | Attività |
|---|---|
| -3 | Reclutamento, informativa, consenso, certificato medico |
| -2 | 2 sessioni di familiarizzazione con i test |
| -1 | **Misure iniziali**; randomizzazione con `randomizza.py`; consegna delle confezioni codificate |
| 1-8 | Assunzione + allenamento standardizzato; diario giornaliero delle dosi e degli effetti indesiderati; conteggio delle capsule restituite |
| 4 | Misura intermedia (facoltativa) |
| 9 | **Misure finali** alle stesse condizioni |
| 10 | Apertura della chiave; analisi con `analizza.py`; relazione |

### Come usare gli strumenti

```bash
# 1. elenco partecipanti (colonne: id, strato) -> assegnazione in cieco
python3 strumenti-trial/randomizza.py partecipanti.csv --seme 2026
#    per un crossover:  ... --crossover

# 2. a fine studio: risultati.csv con colonne id, test, prima, dopo
python3 strumenti-trial/analizza.py risultati.csv chiave_segreta.csv
#    per un crossover: colonne id, test, valore_A, valore_B  e opzione --crossover
```

Il file di esempio [`strumenti-trial/esempio_partecipanti.csv`](strumenti-trial/esempio_partecipanti.csv)
mostra il formato. **Come leggere i risultati**:
- **diff**: di quanto il gruppo con il prodotto è migliorato più del gruppo placebo;
- **d**: dimensione dell'effetto (0,2 piccolo, 0,5 medio, 0,8 grande);
- **p**: sotto 0,05 è poco probabile che la differenza sia dovuta al caso. Un p sopra 0,05
  **non dimostra** che il prodotto non funzioni, se i partecipanti erano pochi.

Prova su dati simulati (24 persone): con un effetto reale sullo squat di +5,6 kg rispetto al
placebo, lo strumento ha restituito **d = 1,42 e p = 0,001**; su un test dove l'effetto
simulato era nullo ha restituito **p = 0,57**, cioè nessun effetto, come atteso.

---

## 6. Aspetti etici, legali e di sicurezza (Italia)

| Tema | Cosa fare |
|---|---|
| **Comitato etico** | Uno **studio di ricerca** su persone (anche con integratori già in commercio), soprattutto se se ne vogliono **pubblicare** i risultati o usarli per **pubblicità**, va approvato da un **Comitato Etico Territoriale**. Il modo più semplice: farlo **in collaborazione con un'università o un medico/ospedale** che presenta la domanda come promotore. |
| **Consenso informato** | Scritto, con scopo, rischi, diritto di ritirarsi in qualsiasi momento, gestione dei dati |
| **Certificato medico** | Almeno non agonistico, valido; esclusione di gravidanza, patologie cardiache, renali, psichiatriche o in terapia farmacologica non compatibile |
| **Assicurazione** | Gli studi interventistici richiedono di norma una **polizza specifica** per la sperimentazione: verificare con il comitato etico e con l'assicuratore |
| **Dati** | Dati sanitari (GDPR art. 9): consenso esplicito, codici al posto dei nomi, accesso limitato |
| **Prodotti** | Solo integratori **notificati al Ministero della Salute** e, per i *novel food*, autorizzati in UE (niente NMN finché non è autorizzato, niente sostanze vietate) |
| **Antidoping** | Escludere o avvisare gli **atleti tesserati**; usare solo lotti certificati |
| **Pubblicità dei risultati** | I claim sulla salute degli integratori sono regolati dal **Reg. UE 1924/2006**: un trial interno **non autorizza** nuovi claim in etichetta o in pubblicità. Si possono comunicare i risultati in modo corretto ("nel nostro test su 30 soci…"), senza promesse di salute non autorizzate |
| **Effetti indesiderati** | Registro scritto; interruzione immediata e avviso al medico per qualsiasi evento serio |

> **Distinzione utile**: una semplice **valutazione interna** ("proviamo 2 prodotti in cieco
> per decidere quale mettere a listino", senza pubblicazione e con prodotti in commercio
> usati alle dosi indicate in etichetta) è molto più leggera di uno **studio di ricerca**.
> Il confine va comunque verificato con un consulente o con il comitato etico.

---

## 7. Il trial come business: "MFC Performance Lab"

Le aziende di integratori hanno bisogno di **dati sulle persone reali** per i loro prodotti, e
gli studi universitari costano molto e richiedono tempo. Una palestra ben organizzata, **in
partnership con un'università**, può offrire studi pilota a costi più bassi.

### Tre linee di ricavo

| Linea | Cliente | Prezzo indicativo* |
|---|---|---|
| **Test interni** per scegliere i prodotti da vendere | MFC stessa | Costo interno; aumenta i margini sugli integratori perché si vende solo ciò che funziona |
| **Studio pilota per un'azienda** (crossover o 8 settimane, 30-40 persone, relazione finale) | Brand di integratori, startup | **8.000-25.000 €** a studio |
| **Studio con università** e pubblicazione scientifica | Brand + università (anche con fondi pubblici o bandi) | 25.000-80.000 €, ma con tempi di 12-24 mesi |

\* *Stime da validare chiedendo preventivi a laboratori e università.*

### Conto economico di uno studio pilota (esempio, 36 partecipanti, 8 settimane)

| Voce | Importo |
|---|---|
| Ricavo dall'azienda | **15.000 €** |
| Incentivo ai partecipanti (3 mesi di abbonamento gratuito, ~150 € × 36) | -5.400 € |
| Tempo dello staff (test, supervisione: ~120 h × 25 €) | -3.000 € |
| Statistico / consulenza universitaria | -1.500 € |
| Comitato etico e assicurazione (se necessari) | -1.500 / -3.000 € |
| Materiali, stampa, gestione dati | -500 € |
| **Margine** | **~2.000-3.000 €** + **36 persone** che hanno provato la palestra (alcune restano come clienti paganti) |

Il margine diretto è modesto: il valore vero sta nella **reputazione**, nei **nuovi iscritti**
e nella **relazione con i brand** (sponsorizzazioni, forniture a prezzo migliore, eventi).

### Investimento in attrezzatura per i test

| Strumento | Costo indicativo |
|---|---|
| Tappetino/pedana per il salto (CMJ) | 300-3.000 € |
| Dinamometro per la forza di presa | 50-300 € |
| Vogatore/bike con monitor di potenza (spesso già presenti) | 0-2.000 € |
| Bilancia a bioimpedenza professionale | 3.000-15.000 € |
| Cardiofrequenzimetri a fascia | 50-100 € l'uno |
| **Totale** | **~4.000-20.000 €**, riutilizzabile per il "Performance Lab" e il programma GLP-1 |

---

## 8. Prossimi passi proposti

1. Fare un **trial crossover sulla caffeina** con 20 soci volontari: costa poco, dura
   3 settimane e serve a collaudare procedura, test e strumenti.
2. Subito dopo, un **trial sulla creatina** di 8 settimane come "controllo di qualità":
   se il sistema di misura funziona, il risultato atteso è positivo.
3. Contattare il **corso di laurea in Scienze Motorie** più vicino per una convenzione (tesi,
   comitato etico, statistica).
4. Con 2 trial completati e ben documentati, proporre il **"MFC Performance Lab"** alle
   aziende di integratori.

---

## Fonti e riferimenti

- Maughan R.J. et al., *IOC consensus statement: dietary supplements and the high-performance athlete*, British Journal of Sports Medicine 2018
- Guest N.S. et al., *International Society of Sports Nutrition position stand: caffeine and exercise performance*, JISSN 2021
- Kreider R.B. et al., *ISSN position stand: safety and efficacy of creatine supplementation*, JISSN 2017
- Trexler E.T. et al., *ISSN position stand: beta-alanine*, JISSN 2015
- Jones A.M., *Dietary nitrate supplementation and exercise performance*, Sports Medicine 2014
- Hurst P. et al., *The placebo and nocebo effect on sports performance: a systematic review*, European Journal of Sport Science 2020
- Hopkins W.G., *Measures of reliability in sports medicine and science*, Sports Medicine 2000
- Regolamento UE 1924/2006 (claim nutrizionali e sulla salute); Regolamento UE 2016/679 (GDPR), art. 9
- Documenti collegati in questo repository: [integratori e molecole in sperimentazione](sperimentazioni-performance-nad-nadh-vitamina-c.md), [GLP-1 e muscolo](glp1-e-muscolo-programma-mfc.md)
