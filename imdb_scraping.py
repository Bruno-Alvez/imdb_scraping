import requests
import time
import csv
import random
import concurrent.futures
from bs4 import BeautifulSoup

# Cabeçalho HTTP padrão usado para simular um navegador real
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
}

# Número máximo de threads para execução paralela
MAX_THREADS = 10

# Nome do arquivo CSV de saída
CSV_FILE = 'movies.csv'

def extract_movie_details(movie_link):
    """
    Acessa a página de detalhes de um filme e extrai informações como título, data de lançamento,
    nota e sinopse. Retorna um dicionário com os dados extraídos ou None em caso de falha.
    """
    try:
        time.sleep(random.uniform(0, 0.2))  # Espera aleatória para evitar bloqueios por scraping
        response = requests.get(movie_link, headers=HEADERS, timeout=10)

        if response.status_code != 200:
            print(f"Erro ao acessar {movie_link}")
            return None

        movie_soup = BeautifulSoup(response.content, 'html.parser')

        title_tag = movie_soup.find('h1')
        title = title_tag.get_text(strip=True) if title_tag else None

        date_tag = movie_soup.find('a', href=lambda href: href and 'releaseinfo' in href)
        date = date_tag.get_text(strip=True) if date_tag else None

        rating_tag = movie_soup.find('div', attrs={'data-testid': 'hero-rating-bar__aggregate-rating__score'})
        rating = rating_tag.get_text(strip=True) if rating_tag else None

        plot_tag = movie_soup.find('span', attrs={'data-testid': 'plot-xs_to_m'})
        plot_text = plot_tag.get_text(strip=True) if plot_tag else None

        if all([title, date, rating, plot_text]):
            print(f"Filme processado: {title}")
            return {'Title': title, 'Release Date': date, 'Rating': rating, 'Plot': plot_text}
        else:
            print(f"Dados incompletos encontrados em {movie_link}")
            return None

    except Exception as e:
        print(f"Erro ao processar {movie_link}: {e}")
        return None

def extract_movies(soup):
    """
    Extrai os links dos filmes a partir do conteúdo HTML da página principal.
    Retorna uma lista de URLs de filmes.
    """
    movie_links = []
    try:
        container = soup.find('div', attrs={'data-testid': 'chart-layout-main-column'})
        movies = container.find_all('li')
        movie_links = [
            'https://imdb.com' + li.find('a')['href'].split('?')[0]
            for li in movies if li.find('a')
        ]
    except Exception as e:
        print(f"Erro ao extrair links dos filmes: {e}")
    return movie_links

def save_movies_to_csv(movies):
    """
    Salva os dados dos filmes em um arquivo CSV com cabeçalhos apropriados.
    """
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Title', 'Release Date', 'Rating', 'Plot']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for movie in movies:
            writer.writerow(movie)

def main():
    """
    Função principal do script:
    - Acessa a página de filmes populares do IMDb
    - Extrai os links dos filmes
    - Processa os detalhes de cada filme com multithreading
    - Salva os dados extraídos em um arquivo CSV
    """
    start_time = time.time()

    print("Iniciando extração dos filmes mais populares...")
    url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
    response = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(response.content, 'html.parser')
    movie_links = extract_movies(soup)

    print(f"Total de filmes encontrados: {len(movie_links)}. Iniciando coleta de detalhes...")

    movies_data = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(MAX_THREADS, len(movie_links))) as executor:
        results = executor.map(extract_movie_details, movie_links)
        movies_data = [movie for movie in results if movie]

    if movies_data:
        save_movies_to_csv(movies_data)
        print(f"Dados salvos com sucesso no arquivo '{CSV_FILE}'.")
    else:
        print("Nenhum dado foi salvo.")

    duration = round(time.time() - start_time, 2)
    print(f"Tempo total de execução: {duration} segundos.")

if __name__ == '__main__':
    main()
