# tab2_diagramme.py
# ================================================================================
# TAB 2: Diagramme 
# ================================================================================
import streamlit as st
import pandas as pd

def render_tab2(df_layouts, df_zeiten):
    st.subheader("\U0001F4C8 Fortschritt deiner Rundenzeiten")

    # Strecke wählen
    streckenauswahl = st.selectbox("Strecke wählen", df_layouts["Streckenname"].unique())

    # Layouts passend zur Strecke
    layoutliste = df_layouts[df_layouts["Streckenname"] == streckenauswahl]["Track Layout"].unique()
    layoutauswahl = st.selectbox("Layout wählen", layoutliste)

    # Strip gegen Whitespace-Probleme
    layoutauswahl = layoutauswahl.strip()
    df_zeiten["Track Layout"] = df_zeiten["Track Layout"].str.strip()

    # Gefilterte Renndaten
    daten = df_zeiten[df_zeiten["Track Layout"] == layoutauswahl].copy()

    if daten.empty:
        st.info("Keine Daten für dieses Layout gefunden.")
        return

    # Datum konvertieren
    daten["Race_Date"] = pd.to_datetime(daten["Race_Date"], format="%d.%m.%Y", errors="coerce")

    # Zeit umwandeln in Sekunden
    def rundenzeit_in_sekunden(zeit):
        try:
            m, s = zeit.split(":")
            s, ms = s.split(",")
            return int(m) * 60 + int(s) + int(ms) / 1000
        except:
            return None

    daten["Best Lap (s)"] = daten["Best Lap"].apply(rundenzeit_in_sekunden)
    daten = daten.dropna(subset=["Race_Date", "Best Lap (s)"])

    if daten.empty:
        st.info("Keine gültigen Rundenzeiten vorhanden.")
        return

    # Diagramm anzeigen
    st.line_chart(daten.set_index("Race_Date")["Best Lap (s)"])

    # Rohdaten anzeigen (optional)
    st.markdown("### Tabelle der Rennen")
    st.dataframe(daten[["Race_Date", "Race_Time", "Auto", "Best Lap"]].sort_values("Race_Date"))
