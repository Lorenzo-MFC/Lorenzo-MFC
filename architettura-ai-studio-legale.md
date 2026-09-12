# Architettura AI per lo studio legale — dai preventivi hardware al progetto reale

> Documento di **settembre 2026**, complementare a
> [analisi-offerta-workstation-dell-precision-7-t1.md](./analisi-offerta-workstation-dell-precision-7-t1.md).
> Nasce dalla definizione dell'uso previsto: analisi contrattuale e due diligence con AI,
> dashboard gestionale e di cassa, previsioni economico-finanziarie, analisi di strumenti
> finanziari in tempo reale.
>
> **Le considerazioni normative sono un elenco di questioni da affrontare, non un parere
> legale.** Vanno validate dal professionista competente — con l'avvertenza che in questo
> caso il destinatario *è* uno studio legale, e quindi le verifiche sono interne.

---

## 1. Cosa cambia rispetto all'analisi hardware

L'analisi precedente si fermava a un bivio: la macchina serve per ufficio, per produzione
di contenuti o per AI? La risposta è **AI, ma quasi tutta di tipo documentale e gestionale**.

Questo ribalta la conclusione in un modo preciso:

| | Ipotesi precedente | Realtà del caso d'uso |
|---|---|---|
| Il collo di bottiglia | GPU e VRAM | **Qualità del modello, riservatezza dei dati e compliance** |
| Dove va il budget | Hardware | **Software, licenze, dati, consulenza privacy** |
| Peso dell'hardware sul progetto | 100% | **5-20%** |
| Verdetto sulla GPU RTX A1000 | Inadatta per l'AI | **Non serve affatto** — vedi §4 |

Il punto centrale: **tre dei quattro casi d'uso non richiedono alcuna GPU**, e il quarto
(analisi contrattuale in locale) richiede una GPU che questa macchina non può ospitare.

---

## 2. I quattro casi d'uso, smontati

| Caso d'uso | Carico computazionale reale | Serve GPU? | Collo di bottiglia vero |
|---|---|---|---|
| **Analisi contratti fornitori / due diligence** | LLM su testi lunghi | No se cloud. Sì e **grande** se in locale | Qualità del modello + segreto professionale |
| **Dashboard dipendenti, cassa, previsioni** | Web app + database | **No** | Sviluppo software + art. 4 Statuto dei Lavoratori |
| **Previsioni economico-finanziarie** | Fogli di calcolo, modelli statistici, LLM | **No** | Qualità dei dati contabili in ingresso |
| **Analisi titoli e certificati in tempo reale** | Feed dati + elaborazione CPU | **No** | Abbonamento e licenza dei market data |

### 2.1 Analisi contrattuale e due diligence — il caso più delicato

È il caso d'uso con il valore più alto e il rischio più alto. Tre cose vanno dette chiaramente:

- **Un modello da 7-8 miliardi di parametri quantizzato — ciò che entra in 8 GB di VRAM —
  non è affidabile per il lavoro legale.** Su clausole complesse produce omissioni e
  affermazioni inventate con la stessa sicurezza con cui produce quelle corrette. In un
  contesto dove l'errore diventa responsabilità professionale, questo non è un compromesso
  accettabile: è un rischio.
- I modelli che si avvicinano alla qualità necessaria sono i modelli di frontiera (cloud)
  oppure modelli da 70B+ in locale, che richiedono **48-96 GB di VRAM**: hardware da
  5.000-20.000 €, incompatibile con l'alimentatore da 360 W della Precision 7 T1.
- **In nessuno scenario l'output dell'AI è il prodotto finale.** L'AI fa la prima
  passata — estrae clausole, segnala anomalie, confronta con una checklist — e
  l'avvocato verifica. Questo non è solo prudenza deontologica: è anche il modo in cui
  lo strumento rende davvero, perché il tempo risparmiato è quello della lettura
  meccanica, non quello del giudizio.

### 2.2 Dashboard — è un progetto software, non hardware

Una dashboard su dipendenti, flussi di cassa e previsioni è un'applicazione web con un
database dietro. Gira su qualsiasi macchina, e anzi in genere conviene farla girare su un
piccolo server sempre acceso (o un servizio cloud), non su una workstation che viene spenta
la sera. **La GPU non c'entra nulla.** Vedi §5.1 per la questione più importante: il
perimetro legale del "controllo dei dipendenti".

### 2.3 Previsioni economico-finanziarie — il limite è a monte

