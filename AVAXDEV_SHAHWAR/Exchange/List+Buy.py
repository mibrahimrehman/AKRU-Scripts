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
import allure


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument('--no-sandbox')
        # s = Service('/home/ubuntu/script/pipeline/test/chromdriver/chromedriver')
        #s = Service('/Users/qualityassurance/Desktop/automation-scripts/AVAXDEV_SHAHWAR/chromedriver')
        PATH = "chromedriver"
        self.driver = webdriver.Chrome(PATH, options=chrome_options)

    def test_search_in_python_org(self):
        self.driver.maximize_window()
        actions = ActionChains(self.driver)
        url = "https://avaxdev.akru.co"
        afterLoginURL = 'https://avaxdev.akru.co/dashboard'
        emailseller = "ib_automation_seller@yopmail.com"
        emailbuyer = "ib_automation_buyer@yopmail.com"
        propertyIDGoalReached = "property6299b90a6cd03d05b901f8aa"
        AmountOfTokensToBuy = "1"
        PriceOfTokensToBeListedd = "1200"
        QuantityOfTokensToBeListedd = "1"
        token_name = 'AK-EX03'

        self.driver.get(url)
        print('SUCCESS: "'+url+'" saved in webdriver')
        wait = WebDriverWait(self.driver, 120)

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
            emailBox.send_keys(emailseller)
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
                search.send_keys(emailseller)
                search.send_keys(Keys.RETURN)
                print('SUCCESS: Email entered in YOPMAIL input field')
            except:
                print('FAILED: Email could not be entered in YOPMAIL input field')
                raise Exception

            time.sleep(5)
            self.driver.refresh()
            time.sleep(3)

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

        if self.driver.current_url == afterLoginURL:
            print('SUCCESS: SUCCESSFULLY LOGGED IN. New URL is '+ afterLoginURL)
        else:
            print('\nFAILED: Could not login. As dashboard did not appear.\n')
            # print('\nFAILED: Success toaster could not be appeared. Instead toaster with the text: "'+LoginToasterMessage.text+'" appeared\n')
            raise Exception
        
        print('Successfully logged in as: '+emailseller)

        try:
            MyPortfolio=wait.until(EC.element_to_be_clickable((By.ID, 'toPortfolio')))
            MyPortfolio.click()
            print('SUCCESS: My Portfolio is Clicked')
        except:
            print('FAILED: Could not click My Portfolio')
            raise Exception

        self.driver.refresh()

        try:
            time.sleep(5)
            loader = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay')))
            time.sleep(3)
            print('SUCCESS: Loader Disappeared')
        except:
            print('FAILED: Loader did not appear or still loading')

        try:
            ListTokens=wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="List Tokens"]')))
            ListTokens.click()
            print('SUCCESS: List Tokens is Clicked')
        except:
            print('FAILED: Could not click List Tokens')
            raise Exception

        time.sleep(3)
        try:
            DropDownPropertyToBeListed=wait.until(EC.presence_of_element_located((By.ID, 'demo-simple-select-outlined')))
            DropDownPropertyToBeListed.click()
            print('SUCCESS: Dropdown of property to be listed is clicked')
        except:
            print('FAILED: Could not click dropdown of property to be listed')
            raise Exception

        time.sleep(3)
        try:
            PropertyToBeListed=wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@data-value="'+token_name+'"]')))
            PropertyToBeListed.click()
            print('SUCCESS: Property to be listed is selected')
        except:
            print('FAILED: Could not select property to be listed')
            raise Exception

        time.sleep(3)
        try:
            PriceOfTokensToBeListed=wait.until(EC.element_to_be_clickable((By.ID, 'outlined-secondary-price')))
            PriceOfTokensToBeListed.send_keys(PriceOfTokensToBeListedd)
            print('SUCCESS: Price of token(s) to be listed is entered')
        except:
            print('FAILED: Could not enter price of token(s) to be listed')
            raise Exception

        time.sleep(3)
        try:
            QuantityOfTokensToBeListed=wait.until(EC.element_to_be_clickable((By.ID, 'outlined-secondary-quantity')))
            QuantityOfTokensToBeListed.send_keys(QuantityOfTokensToBeListedd)
            print('SUCCESS: Quantity of token(s) to be listed is entered')
        except:
            print('FAILED: Could not enter quantity of token(s) to be listed')
            raise Exception

        time.sleep(3)
        try:
            SellButtonOfTokensToBeListed=wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="sell-btn"]//button[@class="primary-btn"]')))
            SellButtonOfTokensToBeListed.click()
            print('SUCCESS: Sell Button while listing the token(s) is clicked')
        except:
            print('FAILED: Could not click the sell button while listing the token(s)')
            raise Exception

        try:
            time.sleep(5)
            loader = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay')))
            time.sleep(5)
            print('SUCCESS: Loader Disappeared')
        except:
            print('FAILED: Loader did not appear or still loading')

        try:
            ListedToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Toaster Appeared')
        except:
            print('FAILED: Toaster could not be appeared')

        if ListedToasterMessage.text == 'Listed '+QuantityOfTokensToBeListedd+' '+token_name:
            print('\nSUCCESS: TOKENS LISTED SUCCESSFULLY. Toaster Appeared having text: "'+ListedToasterMessage.text+'"\n')
            ListedToasterMessage.click()
        else:
            print('\nFAILED: Tokens listed successfully toaster could not be appeared. Instead toaster with the text: "'+ListedToasterMessage.text+'" appeared\n')
            raise Exception

        time.sleep(5)
        try:
            LogoutIcon=wait.until(EC.element_to_be_clickable((By.ID, "Path_679")))
            LogoutIcon.click()
            print('SUCCESS: Logout icon clicked')
        except:
            print('FAILED: Could not click logout icon')
            raise Exception

        time.sleep(5)
        self.driver.refresh()

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
            emailBox.send_keys(emailbuyer)
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
                search.send_keys(emailbuyer)
                search.send_keys(Keys.RETURN)
                print('SUCCESS: Email entered in YOPMAIL input field')
            except:
                print('FAILED: Email could not be entered in YOPMAIL input field')
                raise Exception

            time.sleep(5)
            self.driver.refresh()
            time.sleep(3)

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

        if self.driver.current_url == afterLoginURL:
            print('SUCCESS: SUCCESSFULLY LOGGED IN. New URL is '+ afterLoginURL)
        else:
            print('\nFAILED: Could not login. As dashboard did not appear.\n')
            # print('\nFAILED: Success toaster could not be appeared. Instead toaster with the text: "'+LoginToasterMessage.text+'" appeared\n')
            raise Exception

        print('Successfully logged in as: '+emailbuyer)

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
            AmountOfTokens=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='quantity1']/parent::span//span[text() = '+']")))
            AmountOfTokens.click()
            # AmountOfTokens.send_keys(Keys.BACKSPACE)
            # AmountOfTokens.send_keys(AmountOfTokensToBuy)
            print('SUCCESS: Amount to buy listed tokens is entered: ' + AmountOfTokensToBuy)
        except:
            print('FAILED: Could not enter amount of tokens to buy from listed tokens')
            raise Exception

        time.sleep(3)
        try:
            BuyNowButton=wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'action-btn')))
            BuyNowButton.click()
            print('SUCCESS: Buy now button is clicked')
        except:
            print('FAILED: Could not click buy now button')
            raise Exception

        time.sleep(10)

        try:
            time.sleep(5)
            loader = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay')))
            time.sleep(5)
            print('SUCCESS: Loader Disappeared')
        except:
            print('FAILED: Loader did not appear or still loading')

        try:
            TokensBoughtToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Toaster Appeared')
        except:
            print('FAILED: Toaster could not be appeared')

        if TokensBoughtToasterMessage.text == 'Tokens Bought Successfully':
            print('\nSUCCESS: TOKENS BOUGHT SUCCESSFULLY. Toaster Appeared having text: "'+TokensBoughtToasterMessage.text+'"\n')
        else:
            print('\nFAILED: Success toaster could not be appeared. Instead toaster with the text: "'+TokensBoughtToasterMessage.text+'" appeared\n')
            raise Exception

    def tearDown(self):
        time.sleep(3)
        self.driver.save_screenshot("list+buy.PNG")
        allure.attach.file(r"list+buy.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()