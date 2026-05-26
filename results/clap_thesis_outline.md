# Afstudeerrapport — Outline

*Gegenereerd uit: run_CLAP_project_writeup.md. Volgt richtlijnen HvA HBO-ICT, Januari 2024.*

## Dekkingsoverzicht (gap-analyse)

| Sectie | Status | Notitie |
|---|---|---|
| Omslag / voorblad | ONTBREEKT | geen auteursinformatie in bron |
| Titelpagina | ONTBREEKT | geen studentnummer, begeleiders, datum |
| Samenvatting | ONTBREEKT | nog te schrijven |
| Inleiding | AANVULLEN | aanleiding en context aanwezig; probleemstelling en leeswijzer missen |
| 1.1 Bedrijf / organisatie | GEDEKT | Sensemakers Amsterdam beschreven |
| 1.2 Opdrachtomschrijving | GEDEKT | stadsklanken classificeren, motief uitgelegd |
| 1.3 Analyse van de opdracht | AANVULLEN | context aanwezig, formele analyse mist |
| 1.4 Probleemvraag | AANVULLEN | probleem beschreven, maar niet als formele vraag geformuleerd |
| 1.7 Deelvragen | ONTBREEKT | niet geformuleerd |
| 2. Methodebeschrijving | AANVULLEN | CLAP, dataset en notebooks beschreven; verantwoording mist |
| 3. Onderzoek | AANVULLEN | resultaten impliciet aanwezig, niet per deelvraag gestructureerd |
| 4. Ontwerp en realisatie | GEDEKT | Pi-script, MQTT, sound_scapes.py beschreven |
| 5. Testresultaten | GEDEKT | noise robustness tests gedaan en besproken |
| Conclusies | AANVULLEN | takeaways aanwezig, geen formele conclusieparagraaf |
| Aanbevelingen | AANVULLEN | "what's next" aanwezig, niet formeel gescheiden |
| Bronnenlijst | AANVULLEN | URLs aanwezig, APA-opmaak ontbreekt |
| Bijlagen | AANVULLEN | code, notebooks, slides beschreven in bron |

---

## 1. Omslag / voorblad

[ONTBREEKT — nog te schrijven door student]

Vereiste velden:
- Titel: *Listening to the City: Testing CLAP for Urban Sound Classification* [VERTALEN]
- Naam bedrijf / opdrachtgever: Sensemakers Amsterdam
- Naam auteur
- HvA-begeleider
- Bedrijfsbegeleider

---

## 2. Titelpagina

[ONTBREEKT — nog te schrijven door student]

Vereiste velden: alles van de omslag, plus studentnummer, plaats & datum, versie, onderwijsinstelling, opleiding, stageperiode. Géén citaten, géén dankwoorden.

---

## 3. Samenvatting

[ONTBREEKT — nog te schrijven door student. Max 1 pagina, bevat: onderwerp, probleemomschrijving, probleemvraag, onderzoeksmethode, belangrijkste resultaten, belangrijkste conclusies.]

---

## 4. Inhoudsopgave

[Wordt automatisch gegenereerd in Word]

---

## 5. Inleiding

*Uit bron (aanvullen en herschrijven):*

- Sensemakers Amsterdam werkt sinds 2019 aan stadsklanken classificatie als alternatief voor louter geluidsmetingen in decibel [VERTALEN]
- Standaard geluidsmeters meten sterkte, niet aard; classificatie geeft rijkere informatie over de akoestische omgeving van een wijk [VERTALEN]
- CLAP (Contrastive Language-Audio Pretraining) maakt zero-shot classificatie mogelijk: geen hertraining nodig voor nieuwe geluidsklassen [VERTALEN]

[AANVULLEN — leeswijzer en formele probleemstelling missen; geen "ik/wij" gebruiken]

---

## Hoofdstuk 1 — Context van de opdracht

### 1.1 Het bedrijf

*Uit bron:*

- Sensemakers is een Amsterdamse community van makers die werken met sensoren, netwerken en machine learning [VERTALEN]
- Actief sinds de vroege IoT-golf; urban sounds is een van de langstlopende projecten [VERTALEN]

[AANVULLEN — formele bedrijfsbeschrijving, KvK, grootte, missie nog toe te voegen]

### 1.2 Opdrachtomschrijving

*Uit bron:*

- Classificatie van stadsklanken per locatie in Amsterdam: wat maakt het geluid, wanneer, waar en hoe vaak? [VERTALEN]
- Doel: een akoestische kaart van de wijk — niet alleen een heatmap van volume, maar een beschrijving van het akoestische leven [VERTALEN]
- Eerder werkten zij met CNN-gebaseerde classifiers op spectrogrammen; CLAP vervangt dit door zero-shot classificatie [VERTALEN]

