import streamlit as st
from streamlit_plotly_events import plotly_events
import streamlit.components.v1 as components
import sys
sys.path.append("..")
from widgets import *

ss = st.session_state
init_session_state()
log_event("Wet_regelgeving", "page_load")

st.set_page_config(page_title="Wet- en regelgeving - Landingspagina", layout="wide")
st.markdown(
    """
    <style>
      /* pull content up */
      .block-container { padding-top: 0.9rem !important; }
      /* compact header */
      header[data-testid="stHeader"] { height: 1.2rem; }
      [data-testid="stSidebarNav"] {display: none;}
      [data-testid="stSidebar"] .block-container {
          padding-top: 0 !important;
      }

    section[data-testid="stSidebar"] .block-container > div:first-child,
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child {
    margin-top: -60px !important;   /* <- adjust this number */
    }

    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.page_link("Home.py", label="⬅ Terug naar Home")

    st.header("Filters")
    widget_omzet()
    widget_klantsegment()
    widget_materialen()

# ── Data ────────────────────────────────────────────────────────────────────────
WETTEN = [
    {
        "naam": "REACH",
        "jaar": "2007",
        "jaar_sort": 2007,
        "sub": "Chemische stoffen — doorlopend geüpdatet",
        "doelgroepen": ["producent", "importeur", "distributeur"],
        "kleur": "#534AB7",
        "kleur_licht": "#EEEDFE",
        "kleur_tekst": "#3C3489",
        "omschrijving": "Registratie, evaluatie en autorisatie van chemische stoffen in verf, lijmen, coatings en meubels.",
        "risico": "Hoge boetes, stillegging productie, recall-opdrachten. Verboden stoffen maken producten onverkoopbaar.",
        "ernst": "Hoog",
        "link": "https://ondernemersplein.overheid.nl/wetten-en-regels/verplichtingen-bij-chemische-stoffen-reach/",
    },
    {
        "naam": "CBAM — rapportageplicht",
        "jaar": "okt 2023",
        "jaar_sort": 2023,
        "sub": "Koolstofintensieve producten (staal, aluminium)",
        "doelgroepen": ["importeur"],
        "kleur": "#BA7517",
        "kleur_licht": "#FAEEDA",
        "kleur_tekst": "#633806",
        "omschrijving": "EU-bedrijven die koolstofintensieve producten zoals staal en aluminium importeren moeten CO₂-verklaringen aanleveren.",
        "risico": "Naheffingen bij verkeerde rapportage. Import zonder correcte CO₂-verklaring kan worden tegengehouden.",
        "ernst": "Hoog",
        "link": "https://flim-tool.streamlit.app/~/+/x_CBAM",
    },
    {
        "naam": "ESPR",
        "jaar": "jul 2024",
        "jaar_sort": 2024,
        "sub": "Ecodesign — gefaseerde uitrol vanaf 2026",
        "doelgroepen": ["producent", "importeur", "distributeur"],
        "kleur": "#1D9E75",
        "kleur_licht": "#E1F5EE",
        "kleur_tekst": "#085041",
        "omschrijving": "Stelt minimumvereisten aan levensduur, repareerbaarheid en gebruik van gerecyclede materialen voor producten op de EU-markt.",
        "risico": "Verkoopverbod zonder ecodesign-goedkeuring. Boetes bij schending. OEM's stellen leveranciers aansprakelijk.",
        "ernst": "Hoog",
        "link": "https://flim-tool.streamlit.app/~/+/x_ESPR",
    },
    {
        "naam": "Right to Repair",
        "jaar": "jul 2024",
        "jaar_sort": 2024,
        "sub": "Consumentenproducten incl. meubels",
        "doelgroepen": ["producent", "distributeur"],
        "kleur": "#1D9E75",
        "kleur_licht": "#E1F5EE",
        "kleur_tekst": "#085041",
        "omschrijving": "Fabrikanten en verkopers moeten reparatie van producten faciliteren. Omzetting door lidstaten voor juli 2026.",
        "risico": "Sancties bij niet naleven reparatie- of informatieplicht.",
        "ernst": "Midden",
        "link": "https://commission.europa.eu/law/law-topic/consumer-protection-law/directive-repair-goods_en",
    },
    {
        "naam": "VSME",
        "jaar": "2024",
        "jaar_sort": 2024,
        "sub": "MKB in de keten van CSRD-plichtige klanten",
        "doelgroepen": ["mkb"],
        "kleur": "#378ADD",
        "kleur_licht": "#E6F1FB",
        "kleur_tekst": "#0C447C",
        "omschrijving": "Vrijwillige standaard voor MKB om duurzaamheidsdata gestructureerd te verzamelen en te delen met grote klanten.",
        "risico": "Niet leveren van emissiedata kan contractbreuk opleveren met grote klanten die CSRD-rapportageplichtig zijn.",
        "ernst": "Midden",
        "link": "https://flim-tool.streamlit.app/~/+/x_VSME",
    },
    {
        "naam": "CSRD",
        "jaar": "2025",
        "jaar_sort": 2025,
        "sub": "Grote bedrijven verplicht rapporteren",
        "doelgroepen": ["mkb"],
        "kleur": "#378ADD",
        "kleur_licht": "#E6F1FB",
        "kleur_tekst": "#0C447C",
        "omschrijving": "Grote bedrijven moeten rapporteren over CO₂-uitstoot, grondstoffengebruik en ketenimpact. MKB-leveranciers krijgen indirect te maken via klanteis.",
        "risico": "Leverancier zonder data valt af als ketenpartner. Contractbreuk mogelijk.",
        "ernst": "Hoog",
        "link": "https://flim-tool.streamlit.app/~/+/x_VSME",
    },
    {
        "naam": "EUDR",
        "jaar": "dec 2025",
        "jaar_sort": 2025,
        "sub": "Ontbossingsvrije hout- en houtproducten",
        "doelgroepen": ["producent", "importeur"],
        "kleur": "#BA7517",
        "kleur_licht": "#FAEEDA",
        "kleur_tekst": "#633806",
        "omschrijving": "Bedrijven moeten aantonen dat hout niet afkomstig is van recent ontboste gebieden. Vraagt om ketentraceerbaarheid.",
        "risico": "Boetes tot 4% van omzet, inbeslagname goederen, exportstop. Blokkade grondstoffen bij risicoherkomst.",
        "ernst": "Hoog",
        "link": "https://flim-tool.streamlit.app/~/+/x_EUDR",
    },
    {
        "naam": "CBAM — financiële verplichting",
        "jaar": "2026",
        "jaar_sort": 2026,
        "sub": "Heffing op import koolstofintensieve producten",
        "doelgroepen": ["importeur"],
        "kleur": "#BA7517",
        "kleur_licht": "#FAEEDA",
        "kleur_tekst": "#633806",
        "omschrijving": "Financiële heffing op import van staal en aluminium zonder afdoende CO₂-prijs in het land van herkomst.",
        "risico": "Directe kostenstijging op import. Marginedruk zonder aanpassing van materiaalinkoop.",
        "ernst": "Hoog",
        "link": "https://flim-tool.streamlit.app/~/+/x_CBAM",
    },
    {
        "naam": "DPP — Digitaal Productpaspoort",
        "jaar": "2027",
        "jaar_sort": 2027,
        "sub": "Verplichting voor meubels (in ontwikkeling)",
        "doelgroepen": ["producent", "distributeur"],
        "kleur": "#534AB7",
        "kleur_licht": "#EEEDFE",
        "kleur_tekst": "#3C3489",
        "omschrijving": "Producenten leggen materiaalsamenstelling, onderhoudsinfo en recyclingmogelijkheden digitaal vast per product.",
        "risico": "Boetes bij onvolledige paspoorten. Producten zonder geldig DPP worden geweigerd door retailer of EU-grenscontrole.",
        "ernst": "Hoog",
        "link": "https://flim-tool.streamlit.app/~/+/x_DPP",
    },
    {
        "naam": "UPV Meubels",
        "jaar": "2029–2030",
        "jaar_sort": 2029,
        "sub": "Uitgebreide Producentenverantwoordelijkheid NL",
        "doelgroepen": ["producent", "importeur"],
        "kleur": "#D85A30",
        "kleur_licht": "#FAECE7",
        "kleur_tekst": "#712B13",
        "omschrijving": "Producenten worden financieel verantwoordelijk voor inzameling, verwerking en recycling van meubels aan het einde van de levensduur.",
        "risico": "Boetes bij onderregistratie. Claims van retailers voor non-compliance in de productieketen.",
        "ernst": "Midden",
        "link": "https://flim-tool.streamlit.app/~/+/x_UPV",
    },
]

DOELGROEP_LABELS = {
    "producent":   ("🏭", "Producent / fabrikant"),
    "importeur":   ("🚚", "Importeur / leverancier"),
    "distributeur":("🏪", "Distributeur / verkoper"),
    "mkb":         ("🏢", "Grote bedrijven / MKB"),
}

ERNST_KLEUREN = {
    "Hoog":   ("#FCEBEB", "#791F1F"),
    "Midden": ("#FAEEDA", "#633806"),
}

# ── Stijl injecteren ─────────────────────────────────────────────────────────
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background: #f8f7f4; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; }
h1 { font-size: 1.4rem !important; font-weight: 600 !important; }
.stTabs [data-baseweb="tab"] { font-size: 13px; }
div[data-testid="metric-container"] { background: white; border: 0.5px solid #e2e0d8;
    border-radius: 10px; padding: 12px 16px; }
</style>
""", unsafe_allow_html=True)

