import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument('--no-sandbox')
        #comment at 19
        #s = Service('/home/ubuntu/script/pipeline/test/chromdriver/chromedriver')
        # s = Service('/Users/qualityassurance/Desktop/automation-scripts/AVAXDEV_SHAHWAR/chromedriver')
        PATH = "E:\chromedriver"
        self.driver = webdriver.Chrome(PATH , options=chrome_options)

    def test_search_in_python_org(self):
        self.driver.maximize_window()
        url = "https://avaxdev.akru.co"
        afterLoginURL = 'https://avaxdev.akru.co/dashboard'
        email = "ds_automation_seller@yopmail.com"
        propertyIDGoalReached = "property6232fcca24186e759830a7bc"
        AmountOfTokensToBuy = "1"
        propertyToken = 'AK-EX01'
        wait = WebDriverWait(self.driver, 120)

        self.driver.get(url)
        print('SUCCESS: "'+url+'" saved in webdriver')

        time.sleep(3)
        loginButton=wait.until(EC.element_to_be_clickable((By.ID,"navbar-header-sticky-login")))
        if loginButton:
            loginButton.click()
            print('SUCCESS: Login button clicked')
        else:
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
            ListingButton=wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Listings']")))
            ListingButton.click()
            print('SUCCESS: Listing button clicked')
        except:
            print('FAILED: Could not click lisitng button')
            raise Exception

        time.sleep(3)
        try:
            Property=wait.until(EC.element_to_be_clickable((By.ID, propertyIDGoalReached)))
            Property.click()
            print('SUCCESS: Property clicked from listing')
        except:
            print('FAILED: Could not click property from listing')
            raise Exception

        time.sleep(3)
        try:
            InvestNowButton=wait.until(EC.element_to_be_clickable((By.ID, "singleProperty-secondary-invest")))
            InvestNowButton.click()
            print('SUCCESS: Invest Now button clicked')
        except:
            print('FAILED: Could not click Invest Now button')
            raise Exception

        time.sleep(3)
        try:
            AmountOfTokens=wait.until(EC.element_to_be_clickable((By.ID, 'quantity0')))
            AmountOfTokens.send_keys(Keys.BACKSPACE)
            AmountOfTokens.send_keys(AmountOfTokensToBuy)
            print('SUCCESS: Amount to buy tokens is entered: ' + AmountOfTokensToBuy)
        except:
            print('FAILED: Could not enter amount of tokens to buy')
            raise Exception

        time.sleep(3)
        try:
            InvestNowButtonScrolled=wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="primary-btn d-block w-100"]')))
            InvestNowButtonScrolled.click()
            print('SUCCESS: Invest now button is clicked')
        except:
            print('FAILED: Could not click invest now button')
            raise Exception

        try:
            time.sleep(5)
            loader = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay')))
            time.sleep(5)
            print('SUCCESS: Loader Disappeared')
        except:
            print('FAILED: Loader did not appear or still loading')

        try:
            toasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Toaster Appeared')
        except:
            print('FAILED: Toaster could not be appeared')

        if toasterMessage.text == '$1010 Invested Successfully !!!':
            print('\nSUCCESS: INVESTED SUCCESSFULLY toaster Appeared having text: "'+toasterMessage.text+'"\n')
        else:
            print('\nFAILED: Invested successfully toaster could not be appeared. Instead toaster with the text: "'+toasterMessage.text+'" appeared\n')
            raise Exception

        print('\nSUCCESSFULLY INVESTED IN THE PROPERTY WHOSE GOAL IS REACHED\n')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
