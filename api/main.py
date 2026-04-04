from fastapi import FastAPI, HTTPException
import sqlite3
import requests
import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = "data/newsIA.db"
HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

app = FastAPI(
    title="NewsIA API",
    description="API de gestion d'articles sur l'intelligence artificielle",
    version="1.0.0"
)

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def resumer_texte(texte):
    payload = {
        "inputs": texte[:1000],
        "parameters": {
            "max_length": 150,
            "min_length": 50
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]["summary_text"]
    else:
        return f"Erreur résumé : {response.status_code}"

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur NewsIA API", "version": "1.0.0"}

@app.get("/articles")
def get_articles():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles")
    articles = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"total": len(articles), "articles": articles}

@app.get("/articles/{article_id}")
def get_article(article_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
    article = cursor.fetchone()
    conn.close()
    if article is None:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    return dict(article)

@app.get("/articles/recherche/{mot_cle}")
def rechercher_articles(mot_cle: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE titre LIKE ?", (f"%{mot_cle}%",))
    articles = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"total": len(articles), "articles": articles}

@app.get("/articles/{article_id}/resume")
def get_resume(article_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
    article = cursor.fetchone()
    conn.close()
    if article is None:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    article_dict = dict(article)
    texte = article_dict["titre"]
    resume = resumer_texte(texte)
    return {
        "article_id": article_id,
        "titre": article_dict["titre"],
        "resume": resume,
        "source": article_dict["source"]
    }

@app.get("/stats")
def get_stats():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as total FROM articles")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT source, COUNT(*) as nb FROM articles GROUP BY source ORDER BY nb DESC")
    sources = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {
        "total_articles": total,
        "articles_par_source": sources
    }