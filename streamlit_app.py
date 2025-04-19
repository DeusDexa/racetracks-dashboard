# streamlit_app.py
import streamlit as st
import pandas as pd

# === Eigene Module laden ===
from tab1_logos import render_tab1
from tab2_diagramme import render_tab2
from tab3_autos import render_tab3
from tab4_tabellen import render_tab4


st.set_page_config(page_title="Racetracks Dashboard", layout="wide")
st.title("Racetracks Dashboard")
# Optional: Header-Grafik
st.image("https://i.imgur.com/CzaF31B.png", use_container_width=True)

# === Google Sheet ID ===
sheet_id = "173F858oAFPScHVfa4lrr38LDbd1mJumTraUKOz3bvdk"

# === GID-Werte ===
gid_zeiten = "0"
gid_autos = "1286090232"
gid_racetype = "176028286"
gid_layouts = "970885441"
gid_track_logos = "945868195"

# === URLs ===
url = lambda gid: f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
df_zeiten = pd.read_csv(url(gid_zeiten))
df_autos = pd.read_csv(url(gid_autos))
df_racetype = pd.read_csv(url(gid_racetype))
df_layouts = pd.read_csv(url(gid_layouts))
df_track_logos = pd.read_csv(url(gid_track_logos))

# === Tabs ===
tab1, tab2, tab3, tab4 = st.tabs(["🏁 Streckenlogos", "📈 Fortschritt", "🚗 Fahrzeuge", "📋 Tabellen"])

with tab1:
    render_tab1(df_track_logos, df_layouts, df_zeiten, df_autos)

with tab2:
    render_tab2(df_layouts, df_zeiten)

with tab3:
    render_tab3(df_autos, df_zeiten)

with tab4:
    render_tab4(df_zeiten, df_autos, df_racetype, df_layouts, df_track_logos)
