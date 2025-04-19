# tab3_autos.py
# ================================================================================
# TAB 3: Fahrzeugübersicht mit Filter, Bild und Streckeninfo
# ================================================================================
import streamlit as st
import pandas as pd

def render_tab3(df_autos, df_zeiten):
    st.subheader("\U0001F697 Gefahrene Fahrzeuge")

    # === Dropdown-Filter ===
    col1, col2 = st.columns(2)
    with col1:
        ausgewählte_klasse = st.selectbox("Filter nach Klasse", ["Alle"] + sorted(df_autos["klasse"].dropna().unique()))
    with col2:
        ausgewählter_hersteller = st.selectbox("Filter nach Hersteller", ["Alle"] + sorted(df_autos["Hersteller"].dropna().unique()))

    # === Häufigkeit der Nutzung (Rennanzahl) ===
    renn_counts = df_zeiten["Auto"].value_counts().to_dict()
    df_autos["Rennen"] = df_autos["Auto"].map(renn_counts).fillna(0).astype(int)

    # === Filter anwenden ===
    autos = df_autos.copy()
    if ausgewählte_klasse != "Alle":
        autos = autos[autos["klasse"] == ausgewählte_klasse]
    if ausgewählter_hersteller != "Alle":
        autos = autos[autos["Hersteller"] == ausgewählter_hersteller]

    # === Sortieren nach Anzahl der Rennen ===
    autos = autos.sort_values(by="Rennen", ascending=False)

    # === Anzeige jedes Autos ===
    for _, auto in autos.iterrows():
        st.markdown("---")
        cols = st.columns([1, 2])

        with cols[0]:
            if pd.notna(auto["Car_Image"]):
                st.image(auto["Car_Image"], use_container_width=True)

        with cols[1]:
            st.markdown(f"**{auto['Auto']}**  |  **Rennen:** {auto['Rennen']}")
            st.markdown(f"Hersteller: {auto['Hersteller']}  |  Klasse: {auto['klasse']}")

            # Beste Zeiten pro Layout, max 3 anzeigen
            fahrten = df_zeiten[df_zeiten["Auto"] == auto["Auto"]]
            layouts = (
                fahrten.groupby("Track Layout")["Best Lap"]
                .min()
                .reset_index()
                .sort_values("Best Lap")
                .head(3)
            )

            for _, row in layouts.iterrows():
                st.markdown(f"{row['Track Layout']}: {row['Best Lap']}")

            # Falls weniger als 3: leere Zeilen auffüllen
            for _ in range(3 - len(layouts)):
                st.markdown("&nbsp;")
