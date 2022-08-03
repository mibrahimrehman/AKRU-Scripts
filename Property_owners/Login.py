from collections import abc
from lib2to3.pgen2 import driver
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
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
#from PIL import Image
import allure
#import yopmail_login
from chrome_setup import chrome
import variables
from yopmail_login import yopmail
from tryrequest import emailapi


class Test_signup(unittest.TestCase):
    
    def setUp(self):
        # WINDOW_SIZE = "1920,1080"
        # chrome_options = Options()
        # #chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--start-maximized')
        # chrome_options.add_argument('--disable-setuid-sandbox')
        # #s = Service('/home/ubuntu/script/pipeline/test/chromdriver/chromedriver')
        # # s = Service('/Users/qualityassurance/Desktop/automation-scripts/AVAXDEV_SHAHWAR/chromedriver')
        
        
        # service = ChromeService(executable_path=ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(service=service , options=chrome_options)
       # PATH = "chromedriver"
        #self.driver = webdriver.Chrome(PATH, options=chrome_options)

        csk = chrome()
        self.driver = csk.get_driver()
        driverl = self.driver

        #self.test_search_in_python_org_login(self.driver)

        

    def test_org_signup(self):
        print("Now i am in login")
        driver = self.driver
        driver.maximize_window()
        url = variables.ownersurl

        action = ActionChains (driver)
        def clearTextField():
            action.key_down(Keys.COMMAND).perform()
            action.send_keys('a').perform()
            action.key_up(Keys.COMMAND).perform()
            action.send_keys(Keys.BACK_SPACE).perform()


        self.driver.get(url)
        print('SUCCESS: "'+url+'" saved in webdriver')
        wait = WebDriverWait(self.driver, 150)




        
    

        

        try:
            loginemail=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='email']")))
            loginemail.click()
            clearTextField()
            loginemail.send_keys(variables.login_email)
            print('SUCCESS: Email entered in email field')
        except:
            print("FAILED: Email could not be entered")
            raise Exception

        try:
            verifybutton=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Verify']")))
            verifybutton.click()
            print('SUCCESS: Verify button clicked successfully')
        except:
            print("FAILED: Verify button could not be clicked")
            raise Exception

#magic-iframe

        try:
            checkemailmodale=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe')))
            print('SUCCESS: iframe found and switched to it')
        except:
            print("FAILED: iframe could not be found")
            raise Exception


        try:
            checkemailmodale=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='mg_fj mg_fl _n']")))
            print('SUCCESS: email sended modal appeared')
        except:
            print("FAILED: email sended modal could not be appeared")
            raise Exception
        variables.emailhandler = variables.login_email



        # ym = yopmail(driver)
        # ym.run()

        ym = emailapi(driver)
        ym.fetchlink()

    

        try:
            LoginToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Log in successfully toaster appeared')
        except:
            print("FAILED: Toaster could not appeared")
            raise Exception
        time.sleep(5)

        if LoginToasterMessage.text == 'Successfully logged In!':
            print('\nSUCCESS: SUCCESSFULLY LOGGED IN. Toaster Appeared having text: "'+LoginToasterMessage.text+'"\n')
        else:
            print('\nFAILED: Success toaster could not be appeared. Instead toaster with the text: "'+LoginToasterMessage.text+'" appeared\n')
            raise Exception

        print('\nSUCCESSFULLY Logged in Owner account\n')

        
    def tearDown(self):
        time.sleep(3)
        self.driver.save_screenshot("ownerlogin.PNG")
        allure.attach.file(r"ownerlogin.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
