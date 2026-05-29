# Runbook — Wet- en regelgeving

> **Karakter van dit onderdeel:** anders dan Prijsstijgingen en Leveringszekerheid is dit géén dataset die periodiek wordt ververst, maar **content die voortkomt uit desk research**. De runbook-structuur is hierop aangepast: bronmonitoring, redactie-workflow en kwaliteitscontrole staan centraal in plaats van data-pipelines.

## 1. Overzicht

- **Beschrijving:** Toont voor de gebruiker de relevante Nederlandse en Europese wet- en regelgeving voor de meubelbranche, met focus op verplichtingen rondom circulariteit, productontwerp, materiaalkeuze en rapportage. De inhoud verschilt op basis van bedrijfsprofiel (omzet, aantal medewerkers).
- **Bron-tegel/pagina:** Tegel "Wet- en regelgeving" op `Home.py`; detailpagina `pages/04_wet_regelgeving.py`. In de homepage worden badge-aantallen getoond (`generate_badge`, `generate_badge2` in `widgets.py`) die het aantal relevante wetten/normen weergeven.
- **Type onderhoud:** Content-update (desk research, redactie).
- **Update-frequentie:** [IN TE VULLEN — voorstel: kwartaalreview op nieuwe ontwikkelingen, plus continue monitoring op critical alerts]
- **Laatste update:** [IN TE VULLEN]
- **Volgende update:** [IN TE VULLEN]

## 2. Eigenaarschap

- **Component-eigenaar:** [IN TE VULLEN — vermoedelijk Koninklijke CBM, omdat zij dichtbij regelgeving voor de branche zitten; bevestigen]
- **Uitvoerder(s) desk research:** [IN TE VULLEN]
- **Redacteur (Nederlandse formulering, toegankelijkheid):** [IN TE VULLEN]
- **Reviewer (juridische correctheid):** [IN TE VULLEN — overweeg externe jurist of beleidsmedewerker CBM]
- **Technisch uitvoerder (verwerkt content in app):** [IN TE VULLEN]
- **Escalatie:** [IN TE VULLEN]

## 3. Bronnen om te monitoren

In tegenstelling tot Prijsstijgingen zijn er geen dataset-bronnen, maar **te monitoren publicatiekanalen**. Stel een vaste leeslijst op:

### Europees

- **EUR-Lex** (`https://eur-lex.europa.eu/`) — voor verordeningen, richtlijnen, gedelegeerde handelingen. Aanbevolen: maak een opgeslagen zoekopdracht met trefwoorden als *furniture, circular economy, ecodesign, ESPR, EUDR, EPR*.
- **Publicatieblad van de EU** — voor officiële bekendmakingen.
- **Europese Commissie — DG ENV en DG GROW** — beleidsaankondigingen en consultaties.
- **Specifieke dossiers om actief te volgen:**
  - ESPR (Ecodesign for Sustainable Products Regulation) en bijbehorende werkplannen.
  - EUDR (EU Deforestation Regulation) — relevant voor hout.
  - CSRD / CS3D — duurzaamheidsrapportage en due diligence.
  - PPWR (Packaging and Packaging Waste Regulation).
  - REACH-updates (relevant voor lijmen, coatings).
  - [TODO: lijst aanvullen — controleer huidige inhoud van `pages/04_wet_regelgeving.py` voor exhaustieve lijst van besproken wetten]

### Nederlands

- **Officiële Bekendmakingen** (`https://www.officielebekendmakingen.nl/`).
- **Rijksoverheid.nl** — beleidsdossier Circulaire Economie.
- **RVO** — voor subsidies en uitvoeringsregelingen die raken aan wetgeving.
- **Kamerstukken Tweede Kamer** — voor aanstaande wetgeving.

### Branche-specifiek

- **Koninklijke CBM** — eigen publicaties en signalen vanuit de branche.
- **NEN** — voor relevante normen (NEN-EN 1335 kantoorstoelen, etc.).
- **MVO Nederland**, **Het Groene Brein** — voor circulaire context.

### Licentie & citatievereisten

EU- en Nederlandse overheidspublicaties zijn vrij te citeren. Bij parafrasering geen citatie nodig; bij integrale tekstovername bronvermelding plus link.

## 4. Triggers

- **Tijdgebonden:** kwartaalreview, plus jaarlijkse grondige herziening (voorstel: Q1).
- **Gebeurtenisgebonden:**
  - Publicatie van een nieuwe verordening of richtlijn die de meubelbranche raakt.
  - Inwerkingtreding-datum van een al bekende wet komt binnen 12 maanden.
  - Gedelegeerde handeling onder een bestaande verordening (vooral relevant onder ESPR).
  - Significante uitspraak van het Hof van Justitie EU.
  - Bekendmaking van een nieuw Nederlands kabinetsbeleid op CE/duurzaamheid.