# ── Header ───────────────────────────────────────────────────────────────────
st.title("📋 Wetgeving tijdlijn — meubel & interieur")
st.caption("FLIM-tool · Factor 4: Wet- en regelgeving · Gefilterd op doelgroep en periode")

st.divider()

# ── Filters ───────────────────────────────────────────────────────────────────
col_f1, col_f2, col_f3 = st.columns([2, 2, 1])

with col_f1:
    doelgroep_opties = {
        "Alles": "all",
        "🏭 Producent / fabrikant": "producent",
        "🚚 Importeur / leverancier": "importeur",
        "🏪 Distributeur / verkoper": "distributeur",
        "🏢 Grote bedrijven / MKB": "mkb",
    }
    gekozen_label = st.selectbox(
        "Doelgroep",
        options=list(doelgroep_opties.keys()),
        index=0,
    )
    gekozen_doelgroep = doelgroep_opties[gekozen_label]

with col_f2:
    ernst_filter = st.multiselect(
        "Ernst risico",
        options=["Hoog", "Midden"],
        default=["Hoog", "Midden"],
    )

with col_f3:
    jaar_max = st.selectbox(
        "Tot en met",
        options=["2024", "2025", "2026", "2027", "2030"],
        index=4,
    )

# ── Filter toepassen ──────────────────────────────────────────────────────────
gefilterd = [
    w for w in WETTEN
    if (gekozen_doelgroep == "all" or gekozen_doelgroep in w["doelgroepen"])
    and w["ernst"] in ernst_filter
    and w["jaar_sort"] <= int(jaar_max)
]

