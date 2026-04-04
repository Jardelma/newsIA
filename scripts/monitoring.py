import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/newsIA.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("newsIA")

def log_requete(route, status_code, temps_ms):
    if status_code >= 500:
        logger.error(f"ERREUR CRITIQUE - Route: {route} | Status: {status_code} | Temps: {temps_ms}ms")
    elif status_code >= 400:
        logger.warning(f"ERREUR CLIENT - Route: {route} | Status: {status_code} | Temps: {temps_ms}ms")
    else:
        logger.info(f"OK - Route: {route} | Status: {status_code} | Temps: {temps_ms}ms")

def log_ia(article_id, succes, temps_ms):
    if succes:
        logger.info(f"IA OK - Article: {article_id} | Temps: {temps_ms}ms")
    else:
        logger.error(f"IA ERREUR - Article: {article_id} | Temps: {temps_ms}ms")

def verifier_seuils():
    logger.info("Vérification des seuils de monitoring...")
    log_path = f"{LOG_DIR}/newsIA.log"
    if not os.path.exists(log_path):
        logger.warning("Fichier de log introuvable")
        return
    with open(log_path, "r", encoding="utf-8") as f:
        lignes = f.readlines()
    erreurs = [l for l in lignes if "ERREUR" in l]
    taux_erreur = len(erreurs) / max(len(lignes), 1) * 100
    logger.info(f"Taux d'erreur actuel : {taux_erreur:.1f}%")
    if taux_erreur > 20:
        logger.error(f"ALERTE : Taux d'erreur trop élevé ({taux_erreur:.1f}%) !")

if __name__ == "__main__":
    log_requete("/articles", 200, 45)
    log_requete("/articles/1", 200, 23)
    log_requete("/articles/999", 404, 12)
    log_ia(1, True, 2300)
    verifier_seuils()