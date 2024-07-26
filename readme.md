# Grid Line Properties Scraper

This project is a web scraping tool designed to collect real estate listings from the Grid Line Properties website. The scraper extracts listings, filters them based on a list of specified cities, and saves the results in both a CSV file and a text file.

## Features

- Scrapes real estate listings from multiple pages of the Grid Line Properties website.
- Extracts URLs and addresses of listings.
- Filters listings based on a predefined list of cities.
- Saves filtered listings to a CSV file.
- Generates a text file reporting used and unused addresses along with the total count of listings.
## Dependencies

- Python 3.x +
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mohdtalal3/Google-news-scrapper.git

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Run Command Examples:**
    1. Most recent (no time filter):
    ```bash
    python your_script.py "your search query" --limit 100
    ```
    2. Recent past hours: :
    ```bash
    python your_script.py "your search query" --time_range 1 --hours 6 --limit 100
    ```
    3. Last 24 hours:
    ```bash
    python your_script.py "your search query" --time_range 2 --limit 200
    ```
    4. Past week:
    ```bash
    python your_script.py "your search query" --time_range 3 --limit 150
    ```
    5. Last month:
    ```bash
    python your_script.py "your search query" --time_range 4 --limit 300
    ```
    6. Last year:
    ```bash
    python your_script.py "your search query" --time_range 5 --limit 250
    ```
    7. Custom date range:
    ```bash
    python your_script.py "your search query" --time_range 6 --start_date "06/01/2024" --end_date "06/30/2024" --limit 200
    ```
    
4. **Follow the prompts:**
    Enter your search query.
    Select a time range or choose '0' for the most recent articles.
    Enter the number of news articles to scrape (up to 300).

5. **Output:**
    The script will generate a CSV file (google_news_query_timestamp.csv) containing the scraped news data.

## Exmaple

1. **Input:**

    Enter your search query: artificial intelligence
    Select a time range:
    0. Most recent (no time filter)
    1. Recent past hours
    2. Last 24 hours
    3. Past week
    4. Last month
    5. Last year
    6. Custom date range
    Enter your choice (0-6): 3
    Enter the number of news titles to scrape (max 300): 50


2. **Output:**
    Scraping 50 news articles related to "artificial intelligence" from the past week.
    Data saved to google_news_games_option_6_2024-07-09_01-13-04.csv.


## Sample files also attached