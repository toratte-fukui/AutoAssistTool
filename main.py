from selenium.webdriver.common.by import By

from lib.scraping_tool import ScrapingTool

tool = ScrapingTool(url="https://google.com")

list_details = tool.driver.find_elements(By.CLASS_NAME, "iw-list-detail")
print(list_details)
