# Reverse Shell Framework (Basic)

Ein kleines Reverse-Shell-Framework für Lernzwecke im Bereich Offensive Security, Networking und Payload-Entwicklung.  
Nutzung ausschließlich in einer legalen, kontrollierten Testumgebung (z. B. eigene VM, eigenes Netzwerk).

---

## 📁 Projektstruktur

```
reverse-shell-framework/
│── listener/
│   └── reverse_listener.py
│── client/
│   └── reverse_client.py
└── README.md
```

---

## 🎯 Überblick

Dieses Framework besteht aus:

- **Listener (Server)**  
  Wartet auf eingehende Verbindungen und erlaubt Command Execution.

- **Client (Payload)**  
  Verbindet sich zurück zum Listener, führt Befehle aus und sendet den Output zurück.

Damit lernst du Grundlagen von:
- Reverse Shell Mechanics  
- Networking (Sockets)  
- Command Execution via Python  
- Basis von C2-Frameworks  
- Client-Server-Kommunikation  

---

## 🚀 Listener starten

```bash
python3 listener/reverse_listener.py
```

Standard-Port: **4444**

---

## 📡 Client starten

```bash
python3 client/reverse_client.py
```

Standard-IP: **127.0.0.1**  
→ in `reverse_client.py` anpassbar:

```python
SERVER_IP = "127.0.0.1"
SERVER_PORT = 4444
```

---

## 🛠 Features (Version 1.0)

- Einfache Reverse-Shell-Verbindung  
- Ausführung beliebiger Kommandos  
- Empfang der kompletten Ausgabe  
- Sauber getrennte Struktur (Client/Listener)  
- Klare Grundlage für ein echtes C2-Framework  

---

## 🔧 Geplante Features (Version 2)

- Mehrere Clients gleichzeitig  
- Client-Authentifizierung / Schlüssel  
- AES-Verschlüsselung des Traffics  
- Datei-Upload & Download  
- Persistenz (lokale Testumgebungen)  
- Logging & Sessions  
- Traffic-Obfuscation  

---

## ⚠️ Hinweis

Dieses Projekt dient ausschließlich:
- dem Lernen  
- der technischen Weiterentwicklung  
- eigenen Testumgebungen  
- NICHT für reale Systeme ohne schriftliche Erlaubnis

---

## 👤 Autor

**NotSomewhere**  
https://github.com/NotSomewhere
