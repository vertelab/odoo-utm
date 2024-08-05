# ~ from selenium import webdriver
# ~ from selenium.webdriver.chrome.service import Service
# ~ from selenium.webdriver.common.by import By
# ~ from selenium.webdriver.support.ui import WebDriverWait
# ~ from selenium.webdriver.support import expected_conditions as EC
# ~ from selenium.webdriver.chrome.options import Options
# ~ from selenium.common.exceptions import InvalidArgumentException, WebDriverException



# ~ service = Service()
# ~ driver = webdriver.Chrome(options=self.options)

# ~ driver = self.execute_hook('on_driver_created', self.driver)

from crawl4ai import WebCrawler
from crawl4ai.extraction_strategy import LLMExtractionStrategy

crawler = WebCrawler()
crawler.warmup()



# ~ service = Service('/var/lib/odoo/.cache/selenium/chromedriver/linux64/127.0.6533.88/chromedriver')
# ~ driver = webdriver.Chrome(service=service)
