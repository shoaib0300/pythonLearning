from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Optional: Run in headless mode

# Set the WebDriver executable path for macOS
chrome_driver_path = '/usr/local/bin/chromedriver'  # Replace with your actual ChromeDriver path

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# URL of the website you want to scrape
url = 'https://villa-schmidt.de/'

# Open the webpage
driver.get(url)

try:
    # Extract data from the page
    quotes = driver.find_elements(By.CLASS_NAME, 'text')
    authors = driver.find_elements(By.CLASS_NAME, 'author')

    # Loop through the extracted data and print it
    for quote, author in zip(quotes, authors):
        print(f'Quote: {quote.text}')
        print(f'Author: {author.text}\n')
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    # Close the browser
    driver.quit()
