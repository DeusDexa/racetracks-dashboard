# tab1_logos.py
# ================================================================================
# TAB 1: Logos anzeigen und bei Klick zugehörige Layouts darstellen
# ================================================================================
import streamlit as st

def render_tab1(df_track_logos, df_layouts, df_zeiten, df_autos):
    # Session State initialisieren
    if "ausgewählte_strecke" not in st.session_state:
        st.session_state["ausgewählte_strecke"] = None
    if "ausgewähltes_layout" not in st.session_state:
        st.session_state["ausgewähltes_layout"] = None

    # Query-Parameter auslesen
    params = st.query_params.to_dict()
    if "ausgewählte_strecke" in params:
        st.session_state["ausgewählte_strecke"] = params["ausgewählte_strecke"]
    if "ausgewähltes_layout" in params:
        st.session_state["ausgewähltes_layout"] = params["ausgewähltes_layout"]

    # Dynamischer Titel
    if st.session_state["ausgewähltes_layout"]:
        st.subheader(f"Rennen auf {st.session_state['ausgewähltes_layout']}")
    elif st.session_state["ausgewählte_strecke"]:
        st.subheader(f"Layouts für {st.session_state['ausgewählte_strecke']}")
    else:
        st.subheader("Streckenlogos (Klick auf Logo → Layouts → Rennen)")

    # === Fall 1: Logos anzeigen ===
    if not st.session_state["ausgewählte_strecke"]:
        columns = st.columns(3)
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

    # === Fall 2: Layouts anzeigen ===
    elif st.session_state["ausgewählte_strecke"] and not st.session_state["ausgewähltes_layout"]:
        strecke = st.session_state["ausgewählte_strecke"]
        passende_layouts = df_layouts[df_layouts["Streckenname"] == strecke]

        for _, layout in passende_layouts.iterrows():
            st.markdown(
                f"""
                <a href="?ausgewählte_strecke={strecke}&ausgewähltes_layout={layout['Track Layout']}" style="text-decoration: none;">
                    <img src="{layout['Track Layout Image-Link']}"
                         style="border: 2px solid black; border-radius: 6px; width: 100%;">
                    <div style="text-align: center; font-weight: bold; margin-top: 8px;">{layout['Track Layout']}</div>
                </a>
                """,
                unsafe_allow_html=True
            )

        if st.button("🔙 Zurück zu den Logos"):
            st.session_state["ausgewählte_strecke"] = None
            st.query_params.clear()
            st.rerun()

    # === Fall 3: Rennen auf Layout anzeigen ===
    elif st.session_state["ausgewähltes_layout"]:
        layout = st.session_state["ausgewähltes_layout"]
        rennen = df_zeiten[df_zeiten["Track Layout"] == layout]

        if not rennen.empty:
            st.dataframe(rennen)
        else:
            st.info("Keine Rennen auf diesem Layout gefunden.")

        # Fahrzeuge, die auf diesem Layout fuhren
        autos = rennen["Auto"].unique()
        fahrzeuge = df_autos[df_autos["Auto"].isin(autos)]

        st.subheader(f"🚗 Fahrzeuge auf '{layout}'")

        for _, auto in fahrzeuge.iterrows():
            st.markdown("---")
            cols = st.columns([1, 2])

            with cols[0]:
                if pd.notna(auto["Car_Image"]):
                    st.image(auto["Car_Image"], use_container_width=True)

            with cols[1]:
                st.markdown(f"**{auto['Auto']}**  |  **Hersteller:** {auto['Hersteller']}  |  **Klasse:** {auto['klasse']}")
                fahrten = rennen[rennen["Auto"] == auto["Auto"]]
                st.markdown(f"Rennen: {len(fahrten)}")

                bestzeit = fahrten["Best Lap"].min() if not fahrten.empty else "--"
                st.markdown(f"Bestzeit: {bestzeit}")

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