import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def clean_value(text):
    """Nettoie et convertit un texte brut en une chaîne sans caractères parasites."""
    return text.replace(",", "").replace("−", "-").replace(" ", "").replace(" ", "").strip()

def scrape_population_by_country():
    """
    Scrape la table des populations par pays depuis Worldometers et
    sauvegarde les données nettoyées dans un fichier CSV.
    """
    url = "https://www.worldometers.info/world-population/population-by-country/"
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

    # Création du DataFrame
    df = pd.DataFrame(datarows, columns=headers)

    # Sauvegarde en CSV
    df.to_csv("population_by_country.csv", index=False, encoding='utf-8')
    print("✅ Données sauvegardées dans 'population_by_country.csv'")

if __name__ == "__main__":
    start_time = time.time()
    scrape_population_by_country()
    end_time = time.time()
    print(f"⏱️ Durée d'exécution : {end_time - start_time:.2f} secondes")
