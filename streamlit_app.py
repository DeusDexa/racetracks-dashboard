import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"]::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 0;
            height: 0;
            background-image: url('https://i.imgur.com/tHxDEFy.png');  /* Hier dein Favicon-Link */
            background-size: contain;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ==============================
# App-Titel
# ==============================
st.image("https://i.imgur.com/CzaF31B.png", use_container_width=True)
# st.title("Racetracks Dashboard")

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
tab1, tab2, tab3 = st.tabs(["🏁 Streckenlogos", "📈 Fortschritt", "📊 Tabellenansicht"])



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

        for _, layout in passende_layouts.iterrows():
            st.markdown(
                f"""
                <a href="?ausgewählte_strecke={gewählte_strecke}&ausgewähltes_layout={layout['Track Layout']}" target="_self"  style="text-decoration: none;">
                    <img src="{layout['Track Layout Image-Link']}"
                         style="border: 2px solid black; border-radius: 6px; width: 100%;">
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
            if st.button("🏁 Zurück zu den Logos"):
                st.session_state["ausgewählte_strecke"] = None
                st.session_state["ausgewähltes_layout"] = None
                st.query_params.clear()
                st.rerun()


# ================================================================================
# TAB 2: Diagramme 
# ================================================================================
with tab2:
    st.subheader("📈 Fortschritt deiner Rundenzeiten")

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






# ================================================================================
# TAB 3: Tabellenansicht aller geladenen Daten (zur Kontrolle & Übersicht)
# ================================================================================
with tab3:
    st.subheader("Zeiten")
    st.dataframe(df_zeiten)

    st.subheader("Autos")
    st.dataframe(df_autos)

    st.subheader("Racetype")
    st.dataframe(df_racetype)

    st.subheader("Layouts")
    st.dataframe(df_layouts)

    st.subheader("Track Logos")
    st.dataframe(df_track_logos)
