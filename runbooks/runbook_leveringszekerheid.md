# Runbook — Leveringszekerheid

## Overzicht
- **Wat:** Gewogen risico-indicator per materiaal op basis van marktaandeel per productieland × WGI-score.
- **Pagina's:** `Home.py` (tegel) + `pages/02_Leveringszekerheid.py`
- **Update-frequentie:** jaarlijks (UN Comtrade publiceert met 6–12 maanden vertraging)
- **Bestanden:** `data/material_market_share.xlsx`, `data/wgi_governance_scores_2023_with_iso3.xlsx`
- **Script:** `runbooks/scripts/UN_COMTRADE_API.ipynb`

## Bronnen

### UN Comtrade (marktaandeel per land)
- **URL:** `https://comtradeplus.un.org/` — publiek; API-key aanbevolen voor bulk
- **Berekening:** `market_share = country_export / world_export` per HS-code
- **Werklijst:** `Analyse_factoren.xlsx` → `Data per factor (incl kwal)` → filter `Leveringszekerheid: Geopolitiek risico (productie)` + `Data gebruikt = Ja`

| Materiaal | HS-code |
|---|---|
| Hout algemeen | 4407 |
| Beuken | 440392 |
| Fins vuren | 440321 |
| Eiken | 440391 |
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

### WGI (stabiliteit per land)
- **URL:** `https://www.worldbank.org/en/publication/worldwide-governance-indicators`
- **Gebruik:** `supply_risk = Σ (market_share × WGI_score)` per materiaal, gekoppeld op ISO-landcode
- **Let op:** WGI heeft 6 dimensies — documenteer welke dimensie(s) gebruikt worden

## Triggers
- Jaarlijks zodra nieuw volledig Comtrade-jaar beschikbaar is
- Significante geopolitieke gebeurtenis in een top-3 productieland van een materiaal (sanctie, exportverbod)

## Update-procedure

1. **Comtrade:** voer `UN_COMTRADE_API.ipynb` uit voor alle HS-codes uit de werklijst; sla resultaat op als `data/material_market_share.xlsx`
2. **WGI:** download recentste tabel van worldbank.org; vervang/update `data/wgi_governance_scores_[YYYY]_with_iso3.xlsx`
3. **Code-aanpassing** alleen nodig bij: nieuw materiaal toevoegen, of drempelwaarden bijstellen (`>= 0.6` / `>= 0.45`) in `make_levzeker_bar_figure` in `Home.py`

## Verificatie

- Som van `market_share` per materiaal ≈ 1.0
- Alle ISO-codes valide (3-letter alpha-3)
- WGI-scores in verwacht bereik; geen `NaN` voor Golden Path-materialen
- Start app lokaal, controleer balk-kleuren (groen ≥ 0.6, geel ≥ 0.45, rood < 0.45) en wereldkaart per materiaal

## Bekende aandachtspunten

- Thermoloft, Polyurethaanschuim LC, Polyether: beperkte of geen Comtrade-data (zie `Analyse_factoren.xlsx` → `Hiaten`).
- Polyurethaanschuim LC en Polyether delen HS 392113 — resultaten zijn niet onderscheidend tussen deze twee.
- HS-codes worden ~elke 5 jaar herzien (laatste majeure revisie: HS2022) — controleer bij updates.
