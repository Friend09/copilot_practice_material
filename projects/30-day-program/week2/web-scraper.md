# Week 2 Project: Web Scraper with Data Analysis

## Project Overview
Build a web scraper that collects data from a website and performs basic analysis. This project combines web scraping, data processing, and visualization using GitHub Copilot.

## Features to Implement

### Core Features
1. **Web Scraping**: Extract data from a target website
2. **Data Cleaning**: Process and clean the scraped data
3. **Data Storage**: Save data to CSV or JSON format
4. **Basic Analysis**: Calculate statistics and insights
5. **Visualization**: Create simple charts and graphs

### Target Websites (Choose One)
1. **News Headlines**: Scrape news titles and publication dates
2. **Product Prices**: Monitor e-commerce product prices
3. **Weather Data**: Collect weather information for multiple cities
4. **Job Listings**: Extract job titles, companies, and locations

## Project Structure
```
web-scraper/
├── main.py           # Main application
├── scraper.py        # Web scraping logic
├── analyzer.py       # Data analysis functions
├── visualizer.py     # Chart generation
├── config.py         # Configuration settings
├── requirements.txt  # Dependencies
└── data/            # Output directory
    ├── raw_data.json
    ├── cleaned_data.csv
    └── charts/
```

## Implementation Guidelines

### Libraries to Use
- `requests` or `selenium` for web scraping
- `beautifulsoup4` for HTML parsing
- `pandas` for data manipulation
- `matplotlib` or `plotly` for visualization

### Copilot Prompts
- "Create a function to scrape news headlines from a website using BeautifulSoup"
- "Implement data cleaning to remove duplicates and handle missing values"
- "Generate a bar chart showing the frequency of different categories"

## Ethical Considerations
- Respect robots.txt files
- Add delays between requests
- Don't overload servers
- Use data responsibly

## Getting Started

1. Choose your target website
2. Analyze the HTML structure
3. Implement the scraper with rate limiting
4. Process and clean the data
5. Create visualizations

## Success Criteria

Your scraper should:
- ✅ Successfully extract data from the target site
- ✅ Handle errors and edge cases gracefully
- ✅ Clean and process the data effectively
- ✅ Generate meaningful visualizations
- ✅ Follow ethical scraping practices

