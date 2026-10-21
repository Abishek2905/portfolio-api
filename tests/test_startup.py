import pytest
from fastapi.testclient import TestClient

from app.main import app


def test_valid_environment(monkeypatch):
    monkeypatch.setenv("PORTFOLIO_ENV", " PRODUCTION ")
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Portfolio API"}


def test_invalid_environment(monkeypatch):
    monkeypatch.setenv("PORTFOLIO_ENV", "invalid")
    with pytest.raises(ValueError, match="Invalid PORTFOLIO_ENV"):
        with TestClient(app):
            pytest.fail("Application startup unexpectedly succeeded")
