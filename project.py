from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import statsmodels.api as sm



def clean_value(text):
    """Nettoie et convertit un texte brut en une chaîne sans caractères parasites."""
    return text.replace(",", "").replace("−", "-").replace(" ", "").replace(" ", "").strip()

def scrape_population_by_country():
    """
    Scrape la table des populations par pays depuis Worldometers et
    sauvegarde les données nettoyées dans un fichier CSV.
    """
    url = "https://www.worldometers.info/world-population/morocco-population/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Trouve la première table (c'est celle contenant les données de population)
    table = soup.find("table")

    # Extraction des en-têtes
    headers = [th.text.strip() for th in table.thead.find_all("th")]

    # Extraction des données
    datarows = []
    for row in table.tbody.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) != len(headers):
            continue  # Sauter les lignes malformées
        cleaned_data = [clean_value(cell.text) for cell in cells]
        datarows.append(cleaned_data)


    df = pd.DataFrame(datarows, columns=headers)

    # Sauvegarde en CSV
    df.to_csv("population_of_Morocoo.csv", index=False, encoding='utf-8')
    print(df)

def Modeldata(data) :
    df = pd.read_csv(data)
    df = df.rename(columns={"Year": "Année", "Population": "Population"})  # adapte au besoin
    df["Année"] = df["Année"].astype(int)
    df["Population"] = df["Population"].astype(int)

    # Régression linéaire
    X = df[["Année"]]
    y = df["Population"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Évaluation
    score = model.score(X_test, y_test)
    print(f"R² sur l'ensemble de test : {score:.2f}")

    # Prédiction future
    future_years = pd.DataFrame({"Année": list(range(2024, 2034))})
    future_predictions = model.predict(future_years)

    # Affichage
    plt.figure(figsize=(10, 6))
    plt.plot(df["Année"], df["Population"], label="Données réelles")
    plt.plot(future_years, future_predictions, label="Prédiction", linestyle="--")
    plt.xlabel("Année")
    plt.ylabel("Population")
    plt.legend()
    plt.title("Prévision de la population du Maroc")
    plt.show()

    df = df.sort_values("Année")
    df.set_index("Année", inplace=True)

    # Construction du modèle
    model_arima = sm.tsa.ARIMA(df["Population"], order=(1, 1, 1))
    results_arima = model_arima.fit()

    # Prévision sur 10 ans
    forecast = results_arima.forecast(steps=10)
    print(forecast)

    forecast.plot(title="Prévision ARIMA")
    plt.show()







if __name__ == "__main__":
    start_time = time.time()
    scrape_population_by_country()
    Modeldata("population_of_Morocoo.csv")

    end_time = time.time()
    print(f"⏱️ Durée d'exécution : {end_time - start_time:.2f} secondes")






