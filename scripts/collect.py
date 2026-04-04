import feedparser
import json

def collecter_articles(sujet, nb_articles=10):
    sujet_encode = sujet.replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={sujet_encode}&hl=fr&gl=FR&ceid=FR:fr"
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries[:nb_articles]:
        article = {
            "titre": entry.title,
            "lien": entry.link,
            "date": entry.published,
            "source": entry.source.title if hasattr(entry, "source") else "inconnu"
        }
        articles.append(article)
    return articles

def sauvegarder_articles(articles, nom_fichier):
    chemin = f"data/{nom_fichier}.json"
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
    print(f"{len(articles)} articles sauvegardés dans {chemin}")

if __name__ == "__main__":
    articles = collecter_articles("intelligence artificielle", 10)
    sauvegarder_articles(articles, "articles_ia")