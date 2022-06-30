from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.options import Options
import unittest
#driver = webdriver.Chrome(executable_path = r"C:\Users\Ibrahim\Desktop\Akru script\AVAXDEV_SHAHWAR\SIGNUPS\chromedriver.exe")
url = "https://pythonbasics.org"

WINDOW_SIZE = "1920,1080"
chrome_options = Options()
        #chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-setuid-sandbox')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument('--disable-dev-shm-using')
        # s = Service('/home/ubuntu/script/pipeline/test/chromdriver/chromedriver')
        
        #s = Service('/Users/qualityassurance/Desktop/automation-scripts/AVAXDEV_SHAHWAR/chromedriver')
PATH =  r"C:\Users\Ibrahim\Desktop\Akru script\AVAXDEV_SHAHWAR\SIGNUPS\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)


driver.get(url)
driver.save_screenshot("ss.png")
screenshot = Image.open("ss.png")
screenshot.show()
class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):

        print("in test funvtion")



# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


# # options = webdriver.ChromeOptions()
# # options.headless = True
# # driver = webdriver.Chrome(options=options)

# # URL = 

# # driver.get(URL)


# driver = webdriver.Chrome(executable_path = r"C:\Users\Ibrahim\Desktop\Akru script\AVAXDEV_SHAHWAR\SIGNUPS\chromedriver.exe")
# url = 'https://pythonbasics.org'
# driver.get(url)

# required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
# required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
# driver.set_window_size(required_width, required_height)                                                                                                               
# driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
# screenshot = Image.open('web_screenshot.png')
# screenshot.show()

# driver.quit()

if __name__ == '__main__':
    unittest.main()