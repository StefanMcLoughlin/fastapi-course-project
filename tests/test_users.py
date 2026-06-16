from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app import schemas, models
from app.config import settings
from app.database import get_db, Base
import pytest


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    app.dependency_overrides.clear()


def test_root(client):
    res = client.get("/")
    assert res.json().get("message") == "welcome to my api!!!!"
    assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email": "testuser@example.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "testuser@example.com"
    assert res.status_code == 201