Una previsione di cassa vale quanto i dati che la alimentano. Se i dati contabili sono
frammentati tra gestionale, estratti conto e fogli Excel, nessun modello — AI o statistico
— produce previsioni affidabili. **Il primo lavoro non è scegliere lo strumento: è mettere
in ordine i dati.** Con scadenziario clienti/fornitori strutturato, una previsione di cassa
a 13 settimane si costruisce con metodi ordinari e funziona bene.

### 2.4 Analisi titoli in tempo reale — il costo è il dato, non la macchina

"Tempo reale" ha un prezzo, ed è un prezzo ricorrente:

| Livello | Cosa dà | Costo indicativo |
|---|---|---|
| Dati ritardati (15-20 min) | Sufficiente per analisi fondamentale | Spesso gratuito |
| Real-time retail (un mercato) | Prezzi live | 20-80 €/mese |
| Real-time professionale multi-mercato | Profondità, storico, API | 200-2.000 €/mese |
| Terminali professionali | Tutto + analisi + news | 1.500-2.500 €/mese |

Due avvertenze che contano più della macchina:

- **La licenza "retail" non copre l'uso professionale.** Se i dati alimentano l'attività
  dello studio o strumenti usati per decisioni su patrimoni di terzi, serve una licenza
  professionale. È una clausola contrattuale, non un dettaglio.
- **L'AI non prevede i prezzi.** Nessun modello, locale o cloud, produce previsioni
  affidabili sull'andamento dei mercati — se lo facesse, chi lo possiede non lo venderebbe.
  L'AI ha valore reale nell'**analisi documentale** (leggere prospetti, KID, bilanci,
  confrontare condizioni di certificati, estrarre i costi impliciti) e nel **monitoraggio**
  (segnalare eventi, scadenze, variazioni di rating). Chiederle previsioni di prezzo è
  il modo più rapido per perdere tempo e denaro.

---

## 3. La decisione che conta: cloud, locale o ibrida

Questa è la vera scelta architetturale. L'hardware ne discende, non viceversa.

### Opzione A — AI in cloud con garanzie contrattuali

- ✅ Qualità dei modelli adeguata al lavoro legale
- ✅ Nessun investimento hardware, capacità scalabile
- ✅ Costo indicativo 20-200 €/mese per utente
- ⚠️ I documenti escono dallo studio → richiede tutele contrattuali rigorose (§5.2)
- **Hardware necessario: qualunque PC decente.** La Precision 7 T1 va benissimo, ed è
  anzi sovradimensionata.

### Opzione B — AI interamente in locale

- ✅ Nessun dato lascia lo studio: la soluzione più solida sul segreto professionale
- ❌ **Con 8 GB di VRAM la qualità non è sufficiente** per l'analisi contrattuale
- ❌ Per avvicinarsi alla qualità necessaria servono 48-96 GB di VRAM: **la Precision
  7 T1 con alimentatore da 360 W non può ospitare quelle schede.** Serve un'altra macchina
  e un budget 5-10 volte superiore
- ❌ Manutenzione, aggiornamento modelli e tuning a carico dello studio

### Opzione C — Architettura ibrida ⭐ raccomandata

Divide i carichi secondo la sensibilità del dato:

| Resta in locale | Va in cloud |
|---|---|
| Archivio documentale cifrato | Ragionamento sui contratti |
| OCR e indicizzazione | Sintesi e confronto clausole |
| Ricerca semantica sul repository | Redazione di bozze |
| Dashboard, dati contabili, dati dipendenti | |
| Anagrafiche clienti | |

Con **pseudonimizzazione prima dell'invio**: nomi, partite IVA, importi identificativi
sostituiti da segnaposto, ricostruiti localmente sulla risposta. Riduce molto l'esposizione
e semplifica la posizione verso clienti e Garante.

È l'opzione che massimizza qualità, riservatezza e costo insieme. E anche qui **l'hardware
richiesto è modesto**: l'indicizzazione e la ricerca semantica girano bene su CPU, o al
massimo su una GPU piccola.

---

## 4. Verdetto hardware rivisto

**La workstation va bene. La GPU no — e questa volta non è "sconsigliata": è inutile.**

