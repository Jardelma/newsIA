import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.main import app

client = TestClient(app)

def test_accueil():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Bienvenue sur NewsIA API"

def test_get_articles():
    response = client.get("/articles")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "articles" in data
    assert data["total"] >= 0

def test_get_article_existant():
    response = client.get("/articles/1")
    assert response.status_code == 200
    data = response.json()
    assert "titre" in data
    assert "source" in data

def test_get_article_inexistant():
    response = client.get("/articles/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Article non trouvé"

def test_recherche_articles():
    response = client.get("/articles/recherche/intelligence")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "articles" in data

def test_stats():
    response = client.get("/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_articles" in data
    assert "articles_par_source" in data