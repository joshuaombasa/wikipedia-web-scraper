import requests
from bs4 import BeautifulSoup
import json

# Wikipedia page to scrape
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Function to scrape data
def scrape_wikipedia():
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the first paragraph text
        first_paragraph = soup.find('p').get_text(strip=True)
        
        # Extract all headings (h1, h2, h3)
        headings = [heading.get_text(strip=True) for heading in soup.find_all(['h1', 'h2', 'h3'])]
        
        # Create a structured JSON output
        scraped_data = {
            'url': url,
            'firstParagraph': first_paragraph,
            'headings': headings
        }
        
        # Save to a file
        output_path = 'scraped_data.json'
        with open(output_path, 'w') as file:
            json.dump(scraped_data, file, indent=2)
        
        print("Scraping successful. Data saved to scraped_data.json")
    
    except requests.exceptions.RequestException as error:
        print(f"Failed to retrieve page. Error: {error}")

# Execute the scraping function
scrape_wikipedia()
