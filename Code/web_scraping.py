import requests
from bs4 import BeautifulSoup

# URL da página da Wikipedia com a lista dos ganhadores do Ig Nobel
url = 'https://en.wikipedia.org/wiki/List_of_Ig_Nobel_Prize_winners'

# Fazendo a requisição HTTP para obter o conteúdo HTML da página
response = requests.get(url)

# Parsing do conteúdo HTML com BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrando os anos que estão em mw-heading mw-heading2
anos = soup.find_all('span', {'class': 'mw-headline'})

# Inicializando uma lista para armazenar os dados
ganhadores = []

# Iterando pelos anos e extraindo as informações
for ano in anos:
    # Extraindo o texto do ano
    ano_texto = ano.text

    # Encontrando o próximo elemento que é a lista de prêmios (<ul>)
    ul_element = ano.find_next('ul')

    # Iterando pelos itens da lista (cada <li> contém informações de um ganhador)
    if ul_element:
        for li in ul_element.find_all('li'):
            # Tema do ganhador está em <b> dentro de <ul>
            tema_element = li.find('b')
            tema = tema_element.text if tema_element else "Tema não encontrado"

            # Texto do ganhador está em <a>
            ganhador_element = li.find('a')
            ganhador = ganhador_element.text if ganhador_element else "Ganhador não encontrado"

            # Adicionando o resultado na lista
            ganhadores.append({
                'ano': ano_texto,
                'tema': tema,
                'ganhador': ganhador
            })

# Exibindo os resultados
for ganhador in ganhadores:
    print(f"Ano: {ganhador['ano']}")
    print(f"Tema: {ganhador['tema']}")
    print(f"Ganhador: {ganhador['ganhador']}")
    print("-" * 40)
