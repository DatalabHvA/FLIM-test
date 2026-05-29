# Runbook — Prijsstijgingen

## 1. Overzicht

- **Beschrijving:** Toont per geselecteerd materiaal de prijsvariatie t.o.v. een basisjaar (2015 = 1.00). De balken in de homepage-tegel zijn gekleurd op basis van de relatieve stijging (groen ≤10%, geel ≤20%, rood >20%).
- **Bron-tegel/pagina:** Tegel "Prijsontwikkelingen" op `Home.py`; detailpagina `pages/01_Prijsstijgingen.py`.
- **Type onderhoud:** Dataset-refresh.
- **Update-frequentie:** [IN TE VULLEN — voorstel: jaarlijks Q1, of halfjaarlijks bij sterk fluctuerende materialen]
- **Laatste update:** [IN TE VULLEN — meest recente datum in `prijzen.xlsx`]
- **Volgende update:** [IN TE VULLEN]

## 2. Eigenaarschap

- **Component-eigenaar:** [IN TE VULLEN — wie is verantwoordelijk binnen HvA Datalab/CBM/Circularities?]
- **Uitvoerder(s):** [IN TE VULLEN]
- **Reviewer:** [IN TE VULLEN]
- **Escalatie:** [IN TE VULLEN]

## 3. Bronnen

De prijsdata is een mix van meerdere bronnen. Welke materiaal-kolom uit welke bron komt is vastgelegd via een **ID-koppeling** tussen `prijzen.xlsx` (sheet `Datasheet 260218 (def)`) en `Analyse_factoren.xlsx` (sheet `Data per factor (incl kwal)`).

### Bronoverzicht (per categorie)

| Categorie | Bron | Toegang |
|---|---|---|
| Hout massief (eiken, beuken, sparren, dennen, fins vuren) | Statistisches Bundesamt (Destatis), Genesis-tabel **61231** | `https://www-genesis.destatis.de/datenbank/online/table/61231-0002` t/m `-0006` |
| Hout plaatmateriaal (MDF, multiplex, spaanplaat) | FRED (Federal Reserve Economic Data) | `https://fred.stlouisfed.org/series/WPU0922`, `WPU09220141`, `WPU083` |
| Metaal algemeen, Textiel algemeen, Leer, Plastics algemeen, Schuim algemeen, Thermoloft | Eurostat PPI (NACE-codes C25, C13, C15, C2221, C2016, C1395) | Eurostat databrowser |
| RVS 305 | London Metal Exchange + Outokumpu surcharge (Gold) **of** FRED (huidig in gebruik) | LME/Outokumpu (handmatig); FRED via API |
| Aluminium | London Metal Exchange | LME (handmatig) |
| Polyurethaanschuim LC 2A-6A | FRED | FRED |
| Katoen, Wol | FRED | FRED |
| LDPE, PE | FRED unlaminated sheet + PlasticPortal (LDPE film) | FRED / PlasticPortal |
| Gerecycled kunststof, Gerecycled metaal | FRED | FRED |

### ID-koppeling

De kolommen in `prijzen.xlsx` zijn genummerd met een ID (1, 2, 3, ... 43). Diezelfde ID staat in `Analyse_factoren.xlsx` in de kolom `ID`, samen met `Bron`, `Periode`, `Kwaliteitsscore` en het `MVP Prototype / Golden Path`-label.

**Bij elke update: controleer of er nieuwe IDs zijn toegevoegd, en of bestaande IDs nog dezelfde bron hebben.**

### Licentie & citatievereisten

- **Destatis:** open data onder voorwaarden van Statistisches Bundesamt; bronvermelding `© Statistisches Bundesamt (Destatis), [jaar]` is verplicht.
- **FRED:** publiek toegankelijk; bronvermelding gewenst.
- **Eurostat:** publiek; standaard bronvermelding.
- **LME, Outokumpu, PlasticPortal:** *commerciële bronnen* — verifieer licentievoorwaarden vóór hergebruik. [TODO: dit zelf checken — onduidelijk uit de aangeleverde stukken]

## 4. Triggers

- **Tijdgebonden:** [IN TE VULLEN — voorstel: jaarlijks in Q1 alle reeksen verversen]
- **Gebeurtenisgebonden:**
  - Grote marktontwikkelingen (bv. nieuwe export-restricties op grondstoffen, sterke valutaschommelingen) kunnen een tussentijdse update rechtvaardigen.
  - Wijziging van Destatis tabel-IDs of Eurostat NACE-codes vereist code-aanpassing.
- **Drempelwaarden:** [IN TE VULLEN — bijv. >15% beweging in een hoofdmateriaal sinds laatste update]

## 5. Update-procedure

### Voorbereiding