| Componente | Verdetto | Motivo |
|---|---|---|
| Dell Pro Precision 7 T1 | 🟢 **Acquistare** | CPU e piattaforma adeguate; garanzia 36 mesi; certificazione ISV |
| RAM 32 GB su 1 modulo | 🔴 **Portare a 64 GB dual channel** | Documenti grandi, molte applicazioni, eventuale VM. ~120 € |
| SSD 1 TB singolo | 🔴 **Aggiungere secondo disco** | Un archivio legale su disco singolo senza ridondanza è inaccettabile. ~90-180 € |
| **GPU RTX A1000 510 €** | 🔴 **Non acquistare** | Non serve a nessuno dei quattro casi d'uso |
| Alimentatore 360 W | 🟡 Irrilevante per questo uso | Lo diventa solo se un domani si sceglie l'AI locale — e allora serve un'altra macchina |

**I 510 € della GPU vanno riallocati.** In ordine di rendimento:

| Riallocazione | Costo | Perché rende di più |
|---|---|---|
| RAM a 64 GB dual channel | ~120 € | Impatto immediato e quotidiano su tutto |
| Secondo SSD 2 TB | ~150 € | Archivio + ridondanza locale |
| NAS 2 dischi per backup | ~400 € | Continuità operativa dello studio |
| UPS | ~120 € | Protegge dati e alimentatore |
| **Totale** | **~790 €** | Copre i 510 € risparmiati + ~280 € |

Sono 280 € in più della GPU, e comprano le cose che in uno studio legale contano
davvero: capienza, ridondanza, continuità.

---

## 5. Compliance: sei questioni da risolvere prima di scrivere una riga di codice

Questa è la parte che pesa di più sul progetto, e quella dove il rischio non è
tecnico ma sanzionatorio.

### 5.1 🔴 "Controllo dei dipendenti" — art. 4 Statuto dei Lavoratori

**È il punto più critico dell'intero progetto.**

L'art. 4 della L. 300/1970 stabilisce che gli strumenti dai quali derivi *anche* la
possibilità di controllo a distanza dell'attività dei lavoratori possono essere impiegati
solo per esigenze organizzative, produttive, di sicurezza del lavoro o tutela del
patrimonio aziendale, e **previo accordo sindacale** o, in mancanza, **autorizzazione
dell'Ispettorato del Lavoro**.

Il comma 2 esclude dalla procedura gli strumenti "utilizzati dal lavoratore per rendere
la prestazione lavorativa". Una dashboard che **aggrega metriche di produttività per
dipendente** non rientra in quella eccezione: non è lo strumento di lavoro, è un sistema
di misurazione costruito sopra di esso.

Conseguenze del non rispettarlo: sanzioni penali per il datore (art. 38 L. 300/1970) e
**inutilizzabilità dei dati raccolti a ogni fine**, compresi quelli disciplinari. Cioè:
la dashboard non solo è illegittima, ma è anche inutile proprio nel momento in cui
servirebbe.

**Come impostarla correttamente:**

- Riformulare l'obiettivo da "controllo dei dipendenti" a **gestione dei carichi di lavoro
  e della fatturazione**: ore per pratica, scadenze, stato di avanzamento, redditività
  per cliente. Sono dati di organizzazione del lavoro, non di sorveglianza della persona.
- **Aggregare, non individualizzare**, dove il dato individuale non è necessario.
- Espletare comunque la procedura ex art. 4 se il sistema consente, anche solo
  potenzialmente, il controllo dell'attività.
- **Informativa ex art. 13 GDPR ai dipendenti**, obbligatoria in ogni caso.
- Valutare la **DPIA ex art. 35 GDPR**: il monitoraggio sistematico dei lavoratori è
  tra i trattamenti per cui è tipicamente richiesta.

### 5.2 🔴 Segreto professionale e dati dei clienti

Inviare contratti e documenti di clienti a un servizio AI di terzi tocca l'art. 622 c.p.
e il Codice deontologico forense, oltre al GDPR.

Da mettere in ordine **prima** del primo documento caricato:

- [ ] **Verificare mandati e NDA esistenti**: alcuni clienti — soprattutto societari —
      vietano contrattualmente il trattamento dei loro documenti con AI di terzi, o lo
      subordinano ad autorizzazione. Va controllato, non presunto.
- [ ] **Atto di nomina a responsabile del trattamento ex art. 28 GDPR** con il fornitore AI.
- [ ] **Zero data retention** e **nessun addestramento sui dati** inviati: deve risultare
      dalle condizioni contrattuali, non dalla pagina marketing.
