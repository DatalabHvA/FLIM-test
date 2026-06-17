# pages/03_Klantvraag_Bars.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import sys'
sys.path.append("..")

from widgets import *

ss = st.session_state
init_session_state()
log_event("Klantvraag", "page_load")

st.set_page_config(page_title="Klantvraag B2B/B2C • Analyse", layout="wide")
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
    widget_klantsegment()
    widget_klanttype()
    

if ss.klanttype_value == 'Overheid':
    st.title("Klantvraag — Overheid")

    st.markdown("""
    <div style="display:flex; gap:16px; margin-bottom:24px;">
        <div style="flex:1; border:2px solid #4472C4; border-radius:12px; padding:20px 24px;">
            <div style="font-size:2.4rem; font-weight:700; color:#4472C4; line-height:1.1;">€60 mln</div>
            <div style="margin-top:10px; font-size:0.95rem; line-height:1.5;">jaarlijkse inkoop Werkplekomgeving Rijksoverheid</div>
            <div style="margin-top:10px; font-size:0.8rem; color:#666; font-style:italic;">(jaarbasis, ref. 2022)</div>
        </div>
        <div style="flex:1; border:2px solid #E8A020; border-radius:12px; padding:20px 24px;">
            <div style="font-size:2.4rem; font-weight:700; color:#E8A020; line-height:1.1;">€85 mrd</div>
            <div style="margin-top:10px; font-size:0.95rem; line-height:1.5;">inkoop diensten en producten Rijksoverheid</div>
            <div style="margin-top:10px; font-size:0.8rem; color:#666; font-style:italic;">(jaarbasis, ref. 2021)</div>
        </div>
        <div style="flex:1; border:2px solid #E37222; border-radius:12px; padding:20px 24px;">
            <div style="font-size:2.4rem; font-weight:700; color:#E37222; line-height:1.1;">50%</div>
            <div style="margin-top:10px; font-size:0.95rem; line-height:1.5;">minder inkoop van primaire grondstoffen in 2030</div>
            <div style="margin-top:10px; font-size:0.8rem; color:#666; font-style:italic;">(doelstelling Rijksoverheid)</div>
        </div>
        <div style="flex:1; border:2px solid #4A9A2C; border-radius:12px; padding:20px 24px;">
            <div style="font-size:2.4rem; font-weight:700; color:#4A9A2C; line-height:1.1;">100%</div>
            <div style="margin-top:10px; font-size:0.95rem; line-height:1.5;">circulair inkopen in 2050</div>
            <div style="margin-top:10px; font-size:0.8rem; color:#666; font-style:italic;">(doelstelling Rijksoverheid)</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""

    In 2021 spendeerde de Rijksoverheid ruim **85 miljard euro** aan ingekochte diensten, producten en werken.
    In 2023 was de inkoop van *Werkplekomgeving (Rijksoverheid)* jaarlijks goed voor zo'n **60 miljoen euro**.

    Het gestelde doel is dat per 2030 al voor **50% minder primaire grondstoffen** ingekocht worden, en om dit te laten toenemen tot **100% circulair in 2050**.
    Tevens is ook de ambitie uitgesproken om vanaf **2030 enkel nog gebruik te maken van circulair meubilair**.
    """)
    st.caption("Bron: [Rijksoverheid](https://www.denkdoeduurzaam.nl/actueel/nieuws/2023/11/13/duurzame-revolutie-op-de-werkplek-focus-op-circulair-meubilair-en-consuminderen)")
    st.markdown("""
    ---

    ### MVOI – Wat is het?

    Maatschappelijk Verantwoord Opdrachtgeven en Inkopen is de inkoopstandaard voor overheidsklanten. De overheid koopt daarmee niet alleen op prijs. Via MVOI weegt zij bij aanbestedingen ook milieu- en sociale effecten mee.
    Dit geldt voor centrale én decentrale overheden, inclusief overheidsinstellingen. Circulair inkopen is één van de volgende zes verplichte thema's:
    """)

    st.markdown('''
<style>
.mvoi-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px 24px;margin-bottom:16px;}
.mvoi-item{display:flex;align-items:center;gap:8px;font-size:0.9rem;}
.mvoi-dot{width:18px;height:18px;border-radius:3px;flex-shrink:0;}
.mvoi-g .mvoi-dot{background-color:#e8f5e9;}
.mvoi-b .mvoi-dot{background-color:#e3f2fd;}
.mvoi-o .mvoi-dot{background-color:#fff3e0;}
.mvoi-p .mvoi-dot{background-color:#f3e5f5;}
.mvoi-r .mvoi-dot{background-color:#fce4ec;}
.mvoi-lg .mvoi-dot{background-color:#f1f8e9;}
.mvoi-item span{color:#31333f;}
</style>
<div class="mvoi-grid">
  <div class="mvoi-item mvoi-g"><div class="mvoi-dot"></div><span>Milieu &amp; Biodiversiteit</span></div>
  <div class="mvoi-item mvoi-b"><div class="mvoi-dot"></div><span>Circulair (incl. inkoop)</span></div>
  <div class="mvoi-item mvoi-o"><div class="mvoi-dot"></div><span>Klimaat</span></div>
  <div class="mvoi-item mvoi-p"><div class="mvoi-dot"></div><span>IMVO (Ketenaansprakelijkheid)</span></div>
  <div class="mvoi-item mvoi-r"><div class="mvoi-dot"></div><span>Diversiteit &amp; Inclusie</span></div>
  <div class="mvoi-item mvoi-lg"><div class="mvoi-dot"></div><span>Sociaal Return</span></div>
</div>
''', unsafe_allow_html=True)

    st.caption('Bron: [RIVM – Trends in MVOI](https://www.rivm.nl/maatschappelijk-verantwoord-opdrachtgeven-en-inkopen/trends-in-mvoi)')

    st.markdown("""
    ### Inzet per MVOI-thema
    """)

    df_mvoi = pd.DataFrame({'jaar' : ['2015-2016', '2017-2018', '2019-2020', '2021-2022'],
                            'Totaal MVOI' : [0.78, 0.87, 0.87, 0.79],
                            'Circulair' : [0.26, 0.35, 0.46, 0.39],
                            'Ketenverantwoordelijkheid' : [0.14, 0.23, 0.14, 0.09]})

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df_mvoi['jaar'],
            y=df_mvoi['Totaal MVOI'],
            mode='lines+markers',
            line=dict(color='#1f5f7a', width=3),
            marker=dict(size=8),
            name='Totaal MVOI'
        )
    )

    fig.update_layout(
        title="Aandeel inkoop/aanbesteding met MVOI-criteria",
        yaxis=dict(
            range=[0.70, 0.90],
            tickformat=".0%",
            showgrid=True,
            gridcolor='lightgrey'
        ),
        xaxis=dict(
            showgrid=False
        ),
        margin=dict(l=40, r=40, t=80, b=40)
    )

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=df_mvoi['jaar'],
            y=df_mvoi['Circulair'],
            mode='lines+markers',
            line=dict(color="#0d394c", width=3),
            marker=dict(size=8),
            name='Circulair'
        )
    )
    fig2.add_trace(
        go.Scatter(
            x=df_mvoi['jaar'],
            y=df_mvoi['Ketenverantwoordelijkheid'],
            mode='lines+markers',
            line=dict(color="#d2a905", width=3),
            marker=dict(size=8),
            name='Ketenverantwoordelijkheid'
        )
    )
    fig2.update_layout(
        title="Inzet per MVOI-thema",
        yaxis=dict(
            range=[0.0, 0.50],
            tickformat=".0%",
            showgrid=True,
            gridcolor='lightgrey'
        ),
        xaxis=dict(
            showgrid=False
        ),
        margin=dict(l=40, r=40, t=80, b=40),
        legend=dict(
            orientation="h",          # horizontaal
            yanchor="top",
            y=-0.25,                  # onder de plot
            xanchor="center",
            x=0.5
        )
    )

    st.write("Meer dan 75% van aanbestedingstrajecten past actief MVOI-criteria toe. Meer dan de helft richt zich op grondstoffen, ontwerp en ketenverantwoordelijkheid. (RIVM, 2023)")

    cols = st.columns(2)
    with cols[0]:
        st.plotly_chart(fig)
    with cols[1]: 
        st.plotly_chart(fig2)

    st.markdown("### Ambitieniveau bij uitvraag MVOI")

    st.write('In 2021-2022 besteedde 79% van aanbestedingen aandacht aan MVOI. Het aandeel "Significant" (hoogste lat) groeit ten koste van "Basis" en "Niet toegepast".')

    df_mvi_ambitie = pd.DataFrame({
        "Jaar": ["2015-2016", "2017-2018", "2019-2020", "2021-2022"],
        "Geen MVI toegepast": [0.22, 0.13, 0.13, 0.22],
        "MVI toegepast": [0.78, 0.00, 0.00, 0.00],
        "Basis": [0.00, 0.35, 0.19, 0.19],
        "Significant/ambitieus": [0.00, 0.52, 0.68, 0.59]
    })

    fig3 = go.Figure()

    colors = {
        "Geen MVI toegepast": "#4EA72E",     # lichtgroen
        "MVI toegepast": "#9C2E97",          # paars
        "Basis": "#2E6B1F",                  # donkergroen
        "Significant/ambitieus": "#2492B8"   # blauw
    }

    for col in ["Geen MVI toegepast", "MVI toegepast", "Basis", "Significant/ambitieus"]:
        fig3.add_trace(
            go.Bar(
                x=df_mvi_ambitie["Jaar"],
                y=df_mvi_ambitie[col],
                name=col,
                marker_color=colors[col]
            )
        )

    fig3.update_layout(
        barmode="stack",
        yaxis=dict(
            range=[0, 1],
            tickformat=".0%",
            showgrid=True,
            gridcolor="lightgrey"
        ),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=40, r=40, t=80, b=100)
    )

    cols2 = st.columns(2)
    with cols2[0]:
        st.plotly_chart(fig3)
    st.caption("Bron: [RIVM - Trends in MVOI](https://www.rivm.nl/maatschappelijk-verantwoord-opdrachtgeven-en-inkopen/trends-in-mvoi)")

    st.markdown("""
    ### MVOI-criteria kantoormeubilair per ambitieniveau
    """)

    import streamlit as st
    import pandas as pd

    # --- Data -------------------------------------------------
    data = {
        "🔴 Ambitieniveau 1 – Basis": [
            ("Duurzaam hout",  "Hout voldoet aan Dutch Procurement Criteria", "Minimumeis"),
            ("Textiel",  "Eisen levensduur textiel", "Minimumeis"),
            ("Textiel",  "Geen gehalogeneerde blaasmiddelen", "Minimumeis"),
            ("Kunststof",  "Eisen kunststof onderdelen", "Minimumeis"),
            ("Coating", "Beperking coatingmengsels (H-zinnen)", "Minimumeis"),
            ("Samenstelling",  "Materialen eenvoudig te scheiden", "Minimumeis"),
            ("Samenstelling",  "Levering samenstellingsetiket", "Minimumeis"),
            ("Levensduur", "Nalevering onderdelen 10 jaar", "Minimumeis"),
            ("Levensduur",  "Garantie 10 jaar / 5 jaar refurbished", "Contractbepaling"),
            ("Vervoer",  "Emissieklasse 6 voertuigen", "Minimumeis"),
            ("Verpakkingen",  "Secundaire verpakking gerecycled", "Minimumeis"),
            ("Verpakkingen",  "Toelichting verpakkingskeuze", "Minimumeis"),
            ("ISV",  "Internationale Sociale Voorwaarden", "Minimumeis"),
            ("Social Return",  "Minimaal 5% social return", "Minimumeis"),
            ("Social Return",  "Rapportage social return", "Contractbepaling"),
        ],
        "🟡 Ambitieniveau 2 – Significant": [
            ("Textiel",  "Duurzame bekledingsmaterialen (OEKO-TEX)", "Minimumeis"),
            ("Textiel",  "OEKO-TEX ECO-paspoort toevoegingen", "Minimumeis"),
            ("Materiaalgebruik",  "Hoger % circulair textiel gewaardeerd", "Gunningscriterium"),
            ("Samenstelling", "Levering materialenpaspoort", "Minimumeis"),
            ("Vervoer", "Rapportage CO₂ transport", "Minimumeis"),
            ("Verpakkingen",  "Herbruikbare/recyclebare verpakking gewaardeerd", "Gunningscriterium"),
            ("Social Return",  "Hoger % social return gewaardeerd", "Gunningscriterium"),
        ],
        "🟢 Ambitieniveau 3 – Ambitieus": [
            ("Plaatmateriaal",  "Formaldehyde-emissies <30% E1", "Minimumeis"),
            ("Materiaalgebruik",  "<0,10% REACH stoffen gewaardeerd", "Gunningscriterium"),
            ("Circulaire economie",  "Plan van aanpak circulaire economie", "Gunningscriterium"),
            ("Levenscyclusanalyse",  "Levering LCA", "Minimumeis"),
            ("Verpakkingen", "Inzamelen/recyclen verpakking gewaardeerd", "Gunningscriterium"),
        ],
    }

    def df_for(level_label: str) -> pd.DataFrame:
        df = pd.DataFrame(
            data[level_label],
            columns=["Onderwerp", "Criterium", "Criteriumtype"],
        )
        return df

    # --- UI ---------------------------------------------------
    levels = list(data.keys())
    selected_level = st.selectbox("Selecteer een ambitieniveau", levels, key="ambitieniveau")

    df_show = df_for(selected_level)

    # optioneel: iets netter tonen
    st.caption(f"Huidige MVOI eisen meubilair: {len(df_show)} criteria")
    st.dataframe(df_show, width='stretch', hide_index=True)

    st.markdown('Bezoek voor verdere details de [MVI-criteriatool website](https://www.mvicriteria.nl/nl/webtool#//23/2//nl)')
    st.caption('Bron: [MVI-criteriatool – Kantoormeubels](https://www.mvicriteria.nl/nl/webtool#//23/2//nl)')

