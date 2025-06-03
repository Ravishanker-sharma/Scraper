# 🔍 Yahoo Search Engine with Smart Scraper

This project contains two powerful Python scripts that allow you to perform Yahoo searches, extract real links and their titles, and scrape useful content from those links such as headlines and paragraphs.

## 🚀 Features

- Perform Yahoo searches programmatically
- Extract clean URLs and readable titles
- Scrape headlines (`<h1>, <h2>, <h3>`) and paragraph (`<p>`) content
- Simple and minimalistic code
- Great for research automation and content discovery

## 🧠 How It Works

### 1. `yahoosearchengine.py`

This module:
- Sends a search query to Yahoo
- Parses and extracts real result URLs
- Filters only meaningful titles and links

### 2. `genralscraper.py`

This script:
- Uses the Yahoo search engine module
- Visits each URL retrieved
- Extracts up to 20 headlines and 20 paragraphs per page

## 🔧 Requirements

```bash
pip install beautifulsoup4 requests
