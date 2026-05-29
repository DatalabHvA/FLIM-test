# Runbook — Leveringszekerheid

## 1. Overzicht

- **Beschrijving:** Toont per geselecteerd materiaal de stabiliteit van de belangrijkste productielanden. De score is een gewogen risico-indicator op basis van (a) marktaandeel per productieland en (b) de Worldwide Governance Indicators (WGI) van de Wereldbank. In de homepage-tegel zien gebruikers de WGI-score per materiaal als balkje; in detail kunnen ze de wereldwijde spreiding bekijken.
- **Bron-tegel/pagina:** Tegel "Leveringszekerheid" op `Home.py`; detailpagina `pages/02_Leveringszekerheid.py`.
- **Type onderhoud:** Dataset-refresh (twee gekoppelde bronnen).
- **Update-frequentie:** [IN TE VULLEN — voorstel: jaarlijks; UN Comtrade publiceert met enige vertraging, WGI jaarlijks]
- **Laatste update:** [IN TE VULLEN]
- **Volgende update:** [IN TE VULLEN]

## 2. Eigenaarschap

- **Component-eigenaar:** [IN TE VULLEN]
- **Uitvoerder(s):** [IN TE VULLEN]
- **Reviewer:** [IN TE VULLEN]
- **Escalatie:** [IN TE VULLEN]

## 3. Bronnen

### Bron 1 — UN Comtrade (productie/handel per materiaal)

- **Bron:** UN Comtrade Database (`https://comtradeplus.un.org/`).
- **Toegang:** publiek, met free tier rate-limits; API-key aanbevolen voor bulk.
- **Periode in app:** 1962 tot 2024 (laatste beschikbare jaar). Bij update: ophalen tot meest recente volledig jaar.
- **Materiaal → HS-code mapping:** zie tabel hieronder. Deze codes zijn gebruikt om de huidige dataset op te bouwen.

| Materiaal | HS-code |
|---|---|
| Hout algemeen | 4407 |
| Beuken (regels) | 440392 |
| Fins vuren | 440321 |
| Eiken | 440391 |
| Amerikaans noten | 4407 |
| Dennen | 440711 |
| Sparren | 440712 |
| OSB / spaanplaat (board) | 441012 |
| HPL | 3921 |
| Spaanplaat (particleboard) | 441011 |
| Spaanplaat (fiberboard) | 4411 |
| MDF | 441114 |
| Multiplex algemeen | 4412 / 441233 |
| Multiplex Berken / Populieren | 441233 |
| Multiplex hardhoutmix | 441231 |
| Multiplex naaldhout | 441234 |
| Gefineerde multiplex | 441239 |
| Metaal algemeen | 7202 |
| RVS 305 | 7222 |
| Aluminium | 7606 |
| Schuim algemeen | 3921 |
| Polyurethaanschuim LC 2A-6A | 392113 |
| Polyether LP 1A-6A | 392113 |
| Textiel algemeen | 5407 |
| Katoen | 5208 |
| Wol | 5111 |
| Leer | 4107 |
| Plastics algemeen | 3920 |
| Thermoloft (non/woven) | 5603 |
| LDPE | 390110 |
| PE | 392010 |
| Zacht PVC | 392043 |
| Gerecycled plastic | 3915 |
| Gerecycled metaal | 7204 |
| Vlas | 5301 |
| Jute | 5303 |
| Panelen van plantaardige vezels | 6808 |

**Volledige werklijst:** `Analyse_factoren.xlsx` → sheet `Data per factor (incl kwal)` → filter op `Factor = Leveringszekerheid: Geopolitiek risico (productie)` en `Data gebruikt = Ja`.

### Bron 2 — Worldwide Governance Indicators (stabiliteit per land)

- **Bron:** World Bank Worldwide Governance Indicators.
- **Toegang:** `https://www.worldbank.org/en/publication/worldwide-governance-indicators/interactive-data-access`
- **Update-cadans:** jaarlijks (najaar), historische reeks vanaf 1996.
- **Gebruik in app:** de WGI-scores worden per ISO-landcode gekoppeld aan het marktaandeel uit Comtrade om tot de uiteindelijke `supply_risk` per materiaal te komen.

### Afgeleide dataset — `material_market_share.xlsx`

- **Inhoud:** per materiaal de landen welke aan NL exporteren (ISO-code) met hun aandeel in de handel (1636 rijen, kolommen: `ISO`, `market_share`, `material`).
- **Hoe afgeleid:** script voor ophalen data is runbooks/scripts/UN_COMTRADE_API.ipynb

### Licentie & citatievereisten

- **UN Comtrade:** open data, citatie vereist (`Source: UN Comtrade Database`).
- **WGI:** open onder Creative Commons Attribution 4.0; citatie naar Kaufmann, Kraay, Mastruzzi (et al.) — verifieer de actuele citatie-instructie op de WGI-pagina.

## 4. Triggers

