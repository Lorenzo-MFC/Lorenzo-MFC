# Analisi offerta D.V. Informatica — Workstation Dell Pro Precision 7 T1 + GPU NVIDIA RTX A1000

> Analisi condotta a **settembre 2026** sui due documenti di offerta ricevuti da
> D.V. Informatica (Corso Carlo Alberto 58, 60127 Ancona — amministrazione@dv-informatica.it).
> I prezzi e le disponibilità hanno validità limitata: rifarsi sempre all'offerta firmata.
> Le considerazioni fiscali hanno scopo informativo e **non sostituiscono il parere del
> commercialista**: il trattamento concreto dipende dal regime contabile dell'impresa.

> **⚠️ Aggiornamento — l'uso previsto è ora noto.** La macchina serve a uno **studio legale**
> per: analisi contrattuale e due diligence con AI, dashboard gestionale e di cassa,
> previsioni economico-finanziarie, analisi di strumenti finanziari. Con questo quadro il
> verdetto sulla GPU passa da "sconsigliata" a **"non serve"**, e il baricentro del progetto
> si sposta dall'hardware all'architettura e alla compliance.
> **Leggere [architettura-ai-studio-legale.md](./architettura-ai-studio-legale.md)**, che
> aggiorna le conclusioni dei §6 e §8 di questo documento. L'analisi tecnica ed
> economico-finanziaria che segue resta valida.

---

## 1. Sintesi esecutiva

| | |
|---|---|
| **Oggetto** | Workstation Dell Pro Precision 7 T1 (PW7T1260) + scheda grafica opzionale NVIDIA RTX A1000 8 GB |
| **Prezzo** | 2.465 € + 510 € = **2.975 € IVA esclusa** → **3.629,50 € IVA inclusa** |
| **Costo reale stimato (SRL, post IVA e post imposte)** | **≈ 2.145 €** |
| **TCO 5 anni (accessori, software ed energia inclusi)** | **≈ 4.615 € netti** (≈ 3.715 € se Office e antivirus sono già disponibili) |
| **Verdetto sulla macchina** | Solida, sovradimensionata per uso ufficio, corretta per produzione contenuti |
| **Verdetto sulla GPU proposta** | ⚠️ **Non consigliata come acquistata** — vedi §4.2 e §6 |

**Le tre cose da sapere prima di firmare:**

1. **La workstation a 2.465 € ha solo grafica integrata Intel.** La scheda tecnica è
   esplicita: *"Modello scheda grafica: Intel Graphics — Memoria Dedicata 0 MB — Integrata: Sì"*.
   Il testo commerciale della stessa pagina parla però di *"formidabile scheda grafica
   professionale"* e di *"grafica professionale NVIDIA"*. **Il marketing descrive una
   configurazione diversa da quella quotata.** Va chiarito per iscritto.
2. **L'alimentatore da 360 W è il vero vincolo architetturale** dell'acquisto, più della CPU
   o della RAM. Limita per sempre le GPU installabili a modelli alimentati dal solo slot
   PCIe (≤ 75 W). È la ragione per cui è stata proposta proprio la A1000.
3. **La RTX A1000 è la scheda sbagliata se l'obiettivo è l'AI.** 8 GB di VRAM e soprattutto
   192 GB/s di banda memoria la rendono inadatta all'inferenza LLM locale, che è un carico
   *memory-bound*. Se il driver dell'acquisto è "AI", quei 510 € vanno spesi diversamente (§6).

---

## 2. I dati dell'offerta, in chiaro

### 2.1 Workstation — Dell Pro Precision 7 T1, SKU PW7T1260 — 2.465 € + IVA

