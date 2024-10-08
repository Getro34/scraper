# Web Scraper pour liens Facebook et emails

Ce script Python parcourt une liste de sites web pour extraire les liens Facebook et les adresses email. Il est conçu pour être efficace, rapide et fournir un retour visuel sur la progression.

## Fonctionnalités

- Extraction de liens Facebook à partir de pages web
- Recherche d'adresses email sur les pages de contact
- Traitement multi-thread pour une exécution rapide
- Barre de progression en temps réel
- Sauvegarde des résultats dans des fichiers texte

## Prérequis

- Python 3.6+
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt :
git clone https://github.com/Getro34/scraper.git cd scraper

Copy
2. Installez les dépendances requises :
pip install -r requirements.txt

Copy
## Dépendances

Ce projet utilise les bibliothèques Python suivantes :

- requests
- beautifulsoup4
- tqdm

Ces dépendances sont listées dans le fichier `requirements.txt`.

## Utilisation

1. Créez un fichier `websites.txt` contenant les URLs des sites web à analyser, un par ligne.

2. Exécutez le script :
python scraper.py

Copy
3. Les résultats seront sauvegardés dans deux fichiers :
- `facebook_links_output.txt` : liens Facebook trouvés
- `emails_output.txt` : adresses email découvertes

## Configuration

Vous pouvez ajuster les paramètres suivants dans le script :

- `max_workers` : nombre de threads simultanés (par défaut : 10)
- Nombre de pages de contact à vérifier par site (par défaut : 3)

## Avertissement

Assurez-vous de respecter les conditions d'utilisation des sites web que vous analysez. L'utilisation de ce script peut être soumise à des restrictions légales ou éthiques selon les sites ciblés.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence [MIT](https://opensource.org/licenses/MIT).

Copyright (c) 2024 Getro34
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

