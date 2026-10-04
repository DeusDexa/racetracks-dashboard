import streamlit as st
import pandas as pd
import base64
from pathlib import Path


# Browser-Tab / Favicon
st.set_page_config(
    page_title="DEXA Racing Database",
    page_icon="assets/favicon-32x32.png",
)


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
overview_tab, tab1, tab2, tab3, tab4 = st.tabs(["Übersicht", "Rennstrecken", "Analyse", "Fahrzeuge", "Tabellenansicht"])



# ================================================================================
# ÜBERSICHT: PvP-Kennzahlen
# ================================================================================
with overview_tab:
    st.subheader("Online-Rennen")
    st.caption("Kennzahlen ausschließlich aus Rennen gegen andere Spieler.")

    pvp = df_zeiten[
        df_zeiten["Typ"].astype(str).str.strip().str.upper() == "PVP"
    ].copy()

    pvp["start pos"] = pd.to_numeric(pvp["start pos"], errors="coerce")
    pvp["Finish Pos"] = pd.to_numeric(pvp["Finish Pos"], errors="coerce")

    pvp_gesamt = len(pvp)
    pole_starts = int((pvp["start pos"] == 1).sum())
    siege = int((pvp["Finish Pos"] == 1).sum())
    top5 = int((pvp["Finish Pos"] <= 5).sum())

    positionsdaten = pvp.dropna(subset=["start pos", "Finish Pos"]).copy()
    gehalten_oder_besser = int(
        (positionsdaten["Finish Pos"] <= positionsdaten["start pos"]).sum()
    )

    def _quote(anzahl, basis):
        return (anzahl / basis * 100) if basis else 0.0

    def _asset_data_uri(path):
        suffix = Path(path).suffix.lower().lstrip(".") or "png"
        mime = "jpeg" if suffix in ("jpg", "jpeg") else suffix
        data = base64.b64encode(Path(path).read_bytes()).decode("ascii")
        return f"data:image/{mime};base64,{data}"

    kpi_cards = [
        {
            "titel": "Online-Rennen",
            "wert": str(pvp_gesamt),
            "detail": "Gesamt",
            "icon": "assets/Checkerflag.png",
        },
        {
            "titel": "Pole-Starts",
            "wert": str(pole_starts),
            "detail": f"{_quote(pole_starts, pvp_gesamt):.1f} %".replace(".", ","),
            "icon": "assets/Position.png",
        },
        {
            "titel": "Siege",
            "wert": str(siege),
            "detail": f"{_quote(siege, pvp_gesamt):.1f} %".replace(".", ","),
            "icon": "assets/bestlapcrown.png",
        },
        {
            "titel": "Top 5",
            "wert": str(top5),
            "detail": f"{_quote(top5, pvp_gesamt):.1f} %".replace(".", ","),
            "icon": "assets/LastLap.png",
        },
        {
            "titel": "Startplatz gehalten / verbessert",
            "wert": str(gehalten_oder_besser),
            "detail": (
                f"{_quote(gehalten_oder_besser, len(positionsdaten)):.1f} %"
                .replace(".", ",")
                if len(positionsdaten) else "—"
            ),
            "icon": "assets/Controller.png",
        },
    ]

    kpi_columns = st.columns(5, gap="medium")
    for column, card in zip(kpi_columns, kpi_cards):
        with column:
            icon_uri = _asset_data_uri(card["icon"])
            st.markdown(
                f"""
                <div style="
                    min-height: 190px;
                    padding: 16px;
                    background: #131B21;
                    border: 1px solid #263842;
                    border-radius: 8px;
                ">
                    <img src="{icon_uri}" alt="" style="
                        width: 42px;
                        height: 42px;
                        object-fit: contain;
                        margin-bottom: 14px;
                    ">
                    <div style="
                        font-size: 13px;
                        line-height: 1.35;
                        color: #8E9AA4;
                        min-height: 36px;
                    ">{card["titel"]}</div>
                    <div style="
                        margin-top: 8px;
                        font-family: 'Roboto Mono', Consolas, monospace;
                        font-size: 32px;
                        line-height: 1;
                        font-weight: 700;
                        color: #F2F2F2;
                    ">{card["wert"]}</div>
                    <div style="
                        margin-top: 10px;
                        font-family: 'Roboto Mono', Consolas, monospace;
                        font-size: 13px;
                        color: #23D7FF;
                    ">{card["detail"]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    if len(positionsdaten) != pvp_gesamt:
        st.caption(
            f"Für die Positionsquote wurden {len(positionsdaten)} PvP-Rennen mit gültiger Start- und Zielposition ausgewertet."
        )

    st.divider()
    st.markdown("### Anzahl Rennen pro Strecke")

    rennen_pro_layout = df_zeiten["Track Layout"].value_counts().reset_index()
    rennen_pro_layout.columns = ["Track Layout", "Rennen"]
    layout_mit_strecke = pd.merge(
        rennen_pro_layout,
        df_layouts[["Track Layout", "Streckenname"]],
        on="Track Layout",
        how="left"
    )
    rennen_pro_strecke = (
        layout_mit_strecke.groupby("Streckenname")["Rennen"]
        .sum()
        .reset_index()
        .sort_values("Rennen", ascending=False)
    )

    import altair as alt
    chart = alt.Chart(rennen_pro_strecke).mark_bar(color="#23D7FF").encode(
        x=alt.X("Rennen:Q", title="Rennen"),
        y=alt.Y("Streckenname:N", sort="-x", title="Strecke"),
        tooltip=["Streckenname", "Rennen"]
    ).properties(
        height=430
    ).configure(
        background="#131B21"
    ).configure_view(
        stroke="#263842"
    ).configure_axis(
        labelColor="#8E9AA4",
        titleColor="#F2F2F2",
        gridColor="#263842",
        domainColor="#263842",
        tickColor="#263842"
    )

    st.altair_chart(chart, use_container_width=True)



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
        # Streckenlogos nutzen die volle Breite; Statistik steht jetzt auf der Übersichtsseite.
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

    # === FALL 2: Strecke gewählt, aber noch kein Layout → Layout-Übersicht ===
    elif st.session_state["ausgewählte_strecke"] and not st.session_state["ausgewähltes_layout"]:
        gewählte_strecke = st.session_state["ausgewählte_strecke"]
        # st.markdown(f"---\n### Layouts für **{gewählte_strecke}**:")

        passende_layouts = df_layouts[df_layouts["Streckenname"] == gewählte_strecke]

        # Layouts kompakt als zweispaltige Cards darstellen
        layout_columns = st.columns(2, gap="large")
        for i, (_, layout) in enumerate(passende_layouts.iterrows()):
            with layout_columns[i % 2]:
                st.markdown(
                    f"""
                    <div style="max-width: 600px; margin: 0 auto 24px auto;">
                        <a href="?ausgewählte_strecke={gewählte_strecke}&ausgewähltes_layout={layout['Track Layout']}"
                           target="_self"
                           style="display: block; text-decoration: none; padding: 12px;
                                  background: #131B21; border: 1px solid #263842;
                                  border-radius: 8px;">
                            <img src="{layout['Track Layout Image-Link']}"
                                 style="display: block; width: 100%; max-height: 430px;
                                        object-fit: contain; border-radius: 4px;">
                            <div style="text-align: center; font-weight: 600;
                                        margin-top: 10px; color: #F2F2F2;">
                                {layout['Track Layout']}
                            </div>
                        </a>
                    </div>
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
# TAB 2: Analyse – Fortschritt, Bestzeiten und Aktivität
# ================================================================================
with tab2:
    import altair as alt

    st.subheader("Analyse")
    st.caption("Fortschritt, persönliche Bestzeiten und Aktivität auf Basis deiner gespeicherten Renndaten.")

    st.markdown("### Fortschritt der Rundenzeiten")

    def rundenzeit_in_sekunden(zeit):
        """GT7-Zeitformate wie 1:49,932 oder 0:01:49,932 robust in Sekunden umwandeln."""
        try:
            if pd.isna(zeit):
                return None
            text = str(zeit).strip().replace(".", ",")
            teile = text.split(":")
            if len(teile) == 2:
                minuten, sekunden_ms = teile
                stunden = 0
            elif len(teile) == 3:
                stunden, minuten, sekunden_ms = teile
            else:
                return None

            if "," in sekunden_ms:
                sekunden, millis = sekunden_ms.split(",", 1)
            else:
                sekunden, millis = sekunden_ms, "0"

            millis = (millis + "000")[:3]
            return (
                int(stunden) * 3600
                + int(minuten) * 60
                + int(sekunden)
                + int(millis) / 1000
            )
        except (ValueError, TypeError):
            return None

    def sekunden_als_rundenzeit(sekunden):
        if pd.isna(sekunden):
            return "—"
        minuten = int(sekunden // 60)
        rest = sekunden - minuten * 60
        return f"{minuten}:{rest:06.3f}".replace(".", ",")

    # Nur Strecken anbieten, für die tatsächlich Renndaten vorhanden sind.
    layouts_mit_rennen = set(df_zeiten["Track Layout"].dropna().astype(str).str.strip())
    fortschritt_layouts = df_layouts[
        df_layouts["Track Layout"].astype(str).str.strip().isin(layouts_mit_rennen)
    ].copy()

    strecken = sorted(fortschritt_layouts["Streckenname"].dropna().unique().tolist())

    if not strecken:
        st.info("Für eine Fortschrittsauswertung sind noch keine passenden Renndaten vorhanden.")
    else:
        # Kontext aus dem Reiter "Rennstrecken" übernehmen:
        # Wird dort eine andere Strecke gewählt, startet "Analyse" automatisch mit dieser Strecke.
        kontext_strecke = st.session_state.get("ausgewählte_strecke")
        letzter_kontext = st.session_state.get("_fortschritt_context_strecke")

        if kontext_strecke in strecken and kontext_strecke != letzter_kontext:
            st.session_state["fortschritt_strecke"] = kontext_strecke
            st.session_state["_fortschritt_context_strecke"] = kontext_strecke
            # Abhängige Auswahl zurücksetzen, damit Layout und Fahrzeug zur neuen Strecke passen.
            st.session_state.pop("fortschritt_layout", None)
            st.session_state.pop("fortschritt_auto", None)

        filter_col1, filter_col2, filter_col3 = st.columns(3)

        with filter_col1:
            streckenauswahl = st.selectbox(
                "Strecke",
                strecken,
                key="fortschritt_strecke"
            )

        layouts = (
            fortschritt_layouts[
                fortschritt_layouts["Streckenname"] == streckenauswahl
            ]["Track Layout"]
            .dropna()
            .astype(str)
            .str.strip()
            .unique()
            .tolist()
        )

        with filter_col2:
            layoutauswahl = st.selectbox(
                "Layout",
                sorted(layouts),
                key="fortschritt_layout"
            )

        autos = (
            df_zeiten[
                df_zeiten["Track Layout"].astype(str).str.strip() == layoutauswahl
            ]["Auto"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        with filter_col3:
            autoauswahl = st.selectbox(
                "Fahrzeug",
                sorted(autos),
                key="fortschritt_auto"
            ) if autos else None

        if autoauswahl is None:
            st.info("Für dieses Layout sind noch keine Fahrzeuge mit Renndaten vorhanden.")
        else:
            daten = df_zeiten[
                (df_zeiten["Track Layout"].astype(str).str.strip() == layoutauswahl)
                & (df_zeiten["Auto"].astype(str) == autoauswahl)
            ].copy()

            daten["Best Lap (s)"] = daten["Best Lap"].apply(rundenzeit_in_sekunden)
            daten["Race_Date_dt"] = pd.to_datetime(
                daten["Race_Date"],
                format="%d.%m.%Y",
                errors="coerce"
            )

            # Uhrzeit nur zur stabilen Sortierung am selben Tag ergänzen.
            if "Race_Time" in daten.columns:
                daten["Race_Time_sort"] = pd.to_datetime(
                    daten["Race_Time"].astype(str),
                    errors="coerce"
                ).dt.time
                daten["Race_Time_text"] = daten["Race_Time"].fillna("").astype(str)
            else:
                daten["Race_Time_sort"] = None
                daten["Race_Time_text"] = ""

            daten = daten.dropna(subset=["Race_Date_dt", "Best Lap (s)"]).copy()
            daten = daten.sort_values(
                ["Race_Date_dt", "Race_Time_text"],
                ascending=[True, True]
            ).reset_index(drop=True)

            if daten.empty:
                st.info("Für diese Auswahl sind keine gültigen Rundenzeiten vorhanden.")
            else:
                daten["Rennen"] = range(1, len(daten) + 1)
                daten["PB (s)"] = daten["Best Lap (s)"].cummin()
                daten["Vorherige PB (s)"] = daten["PB (s)"].shift(1)
                daten["Neue PB"] = (
                    daten["Vorherige PB (s)"].isna()
                    | (daten["PB (s)"] < daten["Vorherige PB (s)"] - 0.0005)
                )

                erste_zeit = daten.iloc[0]["Best Lap (s)"]
                bestzeit = daten["Best Lap (s)"].min()
                verbesserung = erste_zeit - bestzeit
                verbesserung_prozent = (
                    verbesserung / erste_zeit * 100
                    if erste_zeit > 0 else 0
                )

                metric1, metric2, metric3, metric4 = st.columns(4)
                metric1.metric("Bestzeit", sekunden_als_rundenzeit(bestzeit))
                metric2.metric("Erste Zeit", sekunden_als_rundenzeit(erste_zeit))
                metric3.metric(
                    "Verbesserung",
                    f"{verbesserung:.3f} s".replace(".", ","),
                    f"{verbesserung_prozent:.1f} %".replace(".", ",")
                )
                metric4.metric("Rennen", len(daten))

                st.markdown("### Zeitentwicklung")

                chart_daten = daten.copy()
                chart_daten["Datum"] = chart_daten["Race_Date_dt"].dt.strftime("%d.%m.%Y")
                chart_daten["Best Lap"] = chart_daten["Best Lap"].astype(str)
                chart_daten["PB"] = chart_daten["PB (s)"].apply(sekunden_als_rundenzeit)

                normale_zeiten = (
                    alt.Chart(chart_daten)
                    .mark_line(point=True, strokeWidth=2, color="#18C7AD")
                    .encode(
                        x=alt.X(
                            "Rennen:Q",
                            title="Rennen (chronologisch)",
                            axis=alt.Axis(tickMinStep=1)
                        ),
                        y=alt.Y(
                            "Best Lap (s):Q",
                            title="Rundenzeit in Sekunden",
                            scale=alt.Scale(zero=False)
                        ),
                        tooltip=[
                            alt.Tooltip("Rennen:Q", title="Rennen"),
                            alt.Tooltip("Datum:N", title="Datum"),
                            alt.Tooltip("Best Lap:N", title="Best Lap"),
                            alt.Tooltip("PB:N", title="PB bis dahin")
                        ]
                    )
                )

                pb_linie = (
                    alt.Chart(chart_daten)
                    .mark_line(strokeWidth=3, color="#23D7FF")
                    .encode(
                        x="Rennen:Q",
                        y=alt.Y("PB (s):Q", scale=alt.Scale(zero=False))
                    )
                )

                pb_punkte = (
                    alt.Chart(chart_daten[chart_daten["Neue PB"]])
                    .mark_point(
                        filled=True,
                        size=95,
                        color="#23D7FF",
                        stroke="#0A0A0A",
                        strokeWidth=1
                    )
                    .encode(
                        x="Rennen:Q",
                        y="PB (s):Q",
                        tooltip=[
                            alt.Tooltip("Rennen:Q", title="Neue PB bei Rennen"),
                            alt.Tooltip("Datum:N", title="Datum"),
                            alt.Tooltip("PB:N", title="Persönliche Bestzeit")
                        ]
                    )
                )

                chart = (
                    (normale_zeiten + pb_linie + pb_punkte)
                    .properties(height=430)
                    .configure(
                        background="#131B21"
                    )
                    .configure_view(
                        stroke="#263842"
                    )
                    .configure_axis(
                        labelColor="#8E9AA4",
                        titleColor="#F2F2F2",
                        gridColor="#263842",
                        domainColor="#263842",
                        tickColor="#263842"
                    )
                )

                st.altair_chart(chart, use_container_width=True)
                st.caption(
                    "Petrol zeigt die Bestzeit jedes Rennens. Cyan zeigt die persönliche Bestzeit-Entwicklung."
                )

                st.markdown("### Persönliche Bestzeiten")

                pb_tabelle = daten[daten["Neue PB"]].copy()
                pb_tabelle["Datum"] = pb_tabelle["Race_Date_dt"].dt.strftime("%d.%m.%Y")
                pb_tabelle["Best Lap"] = pb_tabelle["Best Lap (s)"].apply(sekunden_als_rundenzeit)
                pb_tabelle["Verbesserung zur vorherigen PB"] = (
                    pb_tabelle["Vorherige PB (s)"] - pb_tabelle["PB (s)"]
                )

                def format_pb_delta(wert):
                    if pd.isna(wert):
                        return "—"
                    return f"-{wert:.3f} s".replace(".", ",")

                pb_tabelle["Verbesserung zur vorherigen PB"] = (
                    pb_tabelle["Verbesserung zur vorherigen PB"].apply(format_pb_delta)
                )

                st.dataframe(
                    pb_tabelle[
                        ["Datum", "Auto", "Best Lap", "Verbesserung zur vorherigen PB"]
                    ].rename(columns={"Auto": "Fahrzeug"}),
                    use_container_width=True,
                    hide_index=True
                )


    st.divider()
    st.markdown("### Persönliche Bestzeiten – Gesamtübersicht")
    st.caption("Beste gespeicherte Rundenzeit je Layout und Fahrzeug.")

    analyse_daten = df_zeiten.copy()
    analyse_daten["Track Layout"] = analyse_daten["Track Layout"].astype(str).str.strip()
    analyse_daten["Best Lap (s)"] = analyse_daten["Best Lap"].apply(rundenzeit_in_sekunden)
    analyse_daten["Race_Date_dt"] = pd.to_datetime(
        analyse_daten["Race_Date"],
        format="%d.%m.%Y",
        errors="coerce"
    )
    analyse_daten = analyse_daten.dropna(
        subset=["Track Layout", "Auto", "Best Lap (s)", "Race_Date_dt"]
    ).copy()

    if analyse_daten.empty:
        st.info("Für die Gesamtanalyse sind noch keine gültigen Rundenzeiten vorhanden.")
    else:
        # Je Layout/Fahrzeug die Zeile mit der schnellsten gespeicherten Runde ermitteln.
        pb_indices = analyse_daten.groupby(
            ["Track Layout", "Auto"]
        )["Best Lap (s)"].idxmin()

        pb_gesamt = analyse_daten.loc[
            pb_indices,
            ["Track Layout", "Auto", "Best Lap (s)", "Race_Date_dt"]
        ].copy()

        layout_zu_strecke = (
            df_layouts[["Track Layout", "Streckenname"]]
            .dropna()
            .copy()
        )
        layout_zu_strecke["Track Layout"] = (
            layout_zu_strecke["Track Layout"].astype(str).str.strip()
        )

        pb_gesamt = pb_gesamt.merge(
            layout_zu_strecke,
            on="Track Layout",
            how="left"
        )

        rennen_anzahl = (
            analyse_daten.groupby(["Track Layout", "Auto"])
            .size()
            .rename("Rennen")
            .reset_index()
        )
        pb_gesamt = pb_gesamt.merge(
            rennen_anzahl,
            on=["Track Layout", "Auto"],
            how="left"
        )

        pb_gesamt["Bestzeit"] = pb_gesamt["Best Lap (s)"].apply(sekunden_als_rundenzeit)
        pb_gesamt["Datum"] = pb_gesamt["Race_Date_dt"].dt.strftime("%d.%m.%Y")
        pb_gesamt = pb_gesamt.sort_values(
            ["Streckenname", "Track Layout", "Auto"],
            na_position="last"
        )

        st.dataframe(
            pb_gesamt[
                ["Streckenname", "Track Layout", "Auto", "Bestzeit", "Datum", "Rennen"]
            ].rename(
                columns={
                    "Streckenname": "Strecke",
                    "Track Layout": "Layout",
                    "Auto": "Fahrzeug"
                }
            ),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### Aktivität")
        st.caption("Anzahl gespeicherter Rennen pro Monat.")

        aktivitaet = analyse_daten.copy()
        aktivitaet["Monat_dt"] = aktivitaet["Race_Date_dt"].dt.to_period("M").dt.to_timestamp()
        aktivitaet_monat = (
            aktivitaet.groupby("Monat_dt")
            .size()
            .rename("Rennen")
            .reset_index()
            .sort_values("Monat_dt")
        )
        aktivitaet_monat["Monat"] = aktivitaet_monat["Monat_dt"].dt.strftime("%m/%Y")

        aktivitaets_chart = (
            alt.Chart(aktivitaet_monat)
            .mark_bar(color="#18C7AD")
            .encode(
                x=alt.X(
                    "Monat:N",
                    title="Monat",
                    sort=aktivitaet_monat["Monat"].tolist(),
                    axis=alt.Axis(labelAngle=-45)
                ),
                y=alt.Y("Rennen:Q", title="Rennen"),
                tooltip=[
                    alt.Tooltip("Monat:N", title="Monat"),
                    alt.Tooltip("Rennen:Q", title="Rennen")
                ]
            )
            .properties(height=300)
            .configure(background="#131B21")
            .configure_view(stroke="#263842")
            .configure_axis(
                labelColor="#8E9AA4",
                titleColor="#F2F2F2",
                gridColor="#263842",
                domainColor="#263842",
                tickColor="#263842"
            )
        )
        st.altair_chart(aktivitaets_chart, use_container_width=True)

        st.markdown("### Meistgefahrene Kombinationen")
        st.caption("Strecke, Layout und Fahrzeug mit den meisten gespeicherten Rennen.")

        top_kombinationen = (
            analyse_daten.groupby(["Track Layout", "Auto"])
            .size()
            .rename("Rennen")
            .reset_index()
            .merge(layout_zu_strecke, on="Track Layout", how="left")
            .sort_values("Rennen", ascending=False)
            .head(10)
        )

        st.dataframe(
            top_kombinationen[
                ["Streckenname", "Track Layout", "Auto", "Rennen"]
            ].rename(
                columns={
                    "Streckenname": "Strecke",
                    "Track Layout": "Layout",
                    "Auto": "Fahrzeug"
                }
            ),
            use_container_width=True,
            hide_index=True
        )


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




      
