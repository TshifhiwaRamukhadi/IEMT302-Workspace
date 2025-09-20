# IEMT302 Web Scraping Project

This project demonstrates web scraping using Python and Beautiful Soup to extract interesting local information from South African websites.

## Features

- **Local News Scraping**: Extracts headlines from South African news websites
- **Weather Information**: Scrapes current weather data for Johannesburg
- **Beautiful Soup Demonstration**: Shows various Beautiful Soup methods
- **Data Export**: Saves scraped data in JSON format

## Installation

1. Clone this repository:
```bash
git clone https://github.com/TshifhiwaRamukhadi/IEMT302-Clean.git
cd IEMT302-Clean
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the web scraper:
```bash
python web_scraper.py
```

## Beautiful Soup Examples

```python
from bs4 import BeautifulSoup
import requests

# Parse HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find elements by tag
headlines = soup.find_all('h1', 'h2', 'h3')

# Find elements by class
elements = soup.select('.headline')

# Extract text content
text = element.get_text(strip=True)

# Extract attributes
link = element.get('href')
```

## Author

Tshifhiwa Ramukhadi
Course: IEMT302
