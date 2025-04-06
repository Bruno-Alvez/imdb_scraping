# IMDb Scraping

Script em Python para coletar os 100 filmes mais populares do [IMDb](https://www.imdb.com/chart/moviemeter/) e salvar as informações em um arquivo CSV.

Este projeto foi desenvolvido durante o **curso de Desenvolvimento Full-Stack em Python** da [EBAC](https://ebaconline.com.br/), como parte do módulo de **Python Avançado**. O foco foi a prática de web scraping com ênfase em **concorrência com threads**.

## Funcionalidades

- Coleta título, ano de lançamento, nota e sinopse de cada filme.
- Acessa cada página de filme individualmente.
- Usa `ThreadPoolExecutor` para paralelizar as requisições e acelerar o processo.
- Salva os dados estruturados em `movies.csv`.

## Tecnologias

- Python 3.12
- requests
- BeautifulSoup (bs4)
- concurrent.futures
- csv (módulo padrão)

## Como executar

1 - Clone o repositório:

```bash
git clone https://github.com/Bruno-Alvez/imdb_scraping.git
cd imdb_scraping

2 - Crie e ative um ambiente virtual:

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3 - Instale as dependências:

pip install -r requirements.txt

Execute o script:

python imdb_scraping.py

O arquivo movies.csv será gerado no diretório raiz do projeto.

Exemplo de saída:

Título	Lançamento	Nota	Sinopse
Oppenheimer	2023	8.6	A dramatization of the story...
Duna: Parte 2	2024	8.4	Paul Atreides unites with...
Notas

    O IMDb pode alterar sua estrutura HTML, o que pode quebrar o scraper.

    Delays são adicionados entre as requisições para evitar bloqueio.

    Recomendado rodar com moderação para não sobrecarregar o servidor.

Melhorias futuras

    Tratamento de erros mais robusto

    Logs detalhados

    Exportação para outros formatos (JSON, Excel)

    Visualização dos dados