| Componente | Specifica dichiarata | Lettura critica |
|---|---|---|
| CPU | Intel Core Ultra 9 285, clock max 5,6 GHz | Top di gamma desktop Arrow Lake-S (24 core: 8P + 16E, senza Hyper-Threading) |
| NPU | "Livello Capacità AI: AI PC" | ⚠️ Dicitura commerciale, non una specifica. Vedi §4.5 |
| RAM | 32 GB DDR5 UDIMM 5.600 MHz — **2 banchi totali, 1 libero** | ⚠️ Significa **1 solo modulo da 32 GB → single channel**. Vedi §4.3 |
| RAM max | 128 GB | Espandibilità reale limitata a 2 slot |
| Storage | 1 × SSD 1.024 GB | ⚠️ Disco singolo, **nessuna ridondanza**. Vedi §4.4 |
| Controller RAID | "Raid 0" | Nessun RAID attivo in configurazione |
| GPU | **Intel Graphics integrata, 0 MB dedicati** | ⚠️ Il punto critico dell'offerta |
| Alimentatore | **360 W** | ⚠️ Il vincolo strutturale. Vedi §4.2 |
| Slot | 4 × PCI, 1 × PCIe x16, 1 × PCIe x1 | Buona espandibilità meccanica, non elettrica |
| Porte USB | 6 posteriori + 4 frontali (fino a USB 3.2 Gen 2x2 20 Gbps Type-C) | Ottima dotazione |
| Rete | LAN "non presente" (scheda) — Wireless **non presente**, Bluetooth **no** | ⚠️ Serve presa Ethernet cablata alla postazione. Vedi §4.6 |
| Sistema operativo | Windows 11 Professional | Corretto per uso aziendale (dominio, BitLocker, Intune) |
| Office | Nessuna immagine precaricata — versione **Trial** | ⚠️ **Licenza Office da acquistare a parte**: costo non incluso |
| Antivirus | 0 mesi inclusi | Costo ricorrente non incluso |
| Dimensioni / peso | 494 × 396 × 344 mm — 11,22 kg | Tower pieno: serve spazio sotto/accanto alla scrivania |
| Garanzia | **36 mesi** | Buona — da verificare se on-site o return-to-base |

### 2.2 GPU opzionale — NVIDIA RTX A1000 8 GB — 510 € + IVA

| Componente | Specifica dichiarata | Lettura critica |
|---|---|---|
| Architettura | Ampere (generazione 2020-2021) | ⚠️ Due generazioni indietro rispetto ad Ada / Blackwell |
| CUDA core | 2.304 | Fascia entry-level professionale |
| Tensor core | 72, terza generazione | Presenti, ma pochi |
| RT core | 18, seconda generazione | |
| VRAM | 8 GB GDDR6, bus 128 bit | ⚠️ **Banda 192 GB/s**: il collo di bottiglia per l'AI. Vedi §4.7 |
| Prestazioni | 6,7 TFLOPS FP32 | |
| Interfaccia | PCIe 4.0 x8 | Adeguata |
| Uscite video | **4 × Mini DisplayPort 1.4a soltanto** | ⚠️ Nessuna HDMI, nessuna DisplayPort full-size. Vedi §4.8 |
| Consumo | 50 W | Compatibile con i 360 W dell'alimentatore |
| Formato | Full height, **profilino non sostituibile** | ⚠️ Incompatibile con chassis half-height |
| Garanzia | **12 mesi** | ⚠️ **Asimmetria**: 12 mesi contro i 36 della macchina. Vedi §4.9 |

---

## 3. La contraddizione centrale dell'offerta

Le due schede si contraddicono su tre punti. Non sono sfumature: sono i tre elementi da
mettere nero su bianco prima dell'ordine.

| # | Documento A (workstation) | Documento B (GPU) | Conseguenza |
|---|---|---|---|
| 1 | Testo: *"potente grafica professionale NVIDIA"* | — | La tabella tecnica dello stesso documento dichiara **Intel Graphics integrata**. La GPU NVIDIA è un **opzionale a pagamento**, non inclusa |
| 2 | — | *"Ulteriori requisiti: connettore di alimentazione PCI Express a **16 pin**"* ma anche *"Tipo connettori di alimentazione: **Nessuno** — Numero connettori: **0**"* | La scheda si contraddice al suo interno. Tecnicamente una GPU da 50 W si alimenta dallo slot; il riferimento ai 16 pin è quasi certamente un refuso, ma **su un alimentatore da 360 W va confermato per iscritto** |
| 3 | Modello: **Dell Pro Precision 7 T1** | Elenco compatibilità: Precision 3280, 3460, 3660, 5860, 7820, 7875, 7920, 7960, R3930, T7820XL, T7920XL — **il "Pro Precision 7 T1" non compare** | L'elenco appartiene alla nomenclatura Dell *precedente* al rebranding "Dell Pro". Probabile compatibilità di fatto, ma **la compatibilità va fatta dichiarare dal fornitore** |

