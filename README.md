📈 Prédiction de la population du Maroc
Ce projet a pour objectif de scraper les données de population du Maroc depuis le site Worldometers, puis d'entraîner des modèles prédictifs (régression linéaire et ARIMA) pour estimer l’évolution de la population sur les 5 à 10 prochaines années.

📂 Structure du projet
bash
Copy
Edit
.
├── population_of_Morocoo.csv          # Données historiques de population du Maroc
├── population_by_country.csv          # Données de population par pays (scrapées en bonus)
├── prediction_maroc_population.py     # Script principal : scraping + modélisation
├── README.md                          # Ce fichier
🔧 Dépendances
Ce projet utilise les bibliothèques suivantes :

bash
Copy
Edit
pip install pandas numpy matplotlib scikit-learn statsmodels beautifulsoup4 requests
🚀 Exécution
Pour exécuter le script principal :

bash
Copy
Edit
python prediction_maroc_population.py
Ce script :

Scrape les données historiques de population du Maroc.

Enregistre les données dans population_of_Morocoo.csv.

Entraîne deux modèles prédictifs :

Régression linéaire (via scikit-learn)

ARIMA (via statsmodels)

Affiche les courbes de prédiction pour les années 2024 à 2033.

📊 Modèles utilisés
🔹 Régression Linéaire
Permet d'estimer la tendance linéaire de la croissance de la population.

🔹 ARIMA
Modèle temporel permettant de capturer la dépendance entre les années.

Les résultats sont visualisés sous forme de graphiques avec matplotlib.

🌍 Bonus : Données mondiales
Un second script scrape également les données de population de tous les pays depuis la page :
https://www.worldometers.info/world-population/population-by-country/

Ces données sont enregistrées dans population_by_country.csv.

📌 À améliorer
Ajouter la régression polynomiale pour comparer davantage de modèles.

Implémenter des métriques comme RMSE ou MAE pour une meilleure évaluation.

Ajouter une interface utilisateur simple (CLI ou web).

🧑‍💻 Auteur
Projet réalisé dans le cadre d’un exercice de modélisation en Python.
