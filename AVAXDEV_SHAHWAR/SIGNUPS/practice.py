from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome(executable_path = r"C:\Users\Ibrahim\Desktop\Akru script\AVAXDEV_SHAHWAR\SIGNUPS\chromedriver.exe")
url = "https://www.google.com/"
driver.get(url)
driver.save_screenshot("ss.png")
screenshot = Image.open("ss.png")
screenshot.show()