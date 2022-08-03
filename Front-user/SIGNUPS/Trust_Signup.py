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
from PIL import Image
import allure

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
        #self.driver = webdriver.Chrome(PATH, options=chrome_options)

    def test_search_in_python_org(self):
        self.driver.maximize_window()
        url = "https://avaxdev.akru.co"
        fname = names.get_first_name()
        lname = names.get_last_name()
        email = fname + lname + '123@yopmail.com'
        print("Email generated for signup is: " , email)
        phone_no = '5678956789'
        fnameRep = names.get_first_name()
        lnameRep = names.get_last_name()
        emailRep = fnameRep+lnameRep+'123@yopmail.com'

        action = ActionChains (self.driver)
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
            loginButton=wait.until(EC.element_to_be_clickable((By.ID,"navbar-header-sticky-starter")))
            loginButton.click()
            print('SUCCESS: Get Started button clicked')
        except:
            print("FAILED: Get Started button could not be clicked")
            raise Exception

        try:
            yesAccreditedInvestor=wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'check-label')))
            yesAccreditedInvestor.click()
            print('SUCCESS: Yes selected for "Are you an accredited investor?"')
        except:
            print('FAILED: Yes could not be selected for "Are you an accredited investor?"')
            raise Exception

        try:
            continueAccreditedInvestor=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="primary-btn"][text()="Continue"]')))
            continueAccreditedInvestor.click()
            print('SUCCESS: Continue button clicked for "Are you an accredited investor?"')
        except:
            print('FAILED: Continue button could not be clicked for "Are you an accredited investor?"')
            raise Exception

        try:
            starterPackageSelect=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Select this plan"]')))
            starterPackageSelect.click()
            print('SUCCESS: Select this plan button is clicked for starter packages')
        except:
            print("FAILED: Select this plan button could not be clicked for starter packages")
            raise Exception

    

        try:
            fnameToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name = "firstName"]')))
            fnameToBeEntered.send_keys(fname)
            print('SUCCESS: First name is entered')
        except:
            print("FAILED: First name could not be entered")
            raise Exception

        try:
            lnameToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name = "lastName"]')))
            lnameToBeEntered.send_keys(lname)
            print('SUCCESS: Last name is entered')
        except:
            print("FAILED: Last name could not be entered")
            raise Exception

        try:
            emailToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name = "email"]')))
            emailToBeEntered.send_keys(email)
            print('SUCCESS: Email is entered')
        except:
            print("FAILED: Email could not be entered")
            raise Exception

        try:
            phnoToBeEntered=wait.until(EC.element_to_be_clickable((By.ID,'signup-phone')))
            phnoToBeEntered.click()
            clearTextField()
            phnoToBeEntered.send_keys(phone_no)
            print('SUCCESS: Phone number is entered')
        except:
            print("FAILED: Phone number could not be entered")
            raise Exception

        try:
            agreeTermsAndPrivacy=wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'check-label')))
            agreeTermsAndPrivacy.click()
            print("SUCCESS: To agree to AKRU's terms and privacy policy Checkbox clicked")
        except:
            print("FAILED: To agree to AKRU's terms and privacy policy Checkbox could not be clicked")
            raise Exception

        try:
            selectingTrustRadioButton=wait.until(EC.visibility_of_element_located((By.XPATH,'//span[text()="Trust"]')))
            selectingTrustRadioButton.click()
            print('SUCCESS: Trust Radio Button is clicked')
        except:
            print("FAILED: Trust Radio Button could not be clicked")
            raise Exception

        try:
            agreeAndContinueToSendSignupEmail=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="primary-btn mr-1 "]')))
            agreeAndContinueToSendSignupEmail.click()
            print('SUCCESS: Agree & Continue button clicked')
        except:
            print("FAILED: Could not click Agree & Continue button")
            raise Exception

        try:
            modalWhenEmailisSent=wait.until(EC.visibility_of_element_located((By.XPATH,'//h5[@class="title"]')))
            print("SUCCESS: 'Verify Your Email' modal appeared")
        except:
            print("FAILED: 'Verify Your Email' modal could not be appeared")
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
                wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH , "//iframe[@name='ifmail']")))
            except:
                print("FAILED: Could not switch to iframe in YOPMAIL.")
                raise Exception

            try:
                time.sleep(3)
                LoginEmailButton=wait.until(EC.element_to_be_clickable((By.XPATH,'//b[text()="Verify Email"]')))
                LoginEmailButton.click()
                print('SUCCESS: "Verfy Email" button clicked from YOPMAIL')
            except:
                print('FAILED: Could not click "Verify Email" button. Possibly due to captcha.')
                raise Exception

        emailLogin()

        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)

        try:
            TrustNameToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="trustName"]')))
            TrustNameToBeEntered.send_keys(fname+"'s Trust")
            print('SUCCESS: Trust Name is entered')
        except:
            print("FAILED: Trust name could not be entered")
            raise Exception

        try:
            trustClassificationToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//select[@name="trustClassification"]')))
            trustClassificationToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH, '//select[@name="trustClassification"]//option[@value="Grantor"]'):
                if option.text == 'Grantor':
                    option.click()
                    break
            print('SUCCESS: Trust Classification selected from dropdown')
        except:
            print("FAILED: Trust Classification could not be selected from dropdown")
            raise Exception

        try:
            trustTypeToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//select[@name="trustType"]')))
            trustTypeToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH, '//select[@name="trustType"]//option[@value="Revocable"]'):
                if option.text == 'Revocable':
                    option.click()
                    break
            print('SUCCESS: Trust Type selected from dropdown')
        except:
            print("FAILED: Trust Type could not be selected from dropdown")
            raise Exception

        try:
            IndustryToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//select[@name="industry"]')))
            IndustryToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH, '//select[@name="industry"]//option[@value="Gourmet foods"]'):
                if option.text == 'Gourmet foods':
                    option.click()
                    break
            print('SUCCESS: Industry selected from dropdown')
        except:
            print("FAILED: Industry could not be selected from dropdown")
            raise Exception

        try:
            StateToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//select[@name="juristdiction"]')))
            StateToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH,'//select[@name="juristdiction"]//option[@value="Ohio"]'):
                if option.text == 'Ohio':
                    option.click()
                    break
            print('SUCCESS: State selected from dropdown')
        except:
            print("FAILED: State could not be selected from dropdown")
            raise Exception

        try:
            EINToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="tinNumber"]')))
            EINToBeEntered.send_keys('123456789')
            print('SUCCESS: EIN Number is entered')
        except:
            print("FAILED: EIN number could not be entered")
            raise Exception

        try:
            TrustAgreementToBeUploaded=self.driver.find_element(By.XPATH, '//div[1]/input[@type="file"]')
            filepath = os.path.abspath("blank.pdf")
            TrustAgreementToBeUploaded.send_keys(filepath)
            # TrustAgreementToBeUploaded.send_keys("/Users/qualityassurance/Desktop/automation-scripts/AVAXDEV_SHAHWAR/blank.pdf")
            print('SUCCESS: Trust agreement is uploaded')
        except:
            print("FAILED: Trust agreement could not be uploaded")
            raise Exception

        try:
            BusinessIDdocToBeUploaded=self.driver.find_element(By.XPATH, '//div[3]/input[@type="file"]')
            BusinessIDdocToBeUploaded.send_keys(filepath)
            # BusinessIDdocToBeUploaded.send_keys("/Users/qualityassurance/Desktop/automation-scripts/AVAXDEV_SHAHWAR/blank.pdf")
            print('SUCCESS: Business Identification Document is uploaded')
        except:
            print("FAILED: Business Identification Document could not be uploaded")
            raise Exception

        try:
            addressToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="address"]')))
            addressToBeEntered.click()
            clearTextField()
            addressToBeEntered.send_keys('3825 Edwards Rd #103, Cincinnati, OH 45244, USA')
            time.sleep(2)
            addressToBeEntered.send_keys(Keys.RETURN)
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
            titleToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//select[@name="title"]')))
            titleToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH, '//select[@name="title"]//option[@value="CTO"]'):
                if option.text == 'CTO':
                    option.click()
                    break
            print("SUCCESS: Title 'CTO' is selected from dropdown")
        except:
            print("FAILED: Title 'CTO' could not be selected from dropdown")
            raise Exception

        try:
            fnameToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name = "firstName"]')))
            fnameToBeEntered.click()
            clearTextField()
            fnameToBeEntered.send_keys(fnameRep)
            print('SUCCESS: First name is entered')
        except:
            print("FAILED: First name could not be entered")
            raise Exception

        try:
            lnameToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name = "lastName"]')))
            lnameToBeEntered.click()
            clearTextField()
            lnameToBeEntered.send_keys(lnameRep)
            print('SUCCESS: Last name is entered')
        except:
            print("FAILED: Last name could not be entered")
            raise Exception

        try:
            emailToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name = "email"]')))
            emailToBeEntered.click()
            clearTextField()
            emailToBeEntered.send_keys(emailRep)
            print('SUCCESS: Email is entered')
        except:
            print("FAILED: Email could not be entered")
            raise Exception

        try:
            addressToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name = "address1"]')))
            addressToBeEntered.click()
            clearTextField()
            addressToBeEntered.send_keys(emailRep)
            print('SUCCESS: Address is entered')
        except:
            print("FAILED: Address could not be entered")
            raise Exception

        try:
            RepPersonalIDToBeUploaded=self.driver.find_element(By.XPATH, "//input[@type='file'][@accept='image/png,image/jpg,image/jpeg']")
            # RepPersonalIDToBeUploaded.send_keys("/var/lib/jenkins/script/blank.png")
            pngfilepath = os.path.abspath("blank.png")
            RepPersonalIDToBeUploaded.send_keys(pngfilepath)
            print('SUCCESS: Representative Personal Identification is uploaded')
        except:
            print("FAILED: Representative Personal Identification could not be uploaded")
            raise Exception

        try:
            CityOfRepToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="city2"]')))
            CityOfRepToBeEntered.click()
            clearTextField()
            CityOfRepToBeEntered.send_keys('Cincinnati')
            print('SUCCESS: City of Representative is entered')
        except:
            print("FAILED: City of Representative could not be entered")
            raise Exception

        try:
            StateofRepToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//select[@name="state2"]')))
            StateofRepToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH,'//select[@name="state2"]//option[@value="Ohio"]'):
                if option.text == 'Ohio':
                    option.click()
                    break
            print('SUCCESS: State of Representative selected from dropdown')
        except:
            print("FAILED: State of Representative could not be selected from dropdown")
            raise Exception

        try:
            zipCodeofRepToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="postalCode"]')))
            zipCodeofRepToBeEntered.click()
            clearTextField()
            zipCodeofRepToBeEntered.send_keys('45209')
            print('SUCCESS: Zip code is entered')
        except:
            print("FAILED: Zip code could not be entered")
            raise Exception

        try:
            SSNToBeEntered=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@type="password"]')))
            SSNToBeEntered.send_keys('123456789')
            print('SUCCESS: SSN is entered')
        except:
            print("FAILED: SSN could not be entered")
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
        self.driver.get('https://avaxdevapi.akru.co/api/user/showOtp/'+email)
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
            dobToBeEntered.send_keys('11/07/2001')
            print('SUCCESS: Date of Birth is entered')
        except:
            print("FAILED: Could not enter date of birth")
            raise Exception
        time.sleep(8)
        try:
            continueButtonAfterStep2Completion=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="primary-btn mr-1"]')))
            continueButtonAfterStep2Completion.click()
            print('SUCCESS: Continue button is clicked after filling the form on step 2')
        except:
            print("FAILED: Continue button could not be clicked after filling the form on step 2")
            raise Exception




        try:
            stateToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@id="investor-purpose"]')))
            stateToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH, '//li[@data-value="capitalAppreciation"]'):
                #if option.text == 'Ohio'
                if True:
                    option.click()
                    break
            print("SUCCESS: investor purpose , Capital Appreciation Supported is selected")
        except:
            print("FAILED: investor purpose , Capital Appreciation Supported is not selected")
            raise Exception
    
        
        
        try:
            stateToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@id="isTradingLowSecurities"]')))
            stateToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH, '//li[@data-value="true"]'):
                #if option.text == 'Ohio'
                if True:
                    option.click()
                    break
            print("SUCCESS: Low trade volume , yes is selected")
        except:
            print("FAILED: Low trade volume , yes is not selected")
            raise Exception


        try:
            stateToBeSelected=wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@id="employmentStatus"]')))
            stateToBeSelected.click()
            for option in self.driver.find_elements(By.XPATH, "//li[@data-value='unemployed']"):
                #if option.text == 'Ohio'
                if True:
                    option.click()
                    break
            print("SUCCESS: Employement status , unemployed is selected")
        except:
            print("FAILED: Employement status , unemployed is not selected")
            raise Exception
        

        try:
            skipAddingBankButton=wait.until(EC.visibility_of_element_located((By.XPATH,'//button[text()="Next"]')))
            skipAddingBankButton.click()
            print('SUCCESS: Next button of account detail is clicked')
        except:
            print("FAILED:  Next button of account detail could not be clicked")
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
            checkingAgreement3=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="point4"]')))
            checkingAgreement3.click()
            print('SUCCESS: Agreement 4 checked')
        except:
            print("FAILED: Agreement 4 could not be checked")
            raise Exception

        try:
            checkingAgreement3=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="point5"]')))
            checkingAgreement3.click()
            print('SUCCESS: Agreement 5 checked')
        except:
            print("FAILED: Agreement 5 could not be checked")
            raise Exception

        try:
            ContinueButtonAfterCheckingAgreements=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="primary-btn ml-auto d-block"]')))
            ContinueButtonAfterCheckingAgreements.click()
            print('SUCCESS: Continue button clicked after checking all 3 agreements')
        except:
            print("FAILED: Continue button could not be clicked after checking all 3 agreements")
            raise Exception

        time.sleep(5)



        try:
            esignature=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@name="eSignature"]')))
            esignature.click()
            esignature.send_keys(fname + lname)
            print('SUCCESS: Esignature is signed')
        except:
            print("FAILED: Esignature could not be signed")
            raise Exception


        try:
            VerifyInfoButtonAtStep5=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="primary-btn ml-auto d-block"]')))
            VerifyInfoButtonAtStep5.click()
            print('SUCCESS: Verify button at step 5 is clicked')
        except:
            print("FAILED: Verify button at step 5 could not be clicked")
            raise Exception

        time.sleep(20)
        try:
            createConnectWalletButton=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[@class="primary-btn ml-auto d-block"]')))
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
                wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH , "//iframe[@name='ifmail']")))
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
            OKButtonAfterSignUpCompletion=wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Ok"]')))
            OKButtonAfterSignUpCompletion.click()
            print('SUCCESS: OK button after signup completion is clicked')
        except:
            print('FAILED: OK button after signup completion could not be clicked')
            raise Exception

        try:
            LoginToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
            print('SUCCESS: Toaster Appeared')
        except:
            print('FAILED: Toaster could not be appeared')

        if LoginToasterMessage.text == 'Registered successfully!':
            print('\nSUCCESS: SUCCESSFULLY LOGGED IN. Toaster Appeared having text: "'+LoginToasterMessage.text+'"\n')
        else:
            print('\nFAILED: Success toaster could not be appeared. Instead toaster with the text: "'+LoginToasterMessage.text+'" appeared\n')
            raise Exception

        print('\nSUCCESSFULLY SINGED UP TRUST ACCOUNT\n' + "Email: " + email)

    def tearDown(self):
        self.driver.save_screenshot("trustsig.PNG")
        allure.attach.file(r"trustsig.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
