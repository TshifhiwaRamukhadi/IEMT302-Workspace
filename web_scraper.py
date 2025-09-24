#!/usr/bin/env python3
"""
IEMT302 Web Scraping Project
Demonstrates Beautiful Soup usage to extract local information from South African websites
"""

import spacy
from telegram import Update
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_local_news():
    """Scrape local news headlines from South African news websites"""
    try:
        # Using a South African news website
        url = "https://www.news24.com/"
        
        print("Scraping local news from News24...")
        
        # Set headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract news headlines
        headlines = []
        
        # Look for different types of headline elements
        headline_selectors = [
            'h1', 'h2', 'h3',  # Common headline tags
            '.headline',        # Class-based selectors
            '.title',
            '[data-testid*="headline"]'  # Data attribute selectors
        ]
        
        for selector in headline_selectors:
            elements = soup.select(selector)
            for element in elements[:5]:  # Limit to 5 headlines per selector
                text = element.get_text(strip=True)
                if text and len(text) > 10:  # Filter out very short text
                    headlines.append({
                        'text': text,
                        'tag': element.name,
                        'class': element.get('class', [])
                    })
        
        # Remove duplicates
        unique_headlines = []
        seen_texts = set()
        for headline in headlines:
            if headline['text'] not in seen_texts:
                unique_headlines.append(headline)
                seen_texts.add(headline['text'])
        
        return {
            'source': url,
            'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_headlines': len(unique_headlines),
            'headlines': unique_headlines[:10]  # Limit to 10 headlines
        }
        
    except Exception as e:
        print(f"Error scraping news: {e}")
        return {'error': str(e)}

def demonstrate_beautiful_soup():
    """Demonstrate Beautiful Soup functionality with sample HTML"""
    print("=== Beautiful Soup Demonstration ===")
    
    # Sample HTML content (simulating a local news website)
    sample_html = """
    <html>
    <head><title>Local News</title></head>
    <body>
        <div class="news-container">
            <h1 class="main-headline">Breaking: Local Development Project Approved</h1>
            <div class="article">
                <h2 class="article-title">New Shopping Center Coming to Johannesburg</h2>
                <p class="article-content">The city council has approved a new shopping center development...</p>
                <span class="article-date">2024-01-15</span>
                <div class="article-tags">
                    <span class="tag">Development</span>
                    <span class="tag">Johannesburg</span>
                    <span class="tag">Business</span>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Parse the HTML using Beautiful Soup
    soup = BeautifulSoup(sample_html, 'html.parser')
    
    # Extract main headline
    main_headline = soup.find('h1', class_='main-headline')
    print(f"Main Headline: {main_headline.get_text()}")
    
    # Extract all article titles using Beautiful Soup
    article_titles = soup.find_all('h2', class_='article-title')
    print(f"Article Titles ({len(article_titles)} found):")
    for i, title in enumerate(article_titles, 1):
        print(f"  {i}. {title.get_text()}")
    
    # Extract all tags using Beautiful Soup
    tags = soup.find_all('span', class_='tag')
    print(f"Tags found: {[tag.get_text() for tag in tags]}")
    
    print("Beautiful Soup demonstration completed!\n")

def main():
    """Main function to run the web scraper"""
    print("=== IEMT302 Web Scraping Project ===")
    print("Using Beautiful Soup to extract local information from South African websites")
    print("=" * 70)
    
    # Demonstrate Beautiful Soup functionality
    demonstrate_beautiful_soup()
    
    # Scrape real local information
    print("Scraping local news headlines...")
    news_data = scrape_local_news()
    
    # Combine all data
    all_data = {
        'project': 'IEMT302 Web Scraping with Beautiful Soup',
        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'news': news_data
    }
    
    # Save data to JSON file
    with open('scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 70)
    print("Web scraping completed!")
    print("Data saved to 'scraped_data.json'")
    print("=" * 70)
    
    # Display some results
    print("\nSample Results:")
    print("-" * 30)
    
    if 'headlines' in news_data and news_data['headlines']:
        print(f"News Headlines ({len(news_data['headlines'])} found):")
        for i, headline in enumerate(news_data['headlines'][:3], 1):
            print(f"  {i}. {headline['text']}")
    
    print(f"\nBeautiful Soup successfully used to extract local information!")
    print("Key Beautiful Soup methods demonstrated:")
    print("• BeautifulSoup() - HTML parsing")
    print("• find() and find_all() - Element selection")
    print("• select() - CSS selectors")
    print("• get_text() - Text extraction")
    print("• get() - Attribute access")

if __name__ == "__main__":
    main()