- [ ] Preferire il **trattamento in UE**; se ci sono trasferimenti extra-UE, verificare
      la base giuridica (decisione di adeguatezza o SCC).
- [ ] **Aggiornare informative e registro dei trattamenti** dello studio.
- [ ] Definire per iscritto **quali categorie di documenti possono uscire e quali no**.
- [ ] Valutare la **pseudonimizzazione** sistematica prima dell'invio.

### 5.3 🟡 AI Act — i sistemi sul personale sono ad alto rischio

Il Regolamento (UE) 2024/1689 classifica come **ad alto rischio** i sistemi di AI destinati
a essere usati nella gestione dei lavoratori — tra cui l'assegnazione di compiti e il
monitoraggio o la valutazione delle prestazioni (Allegato III). Per chi li utilizza
(deployer) ne discendono obblighi non banali: sorveglianza umana, informativa ai
lavoratori, conservazione dei log, valutazione d'impatto.

Le date di applicazione delle diverse parti del regolamento sono scaglionate e vanno
verificate puntualmente. Il punto da tenere fermo è un altro: **una dashboard AI che
valuta i dipendenti non è un progetto tecnico neutro.** Se l'obiettivo si riformula come
in §5.1 — organizzazione del lavoro e fatturazione, senza valutazione algoritmica delle
persone — il problema si ridimensiona molto.

### 5.4 🟡 Consulenza finanziaria — dove passa il confine

Va distinto con chiarezza, perché il confine è presidiato da sanzioni:

