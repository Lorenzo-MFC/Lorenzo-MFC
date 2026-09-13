# Guida all'investimento in certificati Cash Collect autocallable

**Analisi di prodotto, rendimenti, costi e regole operative**
Casi di studio: **Barclays `XS3183930109`** e **Vontobel `DE000BD2KYU6`**

> Documento operativo aggiornato al **13 settembre 2026**, costruito sulle chiusure del
> 9 settembre 2026. Complementare a
> [`valutazione-certificati-barclays-xs3183930109-vontobel-de000bd2kyu6.md`](valutazione-certificati-barclays-xs3183930109-vontobel-de000bd2kyu6.md),
> che contiene la valutazione di fair value: qui si parte da quei risultati per rispondere
> alla domanda pratica *quanto rende, quanto costa, cosa devo sapere prima di firmare*.
>
> **Non è consulenza finanziaria**, non è un'offerta né una sollecitazione al pubblico
> risparmio. Entrambi i prodotti sono classificati dagli emittenti **"a complessità molto
> elevata"**. Prima di qualsiasi operazione fanno fede esclusivamente Termsheet, Final Terms
> e KID dell'emittente.

---

## 1. La pagina che conta

Se si legge una sola tabella, è questa: **il rendimento atteso netto**, dopo imposte e costi,
confrontato con l'alternativa priva di rischio.

| Al prezzo di 100 | **A — Barclays** | **B — Vontobel** | Conto deposito 6 mesi |
|---|---|---|---|
| Cedola facciale | 11,64% p.a. | 7,20% p.a. | 3,25% lordo |
| **Rendimento atteso netto** *(senza minusvalenze)* | **2,74% p.a.** | **2,04% p.a.** | **2,21% p.a.** |
| **Rendimento atteso netto** *(con minusvalenze da compensare)* | **7,68% p.a.** | **5,11% p.a.** | 2,21% p.a. |
| Probabilità di perdere denaro | **20,5%** | **18,6%** | 0% (FITD fino a 100k) |
| Probabilità di fare peggio del deposito | **20,6%** | **18,6%** | — |
| Capitale protetto | no | no | sì |

*Rendimenti attesi da simulazione Monte Carlo in misura reale (premio al rischio azionario
+5%), al netto di imposta 26%, bollo 0,20% annuo e commissioni. Il dato del conto deposito
proviene dalla [ricerca Crédit Agricole](credit-agricole-prodotti-finanziari-conti-deposito.md)
già presente in questo repository.*

**Tre conclusioni che cambiano la decisione:**

1. **La cedola facciale non è il rendimento.** L'11,64% di A diventa un rendimento atteso
   netto del **2,74%**. Il divario non è un artificio contabile: è la probabilità di perdita
   che si porta via la differenza.
2. **Il certificato B, comprato a 100 da chi non ha minusvalenze, rende meno di un conto
   deposito** (2,04% contro 2,21%) *e in più può far perdere il capitale nel 18,6% dei casi*.
   È un esito dominato: nessun investitore razionale dovrebbe accettarlo.
3. **La fiscalità vale più della struttura.** Passare da "senza minusvalenze" a "con
   minusvalenze" aggiunge **+4,9 punti annui** su A e **+3,1** su B. È la singola leva più
   potente a disposizione dell'investitore, e non dipende dal mercato.

---

## 2. Anatomia del prodotto: cosa si compra davvero

Un Cash Collect autocallable non è un titolo: è un **pacchetto di tre contratti** venduto
in blocco. Scomponendolo con il modello si vede esattamente per cosa si stanno pagando 100 euro.

### 2.1 Le tre gambe