- **Signaal-mechanismen:**
  - [Voorstel: Google Alerts of EUR-Lex alerts op trefwoorden]
  - [Voorstel: maandelijkse synchronisatie tussen CBM-beleidsmedewerker en uitvoerder]

## 5. Update-procedure

### Stap 1 — Signalering (continu)

- Monitor bronnen uit sectie 3.
- Log relevante signalen in een **bronnen-log** (bijv. een gedeelde sheet of issue-tracker), met velden: datum signaal, bron-URL, samenvatting (max. 3 zinnen), inschatting impact (laag/midden/hoog), wel/niet opnemen in FLIM.

### Stap 2 — Triage (kwartaal)

- Component-eigenaar en redacteur lopen de bronnen-log samen door.
- Per signaal: opnemen, niet opnemen, of "later, monitoren".
- Resultaat: een prioriteringsoverzicht van wat in deze ronde de app in moet.

### Stap 3 — Redactie

Per wet/regeling die toegevoegd of bijgewerkt wordt:

1. **Korte titel** (max 60 tekens), in begrijpelijk Nederlands, geen jargon.
2. **Wat is het?** — 2-3 zinnen.
3. **Wat betekent dit voor jouw bedrijf?** — toegespitst op meubelmakers.
4. **Voor wie geldt het?** — afhankelijk van filters (omzet/medewerkers/branche).
5. **Vanaf wanneer?** — concrete datum of fase.
6. **Wat kun je nu doen?** — concrete handelingsperspectieven (1-3 stappen).
7. **Bron** — link naar officiële publicatie.

### Stap 4 — Juridische review

- Reviewer (jurist of beleidsmedewerker) controleert op feitelijke juistheid.
- Specifieke aandacht voor data, drempelwaarden (bv. >€50M omzet, >250 FTE), en uitzonderingen.
- Verwerken van reviewer-commentaar.

### Stap 5 — Verwerking in app

- Maak een feature-branch: `feature/update-wetgeving-[YYYY-Q]`.
- Pas content aan in `pages/04_wet_regelgeving.py` en/of de badge-tellingen in `widgets.py` (`generate_badge`, `generate_badge2`).
- Update conditionele logica in `Home.py` als de telling per profiel (`omzet_value == ">€50M"` of `medewerkers_value == "250+ fte"`) wijzigt.
- Pull request met de reviewer als verplichte reviewer.

### Stap 6 — Publicatie

- Merge naar `main`.
- Update changelog (sectie 8).
- Communiceer wijziging naar CBM-leden via gebruikelijk kanaal [IN TE VULLEN].

## 6. Verificatie

### Inhoudelijk

- Elke vermelde wet heeft een werkende bron-URL die naar de officiële publicatie wijst.
- Drempelwaardes (omzet, FTE) komen overeen met de officiële tekst.
- Ingangsdata zijn correct en bij voorkeur expliciet (geen "binnenkort").

### Redactioneel

- Tekst is gericht aan een ondernemer, niet aan een jurist.
- Geen "EU-jargon" zonder uitleg (afkortingen voluit bij eerste gebruik).
- Handelingsperspectieven zijn concreet en uitvoerbaar voor een MKB-meubelmaker.

### Visueel / functioneel

- Start Streamlit lokaal. Doorloop de tegel met verschillende profiel-filters.
- Bevestig dat badge-tellingen kloppen met het werkelijke aantal getoonde wetten/normen.
- Controleer dat conditionele content (>€50M / 250+ fte) correct verschijnt en verdwijnt.

## 7. Rollback

- Vorige versie van wet-content terug te halen via git.
- Bij feitelijke onjuistheid die na publicatie wordt opgemerkt: hotfix-branch, met versnelde review.

## 8. Changelog

| Datum | Persoon | Wijziging |
|---|---|---|
| [datum] | [naam] | [bv. ESPR-werkplan 2025-2027 toegevoegd, drempelwaarde CSRD aangepast naar wave 2-bedrijven] |

## 9. Bekende aandachtspunten

- **Wet- en regelgeving is altijd in beweging:** een halfjaar oude vermelding kan al achterhaald zijn. Communiceer een "laatst gecontroleerd op"-datum in de app zelf zodat gebruikers weten hoe vers de informatie is.
- **Disclaimer:** de FLIM-tool is bedoeld als bewustwording, niet als juridisch advies. Maak dit expliciet in de tegel of detailpagina.
- **EU/NL-verschil:** veel EU-regelgeving krijgt nationale implementatie met eigen termijnen en uitvoeringsregels. Documenteer beide.
- **Risico van overlap:** sommige wetten raken aan meerdere FLIM-thema's (bv. EUDR raakt aan zowel Wet- en regelgeving als Leveringszekerheid). Beslis per geval waar de hoofdvermelding zit en kruisverwijs.
- **Subsidies en wet- en regelgeving zijn verwant** (subsidies vloeien vaak voort uit beleid). Stem updates af met de runbook van het subsidies-onderdeel.
