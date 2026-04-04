import streamlit as st
import requests
import json

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="NewsIA",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 NewsIA")
st.subheader("Veille sur l'Intelligence Artificielle")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choisir une page",
    ["📰 Articles", "🔍 Recherche", "🤖 Résumé IA", "📊 Statistiques"]
)

def get_articles():
    try:
        response = requests.get(f"{API_BASE}/articles")
        return response.json()
    except:
        return {"total": 0, "articles": []}

def get_stats():
    try:
        response = requests.get(f"{API_BASE}/stats")
        return response.json()
    except:
        return {}

def get_resume(article_id):
    try:
        response = requests.get(f"{API_BASE}/articles/{article_id}/resume")
        return response.json()
    except:
        return {}

if page == "📰 Articles":
    st.header("📰 Tous les articles")
    data = get_articles()
    st.metric("Total articles", data["total"])
    for article in data["articles"]:
        with st.expander(f"📄 {article['titre']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Source :** {article['source']}")
                st.write(f"**Date :** {article['date']}")
            with col2:
                st.link_button("Lire l'article", article['lien'])

elif page == "🔍 Recherche":
    st.header("🔍 Rechercher un article")
    mot_cle = st.text_input("Entrez un mot-clé")
    if mot_cle:
        response = requests.get(f"{API_BASE}/articles/recherche/{mot_cle}")
        data = response.json()
        st.write(f"**{data['total']} résultat(s) trouvé(s)**")
        for article in data["articles"]:
            with st.expander(f"📄 {article['titre']}"):
                st.write(f"**Source :** {article['source']}")
                st.write(f"**Date :** {article['date']}")
                st.link_button("Lire l'article", article['lien'])

elif page == "🤖 Résumé IA":
    st.header("🤖 Résumé automatique par IA")
    data = get_articles()
    articles = data["articles"]
    if articles:
        options = {f"{a['id']} - {a['titre'][:60]}...": a['id'] for a in articles}
        choix = st.selectbox("Choisir un article", list(options.keys()))
        if st.button("Générer le résumé"):
            with st.spinner("L'IA génère le résumé... (20-30 secondes)"):
                article_id = options[choix]
                result = get_resume(article_id)
                if result:
                    st.success("Résumé généré !")
                    st.write(f"**Titre :** {result['titre']}")
                    st.write(f"**Source :** {result['source']}")
                    st.info(f"**Résumé IA :** {result['resume']}")
    else:
        st.warning("Aucun article disponible")

elif page == "📊 Statistiques":
    st.header("📊 Statistiques")
    stats = get_stats()
    if stats:
        st.metric("Total articles", stats["total_articles"])
        st.subheader("Articles par source")
        for source in stats["articles_par_source"]:
            st.progress(
                source["nb"] / stats["total_articles"],
                text=f"{source['source']} : {source['nb']} article(s)"
            )