# Runbook — Wet- en regelgeving

> Anders dan de andere runbooks: géén periodieke dataset, maar **content uit desk research**. Kernactiviteiten zijn bronmonitoring, redactie en verwerking in de app.

## Overzicht
- **Wat:** Relevante Nederlandse en Europese wet- en regelgeving voor de meubelbranche, gefilterd op bedrijfsprofiel (omzet, medewerkers).
- **Pagina's:** `Home.py` (badge-tellingen via `generate_badge` / `generate_badge2` in `widgets.py`) + `pages/04_wet_regelgeving.py`
- **Update-frequentie:** kwartaalreview + direct bij significante nieuwe ontwikkelingen

## Bronnen om te monitoren

**Europees:** EUR-Lex, Publicatieblad EU, DG ENV / DG GROW  
Actieve dossiers: ESPR, EUDR (hout), CSRD / CS3D, PPWR, REACH-updates

**Nederlands:** officielebekendmakingen.nl, Rijksoverheid (CE-dossier), Kamerstukken

**Branche:** Koninklijke CBM, NEN

## Triggers
- Kwartaalreview
- Publicatie van nieuwe verordening of richtlijn relevant voor de meubelbranche
- Inwerkingtredingsdatum van bekende wet nadert binnen 12 maanden
- Gedelegeerde handeling onder bestaande verordening (met name ESPR)

## Update-procedure

1. **Signalering:** noteer relevante wijzigingen met bron-URL, korte samenvatting en impactinschatting (laag / midden / hoog)
2. **Redactie:** per wet/regeling — korte titel, wat is het, wat betekent het voor meubelmakers, voor wie geldt het (profiel-filters), vanaf wanneer, wat kun je nu doen, bron-URL
3. **Check:** drempelwaarden (omzet, FTE) en datums verifiëren tegen de officiële tekst
4. **Verwerking:** pas content aan in `pages/04_wet_regelgeving.py`; update badge-tellingen in `widgets.py` en conditionele logica in `Home.py` als de telling per profiel wijzigt

## Verificatie

- Elke vermelde wet heeft een werkende bron-URL naar de officiële publicatie
- Drempelwaarden (omzet, FTE) kloppen met de officiële tekst; data zijn expliciet (geen "binnenkort")
- Start app lokaal, doorloop tegel met verschillende profiel-filters; bevestig dat badge-tellingen kloppen met het werkelijke aantal getoonde wetten

## Bekende aandachtspunten

- Inhoud kan snel verouderen — overweeg een zichtbare "laatst gecontroleerd op"-datum in de app.
- FLIM is bedoeld als bewustwording, niet als juridisch advies — zorg dat dit expliciet staat in de tegel.
- Sommige wetten raken aan meerdere thema's (bv. EUDR ook relevant voor Leveringszekerheid) — beslis per geval waar de hoofdvermelding zit en kruisverwijs.
- EU-regelgeving krijgt nationale implementatie met eigen termijnen — documenteer beide waar relevant.
