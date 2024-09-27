import requests
from bs4 import BeautifulSoup
import csv

# URL da página oficial dos vencedores do IG Nobel
url = "https://www.improbable.com/ig/winners/"

# Fazer uma requisição para a página
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Analisar o conteúdo HTML da página
    soup = BeautifulSoup(response.content, "html.parser")

    # Criar uma lista para armazenar os dados dos ganhadores
    winners_data = []

    # Encontrar todos os blocos que contêm informações sobre os vencedores (ajustar com base na inspeção do HTML)
    winners = soup.find_all("div", class_="ig-winners-list")

    for winner in winners:
        year = winner.find("h2").text.strip()  # Encontrar o ano
        categories = winner.find_all("h3")  # Encontrar as categorias

        for category in categories:
            category_name = category.text.strip()
            winner_info = category.find_next("p").text.strip()  # Detalhes do vencedor

            # Armazenar os dados em uma lista
            winners_data.append([year, category_name, winner_info])

    # Salvar os dados em um arquivo CSV
    with open("ig_nobel_winners.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Ano", "Categoria", "Informação do Vencedor"])
        writer.writerows(winners_data)

    print("Raspagem concluída e dados salvos no arquivo 'ig_nobel_winners.csv'.")
else:
    print(f"Erro ao acessar a página. Status code: {response.status_code}")