> **Azione**: chiedere a D.V. Informatica una conferma scritta — anche solo via e-mail —
> che la RTX A1000 è **installata, testata e garantita funzionante** nello specifico SKU
> PW7T1260 con l'alimentatore da 360 W. Una riga di e-mail vale come documento
> contrattuale e sposta il rischio sul fornitore.

---

## 4. Analisi tecnica — le nove criticità

### 4.1 La macchina quotata non ha GPU dedicata
È il punto numero uno. A 2.465 € si acquista una workstation la cui grafica è la iGPU del
Core Ultra 9. È una iGPU discreta per l'ufficio e la riproduzione video, **inadeguata** per
rendering 3D, editing video professionale, CAD certificato ISV o qualsiasi carico AI.
Se la ragione dell'acquisto è grafica o AI, **la GPU non è opzionale: è il prodotto**.

### 4.2 L'alimentatore da 360 W è il vincolo che decide tutto
Con 360 W la macchina può ospitare solo GPU alimentate dal solo slot PCIe (limite fisico
75 W). Questo esclude in modo permanente l'intera fascia media e alta delle schede NVIDIA
e AMD. Le conseguenze:

- **Oggi**: la scelta è ristretta a A1000 (50 W), RTX 2000 Ada (70 W) o equivalenti.
- **Domani**: non sarà possibile "aggiornare la scheda video" fra due anni, a meno di
  sostituire anche l'alimentatore — ammesso che Dell ne offra uno più potente per questo
  chassis, cosa **da verificare prima dell'ordine**.
- **Valutazione**: se l'orizzonte d'uso è 5-6 anni e include carichi grafici crescenti,
  questa limitazione pesa più della CPU. Chiedere esplicitamente al fornitore se esiste
  l'opzione PSU superiore (tipicamente 500-750 W) e a che costo **in fase di
  configurazione** — a macchina consegnata è quasi sempre impossibile o antieconomico.

### 4.3 RAM in single channel — perdita di prestazioni evitabile per ~120 €
"Banchi totali 2, banchi liberi 1" significa che i 32 GB sono su **un unico modulo**. In
single channel la banda memoria si dimezza. L'impatto è doppio:

- su tutti i carichi CPU-intensivi, perdita tipica del 5-15%;
- sulla **grafica integrata**, che usa la RAM di sistema come VRAM, la perdita può superare
  il 30-40%. Su una macchina venduta senza GPU dedicata, questo è un problema serio.

> **Azione**: chiedere in sede d'ordine la configurazione **2 × 16 GB** (dual channel, stesso
> prezzo) oppure l'aggiunta di un **secondo modulo da 32 GB** → 64 GB dual channel.
> Costo indicativo 100-150 €. È il singolo euro meglio speso di tutta l'offerta.
> Farlo fare in fabbrica, non dopo: non tocca la garanzia e costa meno del post-vendita.

### 4.4 Disco singolo, nessuna ridondanza
Un SSD da 1 TB senza RAID né secondo disco. Per una macchina aziendale che contiene lavoro
produttivo significa che **un guasto del disco = perdita totale dei dati locali**. La
garanzia sostituisce l'hardware, non i dati. Serve:

- un **secondo SSD** interno (~90 € per 1 TB) o un NAS/disco esterno;
- una **procedura di backup 3-2-1** (3 copie, 2 supporti diversi, 1 fuori sede — es. cloud).

Senza questo, i 2.975 € proteggono l'hardware e lasciano scoperto l'asset che vale di più.

### 4.5 "AI PC" è marketing, non una specifica
La scheda dichiara *"Livello Capacità AI: AI PC"* e il testo promette *"potenti esperienze
AI direttamente sul dispositivo"*. Nella pratica:

- l'NPU integrata nei Core Ultra desktop (Arrow Lake-S) si attesta intorno ai **13 TOPS**,
  mentre la soglia Microsoft per la certificazione **Copilot+ PC è 40 TOPS**;
- l'NPU serve a carichi leggeri e a basso consumo (effetti video in videoconferenza,
  trascrizione, piccoli modelli), **non** all'esecuzione di LLM o alla generazione di immagini.

> **Da verificare**: se l'acquisto viene giustificato con "è un AI PC", chiedere al fornitore
> la dichiarazione **se il sistema è certificato Copilot+ PC**. Molto probabilmente non lo è.
> Non è un difetto della macchina — è un difetto della narrazione commerciale.

