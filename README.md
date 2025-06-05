# 🎬 IMDb Scraping – Python Web Scraper

A Python script that collects the top 100 most popular movies from the [IMDb](https://www.imdb.com/chart/moviemeter/) chart and stores the data in a CSV file.

This project was developed as part of the **Full-Stack Python course** at [EBAC](https://ebaconline.com.br/), specifically during the **Advanced Python** module. The goal was to practice web scraping and concurrency using threads.

## 🚀 Features

- Extracts title, release year, rating, and synopsis for each movie.
- Accesses individual movie pages to retrieve complete data.
- Uses `ThreadPoolExecutor` to parallelize HTTP requests and speed up scraping.
- Saves the structured data into a `movies.csv` file.

## 🛠️ Technologies Used

- Python 3.12
- `requests`
- `BeautifulSoup (bs4)`
- `concurrent.futures`
- Python's built-in `csv` module

## 🧪 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Bruno-Alvez/imdb_scraping.git
cd imdb_scraping

2.Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3.Install the dependencies:

pip install -r requirements.txt

4.Run the script:

python imdb_scraping.py

A movies.csv file will be generated in the project root.

📊 Sample Output

Title         | Year | Rating | Synopsis
----------------------------------------
Oppenheimer   | 2023 | 8.6    | A dramatization of the story...
Dune: Part Two| 2024 | 8.4    | Paul Atreides unites with...

⚠️ Notes

- IMDb’s HTML structure may change and break the scraper.

- Delays are added between requests to avoid IP blocking.

- Use responsibly to avoid overloading the server.

📌 Future Improvements

- Better error handling

-  Logging system

- Export to JSON and Excel

- Basic data visualization


