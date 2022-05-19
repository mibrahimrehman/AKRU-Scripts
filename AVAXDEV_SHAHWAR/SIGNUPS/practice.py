from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome(executable_path = "chromedriver")
url = "https://www.google.com/"
driver.get(url)
driver.save_screenshot("ss.png")
screenshot = Image.open("ss.png")
screenshot.show()