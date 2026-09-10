# Valutazione comparata — due certificati Cash Collect autocallable

**Barclays `XS3183930109`** (4 banche europee, cedola 11,64% p.a.)
vs **Vontobel `DE000BD2KYU6`** (3 blue chip italiane, cedola 7,20% p.a.)

> Analisi al **10 settembre 2026** su chiusure del 9 settembre 2026.
> Documento di ricerca a scopo informativo: **non è consulenza finanziaria**, non è
> un'offerta né una sollecitazione. Entrambi i prodotti sono classificati dagli emittenti
> come **"a complessità molto elevata"** e le schede sono riservate a investitori
> professionali. Prima di qualsiasi operazione fanno fede esclusivamente Termsheet,
> Final Terms e KID dell'emittente.

---

## 1. Sintesi esecutiva

| | **A — Barclays** | **B — Vontobel** |
|---|---|---|
| ISIN | XS3183930109 | DE000BD2KYU6 |
| Sottostanti | MPS, BBVA, Deutsche Bank, Société Générale | Enel, Eni, UniCredit |
| Cedola | 0,970%/mese — **11,64% p.a.** | 0,600%/mese — **7,20% p.a.** |
| Barriera cedola | 50% | 60% (ultima rilevazione 30%) |
| Barriera capitale | **40%** (europea, solo a scadenza) | **50%** (europea, solo a scadenza) |
| Autocall | da 03.05.2027, 100% → 50% (−1%/mese) | da 30.07.2027, 100% → 64,75% (−0,75%/mese) |
| Scadenza | 11.08.2031 (val. 04.08.2031) | 06.08.2031 (val. 30.07.2031) |
| Mercato | EuroTLX | SeDeX |
| **Fair value stimato (modello)** | **93,0** (range 93–96,5) | **90,4** (range 90,5–94,8) |
| Vita attesa (risk-neutral) | 2,90 anni | 3,36 anni |
| P(richiamo anticipato) | 64% | 55% |
| P(perdita in conto capitale) — RN | 32% | 36% |
| P(perdita in conto capitale) — *real world* | 20,5% | 18,6% |
| Cedola di equilibrio (FV = 100) | **15,4% p.a.** (paga 11,64%) | **10,5% p.a.** (paga 7,20%) |

**Conclusione operativa.** Nessuno dei due è conveniente a 100. Entrambi hanno un fair
value modellistico sotto la pari, ma **il certificato A offre un rapporto
cedola/rischio nettamente migliore**: paga il 62% di cedola in più a fronte di barriere
*più lontane* (40%/50% contro 50%/60%) e di una probabilità di perdita analoga.
Il certificato B, per contro, è **strutturalmente sotto-remunerato**: 7,20% p.a. per un
basket che contiene UniCredit al 28% di volatilità è circa 3,3 punti sotto l'equilibrio.

Il prezzo di ingresso conta più della struttura: **soglie indicative di acquisto sul
secondario ≤ 95 per A e ≤ 93 per B**.

---

## 2. Fotografia dei sottostanti (chiusure 09.09.2026)

### 2.1 Certificato A — Barclays (strike 03.08.2026, ~5 settimane di vita)

| Sottostante | Strike | Spot | Perf. da strike | Barriera cedola 50% | Barriera capitale 40% | Spazio residuo al capitale |
|---|---|---|---|---|---|---|
| Banca MPS | 11,576 € | ~11,61 € | **+0,3%** | 5,788 € | 4,630 € | −60,1% |
| BBVA | 24,680 € | ~25,06 € | **+1,5%** | 12,340 € | 9,872 € | −60,6% |
| Deutsche Bank | 32,195 € | 35,04 € | **+8,8%** | 16,098 € | 12,878 € | −63,2% |
| **Société Générale** | 83,090 € | **73,49 €** | **−11,6%** | 41,545 € | 33,236 € | **−54,8%** |

*Worst-of attuale: **Société Générale a 88,4% dello strike**.*