### 4.6 Nessun Wi-Fi, nessun Bluetooth, LAN non dichiarata
La scheda riporta *Wireless: Non Presente* e *Bluetooth: No*; il campo *LAN (velocità)*
risulta *"non presente"* — quasi certamente una lacuna della scheda prodotto, perché ogni
tower Dell Precision monta una NIC cablata. Implicazioni operative concrete:

- serve una **presa di rete cablata** alla postazione (se non c'è, va preventivato un
  cablaggio o un adattatore USB/PCIe Wi-Fi, 25-60 €);
- niente Bluetooth = tastiera/mouse wireless, cuffie e presenter non funzionano senza
  dongle. La dotazione inclusa è tastiera **USB** e mouse **ottico USB**: coerente, ma da
  sapere in anticipo.

### 4.7 8 GB di VRAM e 192 GB/s: perché non basta per l'AI
Nell'inferenza di modelli linguistici la velocità di generazione dei token è limitata
soprattutto dalla **banda della memoria video**, non dalla potenza di calcolo. Con 192 GB/s
la A1000 è in fondo alla classifica delle schede attuali. Per dare la scala:

| Scheda | VRAM | Banda memoria | Consumo | Alimentazione |
|---|---|---|---|---|
| **RTX A1000 (offerta)** | 8 GB | **192 GB/s** | 50 W | Solo slot |
| RTX 2000 Ada | 16 GB | ~224 GB/s | 70 W | Solo slot |
| RTX 4060 Ti 16 GB | 16 GB | ~288 GB/s | 165 W | Cavo aux ⚠️ |
| RTX 5060 Ti 16 GB | 16 GB | ~448 GB/s | 180 W | Cavo aux ⚠️ |

*(Valori indicativi da verificare a listino: servono a fissare gli ordini di grandezza,
non come specifica contrattuale.)*

Cosa significa in pratica con 8 GB:
- ✅ modelli da 7-8 miliardi di parametri **quantizzati** (Q4): funzionano, lentamente;
- ⚠️ Stable Diffusion / SDXL: al limite, con workaround;
- ❌ modelli da 13B+, fine-tuning, video generativo, contesti lunghi: **non eseguibili**.

Le due colonne che contano davvero sono VRAM e banda. **A parità di spesa, la A1000 è
l'opzione peggiore su entrambe.**

### 4.8 Solo Mini DisplayPort: costo nascosto dei cavi
Quattro uscite mDP 1.4a, zero HDMI, zero DisplayPort full-size, zero DVI/VGA. Nessun monitor
in commercio ha un ingresso Mini DisplayPort. Servono quindi **4 cavi o adattatori
mDP → DP/HDMI**, 15-30 € l'uno → **60-120 € non preventivati**. Da chiedere **inclusi
nella fornitura**: è la concessione più facile da ottenere in trattativa.
Verificare inoltre gli ingressi dei monitor già in uso.

### 4.9 Garanzia asimmetrica: 36 mesi contro 12
La workstation è coperta 36 mesi, la GPU **12**. Dal tredicesimo mese si ha una macchina in
garanzia con dentro un componente da 510 € fuori garanzia — proprio il componente che
scalda di più e che, se si guasta, rende inutilizzabile il motivo per cui la si è comprata.

> **Azione**: chiedere l'**allineamento della garanzia GPU a 36 mesi**. È una richiesta
> legittima e normalmente accolta quando la scheda viene integrata in fabbrica da Dell
> (in quel caso segue la garanzia del sistema). Se la scheda è invece montata dal
> rivenditore, la garanzia resta quella del componente: **è una differenza sostanziale**
> e va chiarita prima dell'ordine.

---

## 5. Analisi economico-finanziaria

### 5.1 Il prezzo vero: lordo, netto IVA, netto imposte

| Voce | Importo |
|---|---|
| Workstation | 2.465,00 € |
| GPU RTX A1000 | 510,00 € |
| **Imponibile** | **2.975,00 €** |
| IVA 22% | 654,50 € |
| **Totale da pagare (esborso di cassa)** | **3.629,50 €** |
| IVA recuperabile (soggetto IVA, bene strumentale) | −654,50 € |
| **Costo al netto IVA** | **2.975,00 €** |

