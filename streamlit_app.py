import streamlit as st
import pandas as pd

# ==============================
# App-Titel
# ==============================
st.title("Racetracks Dashboard")

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
tab1, tab2 = st.tabs(["🏁 Streckenlogos", "📊 Tabellenansicht"])


# ================================================================================
# TAB 1: Logos anzeigen und bei Klick zugehörige Layouts darstellen
# ================================================================================
with tab1:
    st.subheader("Streckenlogos (Klick auf Logo für Layouts)")

    # Session-State Variable initialisieren (welche Strecke gewählt wurde)
    if "ausgewählte_strecke" not in st.session_state:
        st.session_state["ausgewählte_strecke"] = None

    # URL-Parameter auslesen (z. B. bei Klick auf ein Logo)
    params = st.query_params.to_dict()
    if "ausgewählte_strecke" in params:
        st.session_state["ausgewählte_strecke"] = params["ausgewählte_strecke"]

    # === Wenn keine Strecke ausgewählt → Logo-Galerie anzeigen ===
    if not st.session_state["ausgewählte_strecke"]:
        columns = st.columns(3)  # 3-Spalten-Grid
        for i, row in enumerate(df_track_logos.itertuples(index=False)):
            with columns[i % 3]:
                st.markdown(
                    f"""
                    <a href="?ausgewählte_strecke={row[1]}" style="text-decoration: none;">
                        <img src="{row[3]}" style="width: 100%; border-radius: 4px;">
                        <div style="text-align: center; font-weight: bold; margin-top: 8px; height: 50px;">{row[1]}</div>
                    </a>
                    """,
                    unsafe_allow_html=True
                )

    # === Wenn Strecke gewählt → zugehörige Layouts anzeigen ===
    if st.session_state["ausgewählte_strecke"]:
        gewählte_strecke = st.session_state["ausgewählte_strecke"]
        st.markdown(f"---\n### Layouts für **{gewählte_strecke}**:")

        passende_layouts = df_layouts[df_layouts["Streckenname"] == gewählte_strecke]

        for _, layout in passende_layouts.iterrows():
            # Layout-Grafik mit schwarzem Rahmen + Beschriftung
            st.markdown(
                f"""
                <div style="margin-bottom: 24px;">
                    <img src="{layout['Track Layout Image-Link']}"
                         style="border: 2px solid black; border-radius: 6px; width: 100%;">
                    <div style="text-align: center; font-weight: bold; margin-top: 8px;">
                        {layout['Track Layout']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Wenn keine Layouts gefunden wurden
        if len(passende_layouts) == 0:
            st.info("Keine Layouts gefunden.")

        # === Zurück-Button zur Logogalerie ===
        if st.button("🔙 Zurück zu den Logos"):
            st.session_state["ausgewählte_strecke"] = None
            st.query_params.clear()
            st.rerun()


# ================================================================================
# TAB 2: Tabellenansicht aller geladenen Daten (zur Kontrolle & Übersicht)
# ================================================================================
with tab2:
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
