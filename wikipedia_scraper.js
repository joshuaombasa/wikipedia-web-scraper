const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

// Wikipedia page to scrape
const url = "https://en.wikipedia.org/wiki/Web_scraping";

// Function to scrape data
async function scrapeWikipedia() {
    try {
        const response = await axios.get(url);
        const $ = cheerio.load(response.data);
        
        // Extract the first paragraph text
        const firstParagraph = $('p').first().text().trim();
        
        // Extract all headings
        const headings = [];
        $('h1, h2, h3').each((_, element) => {
            headings.push($(element).text().trim());
        });
        
        // Create a structured JSON output
        const scrapedData = {
            url,
            firstParagraph,
            headings
        };
        
        // Save to a file
        const outputPath = path.join(__dirname, 'scraped_data.json');
        fs.writeFileSync(outputPath, JSON.stringify(scrapedData, null, 2));
        
        console.log("Scraping successful. Data saved to scraped_data.json");
    } catch (error) {
        console.error(`Failed to retrieve page. Error: ${error.message}`);
    }
}

// Execute the scraping function
scrapeWikipedia();