1. Maak een feature-branch: `feature/update-prijzen-[YYYY-Q]`
2. Open `Analyse_factoren.xlsx` → sheet `Data per factor (incl kwal)` → filter op `Factor = Prijsstijgingen` en `Data gebruikt = Ja`. Dit is de **werklijst**.

### Per bron

**Destatis (hout massief):**
1. Ga naar elke Genesis-tabel uit de werklijst (61231-0002 t/m -0006).
2. Download de tijdreeks vanaf 2015 in dezelfde structuur als de huidige kolommen.
3. Normaliseer naar basis 2015-01 = 1.00.
4. Plak in `prijzen.xlsx` sheet `Datasheet 260218 (def)` onder de juiste ID-kolom.

**FRED (plaatmateriaal, schuim, kunststof, katoen, wol, gerecycled):**
1. Per FRED-series-URL: download CSV.
2. Normaliseer naar basis 2015-01 = 1.00 (of pas het basisjaar consistent toe; controleer huidige conventie in `Datasheet 260218 (def)`).
3. Plak in `prijzen.xlsx` onder juiste ID-kolom.

**Eurostat (algemene categorieën, NACE-codes):**
1. Open de PPI-databrowser, filter op de juiste NACE-code.
2. Download monthly, vanaf 2015.
3. Normaliseer en plak onder juiste ID.

**LME / Outokumpu / PlasticPortal:**
1. [IN TE VULLEN — handmatige procedure; documenteer hier de exacte stappen, accounts, exports]

### Codepaden / bestanden die meegaan

- `data/prijzen.xlsx` of de afgeleide CSV die de app daadwerkelijk inleest (verifieer welk pad de Streamlit-app gebruikt; in `Home.py` wordt `ss.df_now_prijs` aangesproken — herleidbaar via `widgets.py`).
- Eventueel `widgets.py` als er materialen worden toegevoegd of hernoemd.

### Branch / commit-conventie

- Branch: `feature/update-prijzen-[YYYY-Q]`
- Commit-bericht: `data: refresh prijsstijgingen [YYYY-Q] — sources: Destatis, FRED, Eurostat`
- PR-titel: `Prijsstijgingen Q[X] [YYYY] refresh`

## 6. Verificatie

### Sanity-checks

- Geen `NaN`-waarden in de Golden Path-materialen (zie `MVP Prototype / Golden Path = Gold` in `Analyse_factoren.xlsx`).
- Aantal rijen klopt met aantal maanden tussen 2015-01 en meest recente datapunt.
- Eerste rij (2015-01) staat overal op 1.00 (of waarde van basisjaar).
- Geen extreme uitschieters (bv. >5× basiswaarde) tenzij verifieerbaar.

### Visuele controle

- Start Streamlit-app lokaal: `streamlit run Home.py`.
- Doorloop de tegel "Prijsontwikkelingen" met standaard filterinstellingen.
- Bekijk detailpagina `01_Prijsstijgingen.py` per Golden-Path materiaal.
- Controleer dat balken kleuren correct (groen/geel/rood) op basis van `risk2 * 100`.

### Smoke-test filters

- Doorloop minimaal: B2C / B2B / Overheid (klanttype), kleine en grote omzet, alle drie hoofdmaterialen.

## 7. Rollback

- Vorige versie van `prijzen.xlsx` is altijd terug te halen via git (`git checkout HEAD~1 -- data/prijzen.xlsx`).
- Bewaar voor de zekerheid een gedateerde kopie buiten de repo (bijv. `data/archive/prijzen_YYYY-MM-DD.xlsx`) bij elke release.

## 8. Changelog

| Datum | Persoon | Wijziging |
|---|---|---|
| [datum] | [naam] | [bv. Refresh alle Destatis-reeksen t/m Q4 2025; geen structurele wijzigingen] |

## 9. Bekende aandachtspunten

- **Destatis URLs:** Genesis-tabellen kunnen periodiek hernummeren. Controleer altijd of `61231-XXXX` nog dezelfde inhoud heeft.
- **Spaanplaat heeft twee FRED-bronnen:** `WPU0922` (gebruikt) en FAOSTAT (niet gebruikt). Niet vermengen.
- **LDPE en PE delen ID 20** in `prijzen.xlsx` — controleer of dit bewust is.
- **PlasticPortal data is niet altijd consistent** met FRED unlaminated sheet — beslis per update welke leidend is.
- **Datakwaliteit (DQS-score):** in `Analyse_factoren.xlsx` sheet `FLIM DQS` staat het scoringsmodel. Update kwaliteitsscores bij significante wijziging van een bron.
- **Hiaten:** geen FRED-data voor Fins vuren, Amerikaans noten, OSB, HPL, Buigtriplex — zie tab `Hiaten` in `Analyse_factoren.xlsx`. Tony zou hiernaar kijken.
