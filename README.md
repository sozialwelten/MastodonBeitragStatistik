# Mastodon Beitrag Statistik

Ein einfaches Python-Tool, das deine Mastodon-Posting-Aktivität analysiert und übersichtlich in der Kommandozeile darstellt.

## Features

- 📊 Zeigt Posts pro Monat seit Account-Erstellung
- 📅 Optional nur aktuellen Monat anzeigen
- 📈 Visuelles Balkendiagramm in der Konsole
- 🔒 **Unterstützt Authentifizierung für private/unlisted Posts**
- 🔄 Automatische Pagination für große Post-Mengen
- ❌ Boosts werden automatisch herausgefiltert (nur eigene Posts)
- 🔓 Funktioniert auch ohne Authentifizierung für öffentliche Profile

## Installation

### Voraussetzungen

- Python 3.6 oder höher
- `requests` Bibliothek

### Installation der Abhängigkeiten

```bash
pip install requests
```

## Authentifizierung einrichten (optional)

Um auch nicht-öffentliche Posts (unlisted, followers-only, private) zu analysieren, benötigst du einen Access Token:

### Access Token erstellen

1. Gehe auf deine Mastodon-Instanz → **Einstellungen** → **Entwicklung**
2. Klicke auf **Neue Anwendung**
3. Name: z.B. "Stats Tool"
4. Berechtigungen: **Nur `read:accounts` und `read:statuses` aktivieren**
5. Speichern und den generierten **Access Token** kopieren

### Token sicher verwenden

**Empfohlen: Via Umgebungsvariable**
```bash
export MASTODON_TOKEN="dein_access_token_hier"
```

Dann kannst du das Tool ohne Token-Parameter nutzen.

## Verwendung

### Öffentliche Profile (ohne Authentifizierung)

```bash
# User auf mastodon.social
python mastodon_stats.py john

# User auf anderer Instanz
python mastodon_stats.py maria -i chaos.social

# Nur aktueller Monat
python mastodon_stats.py john -c
```

### Eigener Account mit Authentifizierung

**Via Umgebungsvariable (empfohlen):**
```bash
export MASTODON_TOKEN="dein_token"
python mastodon_stats.py -i deine.instanz
```

**Via Parameter:**
```bash
python mastodon_stats.py -i deine.instanz -t "dein_token"
```

**Nur aktueller Monat:**
```bash
python mastodon_stats.py -i deine.instanz -c
```

### Anderen Account mit Authentifizierung

```bash
python mastodon_stats.py username -i instanz -t "dein_token"
```

Dies zeigt alle Posts, die für dich sichtbar sind (z.B. wenn du dem Account folgst).

## Parameter

| Parameter | Kurzform | Beschreibung | Standard |
|-----------|----------|--------------|----------|
| `username` | - | Benutzername (ohne @ und Instanz). Optional bei `--token` für eigenen Account | *optional* |
| `--instance` | `-i` | Mastodon-Instanz | `mastodon.social` |
| `--current` | `-c` | Nur aktuellen Monat anzeigen | `False` |
| `--token` | `-t` | Access Token für private Posts | `None` |

**Umgebungsvariable:** `MASTODON_TOKEN` wird automatisch erkannt, wenn gesetzt.

## Ausgabeformat

### Vollständige Statistik

```
Rufe eigenen Account von chaos.social ab...
Account: @maria
Account erstellt am: 2022-11-15
Lade Posts (inkl. nicht-öffentliche)...

═══════════════════════════════════
  Statistik: Posts pro Monat
═══════════════════════════════════
  2022-11:   12 ██████
  2022-12:   45 ██████████████████████
  2023-01:   67 █████████████████████████████████
  2023-02:   89 ████████████████████████████████████████████
  2025-11:   23 ███████████ ← Aktueller Monat
═══════════════════════════════════
  Gesamt: 236 Posts
═══════════════════════════════════
```

### Nur aktueller Monat

```
═══════════════════════════════════
  Aktueller Monat (2025-11)
═══════════════════════════════════
  Posts: 23
═══════════════════════════════════
```

## Authentifizierung vs. Öffentlich

| Modus | Was wird angezeigt |
|-------|-------------------|
| **Ohne Token** | Nur öffentliche Posts |
| **Mit Token (eigener Account)** | Alle eigenen Posts (public, unlisted, followers-only, private) |
| **Mit Token (fremder Account)** | Alle Posts, die für dich sichtbar sind |

## Technische Details

- Nutzt die Mastodon API v1
- Balkendiagramm: Jeder Block (█) = 2 Posts, maximale Breite bei 100 Posts
- Boosts (Reblogs) werden nicht mitgezählt
- Pagination wird automatisch durchgeführt (40 Posts pro Request)
- Token-Berechtigungen: `read:accounts`, `read:statuses`

## Sicherheit

⚠️ **Wichtig:**
- Speichere deinen Access Token nie in Skripten oder Git-Repositories
- Nutze Umgebungsvariablen für den Token
- Setze nur minimal nötige Berechtigungen (read-only)
- Du kannst den Token jederzeit in den Mastodon-Einstellungen widerrufen

## Beispiel-Workflow

```bash
# 1. Token als Umgebungsvariable setzen (einmalig pro Session)
export MASTODON_TOKEN="dein_super_geheimer_token"

# 2. Verschiedene Accounts analysieren
python mastodon_stats.py -i mastodon.social    # Eigener Account
python mastodon_stats.py alice -i chaos.social  # Fremder Account
python mastodon_stats.py -i mastodon.social -c  # Nur aktueller Monat

# 3. Token aus Environment entfernen (optional)
unset MASTODON_TOKEN
```

## Lizenz

GPL 3.0

## Author

Michael Karbacher