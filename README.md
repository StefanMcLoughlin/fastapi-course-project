# FastAPI Kursprojekt

Status: Abgeschlossenes Ausbildungsprojekt – Fokus auf Backend-Entwicklung mit FastAPI, PostgreSQL, SQLAlchemy, JWT-Authentifizierung und automatisierten Tests.

Dieses Projekt wurde im Rahmen meiner Ausbildung zum Backend- und AI-Entwickler erstellt.

Ziel war es, moderne Backend-Entwicklung mit Python, FastAPI, PostgreSQL und SQLAlchemy praxisnah zu erlernen und dabei professionelle Entwicklungsprozesse wie Datenbankmigrationen, Authentifizierung und automatisierte Tests umzusetzen.

---

# Funktionen

## Benutzerverwaltung

* Benutzerregistrierung
* Passwort-Hashing mit bcrypt
* Benutzer-Login
* JWT-Authentifizierung
* OAuth2 Password Flow

## Authentifizierung & Autorisierung

* Geschützte Endpunkte
* JWT Access Tokens
* Benutzer können nur ihre eigenen Beiträge bearbeiten oder löschen
* Rollenbasierte Zugriffskontrolle über Owner-Prüfungen

## Posts

* Beitrag erstellen
* Alle Beiträge abrufen
* Einzelnen Beitrag abrufen
* Beitrag aktualisieren
* Beitrag löschen
* Pagination (Limit & Offset)
* Suchfunktion über Titel

## Voting-System

* Beiträge liken/voten
* Votes entfernen
* Doppelte Votes verhindern
* Composite Primary Keys
* Foreign-Key-Beziehungen

---

# Datenbank

Verwendete Technologien:

* PostgreSQL
* SQLAlchemy ORM
* Relationale Datenbanken
* Foreign Keys
* Relationships
* Dependency Injection für Datenbank-Sessions

---

# Datenbank-Migrationen

Für Versionsverwaltung der Datenbankstruktur wurde Alembic verwendet.

Funktionen:

* Migrationen erstellen
* Datenbankschema versionieren
* Upgrades
* Downgrades
* Nachvollziehbare Datenbankänderungen

---

# Testing

Das Projekt enthält automatisierte Tests mit pytest.

Getestete Bereiche:

* Benutzerregistrierung
* Login
* JWT Tokens
* Authentifizierung
* Autorisierung
* CRUD-Funktionen
* Voting-System

Verwendete Konzepte:

* FastAPI TestClient
* Fixtures
* Dependency Overrides
* Separate Testdatenbank
* Parametrized Tests

---

# Verwendete Technologien

## Backend

* Python
* FastAPI
* Uvicorn

## Datenbank

* PostgreSQL
* SQLAlchemy
* Alembic

## Authentifizierung

* JWT
* OAuth2
* Passlib (bcrypt)

## Testing

* pytest
* FastAPI TestClient

## Entwicklung

* Git
* GitHub
* Postman
* pgAdmin

---

# Projektstruktur

```text
app/
├── routers/
│   ├── post.py
│   ├── user.py
│   ├── auth.py
│   └── vote.py
│
├── database.py
├── models.py
├── schemas.py
├── oauth2.py
├── config.py
├── utils.py
└── main.py

tests/
├── conftest.py
├── test_users.py
├── test_posts.py
└── test_votes.py

alembic/
└── versions/
```

---

# API-Endpunkte

## Benutzer

```http
POST /users/
POST /login
```

## Posts

```http
GET    /posts/
GET    /posts/{id}
POST   /posts/
PUT    /posts/{id}
DELETE /posts/{id}
```

## Votes

```http
POST /vote/
```

---

# Projekt starten

## Virtuelle Umgebung erstellen

```bash
python -m venv .venv
```

## Virtuelle Umgebung aktivieren

```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

## Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

## FastAPI starten

```bash
uvicorn app.main:app --reload
```

---

# Tests ausführen

```bash
pytest
```

---

# Was ich in diesem Projekt gelernt habe

* Entwicklung moderner REST APIs
* FastAPI Framework
* PostgreSQL
* SQLAlchemy ORM
* JWT Authentifizierung
* OAuth2
* Autorisierung über Owner-Prüfungen
* Alembic Migrationen
* pytest
* Testdatenbanken
* Git & GitHub Workflows
* Strukturierung größerer Backend-Projekte

---

# Nächste Schritte

Geplante Erweiterungen und Lernziele:

* Docker
* CI/CD Pipelines
* GitHub Actions
* Deployment auf Linux-Servern
* NGINX
* Cloud Deployment
* Eigene produktionsreife Backend-Projekte

---

# Autor

**Stefan McLoughlin**

Backend Development • AI Engineering • Automation

GitHub:
https://github.com/StefanMcLoughlin
