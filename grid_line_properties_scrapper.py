import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
def get_total_pages(soup):
    paging = soup.find('ol', class_='paging')
    if paging:
        last_page = paging.find_all('li')[-2]  # Second to last <li> usually contains the last page number
        return int(last_page.text.strip())
    return 1  # If we can't find paging, assume there's only one page

def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://www.gridlineproperties.com/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
    }

    cookies = {
        "visitor_id923983": "1645789980",
        "visitor_id923983-hash": "e8a533775eefe2838434db8df3ef98b09e0d16528f86cfbe49f298ee2fd36a8afe844717d15578498c5e61a7e3e1284cc07dcff8"
    }

    try:
        response = requests.get(url, headers=headers, cookies=cookies, timeout=30)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        exit()

    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all listing boxes
    listings = soup.find_all('article', class_='placard')

    page_listings = []
    for listing in listings:
        url_element = listing.find('a', class_='placard-carousel-pseudo')
        url = url_element['ng-href'] if url_element else 'URL not found'

        address_element = listing.find('a', class_='subtitle-beta')
        address = address_element.text.strip() if address_element else 'Address not found'

        base_address=listing.find('div', class_='header-col')
        base_address=base_address.find('a').text
        page_listings.append({'url': url, 'address': address,'detail_address': base_address})

    return page_listings, soup

# Base URL
base_url = "https://looplink.gridlineproperties.com/looplink/search/{}/?sk=234a143b4b437bf8508aa68ebcd723af&searchtype=fs"

# List of cities to check
cities = [
    'miami', 'north miami', 'hallandale', 'hollywood', 'fort lauderdale', 'hialeah', 
    'dania', 'davie', 'sunrise', 'plantation', 'pembroke pines', 'aventura', 'miramar', 
    'coral springs', 'north lauderdale', 'lauderdale lakes', 'boca raton', 'opa locka', 
    'weston', 'doral', 'kendall', 'homestead', 'coral gables'
]

all_listings = []
matching_listings = []

# Start with the first page
first_page_listings, first_page_soup = scrape_page(base_url.format(1))
all_listings.extend(first_page_listings)

# Get total number of pages
total_pages = get_total_pages(first_page_soup)
print(f"Total pages: {total_pages}")

# Scrape remaining pages
for page in range(2, total_pages + 1):
    print(f"Scraping page {page}...")
    page_listings, _ = scrape_page(base_url.format(page))
    all_listings.extend(page_listings)
    time.sleep(4)  # Add a delay to be respectful to the server

# Process all listings
for listing in all_listings:
    if any(city.lower() in listing['address'].lower().replace(',', '').split() for city in cities):
        matching_listings.append(listing)

# Report on used and unused addresses
used_addresses = set(listing['address'] for listing in matching_listings)
unused_addresses = set(listing['address'] for listing in all_listings) - used_addresses

df = pd.DataFrame(matching_listings)
df.to_csv('grid_line_properties.csv', index=False)

file_path = 'grid_line_properties addresses_matching_listings.txt'

# Open the file in write mode and write the contents
with open(file_path, 'w') as file:
    file.write("Addresses Used:\n")
    for address in used_addresses:
        file.write(f"{address}\n")
    
    file.write("\nAddresses Not Used:\n")
    for address in unused_addresses:
        file.write(f"{address}\n")
    
    file.write(f"\nTotal listings: {len(all_listings)}\n")
    file.write(f"Matching listings: {len(matching_listings)}\n")
    file.write(f"Non-matching listings: {len(all_listings) - len(matching_listings)}\n")

print(f"Text file and Csv file has been saved.")