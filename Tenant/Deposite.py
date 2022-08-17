from binhex import FInfo
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
#import allure
#import yopmail_login
from yopmail_login import yopmail
import variables
from chrome_setup import chrome
#from combine import combine_allure


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
        
        
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service , options=chrome_options)
        # PATH = "chromedriver"
        # self.driver = webdriver.Chrome(PATH, options=chrome_options)

        csk = chrome()
        self.driver = csk.get_driver()
        driverl = self.driver

        self.test_search_in_python_org(self.driver)

        

    def test_search_in_python_org(self , driver):
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

        def cookiesHandle():
            try:
                time.sleep(3)
                cookiesClickerFound=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='d-flex justify-content-end']/button[3]")))
                cookiesClickerFound.click()
                print('SUCCESS: "Allow all cookies" button clicked')
            except:
                print('FAILED: "Allow all cookies" button could not be clicked')
                raise Exception
        cookiesHandle()

        try:
            mo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,  "#navbar-select-magic")))
            mo.click()
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
            if(wait.until(EC.visibility_of_element_located(By.CLASS_NAME , 'loader-overlay'))):
                print("SUCCESS: Loader found")
                loaderremove = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay')))
                print("SUCCESS: Loader disappeared successfully")
            else:
                print("FAILED: loader did not disappeared or still loading")

        except:
            print("FAILED: Loader did not open")


        # Login from yopmail
        ym = yopmail(driver)
        ym.run()


        try:
            LoginToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Log in successfully toaster appeared')
        except:
            print("FAILED: Toaster could not appeared")
            raise Exception

        #ym = yopmail(driver)
        #ym.run()
        time.sleep(5)
        try:
            depositeb = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='primary-btn']")))
            depositeb.click()
            print('SUCCESS: Deposite button clicked')
        except:
            print("FAILED: Deposite button not clicked")
            raise Exception

        time.sleep(5)
        driver.execute_script("window.scrollBy(0,91)")

    # 27. Scroll window by ('0','70')
        driver.execute_script("window.scrollBy(0,70)")

        # 28. Click 'Continue Payment'
        continue_payment = driver.find_element(By.CSS_SELECTOR,
                                            "#toBankAccount")
        continue_payment.click()

        # 29. Scroll window by ('0','154')
        driver.execute_script("window.scrollBy(0,154)")

        # 30. Click 'amount'
        amount = driver.find_element(By.CSS_SELECTOR,
                                    "#outlined-error-helper-text")
        amount.click()

        # 31. Type '2500' in 'amount'
        amount = driver.find_element(By.CSS_SELECTOR,
                                    "#outlined-error-helper-text")
        amount.send_keys("2500")

        # 32. Click 'Confirm & Pay'
        confirm_pay = driver.find_element(By.XPATH,
                                        "//button[. = 'Confirm & Pay']")
        confirm_pay.click()

        time.sleep(4)

        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get('https://avaxdevapi.akru.co/api/user/showOtp/'+ variables.login_email)
        otp = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/pre')))
        otp_array = list(otp.text)
        otp_code = otp_array[39] + otp_array[40] + \
            otp_array[41] + otp_array[42]
        
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # 33. Click 'v1'
        v1 = driver.find_element(By.CSS_SELECTOR,
                                "#v1")
        v1.click()

        # 34. Type '0' in 'v1'
        v1 = driver.find_element(By.CSS_SELECTOR,
                                "#v1")
        v1.send_keys(otp_code[0])

        # 35. Type '0' in 'v2'
        v2 = driver.find_element(By.CSS_SELECTOR,
                                "#v2")
        v2.send_keys(otp_code[1])

        # 36. Type '0' in 'v3'
        v3 = driver.find_element(By.CSS_SELECTOR,
                                "#v3")
        v3.send_keys(otp_code[2])

        # 37. Type '0' in 'v4'
        v4 = driver.find_element(By.CSS_SELECTOR,
                                "#v4")
        v4.send_keys(otp_code[3])

        # 38. Click 'AUTHORIZE'
        authorize = driver.find_element(By.XPATH,
                                        "//button[. = 'Authorize']")
    
        authorize.click()


        time.sleep(5)
        # try:
        #     continuepayment = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='nav nav-tabs']")))
        #     continuepayment.click()
        #     print('SUCCESS: continue payment bank button clicked')
        # except:
        #     print("FAILED: continue payment bank button not clicked")
        #     raise Exception

        # try:
        #     amount = wait.until(EC.presence_of_element_located((By.ID, 'outlined-error-helper-text')))
        #     amount.click()
        #     amount.send_keys("2000")
        #     print('SUCCESS: amount text feild click')
        # except:
        #     print("FAILED: amount text feild not click")
        #     raise Exception
        


        # try:
        #     amount = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='primary-btn']")))
        #     amount.click()
        #     print('SUCCESS: pay and continue click')
        # except:
        #     print("FAILED: pay and continue not click")
        #     raise Exception



        # try:
        #     amount = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']")))
            
        #     print('SUCCESS: modale appeard')
        # except:
        #     print("FAILED:modale not appeard")
        #     raise Exception


        
        # self.driver.execute_script("window.open('');")
        # self.driver.switch_to.window(self.driver.window_handles[1])
        # self.driver.get('https://avaxdevapi.akru.co/api/user/showOtp/'+ variables.login_email)
        # otp = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/pre')))
        # otp_array = list(otp.text)
        # otp_code = otp_array[39] + otp_array[40] + \
        #     otp_array[41] + otp_array[42]
        
        # self.driver.close()
        # self.driver.switch_to.window(self.driver.window_handles[0])

        # try:
        #     otpt = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='v1']")))
        #     otpr.click()
        #     otpt.send_keys(otp_code)
        #     print('SUCCESS: otp code entered')
        # except:
        #     print("FAILED: otp code not entered")
        #     raise Exception
        # try:
        #     amount = wait.until(EC.presence_of_element_located((By.ID, 'outlined-error-helper-text')))
        #     amount.click()
        #     amount.send_keys("2000")
        #     print('SUCCESS: amount text feild click')
        # except:
        #     print("FAILED: amount text feild not click")
        #     raise Exception
        
        
    def tearDown(self):
        time.sleep(3)
        self.driver.save_screenshot("entsig.PNG")
        #combine_allure("/Users/asadullahkhan/Desktop/AKRU-Scripts/Property_owners/target/allure-results")
        #allure.attach.file(r"entsig.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
