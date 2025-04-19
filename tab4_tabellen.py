# tab4_tabellen.py
# ================================================================================
# TAB 4: Tabellenansicht aller geladenen Daten (zur Kontrolle & Übersicht)
# ================================================================================
import streamlit as st


def render_tab4(df_zeiten, df_autos, df_racetype, df_layouts, df_track_logos):
    st.subheader("\U0001F4CB Tabellenansicht aller Daten")

    st.markdown("#### Zeiten")
    st.dataframe(df_zeiten)

    st.markdown("#### Autos")
    st.dataframe(df_autos)

    st.markdown("#### Racetypen")
    st.dataframe(df_racetype)

    st.markdown("#### Layouts")
    st.dataframe(df_layouts)

    st.markdown("#### Track Logos")
    st.dataframe(df_track_logos)
