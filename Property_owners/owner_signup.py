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
        #driver = gdriver
        driver = self.driver
        driver.maximize_window()

        action = ActionChains (self.driver)
        def clearTextField():
            action.key_down(Keys.COMMAND).perform()
            action.send_keys('a').perform()
            action.key_up(Keys.COMMAND).perform()
            action.send_keys(Keys.BACK_SPACE).perform()

        wait = WebDriverWait(self.driver, 120)

        ym = yopmail(driver)
        ym.run()

        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        try:
            addressToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="address"]')))
            addressToBeEntered.click()
            clearTextField()
            addressToBeEntered.send_keys('3825 Edwards Rd, #103, Cincinnati, OH 45209')
            print('SUCCESS: Address is entered')
        except:
            print("FAILED: Address could not be entered")
            raise Exception

        try:
            stateToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//select[@name="stateName"]')))
            stateToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH, '//select[@name="stateName"]//option[@value="Ohio"]'):
                if option.text == 'Ohio':
                    option.click()
                    break
            print("SUCCESS: State 'Ohio' is selected from dropdown")
        except:
            print("FAILED: State 'Ohio' could not be selected from dropdown")
            raise Exception

        try:
            cityToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="city"]')))
            cityToBeEntered.click()
            clearTextField()
            cityToBeEntered.send_keys('Cincinnati')
            print('SUCCESS: City is entered')
        except:
            print("FAILED: City could not be entered")
            raise Exception

    

        try:
            zipCodeToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="zipCode"]')))
            zipCodeToBeEntered.click()
            clearTextField()
            zipCodeToBeEntered.send_keys('45209')
            print('SUCCESS: Zip code is entered')
        except:
            print("FAILED: Zip code could not be entered")
            raise Exception


        try:
            cityToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='number']")))
            cityToBeEntered.click()
            clearTextField()
            cityToBeEntered.send_keys('3186107885')
            print('SUCCESS: Number is entered')
        except:
            print("FAILED: Number could not be entered")
            raise Exception


        try:
            verfiybuttonToSendOTP=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Verify"]')))
            verfiybuttonToSendOTP.click()
            print('SUCCESS: Verify button is clicked to verify phone number')
        except:
            print("FAILED: Verify button could not be clicked to verify phone number")
            raise Exception

        time.sleep(10)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get('https://avaxdevapi.akru.co/api/user/showOtp/'+variables.signup_email)
        otp = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/pre')))
        otp_array = list(otp.text)
        otp_code = otp_array[39] + otp_array[40] + \
            otp_array[41] + otp_array[42]
        
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        try:
            otptobeentered = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="otp"]')))
            otptobeentered.send_keys(otp_code)
            print('SUCCESS: OTP is entered')
        except:
            print("FAILED: Could not enter OTP")
            raise Exception

        try:
            dobToBeEntered=wait.until(EC.element_to_be_clickable((By.ID,'date-picker-dialog')))
            dobToBeEntered.send_keys(Keys.BACKSPACE)
            dobToBeEntered.send_keys('0')
            print('SUCCESS: Date of Birth is entered')
        except:
            print("FAILED: Could not enter date of birth")
            raise Exception

        try:
            SSNToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="securityNumber"]')))
            SSNToBeEntered.send_keys('123456789')
            print('SUCCESS: SSN is entered')
        except:
            print("FAILED: SSN could not be entered")
            raise Exception

        try:
            continueButtonAfterStep2Completion=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Continue"]')))
            continueButtonAfterStep2Completion.click()
            print('SUCCESS: Continue button is clicked after filling the form on step 2')
        except:
            print("FAILED: Continue button could not be clicked after filling the form on step 2")
            raise Exception
        
        try:
            time.sleep(5)
            loader = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay')))
            time.sleep(5)
            print('SUCCESS: Loader Disappeared')
        except:
            print('FAILED: Loader did not appear or still loading')



       

        try:
            skipAddingBankButton=wait.until(EC.visibility_of_element_located((By.XPATH,'//button[text()="Skip"]')))
            skipAddingBankButton.click()
            print('SUCCESS: Skip button of account detail is clicked')
        except:
            print("FAILED:  Skip button of account detail could not be clicked")
            raise Exception

        time.sleep(5)

        try:
            checkingAgreement1=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="point1"]')))
            checkingAgreement1.click()
            print('SUCCESS: Agreement 1 checked')
        except:
            print("FAILED: Agreement 1 could not be checked")
            raise Exception

        try:
            checkingAgreement2=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="point2"]')))
            checkingAgreement2.click()
            print('SUCCESS: Agreement 2 checked')
        except:
            print("FAILED: Agreement 2 could not be checked")
            raise Exception

        try:
            checkingAgreement3=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="point3"]')))
            checkingAgreement3.click()
            print('SUCCESS: Agreement 3 checked')
        except:
            print("FAILED: Agreement 3 could not be checked")
            raise Exception

        
        try:
            ContinueButtonAfterCheckingAgreements=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="btn btn-info ml-auto d-block"]')))
            ContinueButtonAfterCheckingAgreements.click()
            print('SUCCESS: Continue button clicked after checking all 3 agreements')
        except:
            print("FAILED: Continue button could not be clicked after checking all 3 agreements")
            raise Exception

        time.sleep(5)
        
        



        try:
            VerifyInfoButtonAtStep5=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="btn btn-info ml-auto d-block"]')))
            VerifyInfoButtonAtStep5.click()
            print('SUCCESS: Verify button at step 5 is clicked')
        except:
            print("FAILED: Verify button at step 5 could not be clicked")
            raise Exception

        time.sleep(10)
        try:
            createConnectWalletButton=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="btn btn-info ml-auto d-block"]')))
            createConnectWalletButton.click()
            print('SUCCESS: CREATE/CONNECT wallet button is clicked')
        except:
            print("FAILED: CREATE/CONNECT wallet button could not be clicked")
            raise Exception

        try:
            magicButtonFromSignupModal=wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="donwload-btn"]')))
            magicButtonFromSignupModal.click()
            print('SUCCESS: Magic button is clicked from signup modal')
        except:
            print("FAILED: Magic button could not be clicked from signup modal")
            raise Exception

        try:
            time.sleep(5)
            loader = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay')))
            time.sleep(5)
            print('SUCCESS: Loader Disappeared')
        except:
            print('FAILED: Loader did not appear or still loading')
        
        def emailLogin():
            self.driver.execute_script("window.open('http://www.yopmail.com', 'new window')")
            self.driver.switch_to.window(self.driver.window_handles[1])
            print('SUCCESS: Switched to YOPMAIL tab')

            try:
                time.sleep(3)
                search = wait.until(EC.element_to_be_clickable((By.ID,"login")))
                search.clear()
                search.send_keys(variables.signup_email)
                search.send_keys(Keys.RETURN)
                print('SUCCESS: Email entered in YOPMAIL input field')
            except:
                print('FAILED: Email could not be entered in YOPMAIL input field')
                raise Exception

            time.sleep(3)
            self.driver.refresh()
            time.sleep(5)

            try:
                self.driver.switch_to.frame('ifmail')
            except:
                print("FAILED: Could not switch to iframe in YOPMAIL.")
                raise Exception

            try:
                time.sleep(3)
                LoginEmailButton=wait.until(EC.element_to_be_clickable((By.XPATH,'//strong[text()="Log in to Akru TestNet"]')))
                LoginEmailButton.click()
                print('SUCCESS: "Log in to Akru TestNet" button clicked from YOPMAIL')
            except:
                print('FAILED: Could not find "Log in to Akru TestNet" button. Maybe due to captcha.')
                raise Exception

        emailLogin()

        time.sleep(10)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(10)

        try:
            time.sleep(5)
            loader = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay')))
            time.sleep(5)
            print('SUCCESS: Loader Disappeared')
        except:
            print('FAILED: Loader did not appear or still loading')


        try:
            LoginToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Toaster Appeared')
        except:
            print('FAILED: Toaster could not be appeared')

    

        print('\nSUCCESSFULLY SINGED UP INDIVIDUAL ACCOUNT\n' + "Email: " + variables.signup_email)

    

        
        time.sleep(5)

        
    def tearDown(self):
        time.sleep(3)
        self.driver.save_screenshot("entsig.PNG")
        allure.attach.file(r"entsig.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
