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



        ym = yopmail(driver)
        ym.run()

    

        try:
            LoginToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Log in successfully toaster appeared')
        except:
            print("FAILED: Toaster could not appeared")
            raise Exception
        time.sleep(5)

      
        try:
            self.driver.get("https://avaxdevowners.akru.co/dashboard/property-details?id=62986ac171061cfdd91ba6ca&status=launched")
            print('SUCCESS: Reach on property view details successfully')
        except:
            print("FAILED: Could not reach on property view details")
            raise Exception
        time.sleep(5)
        try:
            amountfeild=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Invite Tenants']")))
            amountfeild.click()
            print('SUCCESS: Invite tenant clicked successfully')
        except:
            print("FAILED: Invite tenant could not be clicked successfully")
            raise Exception

        try:
            firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='firstName']")))
            firstname.click()
            firstname.send_keys("Ibrahim")
            print('SUCCESS: First name entered successfully')
        except:
            print("FAILED: First name could not be entered successfully")
            raise Exception

        try:
            firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='lastName']")))
            firstname.click()
            firstname.send_keys("Rehman")
            print('SUCCESS: last name entered successfully')
        except:
            print("FAILED: last name could not be entered successfully")
            raise Exception

        try:
            firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='email']")))
            firstname.click()
            firstname.send_keys("tenantav1@yopmai.com")
            print('SUCCESS: Email entered successfully')
        except:
            print("FAILED: Email could not be entered successfully")
            raise Exception


        try:
            firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='rentAmount']")))
            firstname.click()
            firstname.send_keys("100")
            print('SUCCESS: Rent amount entered successfully')
        except:
            print("FAILED: Rent amount could not be entered successfully")
            raise Exception

        try:
            firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='feeAmount']")))
            firstname.click()
            firstname.send_keys("120")
            print('SUCCESS: Fee amount entered successfully')
        except:
            print("FAILED: fee amount could not be entered successfully")
            raise Exception

        try:
            firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='securityAmount']")))
            firstname.click()
            firstname.send_keys("110")
            print('SUCCESS: Security amount entered successfully')
        except:
            print("FAILED: Security amount could not be entered successfully")
            raise Exception

        

        try:
            firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='noticePeriod']")))
            firstname.click()
            firstname.send_keys("1")
            print('SUCCESS: Notice period amount entered successfully')
        except:
            print("FAILED: Notice period amount could not be entered successfully")
            raise Exception
       

        try:
            firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Units']/parent::div//div//div")))
            firstname.click()
            
            unitnumber=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@data-value='2']")))
            unitnumber.click()
            print('SUCCESS: Unit no 2 selected successfully')
        except:
            print("FAILED: Unit no 2 could not be selected")
            raise Exception

        try:
            firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Grace Period']/parent::div/child::div")))
            firstname.click()
            
            unitnumber=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@data-value='5']")))
            unitnumber.click()
            print('SUCCESS: Grace period 5 is selected successfully')
        except:
            print("FAILED: Grace period 5 could not be selected")
            raise Exception

        try:
            firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Fee Type']/parent::div//div//div")))
            firstname.click()
            
            unitnumber=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@data-value='lumpSum']")))
            unitnumber.click()
            print('SUCCESS: Fee type lump sum is selected successfully')
        except:
            print("FAILED: Fee type lump sum could not be selected")
            raise Exception

        try:
            uploadagreement=self.driver.find_element(By.XPATH, "//input[@name='agreement']")
            #wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='agreement']")))
            filepath = os.path.abspath("blank.pdf")
            uploadagreement.send_keys(filepath)
            print('SUCCESS: Agreement uploaded successfully')
        except:
            print("FAILED: Agreement could not be uploaded")
            raise Exception

        
        try:
            firstname=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
            firstname.click()
            print('SUCCESS: Submit button clicked successfully')
        except:
            print("FAILED: Submit button could not be clicked successfully")
            raise Exception

        time.sleep(4)



        try:
            print('\nToaster Appeared having text: "'+LoginToasterMessage.text+'"\n')
        except:
            print('\nFAILED: Success toaster could not be appeared. Instead toaster with the text: "'+LoginToasterMessage.text+'" appeared\n')
            raise Exception

        

        
    def tearDown(self):
        time.sleep(3)
        # self.driver.save_screenshot("ownerlogin.PNG")
        # allure.attach.file(r"ownerlogin.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        # time.sleep(3)
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()