### 5.2 Ammortamento e deducibilità (ipotesi: bene strumentale d'impresa)

Le macchine elettroniche d'ufficio si ammortizzano generalmente al **20% annuo**
(D.M. 31/12/1988), con il primo esercizio ridotto al 50% → 10%. Piano su base 2.975 €:

| Esercizio | Aliquota | Quota | Residuo |
|---|---|---|---|
| Anno 1 | 10% | 297,50 € | 2.677,50 € |
| Anno 2 | 20% | 595,00 € | 2.082,50 € |
| Anno 3 | 20% | 595,00 € | 1.487,50 € |
| Anno 4 | 20% | 595,00 € | 892,50 € |
| Anno 5 | 20% | 595,00 € | 297,50 € |
| Anno 6 | 10% | 297,50 € | 0 € |

**Risparmio fiscale complessivo** (ipotesi SRL, IRES 24% + IRAP ≈ 3,9% → ~27,9%):
2.975 € × 27,9% ≈ **830 €**.

> **Costo reale a regime ≈ 2.975 − 830 = 2.145 €** — cioè il **59%** dei 3.629,50 €
> che escono di cassa il giorno del pagamento.

**Due avvertenze che cambiano radicalmente il conto:**

1. **Regime forfettario**: nessuna deduzione dei costi, **IVA non recuperabile**. Il costo
   reale resta **3.629,50 €**, cioè il **69% in più**. Se l'acquirente è in forfettario,
   tutta l'analisi di convenienza va rifatta.
2. **La regola dei 516,46 €** (art. 102 c. 5 TUIR) consente la deduzione integrale
   nell'esercizio per i beni di costo unitario inferiore a tale soglia. La GPU a **510 €**
   ci rientrerebbe per un soffio — **ma solo se acquistata come bene autonomo**. Se viene
   integrata nella workstation diventa parte di un *bene complesso* e segue l'ammortamento
   del bene principale. **Da sottoporre al commercialista**: vale ~140 € di anticipo
   d'imposta, poco in assoluto, ma è il tipo di dettaglio che conviene decidere *prima*
   di come viene fatturato, non dopo.

**Su incentivi e crediti d'imposta**: una workstation generalista **non** possiede i
requisiti di interconnessione richiesti dai beni "4.0". Non contare su crediti d'imposta
senza una verifica puntuale e attuale con il consulente — la normativa su questi strumenti
cambia a ogni legge di bilancio.

### 5.3 TCO a 5 anni — il prezzo di listino non è il costo

| Voce | Netto | Note |
|---|---|---|
| Workstation | 2.465 € | Da offerta |
| GPU RTX A1000 | 510 € | Da offerta |
| 2° modulo RAM 32 GB (dual channel) | ~120 € | **Necessario** (§4.3) |
| SSD secondario 1 TB per backup | ~90 € | **Necessario** (§4.4) |
| Cavi/adattatori mDP → DP/HDMI | ~80 € | **Necessario** se si prende la GPU (§4.8) |
| Licenza Office/Microsoft 365 Business (5 anni) | ~700 € | Non inclusa: solo trial |
| Antivirus/endpoint (5 anni) | ~200 € | Non incluso: 0 mesi |
| UPS 900 VA | ~120 € | Consigliato: protegge disco e alimentatore |
| Energia elettrica 5 anni | ~330 € | Vedi calcolo sotto |
| **TCO 5 anni** | **≈ 4.615 €** | **+55% rispetto ai 2.975 € di listino** |
| *TCO escludendo software già posseduto* | *≈ 3.715 €* | *Se Office e antivirus ci sono già* |

**Calcolo energia**: ~1.800 ore/anno di uso effettivo, assorbimento medio ~130 W con GPU
installata → ~234 kWh/anno → a 0,28 €/kWh ≈ **65 €/anno** → ~330 € in 5 anni.
L'alimentatore da 360 W è la potenza di picco, non il consumo reale: la spesa energetica
non è un fattore decisionale, ma va messa a bilancio.

### 5.4 Costo orario e soglia di convenienza

- **Costo per ora di utilizzo**: 4.615 € ÷ (5 anni × 1.800 h) = **≈ 0,51 €/ora**.
- **Costo mensile equivalente**: ≈ 77 €/mese su 60 mesi.

