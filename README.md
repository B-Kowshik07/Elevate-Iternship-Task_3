# Web Scraping-News Headlines

This project is a simple Python web scraper that extracts news headlines from a news website (e.g., BBC News) and saves them into a text file.

## Features

- Fetches the homepage content from a news site (like [BBC News](https://www.bbc.com/news))
- Parses and extracts headlines using BeautifulSoup
- Prints headlines in the console and saves them line-by-line in a `.txt` file
- Easy to update for other news websites by changing URL and selectors


4. After running, view the headlines in the console or find them saved in the `bbc_headlines.txt` file.

## Note!!

- The HTML structure of news websites can change frequently. You may need to update the tag names or class names in the script by inspecting the news site's webpage.
- To inspect the HTML structure, right-click a headline on the news website and choose "Inspect" in your browser.
- Make sure your internet connection is active when running the scraper.
- The script sends a User-Agent header to mimic a browser request for better compatibility with some websites.

## License
  This project is open source and free to use.



