# Day 12: Web Requests and JSON Processing

## Objective

Today's focus is on working with web APIs, making HTTP requests, and processing JSON data. You will learn how to use the `requests` library to interact with web services and the `json` module to handle JSON data, with GitHub Copilot assisting in generating the necessary code.

## Prerequisites

Install the `requests` library if you haven't already:
```bash
pip install requests
```

## Exercises

### Exercise 1: Basic HTTP Requests

Learn to make different types of HTTP requests using the `requests` library.

1.  **GET Request**: Make a GET request to a public API (e.g., `https://httpbin.org/get`) and print the response.
    -   *Prompting Hint*: `# Make a GET request to httpbin.org/get`
2.  **POST Request**: Make a POST request with JSON data to `https://httpbin.org/post`.
    -   *Prompting Hint*: `# Make a POST request with JSON data`
3.  **Request Headers**: Add custom headers to your request (e.g., User-Agent).
    -   *Prompting Hint*: `# Add custom headers to HTTP request`
4.  **Query Parameters**: Make a GET request with query parameters.
    -   *Prompting Hint*: `# Make GET request with query parameters`
5.  **Error Handling**: Handle HTTP errors (status codes like 404, 500) gracefully.
    -   *Prompting Hint*: `# Handle HTTP errors in requests`

### Exercise 2: Working with JSON Data

Practice parsing and manipulating JSON data from API responses.

1.  **Parse JSON Response**: Make a request to `https://jsonplaceholder.typicode.com/posts/1` and parse the JSON response.
    -   *Prompting Hint*: `# Parse JSON response from API`
2.  **Extract Specific Data**: From the response, extract only the title and body of the post.
    -   *Prompting Hint*: `# Extract title and body from JSON response`
3.  **JSON to Dictionary**: Convert a JSON string to a Python dictionary.
    -   *Prompting Hint*: `# Convert JSON string to Python dictionary`
4.  **Dictionary to JSON**: Convert a Python dictionary to a JSON string.
    -   *Prompting Hint*: `# Convert Python dictionary to JSON string`
5.  **Pretty Print JSON**: Format and pretty-print JSON data for better readability.
    -   *Prompting Hint*: `# Pretty print JSON data`

### Exercise 3: Working with Real APIs

Practice with real-world APIs that don't require authentication.

1.  **Weather API**: Use a free weather API (e.g., OpenWeatherMap's free tier) to get current weather for a city.
    -   *Prompting Hint*: `# Get weather data for a city using API`
2.  **Random User API**: Fetch random user data from `https://randomuser.me/api/` and extract name and email.
    -   *Prompting Hint*: `# Fetch random user data and extract name and email`
3.  **Cat Facts API**: Get a random cat fact from `https://catfact.ninja/fact`.
    -   *Prompting Hint*: `# Get random cat fact from API`
4.  **GitHub API**: Fetch public information about a GitHub user (e.g., `https://api.github.com/users/octocat`).
    -   *Prompting Hint*: `# Fetch GitHub user information`

### Exercise 4: Data Processing and Storage

Combine API requests with data processing and storage.

1.  **Multiple Requests**: Fetch data from multiple API endpoints and combine the results.
    -   *Prompting Hint*: `# Fetch data from multiple API endpoints`
2.  **Save to File**: Save API response data to a JSON file.
    -   *Prompting Hint*: `# Save API response to JSON file`
3.  **Load from File**: Load previously saved JSON data from a file.
    -   *Prompting Hint*: `# Load JSON data from file`
4.  **Data Filtering**: Filter API response data based on specific criteria.
    -   *Prompting Hint*: `# Filter API data based on criteria`

## Challenge Exercise: News Aggregator

Create a simple news aggregator that:
-   Fetches news articles from a free news API (e.g., NewsAPI.org's free tier)
-   Filters articles by keyword
-   Saves the filtered articles to a JSON file
-   Displays the top 5 articles with titles and URLs

*Prompting Hint*: `# Create a news aggregator with keyword filtering`

## Reflection

-   How did Copilot help you understand the structure of API responses?
-   Were there any specific patterns Copilot suggested for error handling in web requests?
-   How effective was Copilot in helping you process and manipulate JSON data?