Rovesciando la domanda — *quanto deve produrre questa macchina per giustificarsi?*
Deve generare **almeno ~600-900 € l'anno** tra ricavi aggiuntivi e costi evitati. In termini
concreti, significa per esempio internalizzare una decina di lavorazioni video l'anno oggi
affidate all'esterno, oppure risparmiare ~2 ore di attesa a settimana su una macchina lenta.
**Se non si riesce a nominare la voce che copre quei 600-900 €, l'acquisto non è maturo.**

### 5.5 Costo opportunità del capitale

Collegamento diretto alla ricerca già presente in questo repository
([conti deposito Crédit Agricole](./credit-agricole-prodotti-finanziari-conti-deposito.md)):
2.975 € parcheggiati a un rendimento **netto** del ~2,2% annuo producono **≈ 65 €/anno**,
circa **330 € in 5 anni**. È l'ordine di grandezza del costo opportunità: reale ma modesto,
e non sufficiente da solo a rinviare un investimento produttivo. Ha però un corollario
operativo: **se la macchina non serve** *adesso*, rinviare l'acquisto di 6 mesi ha un costo
quasi nullo e in più fa scendere il prezzo dell'hardware.

### 5.6 Acquisto, noleggio o Dell APEX?

Il documento cita **Dell APEX PC as-a-Service** (canone mensile, nessun investimento
iniziale). Vale un confronto esplicito:

| | Acquisto | Noleggio operativo / APEX |
|---|---|---|
| Cassa iniziale | 3.629,50 € | ~0 |
| Deducibilità | Ammortamento 6 anni | **Canone interamente deducibile** nell'esercizio |
| IVA | Recupero immediato in un colpo | Recupero spalmato sui canoni |
| Proprietà a fine periodo | Sì (valore residuo di mercato ~15-25%) | No |
| Obsolescenza | A carico dell'impresa | A carico del fornitore |
| Costo totale | Minore | Tipicamente **+15-30%** |

**Regola pratica**: l'acquisto conviene se la macchina resterà in servizio 5+ anni e la
liquidità non è un problema. Il noleggio conviene se si prevede di sostituirla ogni 3 anni,
se si vuole preservare cassa, o se la deducibilità immediata del canone ha valore in un
esercizio con utile elevato. **Con un esborso di 3.600 € la differenza finanziaria è
marginale**: chiedere comunque il preventivo del canone — costa un'e-mail e dà una base
di confronto reale.

---

## 6. Analisi strategica: il problema dell'allineamento uso-configurazione

La domanda giusta non è "l'offerta è buona?" ma "**la configurazione è allineata all'uso?**".
Tre scenari, tre risposte molto diverse.

### Scenario A — Ufficio, gestionale, contabilità, multi-monitor
**La macchina è largamente sovradimensionata.** Un Core Ultra 9 285 con 32 GB per gestionale
e navigazione è come un furgone da 3,5 t per portare la spesa. Una configurazione adeguata
(Core Ultra 5 / i5, 16-32 GB, SSD 512 GB) costa **900-1.300 €**: si risparmiano ~1.500 €
senza alcuna perdita operativa, e la iGPU pilota già 3-4 monitor.

**→ Raccomandazione: non acquistare questa configurazione. Chiedere un preventivo alternativo.**

### Scenario B — Produzione contenuti: video, foto, grafica, social
**La macchina è corretta, la GPU proposta no.** CPU e RAM (portata a 64 GB dual channel)
sono adeguate al montaggio 4K e ad Adobe/DaVinci. Ma su questi carichi la VRAM è il limite:
8 GB sono stretti già oggi su timeline 4K con effetti.

**→ Raccomandazione: acquistare la workstation, sostituire la A1000 con una GPU da 16 GB
alimentata dal solo slot** (fascia RTX 2000 Ada o equivalente attuale, ~70 W: rispetta il
vincolo dei 360 W). Sovrapprezzo indicativo 150-250 €, VRAM raddoppiata, architettura due
generazioni più recente, codificatori video più moderni. **È il singolo cambiamento che
vale di più in tutta l'offerta.** Chiedere al fornitore il prezzo dell'alternativa: se non
la tratta, è un motivo sufficiente per confrontare un secondo rivenditore.

