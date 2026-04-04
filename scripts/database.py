import sqlite3
import json
import os

DB_PATH = "data/newsIA.db"

def creer_base():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            lien TEXT UNIQUE NOT NULL,
            date TEXT,
            source TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("Base de données créée avec succès")

def importer_articles(nom_fichier):
    chemin = f"data/{nom_fichier}.json"
    if not os.path.exists(chemin):
        print(f"Fichier {chemin} non trouvé, import ignoré")
        return
    with open(chemin, "r", encoding="utf-8") as f:
        articles = json.load(f)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    inseres = 0
    doublons = 0
    for article in articles:
        try:
            cursor.execute("""
                INSERT INTO articles (titre, lien, date, source)
                VALUES (?, ?, ?, ?)
            """, (article["titre"], article["lien"], article["date"], article["source"]))
            inseres += 1
        except sqlite3.IntegrityError:
            doublons += 1
    conn.commit()
    conn.close()
    print(f"{inseres} articles insérés, {doublons} doublons ignorés")

def afficher_articles():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, titre, source, date FROM articles")
    articles = cursor.fetchall()
    for article in articles:
        print(f"[{article[0]}] {article[1][:50]}... | {article[2]} | {article[3]}")
    conn.close()

if __name__ == "__main__":
    creer_base()
    importer_articles("articles_ia")
    afficher_articles()