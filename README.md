# Racetracks Dashboard (Gran Turismo 7)

## ✨ Projektziel
Visualisierung und Auswertung von selbst gefahrenen Rennen aus Gran Turismo 7 – inklusive Strecken, Fahrzeuge, Rennmodi, Zeiten und Bildern. Die Daten werden in Google Sheets gepflegt und über Streamlit in einer Web-App dargestellt.

---

## 📂 Datenstruktur (Google Sheets)

### Tabellenblätter:
- **Zeiten**: Gefahrene Rennen mit Datum, Layout, Auto, Reifen, Laps, Gesamtzeit, Best Lap etc.
- **Autos**: Liste verwendeter Fahrzeuge mit Car-ID, Hersteller, Klasse
- **Racetype**: Liste der unterschiedlichen Renn-Modi (Daily, Nations Cup etc.)
- **Layouts**: Alle Streckenlayouts (inkl. Image-Link & Streckenzuordnung)
- **Track_logos**: Logos der Strecken (mit Streckennamen zur Verknüpfung)

---

## 🔗 Google Sheets-Anbindung

Die Tabellen werden direkt per CSV-Link in die App geladen:

```python
sheet_url = "https://docs.google.com/spreadsheets/d/DEIN_SHEET_ID/export?format=csv&gid=TABELLENBLATT_ID"
```

In `streamlit_app.py` per `pandas.read_csv()` geladen und als DataFrames genutzt:

```python
df_zeiten = pd.read_csv(url_zeiten)
df_autos = pd.read_csv(url_autos)
...
```

---

## 💻 Streamlit Setup

### Lokale Projektdateien:
- `streamlit_app.py` – Hauptanwendung
- `requirements.txt` – Python-Abhängigkeiten (`streamlit`, `pandas`)

### Deployment:
1. Projekt auf **GitHub** hochgeladen
2. Deployment über [streamlit.io/cloud](https://streamlit.io/cloud)
3. App-URL: [racetracks-dashboard.streamlit.app](https://racetracks-dashboard-4zcsrreq2ufpw9wvb5mm8q.streamlit.app/)

---

## ✅ Aktueller Stand (Live)
- App lädt alle Tabellenblätter aus Google Sheets
- Tabellen werden direkt in der App angezeigt
- Sheet kann aktualisiert werden – Streamlit lädt beim Refresh neu

---

## 🚀 Nächste Schritte
- Filter (nach Strecke, Auto, Zeitraum)
- Verknüpfungen via IDs (Layout_ID, Car_ID)
- Diagramme: Bestzeitverlauf, Speed-Auswertung
- Bildanzeige: Streckenlogos & Layouts
- UI-Optimierung (Tabs, Menüs, Farben)

---

## 💼 Autor & Projekt
Projektidee & Daten: Dexa  
Umsetzung & Support: ChatGPT + Streamlit Community Cloud  
Status: **Work in Progress**
