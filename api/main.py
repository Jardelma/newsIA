from fastapi import FastAPI, HTTPException
import sqlite3

DB_PATH = "data/newsIA.db"

app = FastAPI(
    title="NewsIA API",
    description="API de gestion d'articles sur l'intelligence artificielle",
    version="1.0.0"
)

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

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