#importaion des bilbliotheque
import requests
from bs4 import BeautifulSoup
import pandas as pd

# appel de site 
url = "https://books.toscrape.com/"
response = requests.get(url)

# verification de requete de site
if response.status_code == 200:
    html_content = response.text
    print(" page trouvée avec succeés!\n")
    print("---- HTML Source (les premiers  500 characteres ) ")
    print(html_content[:500])  # affichage des  500 characters premiers  HTML
else:
    print(" page non trouvée. ", response.status_code)
    exit()

# 2. Analyse HTML en utilisant BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# extraction des titres et prix des livres
titles = [h3.a['title'] for h3 in soup.find_all('h3')]
prices = [price.get_text() for price in soup.find_all('p', class_='price_color')]

# Insertion le titre et le prix dans un liste dictionnaires
data = []
for title, price in zip(titles, prices):
    data.append({'Title': title, 'Price': price})

# affichage des données extraits
print("\n✅ Extracted Data:")
for item in data[:5]:
    print(item)

# 3. sauvegarder le données en utilisant bibliotheque pandas
df = pd.DataFrame(data)
df.to_csv('books.csv', index=False, encoding='utf-8')

print("\n✅ Data saved to 'books.csv'")
