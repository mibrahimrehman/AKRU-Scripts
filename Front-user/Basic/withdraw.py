import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import allure
from selenium.webdriver.common.action_chains import ActionChains

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-setuid-sandbox')
        # s = Service(executable_path=ChromeDriverManager().install())
        #s = Service('/home/ubuntu/script/pipeline/test/chromdriver/chromedriver')
        
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service , options=chrome_options)
        # s = Service('/Users/qualityassurance/Desktop/automation-scripts/AVAXDEV_SHAHWAR/chromedriver')
        #self.driver = webdriver.Chrome(path, options=chrome_options)

    def test_search_in_python_org(self):
        self.driver.maximize_window()
        url = "https://avaxdev.akru.co"
        afterLoginURL = 'https://avaxdev.akru.co/dashboard'
        email = "ib_automation_seller@yopmail.com"
        wait = WebDriverWait(self.driver, 50)

        #comment change
        #new comment
        self.driver.get(url)
        print('SUCCESS: "'+url+'" saved in webdriver')

        time.sleep(3)
        try:
            loginButton=wait.until(EC.element_to_be_clickable((By.ID,"navbar-header-sticky-login")))
            loginButton.click()
            print('SUCCESS: Login button clicked')
        except:
            print("FAILED: Login button could not be clicked")
            raise Exception

        try:
            userPortalButton=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='User portal']")))
            userPortalButton.click()
            print('SUCCESS: User Portal button clicked')
        except:
            print("FAILED: User Portal button could not be clicked")
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

        time.sleep(3)
        MagicModalButtonFound= wait.until(EC.element_to_be_clickable((By.ID,"navbar-select-magic")))
        if MagicModalButtonFound:
            MagicModalButtonFound.click()
            print('SUCCESS: Magic button clicked')
        else:
            print("FAILED: Magic button could not be clicked")
            raise Exception

        time.sleep(3)
        emailBox= wait.until(EC.element_to_be_clickable((By.ID, 'navbar-magic-email')))
        if emailBox:
            emailBox.send_keys(email)
            print('SUCCESS: Email entered in magic modal')
        else:
            print('FAILED: Email could not be entered in magic modal')
            raise Exception

        time.sleep(3)
        magicNextButton = wait.until(EC.visibility_of_element_located((By.ID, "navbar-magic-next")))
        if magicNextButton:
            magicNextButton.click()
            print('SUCCESS: Magic next button clicked')
        else:
            print('FAILED: Magic next button could not be clicked')
            raise Exception

        def emailLogin():
            self.driver.execute_script("window.open('http://www.yopmail.com', 'new window')")
            self.driver.switch_to.window(self.driver.window_handles[1])
            print('SUCCESS: Switched to YOPMAIL tab')

            try:
                time.sleep(3)
                search = wait.until(EC.element_to_be_clickable((By.ID,"login")))
                search.clear()
                search.send_keys(email)
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
                print('SUCCESS: Switched to YOPMAIL iframe')
            except:
                print("FAILED: Could not switch to iframe in YOPMAIL.")
                raise Exception

            try:
                time.sleep(3)
                LoginEmailButton=wait.until(EC.element_to_be_clickable((By.XPATH,'//strong[text()="Log in to Akru TestNet"]')))
                LoginEmailButton.click()
                print('SUCCESS: "Log in to Akru TestNet" button clicked from YOPMAIL')
            except:
                print('FAILED: Could not find "Log in to Akru TestNet" button.')
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
            time.sleep(3)
            print('SUCCESS: Loader Disappeared')
        except:
            print('FAILED: Loader did not appear or still loading')

        try:
            LoginToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Toaster Appeared')
        except:
            print('FAILED: Toaster could not be appeared')

        if self.driver.current_url == afterLoginURL:
            print('\nSUCCESS: SUCCESSFULLY LOGGED IN. New URL is '+ afterLoginURL)
        else:
            print('\nFAILED: Could not login. As dashboard did not appear.\n')
            # print('\nFAILED: Success toaster could not be appeared. Instead toaster with the text: "'+LoginToasterMessage.text+'" appeared\n')
            raise Exception

        

        try:
                time.sleep(3)
                LoginEmailButton=wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@id="toWallet"]')))
                LoginEmailButton.click()
                print('SUCCESS: Wallet button clicked successfully')
        except:
                print('FAILED: Wallet button could not be clicked.')
                raise Exception

        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,91)")

    # 27. Scroll window by ('0','70')
        self.driver.execute_script("window.scrollBy(0,70)")

        # 28. Click 'Continue Payment'
        # continue_payment = self.driver.find_element(By.CSS_SELECTOR,
        #                                     "#toBankAccount")
        # continue_payment.click()

        try:
            time.sleep(3)
            paybox=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Withdraw']")))
            paybox.click()
            time.sleep(3)
            paybox=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Withdraw']")))
            paybox.click()
            print('SUCCESS: Withdraw tab clicked successfully')
        except:
                print('FAILED: Withdraw tab could not be clicked.')
                raise Exception
        
        try:
            amountfeild=wait.until(EC.element_to_be_clickable((By.XPATH,"//div//input[@name='amount']")))
            time.sleep(3)
            amountfeild=wait.until(EC.element_to_be_clickable((By.XPATH,"//div//input[@name='amount']")))
            amountfeild.click()
            amountfeild.send_keys("1000")
            print('SUCCESS: Deposit Amount entered successfully')
        except:
            print("FAILED: Deposit Amount could not be entered successfully")
            raise Exception

        try:
            amountfeild=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Withdraw']"))).click()
            #amountfeild.click()
            print('SUCCESS: Withdraw button clicked successfully')
        except:
            print("FAILED: Withdraw button could not be clicked successfully")
            raise Exception


        time.sleep(4)

        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get('https://avaxdevapi.akru.co/api/user/showOtp/'+ email)
        otp = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/pre')))
        otp_array = list(otp.text)
        otp_code = otp_array[39] + otp_array[40] + \
            otp_array[41] + otp_array[42]
        
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # 33. Click 'v1'
        v1 = self.driver.find_element(By.CSS_SELECTOR,
                                "#v1")
        v1.click()

        # 34. Type '0' in 'v1'
        v1 = self.driver.find_element(By.CSS_SELECTOR,
                                "#v1")
        v1.send_keys(otp_code[0])

        # 35. Type '0' in 'v2'
        v2 = self.driver.find_element(By.CSS_SELECTOR,
                                "#v2")
        v2.send_keys(otp_code[1])

        # 36. Type '0' in 'v3'
        v3 = self.driver.find_element(By.CSS_SELECTOR,
                                "#v3")
        v3.send_keys(otp_code[2])

        # 37. Type '0' in 'v4'
        v4 = self.driver.find_element(By.CSS_SELECTOR,
                                "#v4")
        v4.send_keys(otp_code[3])

        # 38. Click 'AUTHORIZE'
        authorize = self.driver.find_element(By.XPATH,
                                        "//button[. = 'Authorize']")
    
        authorize.click()

        try:
            LoginToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Deposit successfully toaster appeared')
        except:
            print("FAILED: Toaster could not appeared")
            raise Exception
        time.sleep(5)

        try:
            print('\nToaster Appeared having text: "'+LoginToasterMessage.text+'"\n')
        except:
            print('\nFAILED: Success toaster could not be appeared. Instead toaster with the text: "'+LoginToasterMessage.text+'" appeared\n')
            raise Exception


    def tearDown(self):
        time.sleep(3)
        # self.driver.save_screenshot("login.PNG")
        # allure.attach.file(r"login.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        # time.sleep(3)
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()
