import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_usernames(url):
    response = requests.get(url)

    # Asegurarse de que la solicitud fue exitosa
    if response.status_code != 200:
        raise Exception("Failed to load page {}".format(url))

    # Parsea el contenido HTML de la página con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Busca todos los nombres de usuario que comienzan con '@'
    usernames = [user.text for user in soup.find_all('span') if user.text.startswith('@')]

    # Crea un dataframe con los datos extraídos
    df = pd.DataFrame({
        'Username': usernames,
    })

    return df

url = "https://www.hotsale.com.mx/influencers"
df = scrape_usernames(url)

# Imprime el dataframe
print(df)