else:
    st.title(f"Klantvraag — {ss.klanttype_value}")

    if ss.klanttype_value == 'B2C':
        st.markdown("""
        <div style="display:flex; gap:16px; margin-bottom:24px;">
            <div style="flex:1; border:2px solid #4472C4; border-radius:12px; padding:20px 24px;">
                <div style="font-size:2.4rem; font-weight:700; color:#4472C4; line-height:1.1;">50%</div>
                <div style="margin-top:10px; font-size:0.95rem; line-height:1.5;">vindt duurzaamheid belangrijk bij meubels</div>
                <div style="margin-top:10px; font-size:0.8rem; color:#666; font-style:italic;">(CBM &amp; Q&amp;A Retail, 2025)</div>
            </div>
            <div style="flex:1; border:2px solid #E8A020; border-radius:12px; padding:20px 24px;">
                <div style="font-size:2.4rem; font-weight:700; color:#E8A020; line-height:1.1;">40&ndash;50%</div>
                <div style="margin-top:10px; font-size:0.95rem; line-height:1.5;">van duurzame vraag blijft onvervuld</div>
                <div style="margin-top:10px; font-size:0.8rem; color:#666; font-style:italic;">(Milieu Centraal en D&amp;B, 2023)</div>
            </div>
            <div style="flex:1; border:2px solid #E37222; border-radius:12px; padding:20px 24px;">
                <div style="font-size:2.4rem; font-weight:700; color:#E37222; line-height:1.1;">+10%</div>
                <div style="margin-top:10px; font-size:0.95rem; line-height:1.5;">de meerprijs die meer dan 50% van de klanten bereid is te betalen</div>
                <div style="margin-top:10px; font-size:0.8rem; color:#666; font-style:italic;">(CBM &amp; Q&amp;A Retail, 2025)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif ss.klanttype_value == 'B2B':
        st.markdown("""
        <div style="display:flex; gap:16px; margin-bottom:24px;">
            <div style="flex:1; border:2px solid #4472C4; border-radius:12px; padding:20px 24px;">
                <div style="font-size:2.4rem; font-weight:700; color:#4472C4; line-height:1.1;">64%</div>
                <div style="margin-top:10px; font-size:0.95rem; line-height:1.5;">van bedrijven vindt duurzame inkoop relevant</div>
                <div style="margin-top:10px; font-size:0.8rem; color:#666; font-style:italic;">(JARO &amp; CBSIBS, 2023)</div>
            </div>
            <div style="flex:1; border:2px solid #E8A020; border-radius:12px; padding:20px 24px;">
                <div style="font-size:2.4rem; font-weight:700; color:#E8A020; line-height:1.1;">&gt;50%</div>
                <div style="margin-top:10px; font-size:0.95rem; line-height:1.5;">heeft duurzaamheid in inkoopbeleid verankerd</div>
                <div style="margin-top:10px; font-size:0.8rem; color:#666; font-style:italic;">(JARO, 2023)</div>
            </div>
            <div style="flex:1; border:2px solid #E37222; border-radius:12px; padding:20px 24px;">
                <div style="font-size:2.4rem; font-weight:700; color:#E37222; line-height:1.1;">4/10</div>
                <div style="margin-top:10px; font-size:0.95rem; line-height:1.5;">bedrijven past het toe in inkoopstrategieën (+7% t.o.v. 2020)</div>
                <div style="margin-top:10px; font-size:0.8rem; color:#666; font-style:italic;">(JARO, 2023)</div>
            </div>
            <div style="flex:1; border:2px solid #4A9A2C; border-radius:12px; padding:20px 24px;">
                <div style="font-size:2.4rem; font-weight:700; color:#4A9A2C; line-height:1.1;">20%</div>
                <div style="margin-top:10px; font-size:0.95rem; line-height:1.5;">van de Europese meubelmarkt is in 2030 duurzaam</div>
                <div style="margin-top:10px; font-size:0.8rem; color:#666; font-style:italic;">(Grand View Research, 2026)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border = True):
            st.subheader('1. Kansen (in de markt)')
            st.write('Duurzame vraag groeit 2× sneller. De duurzame productcategorie groeit structureel harder dan het traditionele assortiment. Wie nu instapt, pakt een groeiend segment.')
            
            if ss.klanttype_value == 'B2C':
                fig = make_klantvraag_scatter_b2c(ss.klantvraag_df_b2c)
            elif ss.klanttype_value == 'B2B':
                fig = make_klantvraag_scatter_b2b(ss.klantvraag_df_b2b)        
            fig.update_layout(
                title='Vergelijking marktgroei: normale vs duurzame markt',
                legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.35),
                margin=dict(t=40, b=60, l=40, r=40),
            )
            st.plotly_chart(fig)
    
    
    with c2: 
        with st.container(border = True):
            st.subheader("2. Risico's (in de markt)")
            st.write('Afwachten kost marktaandeel. Een groeiend deel van de markt wil duurzame alternatieven. Bedrijven zonder duurzaam aanbod riskeren structureel klantverlies.')

            if ss.klanttype_value == 'B2C':
                pie = go.Pie(labels=['Duurzame meubels', 'Traditionele meubels'], 
                        values=[0.07, 0.93], name='Meubelmarkt in 2030')
            elif ss.klanttype_value == 'B2B':
                pie = go.Pie(labels=['Duurzame meubels', 'Traditionele meubels'], 
                        values=[0.19, 0.81], name='Meubelmarkt in 2030')
            else:
                pie = go.Pie(labels=['Duurzame meubels', 'Traditionele meubels'], 
                        values=[0.16, 0.84], name='Meubelmarkt in 2030')
            fig = go.Figure(data=[pie])
            fig.update_layout(
                title='Meubelmarkt in 2030',
                legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.1),
                margin=dict(t=40, b=40, l=40, r=40),
            )
            st.plotly_chart(fig)
  
    st.write('*Risico: deze aandelen zullen sneller verschuiven naarmate de eisen verder aanscherpen*')
                      
    with st.container(border = True):

        with st.expander('**3.1 Klantkeuze voor duurzaam**'):
            # Data
            if ss.klanttype_value == 'B2B':
                st.write('Op de vraag naar relevantie van duurzame inkoop en verantwoorde ketens antwoordt 64% van de gevraagde bedrijven dat dit belangrijk gevonden wordt. Daarbij vindt slechts 8% dit onbelangrijk')
                categories = ['Erg relevant','Enigzins relevant','Niet erg relevant','Geenzins relevant']
                values = [65, 27, 6, 2]
                colors = ["#05853A", "#2BC417", '#F1C40F', '#E74C3C']  # red, orange, yellow, green
                title_text = "Relevantie van duurzame inkoop en verantwoorde ketens"
            else:
                st.write('Op de vraag "Hoe belangrijk is duurzaamheid voor jou bij het kiezen van meubels?" reageert de meerderheid positief. Slechts 16% acht het onbelangrijk.')
                categories = ['Heel erg belangrijk', 'Belangrijk', 'Neutraal', 'Niet belangrijk']
                values = [8, 42, 34, 16]
                colors = ["#05853A", "#2BC417", '#F1C40F', '#E74C3C']  # red, orange, yellow, green
                title_text = 'Belang van duurzaamheid bij het kiezen van meubels'
            # Cumulative values for text positioning
            cumulative = [sum(values[:i+1]) for i in range(len(values))]

            # Build the figure
            fig = go.Figure()

            for i, (category, value, color) in enumerate(zip(categories, values, colors)):
                fig.add_trace(go.Bar(
                    y=["Respondenten"],
                    x=[value],
                    name=category,
                    orientation='h',
                    marker=dict(color=color),
                    text=f"{value}%",
                    textposition='inside',
                    insidetextanchor='middle',
                    textfont=dict(color="black", size=14),
                    hovertemplate=f"{category}<br>{value}% van respondenten<extra></extra>",
                    legendrank=len(categories) - i
                ))

            # Layout
            fig.update_layout(
                barmode='stack',
                title=title_text,
                xaxis_title='Percentage respondenten',
                yaxis_title='',
                xaxis=dict(range=[0, 100]),
                template='plotly_white',
                height=400,
                legend_title="Verdeling",
                legend=dict(traceorder="reversed")
            )

            # Optional: to center label text better
            fig.update_traces(textfont_size=14, cliponaxis=False)

            st.plotly_chart(fig)
            if ss.klanttype_value == 'B2C':
                st.caption('Bron: [CBM en Q&A Retail, 2025](https://cbm.nl/publicatie/129-level-playingfield-nodig-voor-toekomst-meubelindustrie)')
            else:
                st.caption('Bron: [Unite.eu – Studie duurzame B2B-inkoop](https://unite.eu/nl-nl/media/pers/studie-duurzame-b2b-inkoop)')
                            
        if ss.klanttype_value == 'B2C':
            with st.expander('**3.2 Klantwens vs afzet**'):
                st.write('Klanten willen duurzamer, maar het vertaalt zich nog niet in verkoopcijfers. Ruim 40–50% van de duurzame vraag blijft onvervuld. Sluit het huidige aanbod voldoende aan?')
                
                # Gegevens
                # Data
                
                categorieën = [
                    "Staat open voor gerecycled",
                    "Koopt gerecycled",
                    "Staat open voor refurbished",
                    "Koopt refurbished",
                    "Staat open voor tweedehands",
                    "Koopt tweedehands"
                ]
                waarden = [77, 16, 68, 5, 53, 13]
                types = ["Intentie", "Actie"] * 3

                # DataFrame met naam data3
                data3 = pd.DataFrame({
                    "Categorie": categorieën,
                    "Waarde": waarden,
                    "Type": types
                })

                # Kleurinstellingen
                kleuren = {"Intentie": "steelblue", "Actie": "sandybrown"}

                # Figuur maken
                fig = go.Figure()

                fig.add_trace(go.Bar(
                    y=data3["Categorie"],
                    x=data3["Waarde"],
                    orientation='h',
                    marker_color=[kleuren[t] for t in data3["Type"]],
                    text=[f"{v}%" for v in data3["Waarde"]],
                    textposition="outside",
                    hovertext=data3["Type"],
                    showlegend=False
                ))

                # Layout
                fig.update_layout(
                    title="Voorkeur voor duurzame meubels vs. aandeel in verkoop",
                    xaxis_title="Percentage (%)",
                    yaxis_title="",
                    barmode="overlay",
                    template="plotly_white",
                    height=500,
                    margin=dict(l=220, r=40, t=80, b=40),
                )

                fig.update_yaxes(
                    autorange="reversed",
                    categoryorder="array",
                    categoryarray=categorieën
                )
                st.plotly_chart(fig)

                st.caption('Bron: [Milieu Centraal & Rijkswaterstaat, 2023](https://www.milieucentraal.nl/media/b01enjyy/factsheet-consumenteninzichten-zitmeubilair.pdf)')
        else:
            with st.expander('**3.2 Klantwens vs afzet**'):
                p1, p2 = st.columns(2)
                                
                p1.write("Een grote Duitse studie onder inkopers en bestuurders heeft aangetoond dat duurzaamheid tegenwoordig steeds meer wordt geïntegreerd in inkoopbeleid (51%) en inkoopstrategieën (40%). Beiden tonen een 9% en 7% stijging ten opzichte van 2020. (Jaro, 2023)")
                p1.write("Of beleid en strategieën daadwerkelijk worden toegepast in de dagelijkse activiteiten van het bedrijf, hangt echter af van inkoopbeslissingen. In dit opzicht blijven de daadwerkelijke effecten van beleid en strategieën nog achter, aangezien zaken als levenscycluskostenanalyse, risicobeoordeling en de duurzaamheidsprestaties van leveranciers nog niet bovenaan de lijst staan als het gaat om besluitvormingscriteria (zie visual).")
                
                p2.image('assets/B2B_3_2.png')
                p1.caption('Bron: [JARO, 2023](https://unite.eu/assets/2023_jaro_whitepaperstudie2023_en.pdf)')
        if ss.klanttype_value == 'B2C':
            with st.expander('**3.3 Voorkeur voor lokale productie**'):

                st.write('Ruim 1/3e van de consumenten wil lokaal geproduceerde meubels. Vooral hoge en middeninkomens lopen hierin voorop, precies de doelgroep voor premiumproducten en grotere investeringen.')

                data = [
                    ("Tot 80.000 euro", 25, "#4285F4"),        # blauw
                    ("80.000 tot 120.000 euro", 27, "#EA4335"),# rood
                    ("Meer dan 120.000 euro", 46, "#FBBC05"),  # geel
                    ("Nederland totaal", 31, "#34A853"),       # groen
                ]

                # Plotly toont horizontale bar-categorieën standaard van onder naar boven.
                # Daarom draaien we de lijst om zodat "Nederland totaal" bovenaan komt.
                labels = [d[0] for d in data]
                values = [d[1] for d in data]
                colors = [d[2] for d in data]

                fig = go.Figure(
                    go.Bar(
                        x=values,
                        y=labels,
                        orientation="h",
                        marker=dict(color=colors),
                        text=[f"{v}%" for v in values],
                        textposition="outside",
                        cliponaxis=False,  # laat tekst buiten de as zien
                        hovertemplate="%{y}: %{x}%<extra></extra>",
                    )
                )

                fig.update_layout(
                    title=dict(
                        text="Het is van groot belang dat mijn meubels in<br>eigen land geproduceerd zijn",
                        x=0.5,
                        xanchor="center",
                    ),
                    height=360,
                    margin=dict(l=170, r=60, t=80, b=30),
                    plot_bgcolor="white",
                    xaxis=dict(
                        range=[0, 50],          # zodat 46% nog net past + ruimte voor label
                        showgrid=False,
                        ticks="",
                        title=None,
                    ),
                    yaxis=dict(
                        title=None,
                        ticks="",
                    ),
                    showlegend=False,
                )

                st.plotly_chart(fig)
                st.caption('Bron: [CBM en Q&A Retail, 2025](https://cbm.nl/publicatie/129-level-playingfield-nodig-voor-toekomst-meubelindustrie)')

    with st.container(border = True):
        with st.expander('**4. Prijsperceptie en -acceptatie**'):
            st.write('Meer dan de helft van de consumenten is bereid 10–20% meer te betalen. Dit biedt concrete ruimte voor premiumpositionering en hogere marges, mits duurzaamheid aantoonbaar is.')

            # Data
            if ss.klanttype_value == 'B2C':
                categories = ["Niet bereid", "5% toeslag", "10% toeslag", ">10% toeslag"]
                values = [19.0, 25.0, 24.0, 32.0]
                colors = ["#E38178", "#FBBC05", "#0FAD4E", "#2E7D3E"]
                title_text = "Bereidheid consument om meer te betalen<br>voor duurzaamheid"
            elif ss.klanttype_value == 'B2B':
                categories = ['Bereid om veel meer te betalen','Bereid om enigszins meer te betalen','Bereid om een klein beetje meer te betalen','Weet het niet','Niet bereid om meer te betalen']
                values = [5.50, 38.80, 12.70, 35.40, 7.60]
                colors = ["#E38178", "#FBBC05", "#9EB8A9",  "#0FAD4E", "#2E7D3E"]
                title_text = "Bereidheid bedrijven om meer te betalen voor duurzaamheid"

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=categories,
                    y=values,
                    marker=dict(color=colors),
                    text=[f"{v:.1f}%" for v in values],
                    textposition="inside",
                    textfont=dict(color="black", size=14),
                    hovertemplate="%{x}: %{y:.1f}%<extra></extra>",
                )
            )

            fig.update_layout(
                title=dict(
                    text=title_text,
                    x=0.5,
                    xanchor="center",
                    font=dict(size=22)
                ),
                height=420,
                margin=dict(l=60, r=40, t=100, b=60),
                showlegend=False,
                yaxis=dict(
                    range=[0, max(values)],
                    showgrid=False,
                    ticks=""
                ),
                xaxis=dict(
                    ticks="",
                ),
            )

            st.plotly_chart(fig)

            st.caption('Bron: [PwC, 2024](https://www.pwc.com/gx/en/issues/c-suite-insights/voice-of-the-consumer-survey/2024.html)')
            
    with st.container(border = True):
        st.subheader('5. Voorbeelden uit de praktijk')

        data = [
            ["Gispen",
            "Gispen Circulair (diverse meubellijnen)",
            "Ontwikkelt circulair meubilair volgens strenge duurzame ontwerpcriteria, met hergebruikte en recyclebare materialen en een focus op maximale levensduur, reparatie en herstoffering.",
            "Kantoren, overheid, zorg, onderwijs",
            "Meubel",
            "https://www.gispen.com/nl/circulair-inrichten/nieuw-circulair-meubilair/"],

            ["OPNIEUW!",
            "Refurbished & hergebruikte meubelinrichtingen",
            "Biedt volledig circulaire inrichting met een sterke focus op hergebruik, refurbishing en reconfiguratie van bestaand meubilair, met meetbare circulaire impact (CO₂- en grondstoffenbesparing).",
            "Kantoren, overheid, onderwijs, corporate",
            "Meubel",
            "https://www.opnieuw.nl/"],

            ["Ahrend",
            "Furniture-as-a-Service (o.a. Ahrend Revived, 2020, Balance)",
            "Levert circulair kantoormeubilair via een dienstmodel, waarbij producten eigendom blijven van de producent en ontworpen zijn voor hergebruik, refurbishment en recycling.",
            "Kantoren, overheid, maatschappelijke organisaties",
            "Meubel",
            "https://www.ahrend.com/nl/diensten/furniture-as-a-service/"],

            ["Lande Family",
            "Circulaire collecties (o.a. Lande, De Vorm, Functionals)",
            "Ontwerpt circulair meubilair en neemt producten terug om te repareren, opnieuw te stofferen of in onderdelen te hergebruiken, met de ambitie om afvalvrij te produceren.",
            "Kantoren, hospitality, publieke ruimtes",
            "Meubel",
            "https://www.landefamily.nl/duurzaamheid"],

            ["Label Vandenberg",
            "Herstoffering & refurbishment services",
            "Richt zich op het (opnieuw) bekleden, repareren en hergebruiken van meubels, met gebruik van lokale materialen en minimalisering van transport en afval.",
            "Hospitality, culturele sector, high-end interieur",
            "Meubel",
            "https://label.nl/wp-content/uploads/2022/07/LABEL-Vandenberg_NL_Onderhoudsboekje_Online.pdf"],

            ["Triboo",
            "Greengridz – tafels",
            "Circulaire (werk)tafels opgebouwd uit modulaire componenten, ontworpen voor hergebruik, herconfiguratie en eenvoudige demontage, met een lage milieu-impact.",
            "Kantoren, projectinrichting, overheid",
            "Meubel",
            "https://www.triboo.eu"],

            ["Triboo",
            "Greengridz – bezels",
            "Circulaire tafelbezels die los vervangbaar zijn, ontworpen om esthetische en functionele aanpassingen mogelijk te maken zonder het volledige product te vervangen.",
            "Kantoren, projectinrichting, overheid",
            "Meubel",
            "https://www.triboo.eu"]
        ]

        header = "| Bedrijfsnaam | Product / dienst | Beschrijving | Marktsegment |"
        sep    = "| --- | --- | --- | --- |"
        rows   = [f"| [{d[0]}]({d[5]}) | {d[1]} | {d[2]} | {d[3]} |" for d in data]
        st.markdown('\n'.join([header, sep] + rows))
