from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Initialize the Chrome driver
driver = webdriver.Chrome()  # Make sure the ChromeDriver is in your PATH or provide the path to the driver

# Open the main page
driver.get("https://index.minfin.com.ua/ua/russian-invading/casualties/")

# Wait for the month links to be present
month_links = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@id="months"]/a'))
)

# Extract the href attributes for all month links
month_urls = [link.get_attribute('href') for link in month_links]

data = []

# Visit each month page and extract data
for url in month_urls:
    driver.get(url)
    time.sleep(2)  # Wait for the page to load completely

    # Extract the date
    date = driver.find_element(By.XPATH, '//h4[@class="h4"]').text

    # Extract data from the table
    rows = driver.find_elements(By.XPATH, '//table[@class="casualties"]/tbody/tr')

    for row in rows:
        category = row.find_element(By.XPATH, './td[1]').text
        value = row.find_element(By.XPATH, './td[2]').text

        data.append({
            'date': date,
            'category': category,
            'value': value,
        })

# Save the data to a JSON file
with open('casualties.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Close the driver
driver.quit()
