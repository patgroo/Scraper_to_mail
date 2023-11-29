import requests
from bs4 import BeautifulSoup


def scrape_article_data(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all(
        'article', class_='featured-secondary__wrapper___6uFWZ')

    scraped_data = []

    for article in articles:

        title_tag = article.find(
            'h2', class_='featured-secondary__title___mb8GK')
        author_tag = article.find(
            'span', class_='featured-secondary__byline___qvEKL')
        date_tag = article.find(
            'time', class_='featured-secondary__date___tByAn')
        article_url = title_tag.find('a')['href'] if title_tag else 'No URL'

        title = title_tag.text.strip() if title_tag else 'No Title'
        author = author_tag.text.strip() if author_tag else 'No Author'
        date = date_tag['datetime'] if date_tag else 'No Date'

        article_info = f"Title: {title}\nAuthor: {author}\nDate: {date}\nURL: {article_url}"
        scraped_data.append(article_info)
        print(article_info)

    return scraped_data


if __name__ == "__main__":
    URL = 'https://www.sciencenews.org/'
    scrape_article_data(URL)
