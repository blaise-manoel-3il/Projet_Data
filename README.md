🫀 PRÉDICTION DE MALADIES CARDIAQUES PAR APPRENTISSAGE SUPERVISÉ

**Projet personnel – Mai 2025 – Limoges**


📌 Objectif

Ce projet vise à développer un **modèle de classification supervisée** capable de prédire la présence ou non d’une **maladie cardiaque** à partir de caractéristiques médicales (âge, cholestérol, tension, etc.).


🔍 Étapes du projet

1. **Analyse exploratoire de données (EDA)**

   * Étude des distributions, corrélations et patterns
   * Visualisations avec `Seaborn` et `Matplotlib`

2. **Prétraitement des données**

   * Séparation en jeux d'entraînement et de test (`train_test_split`)
   * Mise à l’échelle des données (`StandardScaler`)

3. **Modélisation**

   * Régression logistique avec `Scikit-learn`
   * Évaluation par courbes ROC, PR et métriques (précision, rappel, AUC)

4. **Prédiction sur un nouveau patient**

   * Transformation des données entrantes
   * Prédiction de la probabilité de maladie



⚙️ Stack technique

* **Google Colab** – Environnement de travail 
* **Pandas** – Manipulation des données
* **Seaborn & Matplotlib** – Visualisation
* **Scikit-learn** – Modélisation et évaluation



✅ Résultats

* Modèle avec **AUC = 0.96** et **AP = 0.97**
* Bonne capacité à prédire les cas positifs et négatifs
* Prédiction fiable sur de nouveaux patients