# ── Metrics ───────────────────────────────────────────────────────────────────
m1, m2, m3, m4 = st.columns(4)
m1.metric("Regelingen zichtbaar", len(gefilterd))
m2.metric("Met hoog risico", sum(1 for w in gefilterd if w["ernst"] == "Hoog"))
m3.metric("Vroegste deadline", gefilterd[0]["jaar"] if gefilterd else "—")
m4.metric("Laatste deadline", gefilterd[-1]["jaar"] if gefilterd else "—")

st.divider()

# ── Tabbladen ─────────────────────────────────────────────────────────────────
tab_tijdlijn, tab_tabel, tab_risico = st.tabs([
    "📅 Tijdlijn",
    "📊 Tabeloverzicht",
    "⚠️ Risicomatrix",
])

# ────────────────────────────────────────────────────────────────────────────────
# TAB 1 — Tijdlijn (HTML-widget)
# ────────────────────────────────────────────────────────────────────────────────
with tab_tijdlijn:
    if not gefilterd:
        st.info("Geen regelingen gevonden voor deze selectie.")
    else:
        # Bouw HTML-rijen dynamisch op basis van gefilterde data
        rijen_html = ""
        for w in gefilterd:
            doelgroep_badges = ""
            for dg in w["doelgroepen"]:
                if dg in DOELGROEP_LABELS:
                    icoon, label = DOELGROEP_LABELS[dg]
                    doelgroep_badges += (
                        f'<span style="display:inline-flex;align-items:center;gap:3px;'
                        f'font-size:11px;font-weight:500;padding:2px 8px;border-radius:12px;'
                        f'background:{w["kleur_licht"]};color:{w["kleur_tekst"]};'
                        f'margin-right:4px;white-space:nowrap;">'
                        f'{icoon} {label}</span>'
                    )

            ernst_bg, ernst_fg = ERNST_KLEUREN.get(w["ernst"], ("#eee", "#333"))
            ernst_badge = (
                f'<span style="font-size:10px;font-weight:500;padding:2px 8px;'
                f'border-radius:10px;background:{ernst_bg};color:{ernst_fg};">'
                f'{w["ernst"]}</span>'
            )

            rijen_html += f"""
            <div style="display:flex;align-items:flex-start;gap:12px;
                        padding:10px 0;border-bottom:0.5px solid #e2e0d8;">
                <div style="min-width:52px;font-size:11px;color:#888;
                            text-align:right;padding-top:2px;line-height:1.4;">
                    {w["jaar"]}
                </div>
                <div style="width:3px;min-height:60px;background:{w["kleur"]};
                            border-radius:2px;flex-shrink:0;margin-top:4px;"></div>
                <div style="flex:1;">
                    <div style="display:flex;align-items:center;gap:8px;margin-bottom:3px;">
                        <span style="font-size:13px;font-weight:600;color:#1a1a18;">
                            {w["naam"]}
                        </span>
                        {ernst_badge}
                    </div>
                    <div style="font-size:11px;color:#888;margin-bottom:6px;">
                        {w["sub"]}
                    </div>
                    <div style="font-size:12px;color:#3d3d3a;margin-bottom:8px;
                                line-height:1.5;">
                        {w["omschrijving"]}
                    </div>
                    <div style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:6px;">
                        {doelgroep_badges}
                    </div>
                    <a href="{w["link"]}" target="_blank"
                       style="font-size:11px;color:{w["kleur"]};text-decoration:none;">
                        Meer info →
                    </a>
                </div>
            </div>
            """

        tijdlijn_html = f"""
        <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
                    background:white;border:0.5px solid #e2e0d8;border-radius:12px;
                    padding:16px 20px;">
            <div style="display:flex;align-items:center;gap:8px;
                        padding-bottom:10px;border-bottom:1px solid #e2e0d8;
                        margin-bottom:4px;">
                <span style="font-size:11px;color:#888;min-width:52px;text-align:right;">
                    Jaar
                </span>
                <div style="width:3px;"></div>
                <span style="font-size:11px;font-weight:500;color:#888;">
                    {len(gefilterd)} regeling(en) — {gekozen_label}
                </span>
            </div>
            {rijen_html}
        </div>
        """

        components.html(tijdlijn_html, height=min(160 + len(gefilterd) * 145, 900),
                        scrolling=True)