Il prezzo di BBVA è ricavato dall'ADR (29,08 USD, cambio EUR/USD 1,1605) e quello di MPS
dall'ADR BMPSY (13,47 USD): sono quindi **approssimazioni**, coerenti ma da verificare
sulle quotazioni di Borsa Italiana e BME.

Da notare: SocGen ha perso l'11,6% in cinque settimane, con due gap rilevanti
(18–19 agosto, da 82,14 a 77,02) e un minimo intraday a 70,29 il 27 agosto. **Non ci sono
stacchi di dividendo nel periodo**: è un ribasso di mercato, non un effetto tecnico.

### 2.2 Certificato B — Vontobel (strike 30.07.2026, ~6 settimane di vita)

| Sottostante | Strike | Spot | Perf. da strike | Barriera cedola 60% | Barriera capitale 50% | Spazio residuo al capitale |
|---|---|---|---|---|---|---|
| **Enel** | 9,835 € | **8,897 €** | **−9,5%** | 5,901 € | 4,918 € | **−44,7%** |
| Eni | 23,513 € | ~23,52 € | **+0,0%** | 14,108 € | 11,757 € | −50,0% |
| UniCredit | 80,160 € | 83,69 € | **+4,4%** | 48,096 € | 40,080 € | −52,1% |

*Worst-of attuale: **Enel a 90,5% dello strike**.*

Enel e UniCredit sono presi dalle linee XETRA (ENL.DEX, CRIN.DEX), Eni da Francoforte
(linea sottile, ultimo scambio 08.09). Il controllo di coerenza è buono: ENL.DEX chiudeva
a 9,849 € il 30.07.2026 contro uno strike fissato a 9,835 €.

### 2.3 Parametri di rischio stimati sui dati (100 sedute)

| | Volatilità realizzata annualizzata |
|---|---|
| Société Générale | **32,3%** |
| Deutsche Bank | **29,6%** |
| UniCredit | **27,2%** |
| Enel | **19,3%** |

**Matrice di correlazione (log-rendimenti giornalieri, 100 sedute comuni)**

| | DBK | GLE | ENL | UCG |
|---|---|---|---|---|
| **DBK** | 1,00 | 0,69 | 0,29 | 0,69 |
| **GLE** | 0,69 | 1,00 | 0,31 | 0,71 |
| **ENL** | 0,29 | 0,31 | 1,00 | 0,34 |
| **UCG** | 0,69 | 0,71 | 0,34 | 1,00 |

Il dato chiave per un *worst-of*: **le banche viaggiano a correlazione ~0,70 fra loro,
Enel a ~0,30 contro le banche**. Questo è il motivo economico per cui A può permettersi
di pagare il 62% in più di cedola pur avendo *quattro* sottostanti invece di tre.

---

## 3. Metodologia di valutazione

Simulazione Monte Carlo (400.000 traiettorie, moto browniano geometrico multivariato con
decomposizione di Cholesky), passo mensile allineato alle date di rilevazione effettive,
sconto ai flussi effettivi con lag di pagamento.

**Ipotesi (le più incerte sono i dividendi):**

| Parametro | Certificato A | Certificato B |
|---|---|---|
| Tasso privo di rischio EUR | 2,30% | 2,30% |
| Spread creditizio emittente | 70 bp (Barclays) | 90 bp (Vontobel) |
| Volatilità | MPS 33%, BBVA 27%, DBK 30%, GLE 32% | Enel 20%, Eni 23%, UCG 28% |
| Dividend yield | MPS 8,0%, BBVA 5,2%, DBK 3,0%, GLE 5,5% | Enel 5,6%, Eni 4,7%, UCG 5,2% |
| Osservazioni residue | 59 (ott. 2026 → ago. 2031) | 59 (set. 2026 → lug. 2031) |

La prima cedola di ciascun prodotto (03.09.2026 per A, 31.08.2026 per B) è già stata
rilevata con tutti i titoli sopra barriera ed è quindi esclusa dalla valutazione.

