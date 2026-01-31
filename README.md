# Finanzdaten-Analysator

## 1. Zielsetzung und Funktionalität

### Zielsetzung

Entwicklung einer Python-Anwendung zur Analyse von Aktien und Kryptowährungen mit folgenden Zielen:

- Automatisierter Abruf von Echtzeit-Finanzdaten über yfinance
- Berechnung statistischer Kennzahlen (Preise, Durchschnitte, Volatilität)
- Interaktive Visualisierung von Preisverläufen
- Bereitstellung von Konsolen- und Web-Interface

### Funktionalität

- **Datenabruf**: Echtzeit-Finanzdaten für Aktien und Kryptowährungen
- **Statistische Analyse**: Aktueller Preis, 52-Wochen-Hoch/Tief, Durchschnittspreise, Volatilität
- **Zwei Benutzeroberflächen**:
  - Konsolen-Anwendung (Befehlszeilen-Interface)
  - Web-Dashboard (Browser-basiert mit Plotly-Diagrammen)
- **Visualisierung**: Interaktive Diagramme mit Preisverlauf und Volumen

## 2. Hinweise zur Ausführung

### Voraussetzungen

- Python 3.8 oder höher
- Internetverbindung

### Installation

1. Repository klonen:
   ```bash
   git clone https://github.com/tarbau/A3-3.git
   cd A3-3
   ```

2. Virtuelle Umgebung erstellen und aktivieren:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

### Anwendung starten

**Konsolen-Anwendung:**
```bash
python -m app.console_app AAPL
```

**Web-Dashboard:**
```bash
python -m app.web_app
```
Dann Browser öffnen: `http://localhost:5000`

## 3. Aufbau des Projekts

### Projektstruktur

```
SemProject/
├── app/
│   ├── console_app.py      # Konsolen-Anwendung
│   └── web_app.py          # Flask-Webanwendung
├── src/
│   ├── analyzer.py         # Finanzanalyse und Statistiken
│   ├── data_fetcher.py     # Datenabruf von yfinance
│   ├── config.py           # Konfiguration
│   ├── utils.py            # Hilfsfunktionen
│   └── extensions/
│       └── forecasting/
│           └── arima_forecaster.py  # ARIMA-Prognose
├── templates/
│   └── index.html          # HTML-Vorlage
├── static/
│   └── style.css           # Styles
├── tests/
│   └── test_utils.py       # Unit-Tests
└── requirements.txt        # Python-Abhängigkeiten
```

### Architektur

- **`app/`**: Anwendungseinstiegspunkte (Konsolen- und Web-Interface)
- **`src/`**: Kernfunktionalität (Datenabruf, Analyse, Konfiguration)
- **`src/extensions/`**: Erweiterte Funktionalitäten (Prognose-Algorithmen)
- **`templates/`** und **`static/`**: Frontend-Ressourcen für Web-Dashboard
- **`tests/`**: Unit-Tests

## 4. Gruppenmitglieder und Teilaufgaben

### Gruppenmitglieder

| Name | Matrikelnummer | Teilaufgaben |
|------|----------------|--------------|
| [Name 1] | [Matrikelnummer] | [Aufgabenbeschreibung] |
| [Name 2] | [Matrikelnummer] | [Aufgabenbeschreibung] |
| [Name 3] | [Matrikelnummer] | [Aufgabenbeschreibung] |

### Detaillierte Aufgabenverteilung

#### [Name 1]
- **Aufgabe 1**: [Beschreibung der übernommenen Aufgabe]
- **Aufgabe 2**: [Beschreibung der übernommenen Aufgabe]
- **Implementierte Module**: [z.B. `src/data_fetcher.py`, `app/console_app.py`]

#### [Name 2]
- **Aufgabe 1**: [Beschreibung der übernommenen Aufgabe]
- **Aufgabe 2**: [Beschreibung der übernommenen Aufgabe]
- **Implementierte Module**: [z.B. `src/analyzer.py`, `app/web_app.py`]

#### [Name 3]
- **Aufgabe 1**: [Beschreibung der übernommenen Aufgabe]
- **Aufgabe 2**: [Beschreibung der übernommenen Aufgabe]
- **Implementierte Module**: [z.B. `templates/index.html`, `static/style.css`]