| Componente | Cert. A | Cert. B | Che cos'è |
|---|---|---|---|
| **(+) Obbligazione zero coupon dell'emittente** | 91,81 | 89,91 | Promessa di 100 euro alla data di uscita, scontata al tasso privo di rischio **più lo spread creditizio dell'emittente** |
| **(+) Strip di opzioni digitali con memoria** | 21,91 | 20,44 | 59 opzioni binarie mensili: pagano la cedola se il peggiore dei sottostanti è sopra barriera |
| **(−) Put down-and-in worst-of venduta all'emittente** | −20,54 | −19,97 | **Questo è il prodotto.** Si vende all'emittente il diritto di consegnare il titolo peggiore se rompe la barriera |
| **(=) Valore teorico** | **93,18** | **90,38** | |
| (−) Prezzo di collocamento | 100,00 | 100,00 | |
| **(=) Margine dell'emittente** | **−6,82** | **−9,62** | |

*Verifica di robustezza: questa scomposizione usa una seconda implementazione indipendente
del modello, con calendario a date reali anziché a mesi di 30,44 giorni. I fair value
ottenuti (93,18 e 90,38) coincidono entro 0,3 punti con quelli della valutazione originale
(92,91 e 90,28). Il risultato non dipende dai dettagli implementativi.*

### 2.2 La lettura economica

**Il cliente non compra un'obbligazione che paga l'11,64%. Vende un'assicurazione contro il
crollo di quattro banche europee e viene pagato in cedole per il premio.**

La put venduta vale **20,5 punti su A e 20,0 su B**: è circa un quinto del capitale investito.
È ciò che consente all'emittente di promettere una cedola quattro volte superiore al tasso
privo di rischio. Non c'è alchimia finanziaria — c'è un rischio trasferito dall'emittente al
cliente, e la cedola ne è il prezzo.

Da qui discendono tre proprietà che sorprendono chi tratta questi strumenti come obbligazioni:

- **L'upside è troncato.** Qualunque cosa facciano i sottostanti, non si riceve mai più di
  100 più le cedole. Se le quattro banche raddoppiano, il certificato viene richiamato a 100.
- **Il downside è pieno.** Sotto barriera si segue il titolo peggiore fino a zero.
- **Si guadagna quando non succede niente.** Il profilo è *short volatility*: il migliore
  scenario possibile è un mercato fermo o in lieve rialzo.

### 2.3 Perché "worst-of" è la parola più importante della scheda

Tutti i livelli — cedola, barriera, richiamo — si misurano **sul peggiore** dei sottostanti,
non sulla media. Aggiungere un sottostante non diversifica: **peggiora il prodotto**.

Con quattro titoli servono quattro successi contemporanei per essere richiamati, e basta un
fallimento per perdere il capitale. È il motivo contro-intuitivo per cui, nella valutazione,
**alzare la correlazione fa salire il valore del certificato** (+2,5 punti su A per
+0,15 di correlazione): titoli che si muovono insieme rendono meno probabile che *uno solo*
sprofondi.

> **Regola pratica.** A parità di cedola, un certificato su 3 sottostanti vale più di uno su
> 5. Se un collocatore presenta il numero di sottostanti come "maggiore diversificazione",
> sta descrivendo il prodotto al contrario.

---

## 3. Rendimenti

### 3.1 Se viene richiamato: il rendimento è piatto

Al richiamo anticipato tutti i sottostanti sono sopra il 100% dello strike, quindi sopra la
barriera cedola: **l'effetto memoria restituisce ogni cedola mai saltata**. Chi viene
richiamato ha sempre incassato il 100% delle cedole maturate.

**Certificato A — Barclays** (cedola 0,97%/mese)

| Data di richiamo | Mesi | Cedole incassate | Totale | IRR @100 | IRR @97 | IRR @95 | IRR @93 |
|---|---|---|---|---|---|---|---|
| 03.05.2027 *(prima data utile)* | 8 | 7,76 | 107,76 | **12,59%** | 18,17% | 22,15% | 26,35% |
| 03.05.2028 | 20 | 19,40 | 119,40 | 12,39% | 14,68% | 16,28% | 17,94% |
| 03.05.2029 | 32 | 31,04 | 131,04 | 12,36% | 13,86% | 14,91% | 15,98% |
| 03.05.2030 | 44 | 42,68 | 142,68 | 12,34% | 13,49% | 14,29% | 15,12% |
| 04.08.2031 *(scadenza, sopra barriera)* | 59 | 57,23 | 157,23 | 12,32% | 13,24% | 13,87% | 14,53% |

