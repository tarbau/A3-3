# 📊 Finanzdaten-Analysator

Eine umfassende Python-Anwendung zur Analyse von Aktien und Kryptowährungen mit sowohl Konsolen-als auch Web-Oberflächen. Abrufen von Echtzeit-Finanzdaten, Berechnung von Statistiken und Visualisierung von Trends mit interaktiven Diagrammen.

## ✨ Funktionen

- **📈 Echtzeit-Datenabruf**: Abrufen aktueller Finanzdaten für Aktien und Kryptowährungen mit yfinance
- **🔢 Statistische Analyse**: Berechnung wichtiger Kennzahlen einschließlich:
  - Aktueller Preis, 52-Wochen-Hoch/Tief
  - Durchschnittspreise (30-Tage, 90-Tage, gesamt)
  - Preisänderungen und Prozentsätze
  - Volatilitätsberechnungen
- **💻 Doppelte Benutzeroberfläche**:
  - **Konsolen-Anwendung**: Befehlszeilen-Interface für schnelle Analysen
  - **Web-Dashboard**: Interaktive browserbasierte Oberfläche mit Plotly-Diagrammen
- **📊 Interaktive Visualisierungen**: Schöne, interaktive Diagramme mit Preisverlauf und Volumen
- **🌐 Multi-Asset-Unterstützung**: Analyse von Aktien (AAPL, GOOGL, TSLA) und Kryptowährungen (BTC-USD, ETH-USD)
- **🏗️ Modulare Architektur**: Saubere, wartbare Codestruktur mit klarer Trennung der Verantwortlichkeiten

## 🚀 Schnellstart

### Voraussetzungen

- Python 3.8 oder höher
- Internetverbindung (zum Abrufen von Daten)

### Installation

1. **Repository klonen**
   ```bash
   git clone https://github.com/tarbau/A3-3.git
   cd A3-3
   ```

2. **Virtuelle Umgebung erstellen und aktivieren**

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

### Anwendung starten

#### Option 1: Konsolen-Anwendung

```bash
python -m app.console_app AAPL
```

Ersetzen Sie `AAPL` durch ein beliebiges Ticker-Symbol (z.B. `GOOGL`, `TSLA`, `BTC-USD`).

#### Option 2: Web-Dashboard

```bash
python -m app.web_app
```

Öffnen Sie dann Ihren Browser und navigieren Sie zu: `http://localhost:5000`

#### Option 3: Batch-Dateien verwenden (Windows)

- Doppelklicken Sie auf `run_console.bat` für die Konsolen-App
- Doppelklicken Sie auf `run_web.bat` für das Web-Dashboard

## 📖 Verwendungsbeispiele

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

## 📁 Projektstruktur

```
SemProject/
├── app/
│   ├── console_app.py      # Einstiegspunkt der Konsolen-Anwendung
│   └── web_app.py          # Flask-Webanwendung
├── src/
│   ├── analyzer.py         # Finanzanalyse und Statistiken
│   ├── data_fetcher.py     # Datenabruf von yfinance
│   ├── config.py           # Konfigurationsverwaltung
│   └── utils.py            # Hilfsfunktionen
├── templates/
│   └── index.html          # HTML-Vorlage für Web-Dashboard
├── static/
│   └── style.css           # Styles für Web-Dashboard
├── tests/
│   └── test_utils.py       # Unit-Tests
├── requirements.txt        # Python-Abhängigkeiten
├── example_usage.py        # Beispiel-Verwendungsskript
├── QUICKSTART.md           # Schnellstart-Anleitung
├── SETUP_GUIDE.md          # Detaillierte Installationsanweisungen
└── README.md               # Diese Datei
```

## 🛠️ Verwendete Technologien

- **Python 3.8+**: Kernprogrammiersprache
- **yfinance**: Finanzdatenabruf
- **pandas**: Datenmanipulation und -analyse
- **numpy**: Numerische Berechnungen
- **Flask**: Web-Framework
- **Plotly**: Interaktive Datenvisualisierung
- **python-dotenv**: Verwaltung von Umgebungsvariablen

## 📊 Unterstützte Ticker

### Aktien
- `AAPL` - Apple Inc.
- `GOOGL` - Alphabet Inc. (Google)
- `MSFT` - Microsoft Corporation
- `TSLA` - Tesla, Inc.
- `AMZN` - Amazon.com, Inc.
- Und viele mehr...

### Kryptowährungen
- `BTC-USD` - Bitcoin
- `ETH-USD` - Ethereum
- `DOGE-USD` - Dogecoin
- `BNB-USD` - Binance Coin
- Und viele mehr...

## ⚙️ Konfiguration

Die Konfiguration wird in `src/config.py` verwaltet. Sie können anpassen:

- **Datenperiode**: Standard ist `1y` (1 Jahr)
  - Optionen: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max`
- **Datenintervall**: Standard ist `1d` (täglich)
  - Optionen: `1m`, `5m`, `15m`, `30m`, `1h`, `1d`, `5d`, `1wk`, `1mo`
- **Flask-Einstellungen**: Debug-Modus, Umgebungsvariablen

## 🐛 Fehlerbehebung

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

## 📚 Dokumentation

- **QUICKSTART.md**: Schnellstart-Anleitung (5 Minuten)
- **SETUP_GUIDE.md**: Detaillierte Installationsanweisungen
- **START_HERE.md**: Schritt-für-Schritt-Anleitung für den Einstieg

## 🧪 Tests

Tests ausführen mit:
```bash
pytest tests/
```

## 🤝 Beitragen

Beiträge sind willkommen! Bitte zögern Sie nicht, einen Pull Request einzureichen.

1. Forken Sie das Repository
2. Erstellen Sie Ihren Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Committen Sie Ihre Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Pushen Sie zum Branch (`git push origin feature/AmazingFeature`)
5. Öffnen Sie einen Pull Request

## 📝 Lizenz

Dieses Projekt ist Open Source und für Bildungszwecke verfügbar.

## 🙏 Danksagungen

- **yfinance**: Für den einfachen Zugang zu Finanzdaten
- **Plotly**: Für schöne interaktive Visualisierungen
- **Flask**: Für das leichtgewichtige Web-Framework

## 📧 Kontakt

Bei Fragen oder Problemen öffnen Sie bitte ein Issue auf GitHub.

## 🤖 LLM-Unterstützung

Dieses Projekt wurde mit Hilfe von Large Language Models (LLMs) entwickelt. LLMs unterstützten bei:
- **Debugging**: Fehleranalyse und Problemlösung
- **Code-Erklärungen**: Dokumentation und Konzept-Vermittlung
- **Frontend-Entwicklung**: UI/UX-Design, responsive Chart-Darstellung und CSS-Optimierung

---

**Viel Erfolg beim Analysieren! 📈**
