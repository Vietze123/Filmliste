# v92 – Datensicherung & PWA-Updates
## Sichere lokale Sicherung
- Bis zu fünf gültige Sicherungsstände des kanonischen `mouseMovieAppV6`-Zustands.
- Sicherung bei Start, relevanter Änderung, Verlassen der Seite und vor PWA-Update.
- Identische Stände werden nicht mehrfach gespeichert.
- Falls der aktuelle JSON-Zustand beschädigt ist, wird beim Start der jüngste gültige Stand verwendet.
- Interne API `window.v92Backup` für manuelle Sicherung/Restore-Erweiterungen.

## PWA
- Einmal pro Sitzung wird kontrolliert nach einem neuen Service Worker gesucht.
- Ein wartendes Update wird nicht überraschend aktiviert.
- Stattdessen erscheint eine kleine mausige Meldung mit „Aktualisieren“.
- Vor Aktivierung wird ein Sicherungsstand erstellt.
- Danach wird genau einmal neu geladen.
