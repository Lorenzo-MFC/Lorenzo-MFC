# Scaletta di analisi — Volume d'affari dell'Avv. Michela

> Documento di lavoro aggiornato a **settembre 2026**. Contiene la scaletta (struttura, metodo,
> tabelle da compilare e parametri fiscali/previdenziali 2026) per analizzare in profondità il
> volume d'affari di uno studio legale individuale. I dati specifici dello studio dell'Avv. Michela
> **non sono presenti in questo repository**: ogni sezione indica quali documenti chiedere e come
> leggerli. Le aliquote e le soglie citate vanno sempre riverificate con il commercialista e sui
> siti ufficiali (Agenzia delle Entrate, Cassa Forense) prima di qualsiasi decisione.
> Il documento ha scopo informativo e non costituisce consulenza fiscale o legale.

---

## 0. Obiettivo, perimetro e assunzioni

**Domanda a cui rispondere**: quanto "gira" davvero lo studio dell'Avv. Michela, da dove viene quel
volume, quanto ne resta in tasca, come si colloca rispetto al mercato e quali leve lo fanno crescere.

**Perimetro dell'analisi** (da confermare con l'interessata):

| Voce | Assunzione di lavoro | Da verificare |
|---|---|---|
| Forma giuridica | Avvocato libero professionista individuale (partita IVA, ATECO 69.10.10) | Studio associato / STA / collaborazione con altro studio? |
| Regime fiscale | Da determinare: forfettario oppure ordinario (regime di cassa) | Copia dell'ultimo Modello Redditi PF |
| Iscrizione Cassa Forense | Iscritta, contributi in autoliquidazione (Modello 5) | Anno di iscrizione, eventuale agevolazione under 35 |
| Orizzonte temporale | Ultimi 3 esercizi chiusi (2023-2024-2025) + 2026 in corso | Disponibilità delle dichiarazioni |
| Unità di misura | Euro, competenza IVA per il volume d'affari, cassa per il reddito | — |

**Confine terminologico** (fondamentale, perché "volume d'affari" ha un significato tecnico):

| Grandezza | Definizione | Dove si legge |
|---|---|---|
| **Volume d'affari** | Somma delle operazioni imponibili, non imponibili ed esenti registrate ai fini IVA nell'anno (art. 20 DPR 633/1972). Include onorari, spese generali forfettarie e il contributo integrativo 4% (CPA). Esclude IVA e spese anticipate in nome e per conto del cliente (art. 15). | Dichiarazione IVA, quadro VE (rigo VE50); Modello 5 Cassa Forense |
| **Fatturato** | Uso comune, spesso coincide con il volume d'affari ma può includere le spese art. 15 e talvolta l'IVA se si guarda il "totale fattura". | Gestionale di studio |
| **Compensi** | Corrispettivi effettivamente incassati nell'anno (principio di cassa), al netto della CPA che va alla Cassa. | Modello Redditi PF, quadro RE (rigo RE2) |
| **Reddito professionale** | Compensi meno spese deducibili (quadro RE) o compensi × 78% se in forfettario (quadro LM). | Quadro RE / LM |
| **Reddito netto disponibile** | Reddito professionale meno contributi Cassa Forense e imposte. | Calcolo interno (sezione 4) |

Il primo errore da evitare è confrontare il volume d'affari (lordo, competenza IVA) con il reddito
(netto, cassa): lo scarto fra i due è esattamente l'oggetto dell'analisi.

---

## 1. Cosa entra e cosa non entra nel volume d'affari di un avvocato

Struttura tipica di una parcella e trattamento di ogni componente:

