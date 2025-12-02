# Reverse Shell Framework (Basic)

Ein kleines Reverse-Shell-Framework für Lernzwecke.

## Komponenten

- `listener/` – Einfacher Listener (C2-ähnlich), der auf eingehende Verbindungen wartet  
- `client/` – Reverse-Shell-Client, der sich zum Listener verbindet und Kommandos ausführt

> Nutzung nur in einer kontrollierten, legalen Testumgebung (z. B. eigene VM, eigenes Netzwerk).

---

## Listener starten

```bash
python3 listener/reverse_listener.py
