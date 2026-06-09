# Runbook — Prijsstijgingen

## Overzicht
- **Wat:** Prijsvariatie per materiaal t.o.v. basisjaar (2015 = 1.00). Balken in de homepage-tegel: groen ≤10%, geel ≤20%, rood >20%.
- **Pagina's:** `Home.py` (tegel) + `pages/01_Prijsstijgingen.py`
- **Update-frequentie:** jaarlijks Q1 (voorstel)
- **Bestanden:** `data/prijzen.xlsx`, mapping in `Analyse_factoren.xlsx` → sheet `Data per factor (incl kwal)` → filter `Prijsstijgingen` + `Data gebruikt = Ja`

## Bronnen

| Categorie | Bron | Referentie |
|---|---|---|
| Hout massief (eiken, beuken, sparren, dennen, fins vuren) | Destatis Genesis | tabellen 61231-0002 t/m -0006 |
| Hout plaatmateriaal (MDF, multiplex, spaanplaat) | FRED | WPU0922, WPU09220141, WPU083 |
| Metaal, Textiel, Leer, Plastics, Schuim, Thermoloft | Eurostat PPI | NACE C25, C13, C15, C2221, C2016, C1395 |
| RVS 305 | FRED | - |
| Aluminium | LME | handmatig |
| Polyurethaan, Katoen, Wol, LDPE, PE, Gerecycled | FRED | - |

> LME, Outokumpu en PlasticPortal zijn commerciële bronnen — controleer licentievoorwaarden voor hergebruik.

## Triggers
- Jaarlijks Q1
- Grote marktontwikkelingen (exportrestricties, valutaschommelingen)
- Gewijzigde Destatis tabel-IDs of Eurostat NACE-codes → dan ook code-aanpassing nodig

## Update-procedure

1. Open werklijst: `Analyse_factoren.xlsx` → `Data per factor (incl kwal)` → filter `Prijsstijgingen` + `Data gebruikt = Ja`
2. Per bron: download tijdreeks vanaf 2015, normaliseer naar 2015-01 = 1.00
3. Plak onder de juiste ID-kolom in `prijzen.xlsx` → sheet `Datasheet 260218 (def)`
4. LME / Outokumpu / PlasticPortal: handmatige procedure — nog te documenteren

## Verificatie

- Geen `NaN` in Golden Path-materialen (`MVP Prototype / Golden Path = Gold`)
- Rij 2015-01 = 1.00 voor alle kolommen
- Geen onverklaarde uitschieters (>5× basiswaarde)
- Start app lokaal, doorloop tegel + detailpagina; controleer balk-kleuren (groen/geel/rood)

## Bekende aandachtspunten

- Destatis Genesis-tabelnummers kunnen hernummeren — controleer bij elke update.
- Spaanplaat: gebruik alleen `WPU0922` (FRED), niet FAOSTAT.
- PlasticPortal is niet altijd consistent met FRED unlaminated sheet — beslis per update welke leidend is.
- Datakwaliteitsscores staan in `Analyse_factoren.xlsx` → sheet `FLIM DQS`; update bij significante bronwijziging.