**Regole di payoff modellate fedelmente alle schede:**
- Effetto memoria pieno su entrambi.
- **A**: a scadenza, worst ≥ 50% → 100 + cedola; 40% ≤ worst < 50% → **100 senza cedola**
  (gradino di protezione che B non ha); worst < 40% → 100 × perf. peggiore.
- **B**: a scadenza la barriera cedola scende al **30%**, quindi worst ≥ 50% → 100 + cedola;
  30% ≤ worst < 50% → 100 × perf. peggiore **+ cedola e memoria**; worst < 30% → sola
  performance.

---

## 4. Risultati

### 4.1 Valutazione centrale

| | **A — Barclays** | **B — Vontobel** |
|---|---|---|
| **Fair value** | **92,97 €** (± 0,06) | **90,43 €** (± 0,04) |
| di cui PV gamba rimborso | 71,01 | 70,03 |
| di cui PV gamba cedolare | 21,94 | 20,43 |
| Vita attesa | 2,90 anni | 3,36 anni |
| P(autocall) totale | 64,4% | 55,0% |
| — entro 1 anno | 26,0% | 12,9% |
| — entro 2 anni | 42,6% | 30,9% |
| — entro 3 anni | 51,9% | 41,4% |
| P(arrivo a scadenza) | 35,6% | 45,0% |
| P(perdita capitale) | 31,6% | 36,1% |
| **Perdita media condizionata** | **−75,8%** | **−64,7%** |
| Cedole cumulate attese (nominali) | 22,88 € | 22,09 € |

Da leggere insieme: **A ha una probabilità di perdita più bassa ma una coda più profonda**
(−75,8% contro −64,7% quando la perdita si verifica). È la conseguenza diretta della
correlazione: quattro banche a 0,70 crollano insieme, e quando la barriera al 40% viene
rotta lo è di molto.

### 4.2 Analisi di sensibilità

| Scenario | A — fair value | A — P(perdita) | B — fair value | B — P(perdita) |
|---|---|---|---|---|
| **Centrale** | 92,97 | 31,6% | 90,43 | 36,1% |
| Volatilità +5 punti (skew/stress) | 87,35 | 36,6% | 83,32 | 42,8% |
| Correlazione +0,15 | **95,51** | 27,0% | **91,96** | 32,3% |
| Dividendi −1% | 94,8 | 29% | 92,7 | 32% |
| Dividendi −2% | **96,5** | 27% | **94,8** | 28% |
| Spot −20% su tutti | 78,88 | 52,0% | 75,11 | 62,0% |

**Il driver dominante è il dividend yield.** Su cinque anni un'ipotesi di rendimento da
dividendo del 5–8% comprime pesantemente i forward e quindi il valore. Se l'emittente
sconta dividendi ~2 punti più bassi dei miei, i fair value salgono a **96,5 e 94,8**: il
gap effettivo rispetto a 100 sarebbe allora nell'ordine del 3,5–5%, coerente con i margini
tipici di collocamento su questa classe di prodotti. **Il range 93–96,5 (A) e 90,5–94,8 (B)
va quindi letto come la stima onesta, non il solo punto centrale.**

Nota controintuitiva ma importante: **una correlazione più alta fa salire il valore**
(+2,5 punti su A). Nel *worst-of* la diversificazione è nemica del detentore. La
concentrazione settoriale del certificato A è quindi in parte già pagata dalla cedola.

### 4.3 Probabilità "real world" (per la pianificazione, non per il prezzo)

Le probabilità risk-neutral servono a prezzare, non a decidere. Ripetendo la simulazione
con un premio al rischio azionario del 5%:

| | A — Barclays | B — Vontobel |
|---|---|---|
| P(richiamo anticipato) | 76% | 74% |
| Vita attesa | 2,50 anni | 2,77 anni |
| P(perdita in conto capitale) | **20,5%** | **18,6%** |
| Payoff nominale medio | **+7,0 €** | **+7,6 €** |

