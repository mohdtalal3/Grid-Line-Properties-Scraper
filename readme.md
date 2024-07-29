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

1. **Unzip the file:**
    Go to the folder where there are all files and follow next steps.
    
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Run Command Examples:**
    ```bash
    python grid_line_properties_scrapper.py
    ```

4. **Output:**
    The scraper will collect the listings and generate two files:

    `grid_line_properties.json`: Contains the filtered listings with URLs and addresses.
    `grid_line_properties_addresses_matching_listings.txt`: Contains the addresses used and not used, along with a summary of the total, matching, and non-matching listings.

## Sample files also attached