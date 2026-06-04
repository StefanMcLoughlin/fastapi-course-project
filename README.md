# FastAPI Kursprojekt

## Überblick

Dieses Projekt wurde im Rahmen eines FastAPI-Backend-Kurses entwickelt und dient als praktische Lernanwendung für moderne Backend- und API-Entwicklung mit Python.

Das Projekt hat sich von einer einfachen CRUD-API zu einer vollständigen Backend-Anwendung mit Datenbankanbindung, Benutzerverwaltung und JWT-Authentifizierung entwickelt.

## Funktionen

### Beiträge (Posts)

* Beiträge erstellen
* Alle Beiträge abrufen
* Einzelne Beiträge abrufen
* Beiträge aktualisieren
* Beiträge löschen

### Benutzerverwaltung

* Benutzer registrieren
* Benutzerdaten abrufen
* Sichere Speicherung von Passwörtern durch Hashing
* Passwörter werden niemals über die API zurückgegeben

### Authentifizierung

* Benutzer-Login
* Erstellung von JWT Access Tokens
* Token-Validierung
* Geschützte Endpunkte über OAuth2
* Authentifizierung über Dependency Injection

---

## Verwendete Technologien

### Backend

* Python
* FastAPI
* SQLAlchemy ORM
* PostgreSQL

### Sicherheit

* JWT (JSON Web Tokens)
* OAuth2 Password Flow
* bcrypt
* Passlib

### Datenvalidierung

* Pydantic v2

### Entwicklungstools

* Postman
* pgAdmin 4
* Git
* GitHub

---

## Projektstruktur

```text
app/
├── routers/
│   ├── post.py
│   ├── user.py
│   └── auth.py
│
├── database.py
├── models.py
├── schemas.py
├── oauth2.py
├── utils.py
└── main.py
```

---

## Erlernte Konzepte

### Datenbanken

* PostgreSQL Einrichtung und Verwaltung
* SQL-Grundlagen
* SQLAlchemy ORM
* Datenbanksitzungen (Sessions)
* Dependency Injection

### API-Entwicklung

* CRUD-Operationen
* Request- und Response-Modelle
* Datenvalidierung
* Fehlerbehandlung
* Strukturierung mit APIRoutern

### Sicherheit

* Passwort-Hashing
* JWT-Authentifizierung
* OAuth2
* Geschützte API-Endpunkte
* Nutzung von Umgebungsvariablen (.env)

---

## Nächste Schritte

* Datenbank-Migrationen mit Alembic
* Beziehungen zwischen Datenbanktabellen
* Erweiterte Benutzerberechtigungen
* Refresh Tokens
* Rollen- und Rechteverwaltung
* Docker Deployment
* CI/CD Pipelines

---

## Lernziel

Dieses Repository dokumentiert meinen Lernfortschritt im Bereich moderner Backend-Entwicklung mit Python.

Der Fokus liegt auf dem Verständnis von:

* API-Architekturen
* Datenbankintegration
* Authentifizierung und Autorisierung
* Backend-Sicherheit
* Best Practices für Python-Webanwendungen

Das Projekt ist Teil meines Weges zum Python Backend Developer bzw. AI Engineer.
