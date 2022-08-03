import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import allure

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--enable-extensions")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument('--no-sandbox')
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service , options=chrome_options)
        #PATH = "chromedriver"
        # s = Service('/Users/qualityassurance/Desktop/automation-scripts/AVAXDEV_SHAHWAR/chromedriver')
        #self.driver = webdriver.Chrome(PATH, options=chrome_options)

    def test_search_in_python_org(self):
        self.driver.maximize_window()
        actions = ActionChains(self.driver)
        url = "https://avaxdev.akru.co"
        afterLoginURL = 'https://avaxdev.akru.co/dashboard'
        email = "ib_automation_seller@yopmail.com"
        wait = WebDriverWait(self.driver, 10)
        
        self.driver.get(url)
        print('SUCCESS: "'+url+'" saved in webdriver')

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

        try:
            cookiesClickerFound=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='d-flex justify-content-end']/button[3]")))
            cookiesClickerFound.click()
            print('SUCCESS: "Allow all cookies" button clicked')
        except:
            print('FAILED: "Allow all cookies" button could not be clicked')
            raise Exception

        try:
            MagicModalButtonFound= wait.until(EC.element_to_be_clickable((By.ID,"navbar-select-magic")))
            MagicModalButtonFound.click()
            print('SUCCESS: Magic button clicked')
        except:
            print("FAILED: Magic button could not be clicked")
            raise Exception

        try:
            emailBox= wait.until(EC.element_to_be_clickable((By.ID, 'navbar-magic-email')))
            emailBox.send_keys(email)
            print('SUCCESS: Email entered in magic modal')
        except:
            print('FAILED: Email could not be entered in magic modal')
            raise Exception

        try:
            magicNextButton = wait.until(EC.element_to_be_clickable((By.ID, "navbar-magic-next")))
            magicNextButton.click()
            print('SUCCESS: Magic next button clicked')
        except:
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

        time.sleep(10 )
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
            toasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Toaster Appeared')
        except:
            print('FAILED: Toaster could not be appeared')

        if self.driver.current_url == afterLoginURL:
            print('SUCCESS: SUCCESSFULLY LOGGED IN. New URL is '+ afterLoginURL)
        else:
            print('\nFAILED: Could not login. As dashboard did not appear.\n')
            # print('\nFAILED: Success toaster could not be appeared. Instead toaster with the text: "'+LoginToasterMessage.text+'" appeared\n')
            raise Exception

        try:
            MyPortfolio=wait.until(EC.element_to_be_clickable((By.ID, 'toPortfolio')))
            MyPortfolio.click()
            print('SUCCESS: My Portfolio is Clicked')
        except:
            print('FAILED: Could not click My Portfolio')
            raise Exception
            
        try:
            ActionButtonToPlaceCounterOfferCheckk=wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "action")))
            ActionButtonToPlaceCounterOfferCheckk.click()
        except:
            print('NOTHING LISTED')

        cancelOption = False
        try:
            CancelOptionFromActionButtons=wait.until(EC.element_to_be_clickable((By.ID, "counteredCancelButton1")))
            if(CancelOptionFromActionButtons):
                cancelOption = True
        except:
            print('NO COUNTERED OFFER TO CANCEL')

        while(cancelOption == True):
            try:
                CancelOptionFromActionButtons=wait.until(EC.element_to_be_clickable((By.ID, "counteredCancelButton1")))
                CancelOptionFromActionButtons.click()
                print('SUCCESS: Cancel Option from Action buttons is clicked by the seller to cancel the whole exchange')
            except:
                print('FAILED: Could not click Cancel Option from Action buttons by the seller to cancel the whole exchange')
                raise Exception

            actionButton = False
            time.sleep(30)

            try:
                ActionButtonToPlaceCounterOfferCheck=wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "action")))
                ActionButtonToPlaceCounterOfferCheck.click()
                CancelOptionFromActionButtons=wait.until(EC.element_to_be_clickable((By.ID, "counteredCancelButton1")))
                if(CancelOptionFromActionButtons):
                    actionButton = True
                print('\nCountered Offer(s) still exists...\n')
            except:
                print('No more countered offer(s) left...')

        self.driver.refresh()
        time.sleep(10)

        actionButton = False
        try:
            ActionButtonToPlaceCounterOfferCheckk=wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "action")))
            if(ActionButtonToPlaceCounterOfferCheckk):
                actionButton = True
        except:
            print('NOTHING LISTED')

        while(actionButton == True):
            try:
                ActionButtonToPlaceCounterOffer=wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "action")))
                ActionButtonToPlaceCounterOffer.click()
                print('SUCCESS: Action button for options is clicked')
            except:
                print('FAILED: Could not click action button for options')
                raise Exception

            try:
                CounterOptionFromActionButtons=wait.until(EC.element_to_be_clickable((By.ID, "cancelButton1")))
                CounterOptionFromActionButtons.click()
                print('SUCCESS: Cancel Option from Action buttons is clicked by the seller to cancel the whole exchange')
            except:
                print('FAILED: Could not click Cancel Option from Action buttons by the seller to cancel the whole exchange')
                raise Exception

            actionButton = False
            time.sleep(30)

            try:
                ActionButtonToPlaceCounterOfferCheck=wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "action")))
                if(ActionButtonToPlaceCounterOfferCheck):
                    actionButton = True
                    print('\nListing(s) still exists...\n')
            except:
                print('No more listing(s) left...')

        print('\nSUCCESSFULLY CANCELED ALL LISTED EXCHANGES\n')

    def tearDown(self):
        time.sleep(3)
        self.driver.save_screenshot("cancel_all_listed.PNG")
        allure.attach.file(r"cancel_all_listed.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
