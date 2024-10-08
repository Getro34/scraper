import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# Chargement des sites depuis un fichier texte
with open("websites.txt", "r") as file:
    websites = [line.strip() for line in file]

# Header de la requête HTTP
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

# Listes pour stocker les résultats
facebook_links = []
emails = []

# Fonction pour extraire les liens Facebook et les emails d'un site web
def find_facebook_links_and_emails(url, session):
    try:
        response = session.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Recherche des liens Facebook
            for a in soup.find_all('a', href=True):
                href = a['href']
                if 'facebook.com' in href or '/facebook' in href:
                    facebook_links.append(urljoin(url, href))
            
            # Recherche des pages "Contact" pour les emails
            contact_links = [a['href'] for a in soup.find_all('a', href=True) if 'contact' in a['href']][:3]  # Limiter à 3 pages de contact
            for contact_link in contact_links:
                contact_url = urljoin(url, contact_link)
                try:
                    contact_response = session.get(contact_url, headers=headers, timeout=10)
                    if contact_response.status_code == 200:
                        contact_soup = BeautifulSoup(contact_response.text, 'html.parser')
                        found_emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", contact_soup.text))
                        emails.extend(found_emails)
                except requests.RequestException:
                    pass
        else:
            print(f"Erreur : Impossible de récupérer la page {url} (status code: {response.status_code})")
    except requests.RequestException as e:
        print(f"Erreur d'accès au site {url}: {e}")

# Fonction pour traiter un site web
def process_website(website):
    with requests.Session() as session:
        find_facebook_links_and_emails(website, session)

# Utilisation de ThreadPoolExecutor pour le multithreading
with ThreadPoolExecutor(max_workers=10) as executor:
    list(tqdm(executor.map(process_website, websites), total=len(websites), desc="Progression"))

# Sauvegarde des résultats dans des fichiers texte
with open('facebook_links_output.txt', 'w') as file:
    for link in set(facebook_links):  # Utiliser un set pour éliminer les doublons
        file.write(link + '\n')

with open('emails_output.txt', 'w') as file:
    for email in set(emails):  # Utiliser un set pour éliminer les doublons
        file.write(email + '\n')

print("Liens Facebook et emails trouvés et enregistrés dans les fichiers 'facebook_links_output.txt' et 'emails_output.txt'")