### 1.3 Analyse van de opdracht

[AANVULLEN — bron beschrijft context en aanleiding uitgebreid, maar een formele analyse van de opdracht (scope, afbakening, risico's) ontbreekt]

### 1.4 Probleemvraag

[AANVULLEN — bron beschrijft het probleem maar formuleert geen expliciete probleemvraag. Suggestie op basis van bron:
*"In hoeverre is het CLAP-model geschikt voor zero-shot classificatie van stadsklanken in Amsterdam, en onder welke omstandigheden kan het op een Raspberry Pi worden ingezet?"*
— dit dient door de student zelf geformuleerd en vastgesteld te worden.]

### 1.5 Definities

*Uit bron (selectie):*

- **CLAP** — Contrastive Language-Audio Pretraining; neuraal netwerk getraind op (audio, tekst)-paren [VERTALEN]
- **Zero-shot classificatie** — classificatie zonder hertraining, via tekstlabels op inferentietijd [VERTALEN]
- **MQTT** — protocol voor publicatie van sensordata [VERTALEN]
- **Soundscape** — akoestisch profiel van een locatie over tijd [VERTALEN]

### 1.6 Randvoorwaarden

*Uit bron:*

- Inzet op Raspberry Pi (low-power edge device) [VERTALEN]
- Labels configureerbaar per locatie via `sound_scapes.py` [VERTALEN]
- MQTT-credentials opgeslagen in `config.py` (niet in repository) [VERTALEN]

[AANVULLEN — formele randvoorwaarden (budget, tijdlijn, privacy, AVG) ontbreken]

### 1.7 Deelvragen

[ONTBREEKT — nog te formuleren door student op basis van de probleemvraag. Aanzet vanuit bron:
- Hoe presteert CLAP zero-shot op stedelijke geluidsklassen vergeleken met een gespecialiseerd CNN-model?
- Welk CLAP-model (`larger_clap_general` vs. `larger_clap_music_and_speech`) presteert beter op urban-sound data?
- In hoeverre is het model robuust tegen additief ruis (wind, achtergrondverkeer)?
- Is CLAP uitvoerbaar op een Raspberry Pi voor continue inzet?
— bovenstaande zijn voorstellen; de student formuleert de definitieve deelvragen.]

---

## Hoofdstuk 2 — Methodebeschrijving en -verantwoording

*Uit bron:*

- Twee CLAP-modellen getest: `larger_clap_general` en `larger_clap_music_and_speech` (LAION, Hugging Face) [VERTALEN]
- Dataset: **UrbanSoundsNew** — 216 samples, negen klassen, samengesteld voor Amsterdam [VERTALEN]
- Exploratie via Jupyter notebooks (Hugging Face `transformers`-bibliotheek) [VERTALEN]
- Noise robustness test: schone samples progressief vervuild met 10%, 25%, 50%, 100% witte ruis [VERTALEN]
- Edge deployment getest op Raspberry Pi; CPU-gebruik gemonitord via `cpu_usage/`-script [VERTALEN]

[AANVULLEN — verantwoording van methodekeuzes ontbreekt; waarom deze dataset, waarom deze testaanpak?]

**AI-gebruik:** Claude Code (Anthropic) is ingezet bij het opstellen van deze outline. Werkwijze: bronbestand aangeleverd; outline gegenereerd conform HvA HBO-ICT richtlijnen Januari 2024. Zie Bijlage B voor de gebruikte prompts.

---

## Hoofdstuk 3 — Onderzoek naar hoofd- en deelvragen

### 3.1 Baseline: werkt CLAP op urban sounds?

*Uit bron:*

- Notebook *UrbanSoundsII dataset with CLAP.ipynb*: model geladen, dataset geladen, inferentie uitgevoerd [VERTALEN]
- Resultaat: top-predicted label komt "encouragingly often" overeen met ground truth [VERTALEN]

[AANVULLEN — exacte accuracy-cijfers ontbreken in de bron]

### 3.2 Embeddings en visualisatie

*Uit bron:*

- Notebook *CLAP embeddings.ipynb*: audio-embeddings gegenereerd; PCA/t-SNE visualisaties tonen hoe het model klassen groepeert [VERTALEN]
- Strak geclusterde klassen zijn makkelijk voor het model; klassen die overlappen geven problemen [VERTALEN]

### 3.3 Veldopnames

*Uit bron:*

- Notebook *Real UrbanSoundsSamples with CLAP.ipynb*: model getest op echte veldopnames met wind op microfoon, achtergrondverkeer en overlappende gebeurtenissen [VERTALEN]

### 3.4 Robustness tegen ruis

*Uit bron:*

- Witte ruis toegevoegd in stappen van 10%, 25%, 50%, 100% [VERTALEN]
- Conclusie: "even with 100% white noise added, the audio classification is still good" [VERTALEN]
- Hypothese: CLAP-trainingsdata bevatte al veel ruisige opnames; contrastive objective beloont focus op saillante kenmerken [VERTALEN]

### 3.5 Modelvergelijking

*Uit bron:*

- `larger_clap_general` presteert consistent beter dan `larger_clap_music_and_speech` op urban-sound data [VERTALEN]

---

## Hoofdstuk 4 — Ontwerp en realisatie

### 4.1 Architectuur

*Uit bron:*

- Productiescript: `urban_sounds_3.5.py` — audio capture → CLAP inferentie → MQTT publicatie [VERTALEN]
- Locatiespecifieke labelsets in `sound_scapes.py`; huidige locatie: **Marineterrein Amsterdam** [VERTALEN]
- MQTT-credentials in `config.py` (buiten repository gehouden) [VERTALEN]

### 4.2 Edge deployment

*Uit bron:*

- Doelplatform: Raspberry Pi (low-power, lamppost-monteerbaar) [VERTALEN]
- CPU-monitoring via `cpu_usage/`-subfolder: matplotlib-grafieken van processorbelasting tijdens inferentie [VERTALEN]
- Bevinding: zorgvuldige sample scheduling en aanvaardbare latentie zijn vereist voor continue inzet [VERTALEN]

[Zie Bijlage C voor volledige deployment-configuratie]

---

## Hoofdstuk 5 — Testresultaten en evaluatie

*Uit bron:*

- Noise robustness: classificatie blijft goed tot en met 100% additief witte ruis [VERTALEN]
- CPU: Pi kan CLAP draaien, "maar nipt" — scheduling en batchgrootte zijn kritiek [VERTALEN]
- Zero-shot: negen urban-sound klassen geclassificeerd zonder hertraining [VERTALEN]
- Explainability: nog onopgelost — folder `5_explainability` bevat lopende experimenten [VERTALEN]

[AANVULLEN — kwantitatieve evaluatiemetrieken (precision, recall, F1 per klasse) ontbreken in de bron]

---

## Conclusies

*Uit bron (herschrijven in tegenwoordige tijd, geen nieuwe informatie):*

- Zero-shot classificatie via CLAP is toepasbaar op stedelijke geluidsklassen zonder hertraining [VERTALEN]
- `larger_clap_general` is het meest geschikte model voor deze toepassing [VERTALEN]
- Het model is robuust tegen additief ruis, wat buiteninstallatie zonder dure behuizing mogelijk maakt [VERTALEN]
- Edge deployment op Raspberry Pi is haalbaar maar vereist zorgvuldig resourcebeheer [VERTALEN]

[AANVULLEN — directe beantwoording van de probleemvraag en deelvragen nog toe te voegen]

---

## Aanbevelingen

*Uit bron:*

- Opschalen naar een wijkbreed netwerk van apparaten met dashboards en alerts [VERTALEN]
- Explainability ontwikkelen zodat niet-ML-bewoners de output kunnen interpreteren [VERTALEN]
- Nieuwe locaties toevoegen aan `sound_scapes.py` [VERTALEN]

[AANVULLEN — aanbevelingen dienen expliciet voort te vloeien uit de conclusies; onderbouwing toevoegen]

---

## Bronnenlijst

*Bronverwijzingsstijl: APA*

[AANVULLEN — onderstaande URLs omzetten naar volledige APA-vermeldingen]

- CLAP paper: https://arxiv.org/abs/2211.06687
- CLAP model (Hugging Face): https://huggingface.co/laion/larger_clap_general
- Dataset UrbanSoundsNew: https://huggingface.co/datasets/UrbanSounds/UrbanSoundsNew
- GitHub repository: https://github.com/MichielBontenbal/run_CLAP
- Anthropic. (2025). *Claude Sonnet 4.6* [Large language model]. https://www.anthropic.com

---

## Bijlagen

**Bijlage A — Onderzoeksplan**
[ONTBREEKT]

**Bijlage B — AI-prompts en -antwoorden**
Overzicht van prompts gebruikt bij het genereren van deze outline met Claude Sonnet 4.6.

**Bijlage C — Deployment-configuratie en volledige scripts**
`urban_sounds_3.5.py`, `sound_scapes.py`, `config.py`-structuur.

**Bijlage D — Notebookoverzicht**
Beschrijving van alle Jupyter notebooks in `1_test_CLAP_notebooks/`.

**Bijlage E — Presentatiemateriaal**
Slides en afbeeldingen uit `4_CLAP_documentation/`.
