import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def resumer_article(texte):
    payload = {
        "inputs": texte,
        "parameters": {
            "max_length": 150,
            "min_length": 50
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]["summary_text"]
    else:
        print(f"Erreur : {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    texte_test = """
    Artificial intelligence is transforming the job market at an unprecedented pace.
    Many companies are adopting AI tools to automate repetitive tasks, which is raising
    concerns about job displacement. However, experts argue that AI will also create
    new types of jobs that require human creativity and critical thinking.
    The key challenge for workers is adapting their skills to work alongside AI systems.
    """
    print("Résumé généré :")
    print(resumer_article(texte_test))