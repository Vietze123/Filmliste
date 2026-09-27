# v91 – Performance & Bedienung

Basis: v90.1.

## Schwerpunkt
- „Überrasche mich“ gegen Doppelauslösung und versehentliche schnelle Folge-Taps geschützt.
- 720 ms Cooldown nach einer gültigen Auslösung.
- Kurzes, bewusstes Touch-Feedback vor der Auswahl.
- Historische Touch-/Click-Duplikate werden am Überraschungsbutton abgefangen.
- Hauptaktionen erhalten Schutz gegen sehr schnelle doppelte Pointer-Aktionen.
- Filmkarten werden für neue v91-Logik gecacht statt bei jeder Abfrage neu gesammelt.
- Cache wird nur invalidiert, wenn Filmkarten tatsächlich zum DOM hinzukommen/entfernt werden.
- Bestehende Feature-Handler wurden nicht neu geschrieben, um die bestätigte Funktionalität von v89.3/v90.1 zu erhalten.
- Mausig-Design, Filmabend, Easter Eggs, intelligente Suche, Vorschläge und Angesehen-Liste bleiben erhalten.

## Technischer Ansatz
v91 ist eine gezielte Konsolidierung der Interaktionsschicht. Kritische historische Feature-Implementierungen werden nicht pauschal entfernt; stattdessen werden Mehrfachauslösungen zentral vor den bestehenden Handlern gefiltert.