### Scenario C — AI locale, LLM, modelli generativi
**La piattaforma è quella sbagliata.** Il vincolo dei 360 W impedisce per sempre di
installare una GPU adatta all'AI. Le tre strade alternative:

1. **Cloud/API** — nessun investimento, zero obsolescenza. 510 € equivalgono a molti mesi
   di utilizzo intensivo di API commerciali, e i modelli disponibili sono incomparabilmente
   più capaci di qualsiasi cosa giri in locale su 8 GB.
   *Contro*: i dati escono dall'azienda — valutare se è accettabile (privacy, GDPR).
2. **GPU cloud a ore** (noleggio) — per fine-tuning o carichi discontinui: si paga l'uso.
3. **Macchina dedicata diversa** — se serve davvero l'AI on-premise: chassis con
   alimentatore 750 W+ e GPU consumer da 16 GB. Costo simile, capacità AI 3-5 volte
   superiore. *Contro*: niente certificazione ISV, niente supporto workstation.

**→ Raccomandazione: non comprare la A1000 per fare AI. Se l'AI è il vero driver, riaprire
la discussione sull'intera architettura prima di firmare.**

---

## 7. Il processo d'acquisto: cosa chiedere, su cosa trattare

### 7.1 Le dieci domande da mandare al fornitore (una sola e-mail)

1. La RTX A1000 è **compatibile e certificata** sullo SKU PW7T1260 con alimentatore 360 W?
   Viene **installata e testata** da voi prima della consegna?
2. La GPU richiede un **connettore di alimentazione ausiliario**? (La vostra scheda si
   contraddice: "16 pin" in un punto, "nessuno / 0 connettori" in un altro.)
3. La garanzia della GPU può essere **allineata ai 36 mesi** del sistema?
4. La garanzia 36 mesi è **on-site con intervento entro il giorno lavorativo successivo**
   o return-to-base? Qual è il costo dell'upgrade a ProSupport NBD?
5. I 32 GB sono su **1 o 2 moduli**? Qual è il costo per avere **64 GB in dual channel**
   configurati in fabbrica?
6. Esiste l'opzione **alimentatore di potenza superiore** per questo chassis? A che prezzo,
   e va scelta ora o è aggiungibile dopo?
7. Il sistema è **certificato Copilot+ PC**? Qual è la potenza dell'NPU in TOPS?
8. Sono inclusi i **cavi/adattatori Mini DisplayPort → DisplayPort/HDMI**? Quanti?
9. Sono inclusi **trasporto, consegna, installazione e migrazione dati**? Se no, quanto costano?
10. Qual è il **prezzo per entrambi i prodotti insieme** e quali sono i **termini di
    pagamento** (30/60 gg)? Qual è il canone mensile equivalente in noleggio/APEX?

### 7.2 Leve di trattativa, in ordine di probabilità di successo

| Leva | Valore | Probabilità |
|---|---|---|
| Cavi/adattatori mDP inclusi | 60-120 € | 🟢 Alta |
| Consegna e installazione incluse | 100-200 € | 🟢 Alta |
| Sconto per acquisto congiunto dei due articoli | 3-7% (90-210 €) | 🟢 Alta |
| Upgrade a 64 GB dual channel a costo agevolato | 100-150 € | 🟡 Media |
| Allineamento garanzia GPU a 36 mesi | 80-150 € | 🟡 Media |
| Secondo SSD da 1 TB incluso | ~90 € | 🟡 Media |
| Pagamento a 60 gg | Valore finanziario | 🟡 Media |
| Sostituzione con GPU 16 GB a sovrapprezzo contenuto | Valore d'uso alto | 🟡 Media |

> **Benchmark di prezzo**: prima di trattare, confrontare lo stesso SKU su Dell.it (prezzo
> diretto, spesso con promozioni business) e presso un secondo rivenditore. Il margine tipico
> di un rivenditore su una workstation lascia **5-10% di spazio negoziale**. Avere un
> secondo preventivo in mano vale più di qualsiasi argomento: **non trattare mai con un
> solo fornitore**.

### 7.3 Checklist pre-ordine

