from webbrowser import Chrome
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def pageWait(delayWait):
    browser=webdriver.Chrome(service=service)
    delay=delayWait
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")


driver.get('https://www.facebook.com')
pageWait(delayWait=3)