Circa **una possibilità su cinque di perdere capitale** su entrambi, in uno scenario
benigno di mercato. Non è un prodotto "obbligazionario".

### 4.4 Cedola di equilibrio

| | Cedola pagata | Cedola che porterebbe il FV a 100 | Gap |
|---|---|---|---|
| **A — Barclays** | 11,64% p.a. | **15,38% p.a.** | **−3,74 pt** |
| **B — Vontobel** | 7,20% p.a. | **10,52% p.a.** | **−3,32 pt** |

Il gap in punti annui è simile, ma in termini *relativi* B è molto più penalizzato: manca
il 32% della cedola equa contro il 24% di A.

---

## 5. Analisi strutturale e gestionale

### 5.1 La condizione di richiamo è il vero nodo

Entrambi i prodotti richiedono, alla prima data utile, che **tutti** i sottostanti siano
sopra il 100% dello strike. Oggi:

- **A**: SocGen deve recuperare **+13,1%** (da 73,49 a 83,09 €) entro il 03.05.2027.
- **B**: Enel deve recuperare **+10,5%** (da 8,897 a 9,835 €) entro il 30.07.2027.

In entrambi i casi **il richiamo anticipato dipende interamente dal titolo in ritardo**,
non dalla salute media del basket. Deutsche Bank a +8,8% e UniCredit a +4,4% non aiutano.
È il motivo per cui la probabilità di richiamo entro un anno è solo del 26% (A) e del 13% (B).

Il meccanismo di **autocall decrescente** è la vera protezione contro l'immobilizzo: la
soglia scende di 1 punto al mese su A e di 0,75 su B. A dicembre 2029 A richiama con i
titoli a −68% dallo strike; B, più lento, richiede ancora −78%. **A si "libera" più in
fretta**, ed è la ragione principale della differenza di vita attesa (2,90 vs 3,36 anni).

### 5.2 Confronto delle strutture, voce per voce

**A favore del certificato A**
- Barriere assolute più lontane: capitale 40% contro 50%, cedola 50% contro 60%.
- **Gradino di protezione**: fra 40% e 50% A rimborsa il nominale pieno. B in quella
  fascia rimborsa già in perdita (a −45% del worst, B paga 55,60 €; A paga 100 €).
- Autocall più precoce (maggio 2027 vs luglio 2027) e più rapido nel decadere.
- Emittente più solido (vedi 5.4).
- Cedola 11,64% vs 7,20%: il differenziale di 4,44 punti annui su 5 anni vale ~22 punti
  nominali di nominale.

**A favore del certificato B**
- Basket genuinamente diversificato (utility + oil + banca, correlazioni 0,34–0,42) contro
  una scommessa monosettoriale pura.
- Volatilità del basket sensibilmente più bassa (Enel al 19,3%).
- **Barriera cedola finale al 30%**: anche in uno scenario di perdita fino a −70% si incassa
  l'ultima cedola con tutta la memoria. Un'opzione che A non ha, ma di valore modesto
  (~0,3–0,5 punti nel modello).
- SeDeX è tipicamente più liquido di EuroTLX per il retail italiano.

**Il verdetto**: il gradino 40–50% di A e le barriere più lontane superano il vantaggio di
diversificazione di B. B paga meno *e* protegge meno in termini di distanza dalla barriera.

### 5.3 Concentrazione settoriale — il rischio non prezzato

Il certificato A è, in sostanza, **una put venduta a leva sul settore bancario europeo**.
I quattro nomi condividono le stesse esposizioni: curva dei tassi, qualità del credito,
spread sovrani (BTP per MPS, OAT per SocGen), requisiti regolamentari, rischio M&A.

Il modello, con correlazioni fisse a 0,55–0,70, **sottostima questo rischio**: in una crisi
bancaria vera la correlazione va a 1 e la coda si materializza tutta insieme. La sensibilità
"correlazione +0,15" mostra che il *prezzo* migliora, ma è un miglioramento di valore
atteso, non una riduzione del rischio di rovina.

