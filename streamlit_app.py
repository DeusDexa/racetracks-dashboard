import streamlit as st
import pandas as pd
import base64
from pathlib import Path


# Lokale DEXA-Fonts aus dem Repository einbetten
def _font_b64(relative_path):
    return base64.b64encode(Path(relative_path).read_bytes()).decode("ascii")

_inter_font_b64 = _font_b64("assets/Fonts/Inter-VariableFont_opsz,wght.ttf")
_roboto_mono_b64 = _font_b64("assets/Fonts/RobotoMono-VariableFont_wght.ttf")

# DEXA Design System V1 – rein visuelle Anpassung
_font_css = f"""
    @font-face {{
        font-family: 'Inter';
        src: url(data:font/ttf;base64,{_inter_font_b64}) format('truetype');
        font-style: normal;
        font-weight: 100 900;
        font-display: swap;
    }}

    @font-face {{
        font-family: 'Roboto Mono';
        src: url(data:font/ttf;base64,{_roboto_mono_b64}) format('truetype');
        font-style: normal;
        font-weight: 100 900;
        font-display: swap;
    }}
"""

st.markdown("""
    <style>
""" + _font_css + """
    :root {
        --dexa-bg: #0A0A0A;
        --dexa-surface-deep: #0B0F12;
        --dexa-surface: #10161B;
        --dexa-card: #131B21;
        --dexa-border-strong: #1D6170;
        --dexa-border-soft: #263842;
        --dexa-text: #F2F2F2;
        --dexa-text-muted: #8E9AA4;
        --dexa-accent: #18C7AD;
        --dexa-telemetry: #23D7FF;
        --dexa-red: #C1121F;
        --dexa-success: #30E57A;
        --dexa-warning: #F4C542;
        --dexa-info: #42A5FF;
    }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        background: var(--dexa-bg) !important;
        color: var(--dexa-text) !important;
    }

    body, .stApp, button, input, textarea, select {
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
    }

    code, pre, kbd, samp,
    [data-testid="stDataFrame"] [role="gridcell"] {
        font-family: 'Roboto Mono', Consolas, monospace;
    }

    [data-testid="stHeader"] {
        background: var(--dexa-surface-deep) !important;
        border-bottom: 1px solid var(--dexa-border-soft);
    }

    .block-container {
        max-width: 1600px;
        padding-top: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
        padding-bottom: 2.5rem;
    }

    h1, h2, h3, h4, h5, h6,
    p, label, span, div {
        color: var(--dexa-text);
    }

    h1 { font-weight: 600 !important; }
    h2, h3, h4 { font-weight: 600 !important; }
    small, .stCaption, [data-testid="stCaptionContainer"] {
        color: var(--dexa-text-muted) !important;
    }

    hr {
        border: 0 !important;
        border-top: 1px solid var(--dexa-border-soft) !important;
        margin: 1.5rem 0 !important;
    }

    /* Tabs */
    [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid var(--dexa-border-soft);
    }

    button[role="tab"] {
        background: transparent !important;
        color: var(--dexa-text-muted) !important;
        border-radius: 4px 4px 0 0 !important;
        font-weight: 600 !important;
        padding: 0.65rem 0.85rem !important;
        transition: color 150ms ease, border-color 150ms ease, background 150ms ease;
    }

    button[role="tab"]:hover {
        color: var(--dexa-text) !important;
        background: var(--dexa-surface-deep) !important;
    }

    button[role="tab"][aria-selected="true"] {
        color: var(--dexa-text) !important;
    }

    [data-baseweb="tab-highlight"] {
        background-color: var(--dexa-accent) !important;
        height: 3px !important;
    }

    /* Buttons */
    .stButton > button, .stDownloadButton > button {
        background: var(--dexa-card) !important;
        color: var(--dexa-text) !important;
        border: 1px solid var(--dexa-accent) !important;
        border-radius: 4px !important;
        font-weight: 600 !important;
        min-height: 38px;
        box-shadow: none !important;
        transition: background 150ms ease, border-color 150ms ease;
    }

    .stButton > button:hover, .stDownloadButton > button:hover {
        background: var(--dexa-surface-deep) !important;
        border-color: var(--dexa-telemetry) !important;
        color: var(--dexa-text) !important;
    }

    .stButton > button:focus-visible, .stDownloadButton > button:focus-visible {
        outline: 2px solid var(--dexa-accent) !important;
        outline-offset: 2px;
    }

    /* Inputs / Selects / Multiselects */
    [data-baseweb="select"] > div,
    [data-baseweb="input"] > div,
    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea {
        background: var(--dexa-card) !important;
        color: var(--dexa-text) !important;
        border-color: var(--dexa-border-soft) !important;
        border-radius: 4px !important;
    }

    [data-baseweb="select"] > div:focus-within,
    [data-baseweb="input"] > div:focus-within,
    .stTextInput input:focus,
    .stNumberInput input:focus,
    .stTextArea textarea:focus {
        border-color: var(--dexa-accent) !important;
        box-shadow: 0 0 0 1px var(--dexa-accent) !important;
    }

    [data-baseweb="popover"] > div,
    [role="listbox"] {
        background: var(--dexa-card) !important;
        border: 1px solid var(--dexa-border-soft) !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.28) !important;
    }

    /* Alerts / Expander / Data containers */
    [data-testid="stAlert"],
    [data-testid="stExpander"] {
        background: var(--dexa-card) !important;
        border: 1px solid var(--dexa-border-soft) !important;
        border-radius: 8px !important;
        box-shadow: none !important;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid var(--dexa-border-soft);
        border-radius: 8px;
        overflow: hidden;
        background: var(--dexa-card);
    }

    /* Charts */
    [data-testid="stVegaLiteChart"],
    [data-testid="stArrowVegaLiteChart"],
    [data-testid="stPlotlyChart"] {
        background: var(--dexa-card);
        border: 1px solid var(--dexa-border-soft);
        border-radius: 8px;
        padding: 8px;
    }

    /* Links */
    a {
        color: var(--dexa-telemetry) !important;
    }

    a:hover {
        color: var(--dexa-accent) !important;
    }

    /* Images / media */
    img {
        border-radius: 8px;
    }

    /* Mobile */
    @media (max-width: 900px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)



# ==============================
# App-Titel
# ==============================
st.markdown('<div style="height: 8px;"></div>', unsafe_allow_html=True)
st.image("assets/DEXA-LOGO-Database.png", width=520)
st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)

# ==============================
# Google Sheet ID
# ==============================
sheet_id = "173F858oAFPScHVfa4lrr38LDbd1mJumTraUKOz3bvdk"

# ==============================
# GID-Werte für die Tabellenblätter (aus der Google Sheets-URL)
# ==============================
gid_zeiten = "0"
gid_autos = "1286090232"
gid_racetype = "176028286"
gid_layouts = "970885441"
gid_track_logos = "945868195"

# ==============================
# CSV-Export-Links zu den Google Sheets Tabs
# ==============================
url_zeiten = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_zeiten}"
url_autos = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_autos}"
url_racetype = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_racetype}"
url_layouts = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_layouts}"
url_track_logos = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_track_logos}"

# ==============================
# Daten laden aus den CSV-Links
# ==============================
df_zeiten = pd.read_csv(url_zeiten)
df_autos = pd.read_csv(url_autos)
df_racetype = pd.read_csv(url_racetype)
df_layouts = pd.read_csv(url_layouts)
df_track_logos = pd.read_csv(url_track_logos)

# ==============================
# Tabs definieren (Navigation)
# ==============================
tab1, tab2, tab3, tab4 = st.tabs(["🏁 Rennstrecken", "📈 Fortschritt", "🚗 Fahrzeuge", "📊 Tabellenansicht"])



# ================================================================================
# TAB 1: Logos anzeigen und bei Klick zugehörige Layouts darstellen
# ================================================================================
with tab1:
    # --- URL-Parameter auswerten (ganz oben!) ---
    params = st.query_params.to_dict()

    # Session State initialisieren
    if "ausgewählte_strecke" not in st.session_state:
        st.session_state["ausgewählte_strecke"] = None
    if "ausgewähltes_layout" not in st.session_state:
        st.session_state["ausgewähltes_layout"] = None

    # Session State mit Parametern füllen
    if "ausgewählte_strecke" in params:
        st.session_state["ausgewählte_strecke"] = params["ausgewählte_strecke"]
    if "ausgewähltes_layout" in params:
        st.session_state["ausgewähltes_layout"] = params["ausgewähltes_layout"]

    # --- Dynamischer Header je nach Auswahl ---
    if st.session_state["ausgewähltes_layout"]:
        st.subheader(f"Rennen auf {st.session_state['ausgewähltes_layout']}")
    elif st.session_state["ausgewählte_strecke"]:
        st.subheader(f"Layouts für {st.session_state['ausgewählte_strecke']}")
    else:
        st.subheader("Streckenlogos (Klick auf Logo → Layouts → Rennen)")

    # === FALL 1: Kein Logo geklickt → Streckenlogos anzeigen ===
    if not st.session_state["ausgewählte_strecke"]:
        col1, col2 = st.columns([2, 1])  # 2/3 für Logos, 1/3 für Rennstatistik

        # === LINKS: Streckenlogos ===
        with col1:
            columns = st.columns(3)
            for i, row in enumerate(df_track_logos.itertuples(index=False)):
                with columns[i % 3]:
                    st.markdown(
                        f"""
                        <a href="?ausgewählte_strecke={row[1]}" target="_self" style="text-decoration: none;">
                            <img src="{row[3]}" style="width: 100%; border-radius: 4px;">
                            <div style="text-align: center; font-weight: bold; margin-top: 8px; height: 50px;">{row[1]}</div>
                        </a>
                        """,
                        unsafe_allow_html=True
                    )

        # === RECHTS: Anzahl Rennen pro Strecke ===
        with col2:
            st.markdown("#### Anzahl Rennen pro Strecke")
            rennen_pro_layout = df_zeiten["Track Layout"].value_counts().reset_index()
            rennen_pro_layout.columns = ["Track Layout", "Rennen"]
            layout_mit_strecke = pd.merge(
                rennen_pro_layout,
                df_layouts[["Track Layout", "Streckenname"]],
                on="Track Layout",
                how="left"
            )
            rennen_pro_strecke = layout_mit_strecke.groupby("Streckenname")["Rennen"].sum().reset_index()
            rennen_pro_strecke = rennen_pro_strecke.sort_values("Rennen", ascending=False)

            import altair as alt
            chart = alt.Chart(rennen_pro_strecke).mark_bar().encode(
                x=alt.X("Rennen:Q", title="Rennen"),
                # y=alt.Y("Streckenname:N", sort='-x', title="Strecke", axis=alt.Axis(labelAlign="left", labelAngle=0, labelLimit=200)),
                y=alt.Y("Streckenname:N", sort='-x', title="Strecke"),
                tooltip=["Streckenname", "Rennen"]
            ).properties(
                height=400,
                width=600
            )

            st.altair_chart(chart, use_container_width=True)

    # === FALL 2: Strecke gewählt, aber noch kein Layout → Layout-Übersicht ===
    elif st.session_state["ausgewählte_strecke"] and not st.session_state["ausgewähltes_layout"]:
        gewählte_strecke = st.session_state["ausgewählte_strecke"]
        # st.markdown(f"---\n### Layouts für **{gewählte_strecke}**:")

        passende_layouts = df_layouts[df_layouts["Streckenname"] == gewählte_strecke]

        for _, layout in passende_layouts.iterrows():
            st.markdown(
                f"""
                <a href="?ausgewählte_strecke={gewählte_strecke}&ausgewähltes_layout={layout['Track Layout']}" target="_self"  style="text-decoration: none;">
                    <img src="{layout['Track Layout Image-Link']}"
                         style="border: 1px solid #263842; border-radius: 8px; width: 100%;">
                    <div style="text-align: center; font-weight: bold; margin-top: 8px;">{layout['Track Layout']}</div>
                </a>
                """,
                unsafe_allow_html=True
            )

        # Zurück zur Logogalerie
        if st.button("🔙 Zurück zu den Logos"):
            st.session_state["ausgewählte_strecke"] = None
            st.query_params.clear()
            st.rerun()

    # === FALL 3: Layout gewählt → Rennen anzeigen ===
    elif st.session_state["ausgewähltes_layout"]:
        layoutname = st.session_state["ausgewähltes_layout"]
        # st.markdown(f"---\n### Rennen auf **{layoutname}**")

        passende_rennen = df_zeiten[df_zeiten["Track Layout"] == layoutname]

        if not passende_rennen.empty:
            st.dataframe(passende_rennen)
        else:
            st.info("Keine Rennen auf diesem Layout gefunden.")

        # Zurück zu den Layouts oder Logos
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔙 Zurück zu den Layouts"):
                st.session_state["ausgewähltes_layout"] = None
                st.query_params.clear()
                st.rerun()
        with col2:
            if st.button("🏁 Zurück zu den Strecken"):
                st.session_state["ausgewählte_strecke"] = None
                st.session_state["ausgewähltes_layout"] = None
                st.query_params.clear()
                st.rerun()

# ================================================================================
# ERWEITERUNG: Fahrzeuge unter Renntabelle im Layout-Detail (Tab 1)
# ================================================================================
        # Fahrzeuge, die auf diesem Layout gefahren wurden (aus TAB 1)
        if "ausgewähltes_layout" in st.session_state:
            layout_filter = st.session_state["ausgewähltes_layout"]
            autos_auf_layout = df_zeiten[df_zeiten["Track Layout"] == layout_filter]["Auto"].unique().tolist()
            df_autos_auf_layout = df_autos[df_autos["Auto"].isin(autos_auf_layout)]

            st.subheader(f"🚗 Fahrzeuge auf '{layout_filter}'")

            for _, auto in df_autos_auf_layout.iterrows():
                st.markdown("---")
                cols = st.columns([1, 2])

                with cols[0]:
                    if pd.notna(auto["Car_Image"]):
                        st.image(auto["Car_Image"], use_container_width=True)

                with cols[1]:
                    st.markdown(f"**{auto['Auto']}**  |  **Hersteller:** {auto['Hersteller']}  |  **Klasse:** {auto['klasse']}")

                    # Anzahl Rennen + Bestzeit auf diesem Layout
                    rennen = df_zeiten[(df_zeiten["Auto"] == auto["Auto"]) & (df_zeiten["Track Layout"] == layout_filter)]
                    st.markdown(f"Rennen: {len(rennen)}")

                    # Bestzeit berechnen
                    bestzeit = rennen["Best Lap"].min() if not rennen.empty else "--"
                    st.markdown(f"Bestzeit: {bestzeit}")

                    # Dummy: Liste anzeigen (falls gewünscht)
                    layout_liste = rennen["Track Layout"].unique().tolist()
                    for i in range(3):
                        if i < len(layout_liste):
                            st.markdown(f"- {layout_liste[i]}")
                        else:
                            st.markdown("&nbsp;")

# ================================================================================
# TAB 2: Diagramme 
# ================================================================================
with tab2:
    st.subheader("📈 Fortschritt der Rundenzeiten")

    # Strecke auswählen
    streckenauswahl = st.selectbox("Strecke wählen", df_layouts["Streckenname"].unique())

    # Layout-Auswahl passend zur Strecke
    layoutliste = df_layouts[df_layouts["Streckenname"] == streckenauswahl]["Track Layout"].unique()
    layoutauswahl = st.selectbox("Layout wählen", layoutliste)
    # Auto-Auswahl basierend auf vorhandenen Autos in den Rennen für das gewählte Layout
    autos_in_layout = df_zeiten[df_zeiten["Track Layout"] == layoutauswahl]["Auto"].dropna().unique()
    autoauswahl = st.selectbox("Auto wählen", ["Alle"] + sorted(autos_in_layout.tolist()))


    # Debug-Ausgaben – gleiche Einrückungsebene wie oben
    #st.write("Ausgewähltes Layout (per Auswahlfeld):", layoutauswahl)
    #st.write("Alle Layouts in df_zeiten:", df_zeiten["Track Layout"].unique())





    # Strip gegen Leerzeichen-Probleme
    layoutauswahl = layoutauswahl.strip()
    df_zeiten["Track Layout"] = df_zeiten["Track Layout"].str.strip()

    # Gefilterte Renndaten
    daten = df_zeiten[df_zeiten["Track Layout"] == layoutauswahl].copy()
    
    # Filter für das Auto anwenden (wenn nicht "Alle")
    if autoauswahl != "Alle":
        daten = daten[daten["Auto"] == autoauswahl]

    # st.write("Best Lap Rohdaten:", daten["Best Lap"].tolist())
    # Übersichtstabelle mit relevanten Infos
    anzeige = daten[["Race_Date", "Race_Time", "Auto", "Best Lap"]].copy()
    anzeige = anzeige.sort_values("Race_Date", ascending=False)  # Neueste oben

    st.markdown("### Rennen im Überblick")
    st.dataframe(anzeige, use_container_width=True)


    if daten.empty:
        st.info("Keine Daten für dieses Layout gefunden.")
    else:
        # Datum in echtes Format umwandeln
        daten["Race_Date"] = pd.to_datetime(daten["Race_Date"], format="%d.%m.%Y", errors="coerce")

        # Bestzeit in Sekunden umwandeln
        def rundenzeit_in_sekunden(zeit):
            try:
                if not isinstance(zeit, str):
                    return None
                zeit = zeit.strip()
                h, m, sec_ms = zeit.split(":")
                sec, ms = sec_ms.split(",")
                return int(h) * 3600 + int(m) * 60 + int(sec) + int(ms) / 1000
            except Exception as e:
                return None


        daten["Best Lap (s)"] = daten["Best Lap"].apply(rundenzeit_in_sekunden)
        st.write("Konvertierte Zeiten in Sekunden:", daten["Best Lap (s)"].tolist())

        # Nur gültige Werte behalten
        daten = daten.dropna(subset=["Race_Date", "Best Lap (s)"])

        if daten.empty:
            st.info("Keine gültigen Rundenzeiten vorhanden.")
        else:
            st.line_chart(daten.set_index("Race_Date")["Best Lap (s)"])

    st.markdown("## Rennen als Balkendiagramm")

    # Auswahl eines Streckenlayouts
    layoutliste = df_layouts["Track Layout"].dropna().unique()
    layoutauswahl = st.selectbox("Wähle ein Layout", sorted(layoutliste))

    # Daten bereinigen & filtern
    df_zeiten["Best Lap"] = df_zeiten["Best Lap"].astype(str)

    def parse_best_lap(zeit):
        try:
            zeit = str(zeit).strip()
            minuten, rest = zeit.split(":")
            sekunden, millis = rest.split(",")
            return int(minuten) * 60 + int(sekunden) + int(millis) / 1000
        except:
            return None

    df_zeiten["Best Lap (s)"] = df_zeiten["Best Lap"].apply(parse_best_lap)
    df_zeiten["Track Layout"] = df_zeiten["Track Layout"].astype(str).str.strip()

    # Gefilterte Daten
    daten = df_zeiten[df_zeiten["Track Layout"] == layoutauswahl].copy()
    daten["Auto"] = daten["Auto"].fillna("Unbekannt")

    # Auswahl: Autos filtern
    verfügbare_autos = sorted(daten["Auto"].unique())
    auto_filter = st.multiselect("Fahrzeuge filtern", verfügbare_autos, default=verfügbare_autos)

    daten = daten[daten["Auto"].isin(auto_filter)].copy()

    # Laufnummer für gleichmäßige X-Achse
    daten = daten.sort_values("Race_Date")
    daten["Rennlauf"] = range(1, len(daten) + 1)

    # Anzeige prüfen
    if daten.empty:
        st.info("Keine Rennen für dieses Layout und diese Fahrzeugauswahl gefunden.")
    else:
        import altair as alt

        chart = alt.Chart(daten).mark_bar().encode(
            x=alt.X("Rennlauf:O", title="Rennen (chronologisch)", sort=None),
            y=alt.Y("Best Lap (s):Q", title="Bestzeit in Sekunden"),
            color=alt.Color("Auto:N", title="Fahrzeug"),
            tooltip=["Race_Date", "Auto", "Best Lap"]
        ).properties(width=800, height=400)

        st.altair_chart(chart, use_container_width=True)


# ================================================================================
# TAB 3: Fahrzeugübersicht mit Filter, Bild und Streckeninfo
# ================================================================================
with tab3:
    st.subheader("🚗 Fahrzeuge und ihre Einsätze")

    # === Filter: Klasse & Hersteller ===
    klassen = sorted(df_autos["klasse"].dropna().unique().tolist())
    hersteller = sorted(df_autos["Hersteller"].dropna().unique().tolist())

    filter_col1, filter_col2 = st.columns(2)
    with filter_col1:
        klasse_filter = st.selectbox("Klasse wählen", ["Alle"] + klassen)
    with filter_col2:
        hersteller_filter = st.selectbox("Hersteller wählen", ["Alle"] + hersteller)

    # === Daten verknüpfen: Autos + Zeiten ===
    df_autos_stats = df_autos.copy()
    df_autos_stats["Rennen"] = df_autos_stats["Auto"].apply(
        lambda car: (df_zeiten["Auto"] == car).sum()
    )

    # === Optional: Nach meistgefahren sortieren ===
    df_autos_stats = df_autos_stats.sort_values("Rennen", ascending=False)

    # === Filter anwenden ===
    gefiltert = klasse_filter != "Alle" or hersteller_filter != "Alle"
    if klasse_filter != "Alle":
        df_autos_stats = df_autos_stats[df_autos_stats["klasse"] == klasse_filter]
    if hersteller_filter != "Alle":
        df_autos_stats = df_autos_stats[df_autos_stats["Hersteller"] == hersteller_filter]

    # === Bei "Alle" → nur Top 5 zeigen
    if not gefiltert:
        df_autos_stats = df_autos_stats.head(5)
        st.info("Zeige die 5 meistgefahrenen Fahrzeuge. Du kannst mit den Filtern gezielt eingrenzen.")

    # === Darstellung ===
    for _, auto in df_autos_stats.iterrows():
        st.markdown("---")
        cols = st.columns([1, 2])

        # Bild links
        with cols[0]:
            if pd.notna(auto["Car_Image"]):
                st.image(auto["Car_Image"], use_container_width=True)

        # Text rechts
        with cols[1]:
            st.markdown(f"**{auto['Auto']}**  |  **Rennen:** {auto['Rennen']}")

            # Layouts + Bestzeiten ermitteln
            rennen_mit_auto = df_zeiten[df_zeiten["Auto"] == auto["Auto"]]
            layout_gruppen = rennen_mit_auto.groupby("Track Layout")

            # Sortiere nach Häufigkeit der Layouts, nimm max. 3
            meist_gefahrene_layouts = layout_gruppen.size().sort_values(ascending=False).head(3).index.tolist()

            for layout in meist_gefahrene_layouts:
                zeiten = rennen_mit_auto[rennen_mit_auto["Track Layout"] == layout]["Best Lap"]
                bestzeit = zeiten.min() if not zeiten.empty else "--"
                st.markdown(f"- {layout}  _(Bestzeit: {bestzeit})_")

            # Weniger als 3 Layouts? Leere Zeilen einfügen
            for _ in range(3 - len(meist_gefahrene_layouts)):
                st.markdown("&nbsp;")

        st.markdown("\n")



# ================================================================================
# TAB 4: Tabellenansicht aller geladenen Daten (zur Kontrolle & Übersicht)
# ================================================================================
with tab4:
    st.subheader("Zeiten")
    st.dataframe(df_zeiten)   

    
    with st.expander("🧪 Custom EDA für 'Zeiten'"):

        st.markdown("### 🧬 Datentypen")
        st.write(df_zeiten.dtypes)

        st.markdown("### 🔝 Top-Werte (ausgewählte Kategorien)")

        auswahl_spalten = ["Auto", "Track Layout", "Rennen", "Typ", "Klasse"]
        vorhandene_spalten = [col for col in auswahl_spalten if col in df_zeiten.columns]

        for col in vorhandene_spalten:
            st.markdown(f"**{col}**")
            st.write(df_zeiten[col].value_counts().head(5))

        st.markdown("### 📊 Histogramme numerischer Spalten")
        numerisch = df_zeiten.select_dtypes(include=["number"]).columns.tolist()
        for col in numerisch:
            st.markdown(f"**{col}**")
            st.bar_chart(df_zeiten[col].dropna())

    st.subheader("Autos")
    st.dataframe(df_autos)

    st.subheader("Racetype")
    st.dataframe(df_racetype)

    st.subheader("Layouts")
    st.dataframe(df_layouts)

    st.subheader("Track Logos")
    st.dataframe(df_track_logos)




      