**Certificato B — Vontobel** (cedola 0,60%/mese)

| Data di richiamo | Mesi | Cedole incassate | Totale | IRR @100 | IRR @97 | IRR @95 | IRR @93 |
|---|---|---|---|---|---|---|---|
| 30.07.2027 *(prima data utile)* | 11 | 6,60 | 106,60 | **7,63%** | 11,48% | 14,18% | 17,02% |
| 30.07.2028 | 23 | 13,80 | 113,80 | 7,53% | 9,39% | 10,68% | 12,02% |
| 30.07.2029 | 35 | 21,00 | 121,00 | 7,50% | 8,76% | 9,63% | 10,53% |
| 30.07.2030 | 47 | 28,20 | 128,20 | 7,49% | 8,46% | 9,13% | 9,81% |
| 30.07.2031 *(scadenza, sopra barriera)* | 59 | 35,40 | 135,40 | 7,49% | 8,28% | 8,83% | 9,40% |

**Due letture operative.**

- **Comprato a 100, il momento del richiamo è irrilevante**: l'IRR resta 12,3–12,6% (A) e
  7,5–7,6% (B) qualunque sia la data. Non c'è nulla da "cronometrare".
- **Comprato sotto la pari, il richiamo precoce diventa un moltiplicatore**: a 93, un richiamo
  a maggio 2027 rende il 26,35% annuo contro il 14,53% se arriva a scadenza. **Lo sconto sul
  prezzo è l'unica variabile realmente sotto controllo dell'acquirente**, e vale di più
  quanto prima il prodotto si chiude.

### 3.2 Se arriva a scadenza: gli scenari veri

Solo il 35% (A) e il 45% (B) dei percorsi arriva al 2031. Ecco cosa succede in quei casi,
con le cedole effettivamente incassate lungo il cammino calcolate dalla simulazione (non
ipotizzate).

**Certificato A — barriera capitale 40%, barriera cedola 50%**

| Worst-of finale | Peso | Cedole incassate | Rimborso | Totale | Risultato su 100 |
|---|---|---|---|---|---|
| 50% – 100% | 0,4% | 57,23 | 100,00 | 157,23 | **+57,23** |
| **40% – 50%** | **3,6%** | 36,14 | **100,00** | 136,14 | **+36,14** |
| 20% – 40% | 21,1% | 27,58 | 28,92 | 56,50 | **−43,50** |
| 0% – 20% | 10,4% | 19,09 | 14,72 | 33,81 | **−66,19** |