- [ ] Definito e messo per iscritto **l'uso prevalente** della macchina (Scenario A/B/C)
- [ ] Ricevute risposte scritte alle 10 domande di §7.1
- [ ] Ottenuto un **secondo preventivo** comparabile
- [ ] Verificato con il commercialista: **regime fiscale**, deducibilità, soglia 516,46 €
- [ ] Confermata la presenza di una **presa Ethernet** alla postazione
- [ ] Verificati gli **ingressi video dei monitor** esistenti
- [ ] Verificato lo **spazio fisico** (tower 49 × 40 × 34 cm, 11,2 kg)
- [ ] Deciso e preventivato il **piano di backup** (3-2-1)
- [ ] Verificata la disponibilità delle **licenze software** (Office non incluso)
- [ ] Concordata la **data di consegna** e le penali per ritardo

### 7.4 Dopo la consegna — collaudo in 8 punti

1. Verificare che la GPU sia **rilevata** in Gestione dispositivi e in `dxdiag`
2. Verificare che la RAM lavori in **dual channel** (Task Manager → Prestazioni → Memoria:
   "Slot utilizzati 2 di 2") e alla frequenza di targa
3. **Stress test combinato** CPU+GPU per 30-60 minuti: verifica della stabilità
   dell'alimentatore da 360 W sotto carico reale — è il test che conta di più
4. Verificare le temperature sotto carico
5. Installare i **driver NVIDIA Studio/Enterprise**, non i Game Ready
6. Attivare **BitLocker** e configurare le policy di sicurezza
7. Configurare e **testare il ripristino** del backup (un backup non testato non è un backup)
8. Registrare **service tag e data di acquisto**; annotare in calendario la **scadenza
   della garanzia GPU a 12 mesi** se non allineata

---

## 8. Valutazione complessiva

| Dimensione | Voto | Motivazione |
|---|---|---|
| Qualità della macchina | 🟢 8/10 | Piattaforma Dell solida, CPU top di gamma, garanzia 36 mesi, ottima connettività |
| Coerenza della configurazione | 🟡 5/10 | RAM single channel, disco singolo, nessuna GPU nel prezzo base |
| Scelta della GPU opzionale | 🔴 3/10 | Architettura datata, 8 GB, banda 192 GB/s, garanzia 12 mesi, solo mDP |
| Espandibilità futura | 🔴 4/10 | Alimentatore 360 W: vincolo permanente. Solo 2 slot RAM |
| Chiarezza dell'offerta | 🔴 4/10 | Tre contraddizioni documentali (§3) |
| Rapporto qualità/prezzo | 🟡 6/10 | Prezzo in linea di mercato, ma il valore dipende interamente dallo scenario d'uso |
| Trasparenza dei costi | 🟡 5/10 | Office, antivirus, cavi, backup: tutti esclusi e tutti necessari |

### Raccomandazione operativa

**Non firmare così com'è. Tre passi, nell'ordine:**

1. **Definire lo scenario d'uso** (A, B o C di §6). È una decisione di business, non tecnica,
   e determina tutto il resto. Senza questa risposta, ogni preventivo è un tiro a indovinare.
2. **Mandare le 10 domande di §7.1** e ottenere un secondo preventivo. Costa un'ora e vale
   con ogni probabilità 300-600 € tra sconti e correzioni di configurazione.
3. **Riconfigurare prima di ordinare**: 64 GB in dual channel, secondo disco per il backup,
   GPU con 16 GB al posto della A1000 (scenario B), cavi mDP inclusi, garanzia GPU allineata.

Con queste correzioni l'offerta passa da **discutibile** a **solida**. Senza, si rischia di
pagare 2.975 € per una macchina che non fa ciò per cui la si è comprata — oppure di pagarne
1.500 di troppo per una che fa molto meno di quanto può.

---

## 9. Fonti

- `scheda_grafica_opzionale_per_AI.pdf` — D.V. Informatica, scheda prodotto NVIDIA RTX A1000 8 GB
- `offerta_workstation_grafica_integrata.pdf` — D.V. Informatica, scheda prodotto DELL Pro Precision 7 T1 PW7T1260
- [Ricerca interna: conti deposito Crédit Agricole](./credit-agricole-prodotti-finanziari-conti-deposito.md) — usata per il costo opportunità del capitale (§5.5)

> I valori di banda memoria, TOPS dell'NPU e consumi delle GPU alternative citati in §4.7 e
> §6 sono ordini di grandezza indicativi, riportati per il confronto: vanno verificati sulle
> schede tecniche ufficiali del produttore prima di qualsiasi decisione d'acquisto.
