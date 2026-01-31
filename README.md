# Finanzdaten-Analysator

## 1. Zielsetzung und Funktionalität

<<<<<<< HEAD
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
=======
## Funktionen

- **Echtzeit-Datenabruf**: Abrufen aktueller Finanzdaten für Aktien und Kryptowährungen mit yfinance
- **Statistische Analyse**: Berechnung wichtiger Kennzahlen einschließlich:
  - Aktueller Preis, 52-Wochen-Hoch/Tief
  - Durchschnittspreise (30-Tage, 90-Tage, gesamt)
  - Preisänderungen und Prozentsätze
  - Volatilitätsberechnungen
- **Doppelte Benutzeroberfläche**:
  - **Konsolen-Anwendung**: Befehlszeilen-Interface für schnelle Analysen
  - **Web-Dashboard**: Interaktive browserbasierte Oberfläche mit Plotly-Diagrammen
- **Interaktive Visualisierungen**: Schöne, interaktive Diagramme mit Preisverlauf und Volumen
- **Multi-Asset-Unterstützung**: Analyse von Aktien (AAPL, GOOGL, TSLA) und Kryptowährungen (BTC-USD, ETH-USD)
- **Modulare Architektur**: Saubere, wartbare Codestruktur mit klarer Trennung der Verantwortlichkeiten

>>>>>>> e9c015751f0f5e605680cc3f9dbb59cd22cad1b2

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

<<<<<<< HEAD
### Projektstruktur
=======
#### Option 3: Batch-Dateien verwenden (Windows)

- Doppelklicken Sie auf `run_console.bat` für die Konsolen-App
- Doppelklicken Sie auf `run_web.bat` für das Web-Dashboard

## Verwendungsbeispiele

### Konsolen-Anwendung

```bash
# Apple-Aktie analysieren
python -m app.console_app AAPL

# Bitcoin analysieren
python -m app.console_app BTC-USD

# Tesla analysieren
python -m app.console_app TSLA
```

### Web-Dashboard

1. Server starten: `python -m app.web_app`
2. `http://localhost:5000` im Browser öffnen
3. Ticker-Symbol eingeben (z.B. `AAPL`, `GOOGL`, `BTC-USD`)
4. Auf "Analyze" klicken, um interaktive Diagramme und Statistiken zu sehen

### Programmatische Verwendung

```python
from src.data_fetcher import data_fetcher
from src.analyzer import analyzer

# Daten abrufen
ticker_obj = data_fetcher.fetch_data("AAPL")

# Unternehmensinformationen abrufen
company_info = data_fetcher.get_company_info(ticker_obj)

# Aktuellen Preis abrufen
current_price = data_fetcher.get_current_price(ticker_obj)

# Historische Daten abrufen
historical_data = data_fetcher.get_historical_data(ticker_obj)

# Statistiken berechnen
stats = analyzer.calculate_statistics(historical_data, current_price, "USD")
```

Siehe `example_usage.py` für detailliertere Beispiele.

## Projektstruktur
>>>>>>> e9c015751f0f5e605680cc3f9dbb59cd22cad1b2

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

<<<<<<< HEAD
### Architektur
=======
## Verwendete Technologien
>>>>>>> e9c015751f0f5e605680cc3f9dbb59cd22cad1b2

- **`app/`**: Anwendungseinstiegspunkte (Konsolen- und Web-Interface)
- **`src/`**: Kernfunktionalität (Datenabruf, Analyse, Konfiguration)
- **`src/extensions/`**: Erweiterte Funktionalitäten (Prognose-Algorithmen)
- **`templates/`** und **`static/`**: Frontend-Ressourcen für Web-Dashboard
- **`tests/`**: Unit-Tests

<<<<<<< HEAD
## 4. Gruppenmitglieder und Teilaufgaben
=======
## Unterstützte Ticker
>>>>>>> e9c015751f0f5e605680cc3f9dbb59cd22cad1b2

### Gruppenmitglieder

| Name | Matrikelnummer | Teilaufgaben |
|------|----------------|--------------|
| [Name 1] | [Matrikelnummer] | [Aufgabenbeschreibung] |
| [Name 2] | [Matrikelnummer] | [Aufgabenbeschreibung] |
| [Name 3] | [Matrikelnummer] | [Aufgabenbeschreibung] |

<<<<<<< HEAD
### Detaillierte Aufgabenverteilung
=======
## Konfiguration
>>>>>>> e9c015751f0f5e605680cc3f9dbb59cd22cad1b2

#### [Name 1]
- **Aufgabe 1**: [Beschreibung der übernommenen Aufgabe]
- **Aufgabe 2**: [Beschreibung der übernommenen Aufgabe]
- **Implementierte Module**: [z.B. `src/data_fetcher.py`, `app/console_app.py`]

#### [Name 2]
- **Aufgabe 1**: [Beschreibung der übernommenen Aufgabe]
- **Aufgabe 2**: [Beschreibung der übernommenen Aufgabe]
- **Implementierte Module**: [z.B. `src/analyzer.py`, `app/web_app.py`]

<<<<<<< HEAD
#### [Name 3]
- **Aufgabe 1**: [Beschreibung der übernommenen Aufgabe]
- **Aufgabe 2**: [Beschreibung der übernommenen Aufgabe]
- **Implementierte Module**: [z.B. `templates/index.html`, `static/style.css`]

=======
## Fehlerbehebung

### ModuleNotFoundError
- **Lösung**: Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist und die Abhängigkeiten installiert sind
  ```bash
  pip install -r requirements.txt
  ```

### Daten können nicht abgerufen werden
- **Lösung**: 
  - Überprüfen Sie Ihre Internetverbindung
  - Überprüfen Sie, ob das Ticker-Symbol korrekt ist
  - Versuchen Sie ein anderes Ticker (z.B. `AAPL`, `GOOGL`, `BTC-USD`)

### Port 5000 bereits in Verwendung
- **Lösung**: Ändern Sie den Port in `app/web_app.py` (Zeile 207) oder beenden Sie den Prozess, der Port 5000 verwendet

### Ausführungsrichtlinien-Fehler (Windows)
- **Lösung**: Führen Sie diesen Befehl in PowerShell aus:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

## Dokumentation

- **QUICKSTART.md**: Schnellstart-Anleitung (5 Minuten)
- **SETUP_GUIDE.md**: Detaillierte Installationsanweisungen
- **START_HERE.md**: Schritt-für-Schritt-Anleitung für den Einstieg

##  Tests

Tests ausführen mit:
```bash
pytest tests/



##  Danksagungen

- **yfinance**: Für den einfachen Zugang zu Finanzdaten
- **Plotly**: Für schöne interaktive Visualisierungen
- **Flask**: Für das leichtgewichtige Web-Framework


## LLM-Unterstützung

Dieses Projekt wurde mit Hilfe von Large Language Models (LLMs) entwickelt. LLMs unterstützten bei:
- **Debugging**: Fehleranalyse und Problemlösung
- **Code-Erklärungen**: Dokumentation und Konzept-Vermittlung
- **Frontend-Entwicklung**: UI/UX-Design, responsive Chart-Darstellung und CSS-Optimierung
>>>>>>> e9c015751f0f5e605680cc3f9dbb59cd22cad1b2
