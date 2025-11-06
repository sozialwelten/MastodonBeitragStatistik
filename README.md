# Mastodon Beiträge-Statistik Tool

Ein einfaches Python-Tool, das Mastodon-Posting-Aktivität analysiert und übersichtlich in der Kommandozeile darstellt.

## Features

- 📊 Zeigt Posts pro Monat seit Account-Erstellung
- 📅 Optional nur aktuellen Monat anzeigen
- 📈 Visuelles Balkendiagramm in der Konsole
- 🔄 Automatische Pagination für große Post-Mengen
- ❌ Boosts werden automatisch herausgefiltert (nur eigene Posts)
- 🔓 Keine Authentifizierung nötig (nutzt öffentliche API)

## Installation

### Voraussetzungen

- Python 3.6 oder höher
- `requests` Bibliothek

### Installation der Abhängigkeiten

```bash
pip install requests
```

## Verwendung

### Grundlegende Syntax

```bash
python mastodon_stats.py <username> [optionen]
```

### Beispiele

**Statistik für einen User auf mastodon.social:**
```bash
python mastodon_stats.py john
```

**User auf einer anderen Instanz:**
```bash
python mastodon_stats.py maria -i chaos.social
```

**Nur aktuellen Monat anzeigen:**
```bash
python mastodon_stats.py john -c
```

**Vollständiges Beispiel mit allen Optionen:**
```bash
python mastodon_stats.py alice -i fosstodon.org --current
```

## Parameter

| Parameter | Kurzform | Beschreibung | Standard |
|-----------|----------|--------------|----------|
| `username` | - | Benutzername (ohne @ und Instanz) | *erforderlich* |
| `--instance` | `-i` | Mastodon-Instanz | `mastodon.social` |
| `--current` | `-c` | Nur aktuellen Monat anzeigen | `False` |

## Ausgabeformat

### Vollständige Statistik

```
Suche Benutzer @john@mastodon.social...
Account erstellt am: 2022-11-15
Lade Posts...

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

## Technische Details

- Nutzt die öffentliche Mastodon API (v1)
- Balkendiagramm: Jeder Block (█) = 2 Posts, maximale Breite bei 100 Posts
- Boosts (Reblogs) werden nicht mitgezählt
- Pagination wird automatisch durchgeführt (40 Posts pro Request)

## Einschränkungen

- Funktioniert nur mit öffentlichen Profilen
- Zeigt nur öffentliche Posts an
- API-Rate-Limits der jeweiligen Instanz gelten

## Lizenz

GPL 3.0

## Author

Michael Karbacher