# ────────────────────────────────────────────────────────────────────────────────
# TAB 2 — Tabel
# ────────────────────────────────────────────────────────────────────────────────
with tab_tabel:
    if not gefilterd:
        st.info("Geen regelingen gevonden voor deze selectie.")
    else:
        import pandas as pd

        tabel_data = []
        for w in gefilterd:
            dg_labels = ", ".join(
                DOELGROEP_LABELS[dg][1] for dg in w["doelgroepen"]
                if dg in DOELGROEP_LABELS
            )
            tabel_data.append({
                "Wet / Regeling": w["naam"],
                "Jaar": w["jaar"],
                "Van toepassing op": dg_labels,
                "Ernst": w["ernst"],
                "Omschrijving": w["omschrijving"],
            })

        df = pd.DataFrame(tabel_data)

        def kleur_ernst(val):
            if val == "Hoog":
                return "background-color: #FCEBEB; color: #791F1F; font-weight: 500"
            elif val == "Midden":
                return "background-color: #FAEEDA; color: #633806; font-weight: 500"
            return ""

        styled = df.style.map(kleur_ernst, subset=["Ernst"])
        st.dataframe(styled, use_container_width=True, hide_index=True)

        st.download_button(
            label="⬇ Download als CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="flim_wetgeving.csv",
            mime="text/csv",
        )

# ────────────────────────────────────────────────────────────────────────────────
# TAB 3 — Risicomatrix (HTML-widget)
# ────────────────────────────────────────────────────────────────────────────────
with tab_risico:
    if not gefilterd:
        st.info("Geen regelingen gevonden voor deze selectie.")
    else:
        risico_rijen = ""
        for w in gefilterd:
            ernst_bg, ernst_fg = ERNST_KLEUREN.get(w["ernst"], ("#eee", "#333"))
            risico_rijen += f"""
            <div style="display:grid;grid-template-columns:140px 1fr 70px;
                        gap:12px;align-items:start;padding:10px 0;
                        border-top:0.5px solid #e2e0d8;font-size:12px;">
                <div>
                    <span style="font-size:11px;font-weight:600;
                                 padding:2px 8px;border-radius:10px;
                                 background:{w["kleur_licht"]};
                                 color:{w["kleur_tekst"]};">
                        {w["naam"]}
                    </span>
                    <div style="font-size:10px;color:#888;margin-top:4px;">
                        {w["jaar"]}
                    </div>
                </div>
                <div style="color:#3d3d3a;line-height:1.5;">{w["risico"]}</div>
                <div>
                    <span style="font-size:11px;font-weight:500;padding:2px 8px;
                                 border-radius:10px;background:{ernst_bg};
                                 color:{ernst_fg};">
                        {w["ernst"]}
                    </span>
                </div>
            </div>
            """

        risico_html = f"""
        <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
                    background:white;border:0.5px solid #e2e0d8;border-radius:12px;
                    padding:16px 20px;">
            <div style="display:grid;grid-template-columns:140px 1fr 70px;gap:12px;
                        padding-bottom:8px;border-bottom:1px solid #e2e0d8;
                        font-size:11px;font-weight:600;color:#888;">
                <span>Wet</span>
                <span>Financieel risico</span>
                <span>Ernst</span>
            </div>
            {risico_rijen}
        </div>
        """

        components.html(risico_html, height=min(100 + len(gefilterd) * 90, 800),
                        scrolling=True)

        st.caption(
            "Bronnen: Europese Commissie, Rijksoverheid, FLIM-tool. "
            "Klik op 'Meer info' in de tijdlijn voor directe links."
        )
