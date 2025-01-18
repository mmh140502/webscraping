import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = 'http://books.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all book containers on the page
    books = soup.find_all('article', class_='product_pod')
    
    # Create lists to store the extracted information
    titles = []
    prices = []
    availabilities = []
    
    # Loop through each book container and extract the required information
    for book in books:
        # Extract the title of the book
        title = book.h3.a['title']
        titles.append(title)
        
        # Extract the price of the book
        price = book.find('p', class_='price_color').text
        prices.append(price)
        
        # Extract the availability of the book
        availability = book.find('p', class_='instock availability').text.strip()
        availabilities.append(availability)
    
    # Create a DataFrame from the extracted data
    data = {
        'Title': titles,
        'Price': prices,
        'Availability': availabilities
    }
    df = pd.DataFrame(data)
    
    # Write the DataFrame to an Excel file
    df.to_excel('books.xlsx', index=False)
    
    print('Data has been written to books.xlsx')
else:
    print('Failed to retrieve the webpage')
