from collections import abc
from pickle import FALSE
import unittest
from selenium import webdriver
import time
import names
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import os
from PIL import Image
import allure
#import yopmail_login
from yopmail_login import yopmail
import variables


class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-setuid-sandbox')
        #s = Service('/home/ubuntu/script/pipeline/test/chromdriver/chromedriver')
        # s = Service('/Users/qualityassurance/Desktop/automation-scripts/AVAXDEV_SHAHWAR/chromedriver')
        PATH = "chromedriver"
        self.driver = webdriver.Chrome(PATH, options=chrome_options)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.maximize_window()
        url = variables.url

        action = ActionChains (driver)
        def clearTextField():
            action.key_down(Keys.COMMAND).perform()
            action.send_keys('a').perform()
            action.key_up(Keys.COMMAND).perform()
            action.send_keys(Keys.BACK_SPACE).perform()


        self.driver.get(url)
        print('SUCCESS: "'+url+'" saved in webdriver')
        wait = WebDriverWait(self.driver, 120)

        time.sleep(3)
        try:
            loginButton=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#navbar-header-sticky-login")))
            loginButton.click()
            print('SUCCESS: Get Started button clicked')
        except:
            print("FAILED: Get Started button could not be clicked")
            raise Exception

        try:
            tenant_portal = wait.until(EC.element_to_be_clickable((By.XPATH,     "//button[. = 'Tenant portal']")))
            tenant_portal.click()
            print('SUCCESS: Tenant portal option clicked')
        except:
            print("FAILED: Tenant portal option could not be clicked")
            raise Exception

        try:
            modale = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,  "#navbar-select-magic")))
            modale.click()
            print('SUCCESS: Email option from modale clicked')
        except:
            print("FAILED: Email option from modale could not be clicked")
            raise Exception

        
        try:
            emailbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,  "#navbar-magic-email")))
            emailbox.click()
            print('SUCCESS: email box clicked')
        except:
            print("FAILED: email box could not be clicked")
            raise Exception

        try:
            email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar-magic-email")))
            email.click()
            clearTextField()
            email.send_keys(variables.login_email)
            print('SUCCESS: email entered successfully')
        except:
            print("FAILED: email could not be entered")
            raise Exception

        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,  "#navbar-magic-next")))
            next_button.click()
            print('SUCCESS:Next button clicked')
        except:
            print("FAILED:Next button could not be clicked")
            raise Exception

        try:
            if(wait.untill(EC.visibility_of_element_located(By.CLASS_NAME , 'loader-overlay'))):
                print("yes")
        except:
            print


        # Login from yopmail
        ym = yopmail(driver)
        ym.run()


        # try:
        #     tenant_portal = wait.until(EC.element_to_be_clickable((By.XPATH,     "//button[. = 'Tenant portal']")))
        #     tenant_portal.click()
        #     print('SUCCESS:  clicked')
        # except:
        #     print("FAILED:  could not be clicked")
        #     raise Exception

        ym = yopmail(driver)
        ym.run()
        
        
        
        
    def tearDown(self):
        time.sleep(3)
        self.driver.save_screenshot("entsig.PNG")
        allure.attach.file(r"entsig.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
