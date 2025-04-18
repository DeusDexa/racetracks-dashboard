import streamlit as st
import pandas as pd

st.title("Racetracks Dashboard")

# === Google Sheet ID ===
sheet_id = "173F858oAFPScHVfa4lrr38LDbd1mJumTraUKOz3bvdk"

# === GID-Werte für die einzelnen Tabellenblätter ===
gid_zeiten = "0"
gid_autos = "1286090232"
gid_racetype = "176028286"
gid_layouts = "970885441"
gid_track_logos = "945868195"

# === URLs für den CSV-Export der Tabellenblätter ===
url_zeiten = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_zeiten}"
url_autos = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_autos}"
url_racetype = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_racetype}"
url_layouts = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_layouts}"
url_track_logos = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid_track_logos}"

# === Daten laden ===
df_zeiten = pd.read_csv(url_zeiten)
df_autos = pd.read_csv(url_autos)
df_racetype = pd.read_csv(url_racetype)
df_layouts = pd.read_csv(url_layouts)
df_track_logos = pd.read_csv(url_track_logos)

# === Tabs erzeugen ===
tab1, tab2 = st.tabs(["🏁 Streckenlogos", "📊 Tabellenansicht"])

# === Tab 1: Grid mit Logos ===
with tab1:
    st.subheader("Streckenübersicht mit Logos")

    columns = st.columns(3)

    for i, row in enumerate(df_track_logos.itertuples(index=False)):
        with columns[i % 3]:
            st.image(row[3], use_container_width=True)
            st.markdown(
            f"<div style='height: 50px; text-align: center'><b>{row[1]}</b></div>",
            unsafe_allow_html=True
        ) # Streckenname

# === Tab 2: Tabellen wie bisher ===
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