| Componente della fattura | Nel volume d'affari IVA? | Base CPA 4%? | Base IVA 22%? | Ritenuta 20%? | Nel reddito (RE)? |
|---|---|---|---|---|---|
| Onorario (parametri DM 55/2014 o accordo scritto) | Sì | Sì | Sì | Sì (se il cliente è sostituto d'imposta) | Sì |
| Spese generali forfettarie 15% (art. 2 DM 55/2014) | Sì | Sì | Sì | Sì | Sì |
| Contributo integrativo Cassa Forense 4% (CPA) | Sì | — | Sì | **No** | **No** (è della Cassa) |
| Spese anticipate in nome e per conto (art. 15 DPR 633/72: contributo unificato, marche, notifiche) | **No** | No | No | No | No (sono partite di giro) |
| Spese imponibili sostenute per lo studio e riaddebitate (es. trasferte a nome dell'avvocato) | Sì | Sì | Sì | Sì | Sì |
| IVA 22% | No | — | — | No | No |

Casi particolari da verificare per lo studio dell'Avv. Michela:

- **Gratuito patrocinio**: il compenso è liquidato dallo Stato; è imponibile IVA e soggetto a ritenuta,
  concorre al volume d'affari ma con tempi di incasso lunghi (impatto su cassa e DSO).
- **Fatture verso la Pubblica Amministrazione**: split payment (l'IVA la versa la PA) e possibile IVA a
  esigibilità differita; il volume d'affari è invariato ma la liquidità cambia.
- **Domiciliazioni e sostituzioni** ricevute da altri avvocati: sono compensi a tutti gli effetti.
- **Compensi da collaborazione con altri studi** (fatture a colleghi): incidono sulla concentrazione
  del rischio (un solo "cliente" che vale gran parte del volume).
- **Regime forfettario**: niente IVA in fattura e niente ritenuta; il 4% CPA si applica comunque e
  concorre ai ricavi ai fini della soglia (verificare con il commercialista la prassi
  dell'Agenzia sul punto).

---

## 2. Fonti dati per ricostruire il volume d'affari

Ordine consigliato, dal documento più "ufficiale" a quello più gestionale. Ogni fonte serve a
riconciliare le altre.

| # | Fonte | Cosa fornisce | Anni |
|---|---|---|---|
| 1 | **Dichiarazione IVA annuale, quadro VE** | Volume d'affari ufficiale (VE50), operazioni per aliquota, esenti | 2023-2025 |
| 2 | **Modello 5 Cassa Forense** | Volume d'affari IVA e reddito professionale dichiarati alla Cassa, contributi dovuti | 2023-2025 |
| 3 | **Modello Redditi PF, quadro RE** (ordinario) o **LM** (forfettario) | Compensi incassati, spese deducibili, reddito, ritenute subite | 2023-2025 |
| 4 | **Fatture elettroniche SdI** (export XML/CSV dal cassetto fiscale) | Dettaglio per cliente, data, importo, natura, incasso | tutte |
| 5 | **LIPE trimestrali** | Andamento infra-annuale e stagionalità | 2024-2026 |
| 6 | **Registro IVA vendite** | Cronologia emissioni, note di credito | tutte |
| 7 | **Estratti conto bancari** | Incassi effettivi, tempi di pagamento, insoluti | tutte |
| 8 | **Gestionale di studio / parcellazione** | Pratiche aperte, WIP non fatturato, materie, ore | corrente |
| 9 | **ISA (modello DK04U per avvocati)** e punteggio di affidabilità | Coerenza fra volume d'affari, ore lavorate, costi | 2023-2025 |
| 10 | **Prospetto F24 pagati** | Imposte e contributi effettivamente versati | 2023-2026 |

**Quadratura minima da fare**: VE50 (IVA) ≈ volume d'affari Modello 5 ≈ somma fatture SdI al netto di
art. 15 e IVA. Scostamenti superiori al 2-3% vanno spiegati (note di credito, fatture a cavallo
d'anno, errori di classificazione delle spese art. 15).

---

## 3. Analisi della struttura del volume d'affari

### 3.1 Serie storica (3-5 anni)

| Anno | Volume d'affari (VE50) | Var. % | Compensi incassati (RE2) | Incassato / fatturato | N. fatture | Ticket medio |
|---|---|---|---|---|---|---|
| 2023 | | | | | | |
| 2024 | | | | | | |
| 2025 | | | | | | |
| 2026 (proiezione su 9 mesi) | | | | | | |

Domande: il trend è di crescita organica, stagnazione o volatilità legata a poche pratiche grosse?
Il rapporto incassato/fatturato scende (crediti che si accumulano) o è stabile?

### 3.2 Scomposizione per cliente (concentrazione)

- Classifica dei clienti per fatturato triennale; calcolo della quota dei **primi 5 e primi 10**.
- Regola pratica: se i primi 5 clienti superano il 50% del volume, lo studio ha un rischio di
  dipendenza che va gestito prima di parlare di crescita.
- Distinguere: privati, imprese, PA, gratuito patrocinio, altri avvocati/studi, assicurazioni.

### 3.3 Scomposizione per materia e per fase

| Materia | Volume | % | N. pratiche | Ricavo medio / pratica | Ore stimate | Ricavo / ora |
|---|---|---|---|---|---|---|
| Civile contrattuale | | | | | | |
| Famiglia | | | | | | |
| Lavoro | | | | | | |
| Penale | | | | | | |
| Recupero crediti | | | | | | |
| Stragiudiziale / consulenza | | | | | | |

Il **ricavo per ora** è la metrica che collega volume d'affari e processo di studio: una materia con
alto volume ma basso ricavo orario sta "consumando" capacità produttiva.

### 3.4 Modalità di determinazione del compenso

- Parametri forensi (DM 55/2014, aggiornato dal DM 147/2022) vs accordo scritto/preventivo
  (obbligatorio ex art. 13 L. 247/2012) vs forfait vs tariffa oraria vs palmario.
- **Tasso di realizzo**: compenso fatturato / valore teorico a parametri. Sotto l'80% indica sconti
  sistematici o difficoltà di negoziazione.

### 3.5 Stagionalità e cassa

- Fatturato mensile (dalle LIPE e dallo SdI) e incassi mensili (estratti conto).
- **DSO** (giorni medi di incasso) = crediti medi / volume d'affari × 365. Oltre 90 giorni in uno
  studio individuale è un segnale di allarme per la liquidità.
- **WIP**: valore delle attività svolte ma non ancora fatturate (pratiche in corso a parametri).
  È volume d'affari "latente" dei prossimi esercizi.

---

## 4. Dal volume d'affari al reddito netto (waterfall)

### 4.1 Schema

```
Volume d'affari IVA (VE50)
  − Contributo integrativo 4% incassato (va alla Cassa, non è reddito)
  − Differenza fatturato/incassato (crediti verso clienti: principio di cassa)
= Compensi incassati (RE2)
  − Costi di studio deducibili (affitto, collaboratori, software, PEC/PCT, RC professionale,
    formazione obbligatoria, quota Ordine, utenze, ammortamenti)
= Reddito professionale lordo
  − Contributi Cassa Forense soggettivo + maternità (deducibili)
= Reddito imponibile
  − IRPEF (23% / 33% / 43%) + addizionali regionale e comunale   [regime ordinario]
    oppure imposta sostitutiva 15% (5% per i primi 5 anni)      [regime forfettario, base = 78% dei ricavi]
= Reddito netto disponibile
```

### 4.2 Esempio numerico indicativo (dati ipotetici, da sostituire con quelli reali)

Ipotesi: onorari + spese generali 57.500 €, CPA 4% = 2.300 €, quindi **volume d'affari 59.800 €**;
spese art. 15 anticipate 3.000 € (fuori campo); costi di studio 18.000 €; tutto incassato nell'anno;
iscrizione Cassa da oltre 6 anni (nessuna riduzione dei minimi).

| Voce | Regime ordinario | Regime forfettario |
|---|---|---|
| Ricavi rilevanti | 57.500 (compensi, CPA esclusa) | 59.800 (la CPA concorre ai ricavi forfettari) |
| Costi deducibili | 18.000 analitici | 22% forfettario = 13.156 (i 18.000 reali restano comunque un'uscita di cassa) |
| Reddito professionale | 39.500 | 46.644 (78% × 59.800) |
| Contributo soggettivo Cassa 17% | ≈ 6.715 | ≈ 7.930 |
| Contributo maternità (importo annuo fissato dalla Cassa) | ≈ 80 | ≈ 80 |
| Reddito imponibile | ≈ 32.705 | ≈ 38.634 |
| Imposta | IRPEF ≈ 7.990 lorda, ≈ 7.000 netta dopo detrazione lavoro autonomo, + addizionali ≈ 650 | 15% ≈ 5.795 (5% ≈ 1.932 se "start-up") |
| **Reddito netto di cassa** (ricavi − costi reali − contributi − imposte) | **≈ 25.000** | **≈ 28.000** (≈ 31.900 con il 5%) |
| Incidenza netto / volume d'affari | ≈ 42% | ≈ 47% |

Lettura: su circa 60.000 € di volume d'affari, in tasca restano 25-28.000 €, cioè meno della
metà. Nel forfettario il vantaggio è di circa 3.000 € l'anno a parità di volume, ma:

- l'IVA sugli acquisti diventa un costo (non detraibile);
- la clientela business preferisce fatture con IVA detraibile e ritenuta, quindi il forfettario
  favorisce chi lavora soprattutto con privati;
- superata la soglia di **85.000 €** di ricavi si esce dal regime l'anno successivo; oltre
  **100.000 €** si esce **immediatamente** nello stesso anno (con applicazione dell'IVA dalla
  fattura che supera la soglia).

### 4.3 Punto di pareggio dello studio

Costi fissi annui (18.000 €) + contributi minimi Cassa 2026 (2.790 + 355 + maternità ≈ 3.225 €)
≈ 21.225 € di uscite indipendenti dal fatturato. In regime forfettario, con imposta al 15% sul
78%, il volume d'affari minimo per non andare in perdita di cassa è dell'ordine di **26-28.000 €**;
in ordinario è simile ma dipende dalla detraibilità IVA. Ogni euro di volume d'affari oltre il
pareggio genera un netto marginale di circa 0,50-0,55 € (forfettario) e 0,40-0,50 € (ordinario,
per lo scaglione 33%).

---

## 5. Cassa Forense: come il volume d'affari determina i contributi (parametri 2026)

| Contributo | Base di calcolo | Misura 2026 | Minimo 2026 |
|---|---|---|---|
| **Soggettivo** | Reddito professionale netto IRPEF | **17%** fino al tetto di **131.800 €**; **3%** sulla parte eccedente | **2.790 €** |
| **Integrativo (CPA)** | **Volume d'affari IVA** | **4%**, addebitato in fattura al cliente (rivalsa) | **355 €** |
| **Maternità** | Importo fisso annuo | Deliberato annualmente dalla Cassa (ordine di grandezza: poche decine di euro) | — |
| **Modulare volontario** | Reddito | Facoltativo, dall'1% al 10%, deducibile | — |

Regole operative:

- Il **Modello 5** va trasmesso entro il **30 settembre** dell'anno successivo: dichiara reddito
  (quadro RE/LM) e volume d'affari (quadro VE). L'autoliquidazione dell'eccedenza rispetto ai
  minimi si versa nelle rate previste dalla Cassa (l'ultima rata è in prossimità del 30 settembre e
  include la maternità).
- I minimi sono dovuti anche con reddito zero. Il minimo integrativo di 355 € corrisponde a un
  volume d'affari di 8.875 €: sotto quella soglia il 4% incassato dai clienti non copre il minimo.
- **Under 35**: chi si iscrive prima dei 35 anni versa minimi dimezzati (1.395 € soggettivo,
  177,50 € integrativo) per i primi sei anni, con accredito dell'intera annualità contributiva.
  Verificare se l'Avv. Michela rientra ancora nel periodo agevolato.
- Il contributo soggettivo è **interamente deducibile** dal reddito: ogni 1.000 € di contributo
  riducono l'IRPEF di 230-430 € (ordinario) o l'imposta sostitutiva di 150 € (forfettario).
- Il soggettivo è "reddito differito": una pensione contributiva si costruisce sul reddito
  dichiarato, quindi comprimere il reddito oggi comprime la pensione domani.

---

## 6. Benchmark di mercato (dati Cassa Forense / Censis)

| Indicatore | Valore | Anno dato | Nota |
|---|---|---|---|
| Avvocati iscritti in Italia | 228.641 (106.655 donne, 121.966 uomini) | 2025 | In calo di circa 6.400 unità in dieci anni |
| Reddito medio professionale | **51.912 €** (+8,9%) | redditi 2024 | Media, non mediana: la distribuzione è molto asimmetrica |
| Reddito medio donne | **33.829 €** | redditi 2024 | |
| Reddito medio uomini | 67.959 € | redditi 2024 | Il divario di genere è circa 2:1 |
| Volume d'affari complessivo della categoria | > 16 miliardi € (+5,7%) | 2024 | Circa **69-70.000 € di volume d'affari medio per avvocato** (16 mld / 233.260 iscritti 2024) |
| Reddito IRPEF complessivo della categoria | 11,2 miliardi € (+7,1%) | 2024 | Rapporto reddito / volume d'affari di categoria ≈ 0,70 |
| Lombardia, reddito medio | 77.598 € (donne 45.406 €, uomini 112.408 €) | 2023 | Regione più alta; Centro-Sud sotto media tranne il Lazio |

Come usare il benchmark per l'Avv. Michela:

1. Calcolare il suo **rapporto reddito / volume d'affari** e confrontarlo con lo 0,70 di categoria:
   un valore molto più basso indica costi di struttura elevati o troppe spese riaddebitate; molto
   più alto indica uno studio "leggero" (tipico dei forfettari).
2. Posizionare il volume d'affari rispetto alla media di categoria (≈ 70.000 €) **e** rispetto alla
   media di genere e territorio: la distanza fra i 33.829 € medi delle donne e i 67.959 € degli
   uomini è in gran parte spiegata da anzianità, materie, part-time e carichi familiari, non da
   tariffe diverse.
3. Usare il **punteggio ISA**: sotto 8 aumenta la probabilità di controlli; il modello DK04U mette
   in relazione volume d'affari, ore lavorate e costi, quindi è già una "diagnosi" gratuita.

---

## 7. Cruscotto KPI dello studio

| KPI | Formula | Soglia di attenzione | Perché conta |
|---|---|---|---|
| Volume d'affari per ora fatturabile | VA / ore fatturabili annue (es. 1.200) | < 50 €/h | Misura il prezzo reale del tempo |
| Tasso di realizzo | Fatturato / valore a parametri | < 80% | Sconti impliciti |
| Ricavo medio per pratica | VA / pratiche fatturate | dipende dalla materia | Mix di lavoro |
| Concentrazione clienti | Quota primi 5 clienti | > 50% | Rischio di dipendenza |
| DSO | Crediti / VA × 365 | > 90 giorni | Liquidità |
| Insoluti | Crediti > 12 mesi / VA | > 5% | Qualità del portafoglio |
| Incidenza costi fissi | Costi fissi / VA | > 40% | Leva operativa |
| Netto / VA | Reddito netto / VA | < 40% | Efficienza fiscale e di struttura |
| Quota gratuito patrocinio | VA da GP / VA | > 25% | Incassi lenti, tariffe fisse |
| WIP / VA | Lavoro non fatturato / VA | > 30% | Fatturazione in ritardo |
| Distanza dalla soglia forfettaria | 85.000 − ricavi | < 10.000 € | Pianificazione del regime |

---

## 8. Leve di sviluppo del volume d'affari (management)

Ordinate per rapporto impatto / sforzo, da validare con i dati delle sezioni 3 e 7.

1. **Fatturare ciò che è già stato lavorato**: ridurre il WIP con acconti obbligatori all'apertura
   pratica e fatturazione per fase (il preventivo scritto ex art. 13 L. 247/2012 lo consente).
2. **Incassare prima**: solleciti strutturati, domiciliazione SEPA per i clienti ricorrenti,
   diffida a 60 giorni; ogni 30 giorni di DSO in meno su 60.000 € di VA liberano circa 5.000 € di cassa.
3. **Pricing**: applicare i parametri DM 55/2014 aggiornati (DM 147/2022) come base, con
   preventivi a forfait per le pratiche standard e tariffa oraria per la consulenza.
4. **Mix di materie**: spostare capacità dalle materie a basso ricavo orario a quelle ad alto
   ricavo; valutare una specializzazione (titolo di specialista ex DM 144/2015) che giustifica
   tariffe superiori.
5. **Clientela business**: se il regime è ordinario, le imprese sono clienti più redditizi (IVA
   detraibile per loro, contratti continuativi, consulenza ricorrente).
6. **Rete**: domiciliazioni e collaborazioni con studi di altre città o materie; convenzioni con
   associazioni di categoria, sindacati, amministratori di condominio, agenzie immobiliari.
7. **Digitalizzazione dei processi**: gestionale con controllo ore e parcellazione automatica,
   PCT/PPT nativo, firma digitale, archivio cloud; riduce il tempo non fatturabile (che in uno studio
   individuale supera spesso il 40% delle ore).
8. **Comunicazione**: sito professionale, profilo Google Business, contenuti informativi, nel
   rispetto dell'art. 35 del Codice deontologico forense (informazione, non pubblicità comparativa
   o suggestiva).
9. **Struttura**: quando il VA supera stabilmente 80-100.000 €, valutare praticante retribuito o
   collaboratore a partita IVA, poi studio associato o STA; ogni collaboratore deve generare almeno
   2,5-3 volte il proprio costo in volume d'affari.
10. **Pianificazione del regime fiscale**: se il VA si avvicina a 85.000 €, decidere in anticipo
    se restare sotto soglia (rinviando fatture non è lecito, ma si può scegliere il mix di lavoro)
    o passare all'ordinario con una struttura di costi che lo giustifichi.

**Scenario a tre anni** (da compilare):

| | Anno 0 (2025) | Anno 1 | Anno 2 | Anno 3 |
|---|---|---|---|---|
| Volume d'affari | | +10% | +10% | +10% |
| Costi di studio | | | | |
| Regime | | | | |
| Contributi Cassa | | | | |
| Imposte | | | | |
| Netto | | | | |
| Netto / VA | | | | |

---

## 9. Rischi e punti di attenzione

- **Soglie forfettarie** (85.000 € per l'uscita differita, 100.000 € per l'uscita immediata) e
  cause ostative (redditi da lavoro dipendente > 35.000 € nell'anno precedente, partecipazioni in
  SRL con attività riconducibile).
- **Fatturazione elettronica obbligatoria** anche per i forfettari dal 2024: lo SdI è ormai la
  fonte primaria dell'Agenzia e della Cassa per incrociare volume d'affari e Modello 5.
- **Incongruenze ISA**: volume d'affari basso rispetto a ore e costi genera anomalie.
- **Ritenute d'acconto**: crediti IRPEF da ritenute subite (20%) che superano l'imposta dovuta vanno
  gestiti (compensazione o rimborso) per non immobilizzare liquidità.
- **Antiriciclaggio**: obblighi di adeguata verifica sui clienti, rilevanti se cresce la clientela
  business o immobiliare.
- **Assicurazione RC professionale obbligatoria** (L. 247/2012): il massimale va rivisto se il VA e
  il valore delle pratiche crescono.
- **Continuità**: uno studio individuale ha rischio "persona chiave"; polizza infortuni/malattia e
  accordi di sostituzione con colleghi proteggono il volume d'affari.

---

## 10. Checklist documenti da chiedere all'Avv. Michela

- [ ] Modello Redditi PF 2024, 2025, 2026 (quadri RE o LM, RN, RS)
- [ ] Dichiarazione IVA 2024, 2025, 2026 (quadro VE) oppure conferma del regime forfettario
- [ ] Modello 5 Cassa Forense degli ultimi tre anni e prospetto contributi versati
- [ ] Export fatture elettroniche (XML o CSV) 2023-2026 dal cassetto fiscale o dal gestionale
- [ ] Elenco pratiche aperte con valore stimato a parametri (WIP)
- [ ] Scadenzario crediti verso clienti e insoluti
- [ ] Prospetto costi di studio per natura (affitto, collaboratori, software, assicurazione, formazione)
- [ ] Punteggio ISA degli ultimi due anni
- [ ] Anno di iscrizione all'Albo e alla Cassa, eventuali specializzazioni
- [ ] Ore lavorate stimate per settimana e quota di tempo fatturabile
- [ ] Obiettivi personali: reddito target, ore desiderate, propensione a strutturare lo studio

---

## 11. Ordine di lavoro proposto

1. Raccolta documenti (sezione 10) — 1 settimana.
2. Quadratura VE50 / Modello 5 / SdI e costruzione della serie storica (sezioni 2 e 3.1).
3. Scomposizione per cliente, materia, fase e modalità di compenso (sezioni 3.2-3.4).
4. Waterfall reddito reale e confronto fra regimi con i dati veri (sezione 4).
5. Verifica contributi Cassa e proiezione pensionistica (sezione 5).
6. Posizionamento rispetto al benchmark e calcolo KPI (sezioni 6 e 7).
7. Selezione di 3-4 leve e piano a tre anni (sezione 8), con revisione trimestrale sulle LIPE.

---

## Fonti

- [Contributi minimi anno 2026 — Cassa Forense](https://www.cassaforense.it/DettaglioNews?id=16589&tipo=inEvidenza)
- [Contributi in autoliquidazione — Cassa Forense](https://www.cassaforense.it/contributi-in-autoliquidazione)
- [Approvata la riforma del sistema previdenziale — Cassa Forense](https://www.cassaforense.it/DettaglioNews?id=14088&tipo=inEvidenza)
- [Cassa Forense: contributi minimi 2026, prima rata in scadenza il 28 — FISCOeTASSE](https://www.fiscoetasse.com/domande-e-risposte/1309-cassa-forense-contributi-minimi-entro-il-28-febbraio.html)
- [Contributi Cassa Forense 2026: aliquote, minimi e scadenze — Centro Fiscale](https://centrofiscale.com/contributi-cassa-forense-2026/)
- [Cassa Forense 2026: contributi minimi e tetto reddituale — RegimeMinimi](https://www.regimeminimi.com/cassa-forense-2026-contributi-minimi-tetto-reddituale/)
- [Cassa Forense: contributi minimi, aliquote e pensione 2026 — SF Advisor](https://www.sfadvisor.it/cassa-forense-contributi-pensione/)
- [Avvocato in regime forfettario 2026 — TaxMan](https://www.taxmanapp.it/blog/2026/02/15/avvocato-in-regime-forfettario-ecco-come-fare/)
- [Tasse per un avvocato: forfettario e ordinario — Fiscozen](https://www.fiscozen.it/guide/tasse-avvocati/)
- [Regime forfettario 2026: limiti e controlli — Centro Fiscale](https://centrofiscale.com/regime-forfettario-2026-limiti-e-controlli-automatici/)
- [Avvocato forfettario 2026: tasse, Cassa Forense e Modello 5 — RegimeForfettario.it](https://www.regimeforfettario.it/regime-forfettario-avvocato/)
- [Scaglioni IRPEF 2026: aliquote 23%, 33%, 43% — SoluzioneTasse](https://www.soluzionetasse.com/scaglioni-irpef/)
- [IRPEF 2026: come si calcola — IPSOA](https://www.ipsoa.it/guide/irpef-calcolo)
- [CPA 4% della Cassa avvocati: come si calcola — Fiscozen](https://www.fiscozen.it/guide/su-cosa-si-calcola-il-4-della-cassa-avvocati/)
- [Avvocato: come si calcola l'IVA — Fiscozen](https://www.fiscozen.it/guide/iva-avvocato/)
- [Contributo integrativo Cassa Forense: il 4% in fattura — Quantum365](https://www.quantum365.legal/risorse/articoli/contributo-integrativo-cassa-forense)
- [Calcolo parcella avvocato: fattura, IVA, CPA e ritenuta — CSL](https://www.consulenzastudiolegale.it/strumenti/fattura-studio-legale/)
- [Calano gli avvocati, 228.641 nel 2025 — ANSA](https://www.ansa.it/sito/notizie/economia/pmi/2026/04/29/calano-gli-avvocati-228.641-nel-2025-piu-abbandoni-fra-le-donne_21f13398-b88e-4924-9469-d7a31ddac99f.html)
- [Avvocati, redditi in crescita ma disuguaglianze profonde — Mondo Professionisti](https://www.mondoprofessionisti.it/pianeta-avvocato/avvocati-redditi-in-crescita-ma-disuguaglianze-profonde/)
- [Rapporto Avvocatura 2025 — TeamSystem](https://www.teamsystem.com/magazine/legal/rapporto-censis-avvocatura-2025-calano-iscritti-permangono-disparita/)
- [Rapporto Cassa Forense - Censis 2025 — La Previdenza Forense](https://laprevidenzaforense.it/rubriche/previdenza/rapporto-cassa-forense-censis-2025-meno-avvocati-un-po-piu-anziani-e-leggermente-piu-ricchi-tutto-vero/)
- [I numeri dell'Avvocatura 2024 — La Previdenza Forense](https://laprevidenzaforense.it/rubriche/previdenza/i-numeri-dell-avvocatura-2024/)
- [Rapporto sull'Avvocatura 2024 — Cassa Forense (PDF)](https://www.cassaforense.it/media/tzhlltfb/rapporto-avvocatura-2024.pdf)
