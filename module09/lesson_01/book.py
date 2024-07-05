import requests
from bs4 import BeautifulSoup

# URL of the website
url = 'http://books.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object with the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all book containers
    books = soup.find_all('article', class_='product_pod')

    # Loop through each book and extract data
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()

# //*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/h3
# /html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3
        print(f'Title: {title}')
        print(f'Price: {price}')
        print(f'Availability: {availability}')
        print('---')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
