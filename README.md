# Wikipedia Company Revenue Scraper
This project is a web scraper that extracts data from Wikipedia's **List of largest companies in the United States by revenue** page and saves it as a CSV file. It uses `requests` to retrieve the page, `BeautifulSoup` to parse the HTML, and `pandas` to structure and store the data.

## Project Overview
The script collects information about the largest companies in the U.S. by revenue, as listed on Wikipedia. It identifies the specific table within the page, extracts the relevant columns and rows, and saves the data to a CSV file.

This code will:
Access the Wikipedia page
Locate and parse the relevant table
Save the data to a CSV file in the specified output path.
