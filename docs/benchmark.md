# Benchmark des services d'Intelligence Artificielle

## Contexte et besoin
Le projet NewsIA nécessite un service capable de :
- Résumer automatiquement des articles de presse
- Analyser le sentiment d'un article (positif, négatif, neutre)
- Répondre en français

## Services étudiés

### 1. OpenAI GPT-4o-mini
- **Prix** : $0.15 / 1M tokens en entrée
- **Qualité** : Excellente
- **Facilité d'intégration** : Très simple, documentation complète
- **Langue française** : Excellente
- **Éco-responsabilité** : Engagement net zéro d'ici 2050

### 2. HuggingFace (mistralai/Mistral-7B)
- **Prix** : Gratuit jusqu'à un certain quota
- **Qualité** : Bonne
- **Facilité d'intégration** : Moyenne, nécessite plus de configuration
- **Langue française** : Bonne
- **Éco-responsabilité** : Modèles open-source, hébergement flexible

### 3. Mistral AI (API officielle)
- **Prix** : €0.10 / 1M tokens
- **Qualité** : Très bonne
- **Facilité d'intégration** : Simple
- **Langue française** : Excellente (entreprise française)
- **Éco-responsabilité** : Basé en France, engagement environnemental

## Tableau comparatif

| Critère | OpenAI | HuggingFace | Mistral AI |
|---|---|---|---|
| Prix | Payant | Gratuit | Payant |
| Qualité résumé | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Intégration | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Français | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Éco-responsabilité | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

## Recommandation
**Service retenu : HuggingFace** via l'API Inference gratuite.

**Justification :**
- Gratuit, pas de carte bancaire requise
- Suffisant pour un projet de démonstration
- Open-source, meilleure éco-responsabilité
- Permet de démontrer la compétence d'intégration d'un service IA externe