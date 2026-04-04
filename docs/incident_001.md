# Incident 001 — Erreur 500 sur la route /articles/recherche

## Description
Date : 04/04/2026
Sévérité : Haute
Statut : Résolu

## Déclenchement
L'application retournait une erreur 500 sur la route `/articles/recherche/{mot_cle}`
lors de recherches contenant des caractères spéciaux (apostrophes, accents).

## Périmètre impacté
- Route `/articles/recherche/{mot_cle}` inaccessible
- Utilisateurs ne pouvant pas effectuer de recherches

## Diagnostic
Analyse des logs :