- **Tijdgebonden:** jaarlijks. UN Comtrade publiceert data met circa 6-12 maanden vertraging; ververs als een nieuw volledig jaar beschikbaar is.
- **Gebeurtenisgebonden:**
  - Significante geopolitieke gebeurtenis in een top-3 productieland van een materiaal (oorlog, sanctie, exportverbod) → tussentijdse review.
  - Nieuwe WGI-release.
- **Drempelwaarden:** [IN TE VULLEN — bv. >10% verschuiving in marktaandeel van een dominant productieland]

## 5. Update-procedure

### A. Comtrade-data verversen

1. Maak een feature-branch: `feature/update-leveringszekerheid-[YYYY]`.
2. Voor elke HS-code uit de mapping-tabel (sectie 3):
   - Query UN Comtrade voor het meest recente volledige jaar (of meerdere jaren als je een rolling average gebruikt).
   - Filter op export-waarde per `reporter country` (ISO-code).
   - Bereken marktaandeel per land: `share = country_export / world_export`.
3. Schrijf het resultaat naar `material_market_share.xlsx` met kolommen `ISO`, `market_share`, `material`.
4. [IN TE VULLEN — geef de exacte naam/locatie van het bestaande verwerkingsscript, of voeg er één toe als het nog niet bestaat]

### B. WGI-data verversen

1. Download de meest recente WGI-tabel als CSV/XLSX.
2. Houd minimaal de dimensie "Political Stability and Absence of Violence/Terrorism" aan; bevestig welke andere dimensies in de huidige score zijn meegenomen (controleer het scoring-script).
3. Sla op in `data/wgi_[YYYY].xlsx` of -CSV (volg de huidige bestandsconventie in de repo).

### C. Risicoscore berekenen

De `supply_risk`-waarde per materiaal die in `Home.py` op `ss.df_now_lev["supply_risk"]` staat, is een gewogen som over landen:

```
supply_risk_material = Σ (market_share_country × WGI_score_country)
```

[IN TE VULLEN — geef de exacte formule en het script dat dit produceert. Confirm of het script in `widgets.py` zit of een aparte preprocessing-pipeline is.]

### D. Code-aanpassingen

Alleen vereist als:
- Een materiaal wordt toegevoegd/verwijderd.
- De drempelwaardes voor groen/geel/rood (`>= 0.6`, `>= 0.45`) bijgesteld moeten worden in `make_levzeker_bar_figure` in `Home.py`.

## 6. Verificatie

### Sanity-checks

- Som van `market_share` per materiaal komt dicht bij 1.0 (kleine afwijking door rounding acceptabel).
- ISO-codes valide (alle 3-letter ISO 3166-1 alpha-3).
- WGI-scores in verwacht bereik (origineel: −2,5 tot +2,5; check welke normalisatie de app verwacht).
- Geen `NaN` voor Golden-Path materialen.

### Visuele controle

- Streamlit lokaal starten en tegel "Leveringszekerheid" doorlopen.
- Klik op een materiaal en controleer of de wereldkaart/spreiding klopt.
- Verifieer dat de balk-kleuren correct zijn (groen ≥ 0.6, geel ≥ 0.45, rood < 0.45).

### Smoke-test filters

- Doorloop verschillende materiaal-combinaties via de sidebar.
- Controleer of materialen zonder data correct als "Geen data beschikbaar" worden getoond.

## 7. Rollback

- Vorige versie van `material_market_share.xlsx` (en WGI-bestand) terughalen via git.
- Bewaar gedateerde kopie van beide bestanden bij elke release: `data/archive/material_market_share_YYYY-MM-DD.xlsx`.

## 8. Changelog

| Datum | Persoon | Wijziging |
|---|---|---|
| [datum] | [naam] | [korte beschrijving] |

## 9. Bekende aandachtspunten

- **Hiaten** (zie `Analyse_factoren.xlsx` tab `Hiaten`):
  - Thermoloft (non/woven): geen productiedata, alleen exportdata via HS 5603.
  - Schuim algemeen, Polyurethaanschuim LC 2A-6A, Polyether LP 1A-6A: zeer beperkt of geen data.
  - HD/NSA, Buigtriplex, Gerecycled schuim: geen HS-code gevonden.
- **Dubbele HS-codes:** Polyurethaanschuim en Polyether delen beide HS 392113. Resultaten zijn dus niet onderscheidend tussen deze twee subtypes.
- **HS-code revisies:** WCO past HS-codes elke ~5 jaar aan (laatste majeure revisie: HS2022). Bij een nieuwe revisie controleren of alle codes nog bestaan en dezelfde scope dekken.
- **WGI-dimensie keuze:** WGI heeft 6 dimensies (Voice & Accountability, Political Stability, Government Effectiveness, Regulatory Quality, Rule of Law, Control of Corruption). Documenteer welke gebruikt wordt en waarom.
- **Comtrade rate-limits:** free tier heeft beperkingen; gebruik een API-key bij bulk-downloads.
- **Geopolitiek (stabiliteit) wordt nog niet expliciet als aparte tegel gebruikt** — staat in `Analyse_factoren.xlsx` als aparte Factor maar is in de huidige app onderdeel van Leveringszekerheid.