**Certificato B — barriera capitale 50%, barriera cedola 60% (30% all'ultima rilevazione)**

| Worst-of finale | Peso | Cedole incassate | Rimborso | Totale | Risultato su 100 |
|---|---|---|---|---|---|
| 60% – 100% | 1,6% | 35,40 | 100,00 | 135,40 | **+35,40** |
| **50% – 60%** | **7,3%** | 35,40 | **100,00** | 135,40 | **+35,40** |
| 30% – 50% | 25,7% | 35,40 | 39,83 | 75,23 | **−24,77** |
| 0% – 30% | 10,3% | 12,40 | 23,86 | 36,26 | **−63,74** |

**Cosa mostrano queste tabelle e non la scheda prodotto.**

- **La fascia 40–50% di A vale davvero.** In quel 3,6% di scenari il capitale torna intero
  mentre B, nella fascia equivalente, sarebbe già in perdita. È il "gradino di protezione".
- **La barriera cedola finale al 30% di B funziona come pubblicizzato**: nella fascia 30–50%
  l'investitore recupera **tutte e 59 le cedole** (35,40 punti) grazie alla memoria, il che
  trasforma un −60% del sottostante in un −24,77% di portafoglio. È la caratteristica
  migliore del certificato B.
- **Sotto barriera le cedole si fermano presto.** Nello scenario peggiore di A si incassano
  19 punti di cedole su 57 possibili: la memoria non aiuta se il titolo non risale mai sopra
  il 50%. **Non si può contare sulle cedole come ammortizzatore nei crolli.**

### 3.3 Il salto alla barriera: il rischio che nessun grafico mostra

La barriera non è un pendio: è un **precipizio**. Un centesimo di differenza nella chiusura
di un solo titolo, in un solo giorno di agosto 2031, cambia l'esito di decine di punti.

| | Worst-of a **40,0%** | Worst-of a **39,9%** | Differenza |
|---|---|---|---|
| **Cert. A** — rimborso | 100,00 | 39,90 | |
| + cedole medie | 27,6 | 27,6 | |
| **= risultato** | **+27,6** | **−32,5** | **60,1 punti** |

| | Worst-of a **50,0%** | Worst-of a **49,9%** | Differenza |
|---|---|---|---|
| **Cert. B** — rimborso | 100,00 | 49,90 | |
| + cedole medie | 35,4 | 35,4 | |
| **= risultato** | **+35,4** | **−14,7** | **50,1 punti** |

Una sola attenuante, ma sostanziale: **entrambe le barriere sono europee**, osservate
*solo* alla data di valutazione finale. Un crollo intermedio, anche del 70%, non pregiudica
nulla se il titolo recupera entro il 2031. Con una barriera americana (osservazione continua)
lo stesso prodotto varrebbe parecchi punti in meno. **Verificare sempre questo punto nel KID:
è la differenza fra un rischio gestibile e un rischio che scatta una notte qualunque.**

### 3.4 La distribuzione completa: media e mediana raccontano cose opposte

Simulazione in misura reale, prezzo di carico 100, rendimenti lordi:

| | **A — Barclays** | **B — Vontobel** |
|---|---|---|
| IRR **mediana** | **+12,37%** | **+7,51%** |
| IRR **media** | **+6,02%** | **+4,31%** |
| 5° percentile | −23,26% | −9,00% |
| 25° percentile | +11,63% | +7,36% |
| 75° percentile | +12,52% | +7,58% |
| 95° percentile | +12,59% | +7,63% |
| P(rendimento negativo) | 20,5% | 18,6% |

**La distribuzione è bimodale, non a campana.** Nell'80% dei casi si incassa esattamente la
cedola e nulla di più — mediana e 75° percentile quasi coincidono. Nel restante 20% si perde
in media il 65% del capitale. **La media è schiacciata verso il basso da una coda che non si
vede mai finché non arriva.**

Questa è la ragione per cui i certificati Cash Collect producono track record eccellenti per
anni e poi un anno catastrofico: **non stanno generando alfa, stanno accumulando un premio
assicurativo non ancora pagato.**

> **Errore da evitare.** Giudicare questi strumenti dai rendimenti passati. Cinque anni di
> cedole incassate non dicono nulla sulla convenienza: dicono solo che l'evento assicurato
> non si è verificato.

---

## 4. Costi: quello che si paga e quello che non si vede

### 4.1 Lo stack completo, su 10.000 euro di nominale a prezzo 100

**Certificato A — Barclays** *(vita attesa 2,89 anni)*

| Voce | Punti | % annuo | Su 10.000 € | Visibile in rendiconto? |
|---|---|---|---|---|
| **Margine implicito di strutturazione** (100 − fair value) | **7,09** | **2,45%** | **709 €** | **No** |
| Spread denaro/lettera in acquisto (metà di 0,75%) | 0,38 | 0,13% | 38 € | No |
| Commissione di negoziazione (0,20%) | 0,20 | 0,07% | 20 € | Sì |
| Imposta di bollo (0,20% annuo sul dossier) | 0,58 | 0,20% | 58 € | Sì |
| **TOTALE COSTO DI POSSESSO** | **8,24** | **2,85%** | **824 €** | **86% invisibile** |

**Certificato B — Vontobel** *(vita attesa 3,37 anni)*

| Voce | Punti | % annuo | Su 10.000 € | Visibile in rendiconto? |
|---|---|---|---|---|
| **Margine implicito di strutturazione** | **9,72** | **2,88%** | **972 €** | **No** |
| Spread denaro/lettera in acquisto | 0,38 | 0,11% | 38 € | No |
| Commissione di negoziazione | 0,20 | 0,06% | 20 € | Sì |
| Imposta di bollo | 0,67 | 0,20% | 67 € | Sì |
| **TOTALE COSTO DI POSSESSO** | **10,97** | **3,25%** | **1.097 €** | **89% invisibile** |

### 4.2 Tre osservazioni che contano più della tabella

**Il costo vero non compare in nessun documento come "costo".** Il margine di strutturazione
si manifesta solo come differenza fra il prezzo di emissione (100) e il valore teorico
(93 e 90). Il KID lo espone sotto forma di *riduzione del rendimento*, mai come commissione,
e il rendiconto dell'intermediario non lo vedrà mai. **Rappresenta l'86–89% del costo totale.**

**Il confronto con i prodotti sostitutivi è impietoso.**

| Strumento | Costo annuo |
|---|---|
| ETF azionario europeo (TER tipico) | 0,20% |
| Fondo comune azionario attivo | 1,80% |
| **Certificato A** | **2,85%** |
| **Certificato B** | **3,25%** |

Il certificato costa **14–16 volte un ETF** e circa il doppio di un fondo attivo, per
un'esposizione a quattro titoli che si possono comprare direttamente.

**Il costo si diluisce se il prodotto vive a lungo, ma la vita è decisa dall'emittente.**
Il margine è un importo fisso in punti: spalmato su 2,89 anni pesa il 2,45% annuo, su 5 anni
peserebbe l'1,42%. Ma il richiamo anticipato non dipende dall'investitore — **e proprio gli
scenari favorevoli (richiamo precoce) sono quelli in cui il costo annualizzato è più alto.**
Richiamato alla prima data utile (8 mesi), il solo margine implicito vale **10,6% annualizzato**.

### 4.3 Il costo di uscire prima

Vendere sul secondario prima del richiamo espone a tre penalizzazioni simultanee:

1. **Lo spread denaro/lettera**, 0,5–1,0% in condizioni normali, che **si allarga proprio
   quando si vuole uscire** (mercati in tensione).
2. **Il prezzo di mercato segue il modello, non le cedole incassate.** Se il worst-of scende
   al 60% dello strike, il certificato quota 70–75 anche se ha pagato tutte le cedole.
3. **Il market maker è l'unica controparte.** Non esiste un mercato fra investitori: il
   prezzo lo fa l'emittente, che conosce il valore meglio del venditore.

> **Conseguenza operativa: questi strumenti vanno comprati solo con denaro che si può
> immobilizzare fino al 2031.** La liquidabilità formale — sono quotati e si vendono in
> qualsiasi momento — non è liquidità economica.

---

## 5. Fiscalità: la leva più potente e la più trascurata

### 5.1 La regola

I certificati di investimento generano **"redditi diversi"** (art. 67 TUIR), aliquota 26%,
sia sulle cedole sia sulle plusvalenze. Le obbligazioni e i fondi generano invece **"redditi
di capitale"**, che **non sono compensabili** con le minusvalenze.

| | Certificati | Obbligazioni / fondi |
|---|---|---|
| Natura della cedola | Reddito **diverso** | Reddito **di capitale** |
| Aliquota | 26% | 26% (12,5% titoli di Stato) |
| **Compensabile con minusvalenze pregresse** | **Sì** | **No** |

### 5.2 Quanto vale, in euro

Su un investimento di 10.000 euro nel certificato A:

| | Senza minusvalenze | Con minusvalenze capienti |
|---|---|---|
| Cedola annua lorda | 1.164 € | 1.164 € |
| Imposta 26% | −303 € | **0 €** |
| Cedola annua netta | 861 € | **1.164 €** |
| **Rendimento atteso netto** | **2,74%** | **7,68%** |
| **Differenziale** | | **+4,94 punti annui** |

Su B il differenziale è di **+3,07 punti annui** (da 2,04% a 5,11%).

### 5.3 Le condizioni per usarla davvero

- Le minusvalenze devono essere **già realizzate** e registrate nello "zainetto fiscale"
  presso l'intermediario. Le perdite su posizioni ancora aperte non contano.
- Scadono nel **quarto anno successivo** a quello di realizzo. Uno zainetto in scadenza a
  fine 2026 è un motivo concreto per agire ora, non un vantaggio generico.
- Servono in **regime amministrato** presso lo stesso intermediario, oppure va gestita la
  compensazione in dichiarazione (regime dichiarativo).
- **Verificare la capienza.** Non basta il conto "cedola annua × anni": va usato il flusso
  cedolare *atteso*, che sconta le rilevazioni sotto barriera e il richiamo anticipato. Su
  10.000 euro servono circa **2.220 euro di minusvalenze su A** e **1.930 euro su B** per
  azzerare l'imposta sull'intero flusso.

> **Questa è la sola variabile che può ribaltare il giudizio negativo sul fair value.**
> Un certificato che vale 93 comprato a 100 è un cattivo affare; lo stesso certificato che
> converte 2.220 euro di minusvalenze altrimenti perse in credito d'imposta effettivo può
> non esserlo. Il calcolo va fatto sul portafoglio complessivo, non sul singolo strumento.

---

## 6. I dieci rischi, in ordine di importanza

| # | Rischio | Perché conta qui | Come si misura |
|---|---|---|---|
| 1 | **Worst-of** | Basta un titolo sotto barriera per perdere tutto il capitale | SocGen (A) −54,8% dalla barriera; Enel (B) −44,6% |
| 2 | **Concentrazione settoriale** | A è di fatto una put venduta sul settore bancario europeo: 4 nomi, correlazione ~0,70 | In una crisi bancaria la correlazione va a 1 e il modello sottostima la coda |
| 3 | **Emittente** | Credito senior unsecured, **nessuna garanzia, nessun FITD** | Barclays G-SIB (A/A+); Vontobel ~CHF 30 mld di attivi |
| 4 | **Salto alla barriera** | 60 punti di differenza per uno 0,1% di movimento | §3.3 |
| 5 | **Liquidità** | Solo il market maker fa prezzo; spread che si allarga sotto stress | 0,5–1,0%, in stress oltre |
| 6 | **Costo implicito** | 7–10 punti pagati all'ingresso e invisibili | §4.1 |
| 7 | **Reinvestimento** | Nel 65–75% dei casi richiamato a 100 e va reinvestito a condizioni ignote | Vita attesa 2,50 anni (A), 2,78 (B) |
| 8 | **Modello** | Volatilità e correlazione costanti, nessun salto | Vol +5 punti → fair value −5,6 (A), −7,0 (B) |
| 9 | **Dividendi** | Parametro più incerto e più influente | ±2 punti di fair value per punto di yield |
| 10 | **Classificazione** | "Complessità molto elevata", scheda per investitori professionali | Comunicazione Consob 2014 |

### Il rischio numero 11: l'errore di allocazione

**Il più frequente e il più costoso.** Contabilizzare questi strumenti nel comparto
obbligazionario perché "pagano una cedola".

Il profilo di rischio è **azionario con upside troncato**: si prende tutta la discesa e
nessuna salita. Vanno dimensionati contro il budget di rischio *equity*, mai contro quello
obbligazionario. Un portafoglio "60/40" che mette i certificati nel 40 non è un 60/40:
è un 75/25 mascherato.

**Corollario:** comprare A *e* B non diversifica. I due basket condividono l'esposizione
bancaria (MPS, SocGen, Deutsche Bank, BBVA da un lato; UniCredit dall'altro). In una crisi
bancaria europea rompono la barriera insieme.

---

## 7. Come si investe, in pratica

### 7.1 Prima di comprare — le nove verifiche

| # | Cosa verificare | Dove | Valore atteso in questi due casi |
|---|---|---|---|
| 1 | **Tipo di barriera: europea o americana** | KID / Final Terms | **Europea** (solo a scadenza) — da confermare |
| 2 | **Borsa di riferimento di ogni sottostante** | Final Terms | A: Xetra e Parigi. B: Borsa Italiana |
| 3 | **Effetto memoria presente** | Termsheet | Sì su entrambi |
| 4 | **Livello e passo dell'autocall decrescente** | Termsheet | A: −1%/mese da 05.2027. B: −0,75%/mese da 07.2027 |
| 5 | **Barriera cedola all'ultima rilevazione** | Termsheet | A: resta 50%. B: **scende a 30%** |
| 6 | **Seniority e rating dell'emittente** | KID | Senior unsecured, non garantito |
| 7 | **Spread denaro/lettera attuale** | Book del mercato | ≤ 1% accettabile; oltre, rinunciare |
| 8 | **Indicatore di rischio SRI del KID** | KID, prima pagina | Atteso 6 su 7 |
| 9 | **Capienza dello zainetto fiscale** | Estratto dell'intermediario | ~2.220 € (A) / ~1.930 € (B) per 10.000 € investiti |

### 7.2 La regola sul prezzo

Il prezzo di ingresso è **l'unica variabile realmente negoziabile**. Le soglie derivate dal
fair value:

| | Fair value modello | **Soglia di acquisto** | A 100 |
|---|---|---|---|
| **A — Barclays** | 92,9 – 96,5 | **≤ 95** | Sconsigliato |
| **B — Vontobel** | 90,3 – 94,8 | **≤ 93** | **Da evitare** (rende meno del deposito) |

Operativamente: **sempre ordine con limite di prezzo, mai a mercato.** Su strumenti animati
da un solo market maker un ordine al meglio viene eseguito al prezzo che decide la controparte.

### 7.3 Dimensionamento

| Regola | Limite |
|---|---|
| Singolo certificato worst-of | **max 5%** del portafoglio |
| Intera classe (tutti i certificati) | **max 15%** del portafoglio |
| Comparto in cui imputarlo | **Azionario**, mai obbligazionario |
| Denaro impiegabile | Solo liquidità immobilizzabile fino al **2031** |

### 7.4 Il calendario del monitoraggio

Non serve seguirlo quotidianamente. Servono **quattro appuntamenti**:

| Quando | Cosa guardare | Soglia |
|---|---|---|
| **Ogni mese, alla data di rilevazione** | Il worst-of è sopra barriera cedola? | A: SocGen > 41,55 €. B: Enel > 5,90 € |
| **03.05.2027** (A) / **30.07.2027** (B) | Prima data di richiamo | A: SocGen ≥ 83,09 €. B: Enel ≥ 9,835 € |
| **Se il worst-of scende sotto il 60%** | Rivalutare: uscita o mantenimento | Il valore di mercato accelera al ribasso |
| **Ultimo trimestre prima della scadenza** | L'unico momento in cui la barriera capitale conta | A: 04.08.2031. B: 30.07.2031 |

**I soli due titoli che contano oggi sono Société Générale (per A) ed Enel (per B).**
Gli altri cinque sono rumore fino a quando uno di loro non diventa il nuovo peggiore.

### 7.5 Che fare negli scenari

| Scenario | Azione |
|---|---|
| Worst-of risale sopra il 100% prima della data di autocall | Non fare nulla: il richiamo arriva da solo a 100 |
| Worst-of fra 70% e 100% | Mantenere: si incassano le cedole, la barriera è lontana |
| Worst-of fra 50% e 70% | Rivalutare. Le cedole possono fermarsi; il prezzo è già sceso molto. Vendere realizza la perdita ma **genera minusvalenze compensabili** |
| Worst-of sotto il 50% con anni residui | La barriera è **europea**: il recupero è ancora possibile. Vendere qui significa monetizzare il punto di massima convessità, di norma la scelta peggiore |
| Worst-of sotto barriera negli ultimi 6 mesi | Poco da fare. Valutare la vendita solo per la pianificazione fiscale |

---

## 8. Verdetto sui due prodotti

### Certificato A — Barclays `XS3183930109`

**Acquistabile sotto 95, da chi ha minusvalenze da compensare e considera la posizione
azionaria.**

- **Pro:** cedola 11,64% (62% più di B), barriere più lontane (40%/50%), gradino di
  protezione 40–50%, emittente G-SIB, vita attesa più breve, autocall più rapido nel decadere.
- **Contro:** scommessa monosettoriale bancaria pura; coda più profonda (−75,8% quando la
  perdita si verifica); a 100 il rendimento atteso netto senza minusvalenze è del 2,74%,
  incompatibile con un rischio di perdita del 20%.

### Certificato B — Vontobel `DE000BD2KYU6`

**Da evitare a 100. Marginale sotto 93.**

- **Pro:** basket genuinamente diversificato (correlazioni 0,34–0,42); volatilità più bassa;
  barriera cedola finale al 30% che nella fascia 30–50% recupera tutte le cedole; SeDeX più
  liquido per il retail.
- **Contro:** **rende meno di un conto deposito** (2,04% contro 2,21% netto atteso) con
  un rischio di perdita del 18,6%; cedola 3,3 punti sotto l'equilibrio; costo di possesso
  3,25% annuo; premio creditizio Vontobel probabilmente sottostimato di 30–60 bp.

### Il confronto in una riga

Il certificato A paga il 62% in più di cedola **e** protegge di più. B è dominato su
entrambe le dimensioni: paga meno e ha le barriere più vicine. L'unico vantaggio genuino
di B — la diversificazione del basket — è, in un prodotto worst-of, **un vantaggio per
l'emittente, non per il cliente**.

---

## 9. Checklist finale — le sei domande

Se anche una sola risposta è "no", l'operazione non va fatta.

1. **Ho capito che sto vendendo un'assicurazione, non comprando un'obbligazione?**
2. **Posso permettermi di perdere il 60% di questo importo senza conseguenze sul mio piano
   finanziario?**
3. **Ho minusvalenze pregresse capienti da compensare?** *(senza, il rendimento netto atteso
   scende al 2,0–2,7% — meno di un conto deposito su B, di poco più su A)*
4. **Sto comprando sotto 95 (A) o sotto 93 (B)?**
5. **Questo importo resta immobilizzabile fino al 2031 senza che me ne serva prima?**
6. **Sto contabilizzando questa posizione nel comparto azionario del portafoglio?**

---

## 10. Limiti di questa analisi

Valgono integralmente i limiti dichiarati nel §8 del documento di valutazione. In sintesi:

- **Prezzi ricostruiti per calibrazione sugli strike**, non copiati da una fonte milanese
  (nessuna raggiungibile da questo ambiente). Metodo validato da due controlli indipendenti;
  l'unico prezzo con base stimata è Eni, con impatto nullo sulle conclusioni.
- **Dividendi stimati**, non presi da curve implicite: è il parametro a cui il risultato è
  più sensibile (±2 punti di fair value per punto di yield).
- **Volatilità realizzate a 100 sedute**, non implicite *deep out-of-the-money*, che per
  effetto dello skew sarebbero più alte. Lo scenario "vol +5 punti" è probabilmente più
  realistico del centrale.
- **Modello Black-Scholes multivariato** con volatilità e correlazione costanti: non cattura
  salti, volatilità stocastica né il collasso delle correlazioni verso 1 in regime di crisi.
  Tutti effetti che penalizzano il detentore.
- **Costi di negoziazione e spread** sono valori tipici di mercato, non quotazioni ricevute:
  vanno sostituiti con le condizioni effettive del proprio intermediario.
- **Il premio al rischio azionario del 5%** usato per le probabilità *real world* è
  un'ipotesi convenzionale. Con un premio nullo (misura risk-neutral) le probabilità di
  perdita salgono al 31,4% (A) e 36,0% (B) e i rendimenti attesi netti diventano negativi
  in quasi tutti gli scenari.

---

*Documento di ricerca a scopo informativo. Non costituisce consulenza finanziaria né
raccomandazione all'investimento. I rendimenti passati e simulati non sono indicativi di
quelli futuri.*