MPS merita una menzione a sé: dopo l'operazione su Mediobanca è un titolo con dinamiche
societarie proprie, storicamente il più volatile del gruppo e con il payout più aggressivo
(dividend yield stimato all'8%). È il nome che più può muoversi indipendentemente dagli altri.

### 5.4 Rischio emittente

| | Barclays | Vontobel |
|---|---|---|
| Natura | G-SIB britannica, bilancio > £1.500 mld | Banca privata svizzera, ~CHF 30 mld di attivi |
| Rating senior (indicativo) | A / A+ | A |
| CDS | liquido, osservabile | non liquido |
| Regime di risoluzione | UK, con MREL e bail-in strutturato | Svizzero — post Credit Suisse la prevedibilità è, di fatto, minore |
| Seniority del certificato | senior unsecured | senior unsecured |

**Nessuno dei due certificati è garantito, collateralizzato o coperto da fondi di tutela.**
In caso di default dell'emittente si è creditori chirografari e il valore dei sottostanti
è irrilevante. Il differenziale di spread applicato (70 bp vs 90 bp) è probabilmente
*generoso* verso Vontobel: per un emittente di quella dimensione un premio di 120–150 bp
sarebbe più difendibile, il che abbasserebbe ulteriormente il fair value di B di circa
1–1,5 punti.

### 5.5 Fiscalità italiana — un vantaggio strutturale spesso trascurato

Per i certificati di investimento, **sia le cedole sia le plusvalenze sono classificate
come "redditi diversi"** (aliquota 26%). La conseguenza gestionale è rilevante:

- Le **minusvalenze pregresse** (da azioni, ETF venduti in perdita, altri certificati)
  possono essere **compensate con le cedole** incassate.
- Al contrario, le cedole obbligazionarie e i proventi dei fondi sono "redditi di capitale"
  e **non** sono compensabili.

Un investitore con uno zainetto fiscale di minusvalenze in scadenza ha quindi un motivo
concreto e quantificabile per preferire un certificato a cedola alta: **su A, 11,64 € di
cedola annua compensata al 26% vale 3,03 € l'anno di imposta risparmiata**, cioè oltre
3 punti percentuali di rendimento aggiuntivo netto. Su un orizzonte di vita attesa di
2,9 anni sono ~8,8 punti. Questo elemento, da solo, può ribaltare il giudizio sul fair
value negativo del modello.

Va verificato con il proprio intermediario il trattamento specifico e la capienza dello
zainetto fiscale (le minusvalenze scadono nel quarto anno successivo).

### 5.6 Liquidità e collocamento in portafoglio

- Il mercato secondario è **animato dal market maker**, non da scambi fra investitori.
  Spread denaro/lettera tipici 0,5–1,0% su questa classe; in stress si allargano proprio
  quando serve uscire.
- Entrambi sono classificati **"a complessità molto elevata"**. La comunicazione Consob
  del 2014 sui prodotti complessi ne sconsiglia la distribuzione alla clientela retail:
  la dicitura "riservato a investitori professionali" sulle schede non è formale.
- **Errore di allocazione da evitare**: contabilizzare questi strumenti nel comparto
  obbligazionario perché "pagano una cedola". Il profilo di rischio è azionario, con
  upside troncato al nominale e downside pieno. Vanno dimensionati contro il budget di
  rischio *equity*.
- **Rischio di reinvestimento**: nel 64% dei casi (A) il prodotto viene richiamato a 100.
  La cedola alta si incassa per intero solo negli scenari in cui il mercato scende senza
  rompere la barriera — cioè esattamente quelli in cui il resto del portafoglio soffre.
  È un profilo *short volatility*, non un flusso cedolare stabile.

---

## 6. Livelli da monitorare

### Certificato A — Barclays

| Evento | Titolo determinante | Livello | Distanza da oggi |
|---|---|---|---|
| Perdita della cedola mensile | **Société Générale** | 41,545 € | −43,5% |
| Perdita del capitale (a scadenza) | **Société Générale** | 33,236 € | −54,8% |
| Primo richiamo (03.05.2027) | **Société Générale** | 83,090 € | **+13,1%** |

### Certificato B — Vontobel

| Evento | Titolo determinante | Livello | Distanza da oggi |
|---|---|---|---|
| Perdita della cedola mensile | **Enel** | 5,901 € | −33,7% |
| Perdita del capitale (a scadenza) | **Enel** | 4,918 € | −44,7% |
| Primo richiamo (30.07.2027) | **Enel** | 9,835 € | **+10,5%** |

Entrambe le barriere sono **europee** (valutate solo alla data di valutazione finale): un
crollo intermedio, anche profondo, non pregiudica il rimborso se il titolo recupera entro
il 2031. È una caratteristica materialmente favorevole rispetto alle barriere americane.

---

## 7. Raccomandazioni operative

1. **Non acquistare a 100.** Il fair value modellistico è 93–96,5 (A) e 90,5–94,8 (B).
   Prezzi di ingresso indicativi: **≤ 95 per A, ≤ 93 per B**.
2. **Fra i due, A è preferibile** su base rischio/rendimento: cedola superiore del 62%,
   barriere più lontane, gradino di protezione 40–50%, emittente più solido, vita attesa
   più corta. Il prezzo da pagare è la concentrazione monosettoriale bancaria.
3. **B è difficile da giustificare a 100.** 7,20% p.a. per una barriera al 50% su un basket
   con UniCredit al 28% di volatilità è circa 3,3 punti sotto l'equilibrio, e il premio
   creditizio Vontobel è probabilmente sottostimato. Diventa interessante solo sotto 93.
4. **Sfruttare la leva fiscale.** Con minusvalenze pregresse in scadenza, la compensabilità
   delle cedole vale oltre 3 punti annui netti su A: è la singola variabile che più può
   modificare il giudizio.
5. **Dimensionare come equity**, non come obbligazione. Suggerimento prudenziale: non oltre
   il 5% del portafoglio su un singolo certificato worst-of e non oltre il 15% sull'intera
   classe, tenendo conto della sovrapposizione settoriale (A e B condividono l'esposizione
   bancaria via UniCredit/MPS/SocGen/DBK/BBVA — comprarli entrambi **non** diversifica
   quanto sembra).
6. **Monitoraggio.** SocGen per A ed Enel per B sono i soli titoli che contano oggi.
   Un ulteriore −20% del *worst-of* porta il fair value a ~79 (A) e ~75 (B) e la probabilità
   di perdita a 52% e 62%: il profilo si deteriora in modo fortemente non lineare.

---

## 8. Limiti dell'analisi

- **Prezzi**: BBVA e MPS derivati da ADR in dollari, Eni da una linea di Francoforte poco
  scambiata. Da verificare sulle quotazioni ufficiali di BME e Borsa Italiana.
- **Dividendi**: stimati, non presi da una curva di dividendi impliciti. È il parametro a
  cui il risultato è più sensibile (±2 punti di FV per punto di yield).
- **Volatilità**: realizzata a 100 sedute, non implicita. Per un prodotto a 5 anni con
  barriere al 40–50% conta la volatilità implicita *deep out-of-the-money*, sistematicamente
  più alta per effetto dello skew. Lo scenario "vol +5 punti" è probabilmente più realistico
  del centrale per la componente di protezione.
- **Modello**: Black-Scholes multivariato con volatilità e correlazione costanti. Non cattura
  salti, volatilità stocastica né il collasso delle correlazioni verso 1 in regime di crisi —
  tutti effetti che penalizzano il detentore.
- **Volatilità di MPS, BBVA ed Eni**: stimate per analogia settoriale, non calcolate sui dati.