| Uso | Inquadramento |
|---|---|
| Investimenti propri dello studio o dei soci | Libero |
| Analisi a supporto di un incarico legale (es. contenzioso su un prodotto finanziario) | Attività legale |
| **Raccomandazioni di investimento a clienti** | **Riservata**: richiede abilitazione (MiFID II / iscrizione all'albo OCF) |

Esercitare consulenza finanziaria senza abilitazione è abusivismo (art. 166 TUF). Se
l'analisi di titoli e certificati serve solo agli investimenti propri, non c'è problema —
ma è bene che la distinzione sia esplicita nell'organizzazione interna, perché uno
strumento costruito per uso interno tende, con il tempo, a essere mostrato ai clienti.

### 5.5 🟡 Licenze dei dati di mercato

I contratti dei fornitori di market data limitano quasi sempre redistribuzione e uso
derivato, e distinguono nettamente uso "non professionale" da uso professionale. Prima di
costruire una dashboard che si alimenta di un feed: leggere la licenza. È esattamente il
tipo di clausola che lo studio verifica per i clienti e che è facile trascurare per sé.

### 5.6 🟢 Sicurezza del repository documentale

Concentrare l'archivio dello studio su una workstation alza la posta di ogni guasto e di
ogni furto. Minimo indispensabile:

- Cifratura del disco (**BitLocker**, disponibile con Windows 11 Pro incluso)
- **Backup 3-2-1**: tre copie, due supporti diversi, una fuori sede — cifrata
- **Test periodico del ripristino**: un backup mai ripristinato non è un backup
- Autenticazione a più fattori su tutti i servizi cloud
- Piano di continuità: cosa succede allo studio se questa macchina sparisce domani

---

## 6. Il costo reale del progetto — l'hardware è il 5-20%

Stima su 5 anni, 1-3 utenti. Ordini di grandezza, da affinare sui preventivi reali.

| Voce | Minimo | Massimo | Note |
|---|---|---|---|
| Workstation riconfigurata (senza GPU) | 2.600 € | 2.800 € | 64 GB + secondo SSD |
| NAS, backup, UPS | 500 € | 1.200 € | Non comprimibile |
| Licenze AI (5 anni) | 3.000 € | 12.000 € | Secondo utenti e volumi |
| Dati di mercato (5 anni) | 0 € | 30.000 € | Da dati ritardati gratuiti al terminale professionale |
| Sviluppo dashboard | 2.000 € | 15.000 € | Da fai-da-te assistito da AI a sviluppo esterno |
| Consulenza privacy (DPIA, informative, art. 4) | 2.000 € | 5.000 € | Riducibile con competenze interne |
| Software gestionale / integrazioni | 1.000 € | 5.000 € | |
| **Totale 5 anni** | **≈ 11.100 €** | **≈ 71.000 €** | |
| **Peso dell'hardware sul totale** | **~24%** | **~4%** | |

**La lettura**: discutere 510 € di scheda video mentre il progetto vale dieci-settanta volta
tanto è un errore di allocazione dell'attenzione. Le decisioni che spostano davvero il
risultato sono tre: **quale architettura AI** (§3), **come si mettono in ordine i dati**
(§2.3) e **come si risolve la compliance** (§5).

---

## 7. Roadmap in quattro fasi

Ordinata per rapporto valore/rischio, non per entusiasmo.

### Fase 1 — Fondamenta (mese 1-2) · ~3.500 €
1. Acquistare la workstation **senza GPU**, con 64 GB dual channel e secondo SSD
2. NAS, backup 3-2-1, UPS, BitLocker, MFA
3. Riordinare l'archivio documentale: struttura cartelle, nomenclatura, versioning
4. Verificare mandati e NDA sull'uso di AI di terzi (§5.2)

### Fase 2 — Primo caso d'uso, quello a valore più alto (mese 2-4) · ~1.500 €
5. Scegliere il fornitore AI e firmare l'atto ex art. 28 GDPR
6. **Partire dall'analisi contrattuale sui fornitori dello studio**: contratti propri,
   nessun dato di clienti, rischio minimo, risultato misurabile
7. Costruire una checklist di due diligence e misurare quanto tempo fa risparmiare
8. Solo dopo aver validato la qualità su documenti propri, estendere ai clienti

### Fase 3 — Dashboard gestionale (mese 4-8) · ~4.000-15.000 €
9. **Prima la compliance**: art. 4, informative, eventuale DPIA (§5.1)
10. Riformulare l'obiettivo: carichi di lavoro e fatturazione, non controllo
11. Iniziare da **cassa e redditività per pratica** — valore immediato, zero attriti
12. Previsione di cassa a 13 settimane
13. Metriche sulle persone: per ultime, aggregate, e solo dopo la procedura

### Fase 4 — Analisi finanziaria (mese 8+) · variabile
14. Partire da **dati ritardati gratuiti**: per l'analisi fondamentale bastano
15. Passare al real-time solo quando si è dimostrato che serve davvero
16. Verificare la licenza prima dell'abbonamento (§5.5)
17. Usare l'AI per **leggere prospetti e KID**, non per prevedere prezzi

---

## 8. Cosa non fare

| ❌ | Perché |
|---|---|
| Comprare la RTX A1000 | Non serve a nessuno dei quattro casi d'uso |
| Costruire la dashboard dipendenti prima dell'art. 4 | Sanzioni penali e dati inutilizzabili |
| Caricare documenti di clienti su AI prima di verificare mandati e art. 28 | Segreto professionale |
| Aspettarsi previsioni di prezzo dall'AI | Non funziona, e costa tempo |
| Usare un modello da 8 GB per l'analisi contrattuale | Errori silenziosi su materia in cui si risponde professionalmente |
| Accettare l'output AI senza verifica umana | Responsabilità professionale |
| Costruire tutto insieme | Quattro progetti diversi: farne uno alla volta, misurando |
| Sottoscrivere market data professionali prima di aver validato l'uso | 200-2.000 €/mese per un'esigenza non ancora dimostrata |

---

## 9. In una riga

**Comprare la workstation senza scheda grafica, portarla a 64 GB dual channel con un
secondo disco, investire i 510 € risparmiati in backup e continuità, adottare
un'architettura AI ibrida, e risolvere l'art. 4 dello Statuto dei Lavoratori prima
ancora di aprire l'editor per la dashboard.**

---

## 10. Fonti e riferimenti

- [Analisi dell'offerta hardware](./analisi-offerta-workstation-dell-precision-7-t1.md) — documento complementare
- [Ricerca interna sui conti deposito](./credit-agricole-prodotti-finanziari-conti-deposito.md) — costo opportunità del capitale
- L. 300/1970, art. 4 e art. 38 — Statuto dei Lavoratori
- Reg. (UE) 2016/679 (GDPR), artt. 13, 28, 35
- Reg. (UE) 2024/1689 (AI Act), Allegato III
- D.Lgs. 58/1998 (TUF), art. 166; Direttiva 2014/65/UE (MiFID II)
- Art. 622 c.p.; Codice deontologico forense

> I costi indicati sono stime a ordini di grandezza, formulate per dimensionare le scelte
> e non come preventivi. I riferimenti normativi individuano le questioni da affrontare:
> l'applicazione al caso concreto — comprese le date di entrata in vigore scaglionate
> dell'AI Act — va verificata puntualmente.
