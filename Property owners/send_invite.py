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


class Test_login(unittest.TestCase):
    
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

        

    def test_search_in_python_org_login(self):
        print("Now i am in login")
        #driver = gdriver
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
        wait = WebDriverWait(self.driver, 80)

        
        try:
            submityourproperty=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[. = ' Allow selection ']")))
            submityourproperty.click()
            print('SUCCESS: Submit your property button clicked')
        except:
            print("FAILED: Submit your property button could not be clicked")
            raise Exception

        driver.execute_script("window.scrollBy(0,248)")

        # 4. Scroll window by ('0','3498')
        driver.execute_script("window.scrollBy(0,3498)")

        # 5. Scroll window by ('0','-196')
        driver.execute_script("window.scrollBy(0,-196)")

        # 6. Scroll window by ('0','-117')
        driver.execute_script("window.scrollBy(0,-117)")

    

        # try:
        #     start=wait.until(EC.element_to_be_clickable((By.XPATH ,'//button[@data-qa="start-button"]')))
        #     start.click()
        #     print('SUCCESS: Start button clicked')
        # except:
        #     print("FAILED: Start button could not be clicked")
        #     raise Exception
        

        
        
        # try:
        #     officetype=wait.until(EC.element_to_be_clickable((By.XPATH ,'//div[@data-qa-index="3"]')))
        #     officetype.click()
        #     print('SUCCESS: Office type property clicked')
        # except:
        #     print("FAILED: Office type property button could not be clicked")
        #     raise Exception


        # try:
        #     stabilized=wait.until(EC.element_to_be_clickable((By.XPATH ,"//div[@class='TextWrapper-sc-__sc-1f8vz90-0 bFxsfa'][text()='Stabilized Income']")))
        #     stabilized.click()
        #     print('SUCCESS: Stabilized income type clicked')
        # except:
        #     print("FAILED: stabilized income type could not be clicked")
        #     raise Exception


        # try:
        #     address=wait.until(EC.element_to_be_clickable((By.XPATH ,'//input[@type="text"][@autocomplete="name"]')))
        #     address.click()
        #     address.send_keys("california")
        #     print('SUCCESS: Address Entered Successfully')
        # except:
        #     print("FAILED: Address could not be Entered")
        #     raise Exception




        # 3. Scroll window by ('0','248')
        # driver.execute_script("window.scrollBy(0,248)")

        # # 4. Scroll window by ('0','3498')
        # driver.execute_script("window.scrollBy(0,3498)")

        # # 5. Scroll window by ('0','-196')
        # driver.execute_script("window.scrollBy(0,-196)")

        # # 6. Scroll window by ('0','-117')
        # driver.execute_script("window.scrollBy(0,-117)")

        # 7. Click 'submit-form'
        try:
            submityourproperty=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='submit-form']")))
            submityourproperty.click()
            print('SUCCESS: Submit Your property button clicked')
        except:
            print("FAILED: Submit your property button could not be clicked")
            raise Exception
        # submit_form = driver.find_element(By.CSS_SELECTOR,
        #                                 "[name='submit-form']")
        # submit_form.click()
        
        # 8. Click 'Start'
        # Step switches frame driver context.


        try:
            time.sleep(10)
            submityourproperty=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@data-qa="iframe"]')))
            start = wait.until(EC.visibility_of_element_located((By.XPATH,"//button[. = 'Start']")))
            start.click()
            print('SUCCESS: Start button clicked successfully')
        except:
            print("FAILED: Start button could not be clicked")
            raise Exception
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # start = driver.find_element(By.XPATH,
        #                             "//button[. = 'Start']")
        # start.click()

        # 9. Click 'Office'
        # Step switches frame driver context.
        try:
            #driver.switch_to.default_content()
            #officeproperty=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[3]/div/div[2]/iframe")))
            office = wait.until(EC.visibility_of_element_located((By.XPATH,
                                    "//div[2]/div[. = 'Office']")))
            # driver.find_element(By.XPATH,
            #                         "//div[2]/div[. = 'Office']")
            office.click()
            print('SUCCESS: Office type button clicked successfully')
        except:
            print("FAILED: Office button could not be clicked")
            raise Exception


        
        try:
            
            #driver.switch_to.default_content()
            #officeproperty=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[3]/div/div[2]/iframe")))
            office = wait.until(EC.visibility_of_element_located((By.XPATH,
                                    "//div[text() = 'Stabilized Income']")))
            #driver.find_element(By.XPATH,
             #                       "//div[2]/div[. = 'Stabilized Income']")
            office.click()
            print('SUCCESS: Stabilized Income button clicked successfully')
        except:
            print("FAILED: Stabilized Income button could not be clicked")
            raise Exception



        try:
        
            #driver.switch_to.default_content()
            #officeproperty=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[3]/div/div[2]/iframe")))
            name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                "[name='name']")))
            # driver.find_element(By.CSS_SELECTOR,
            #                     "[name='name']")
            name.click()
            name.send_keys("california")

            print('SUCCESS: Address entered successfully')
        except:
            print("FAILED: Address could not be entered")
            raise Exception
        
        try:
            #driver.switch_to.default_content()
            #officeproperty=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[3]/div/div[2]/iframe")))
            okbutton=wait.until(EC.presence_of_element_located((By.XPATH,"//div[2]/section//button[. = 'OK']")))
            okbutton.click()
            print('SUCCESS: OK button clicked successfully')
        except:
            print("FAILED: OK button could not be clicked")
            raise Exception

        # 13. Click 'OK'
        # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # ok = driver.find_element(By.XPATH,
        #                         "//div[2]/section//button[. = 'OK']")
        # ok.click()

        # 14. Click 'name'
        # Step switches frame driver context.

        try:
            #driver.switch_to.default_content()
            #officeproperty=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[3]/div/div[2]/iframe")))
            name = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@ inputmode="numeric"]')))
            #driver.find_element(By.XPATH , '//input[@ inputmode="numeric"]')
                               
            name.click()
            name.send_keys("22000")

            print('SUCCESS: Zip Code entered successfully')
        except:
            print("FAILED: Zip code could not be entered")
            raise Exception



    #      driver.switch_to.default_content()
    # driver.switch_to.frame(
    #     driver.find_element(By.XPATH,
    #                         "/html/body/div[3]/div/div[2]/iframe"))
    # name = driver.find_element(By.CSS_SELECTOR,
    #                            "[name='name']")
    # name.send_keys("22000")
       

        try:
            #driver.switch_to.default_content()
            okbutton=wait.until(EC.presence_of_element_located((By.XPATH,"//div[2]/section//button[. = 'OK']")))
            okbutton.click()
            print('SUCCESS: OK button clicked successfully')
        except:
            print("FAILED: OK button could not be clicked")
            raise Exception

        # 16. Click 'OK'
        # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # ok = driver.find_element(By.XPATH,
        #                         "//div[2]/section//button[. = 'OK']")
        # ok.click()



        try:
            #driver.switch_to.default_content()
            #officeproperty=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[3]/div/div[2]/iframe")))
            name = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@type='text'][@class='InputField-sc-__sc-26uh88-0 gddNmG']")))
            # driver.find_element(By.CSS_SELECTOR,
            #                     "[name='name']")
            name.click()
            name.send_keys("california")

            print('SUCCESS: Address entered successfully')
        except:
            print("FAILED: Address could not be entered")
            raise Exception
        
        try:
            okbutton=wait.until(EC.presence_of_element_located((By.XPATH,"//div[2]/section//button[. = 'OK']")))
            okbutton.click()
            print('SUCCESS: OK button clicked successfully')
        except:
            print("FAILED: OK button could not be clicked")
            raise Exception
        # 17. Click 'name'
        # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # name = driver.find_element(By.CSS_SELECTOR,
        #                         "[name='name']")
        # name.click()

        # # 18. Click 'name'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # name = driver.find_element(By.CSS_SELECTOR,
        #                         "[name='name']")
        # name.click()

        # # 19. Type 'california' in 'name'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # name = driver.find_element(By.CSS_SELECTOR,
        #                         "[name='name']")
        # name.send_keys("california")

        # # 20. Click 'OK'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # ok = driver.find_element(By.XPATH,
        #                         "//div[2]/section//button[. = 'OK']")
        # ok.click()


        try:
            #driver.switch_to.default_content()
            #officeproperty=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[3]/div/div[2]/iframe")))
            name = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@type='text'][@class='InputField-sc-__sc-26uh88-0 gddNmG']")))
            # driver.find_element(By.CSS_SELECTOR,
            #                     "[name='name']")
            name.click()
            name.send_keys("United states")

            print('SUCCESS: Country entered successfully')
        except:
            print("FAILED: Country could not be entered")
            raise Exception
        
        try:
            okbutton=wait.until(EC.presence_of_element_located((By.XPATH,"//div[2]/section//button[. = 'OK']")))
            okbutton.click()
            print('SUCCESS: OK button clicked successfully')
        except:
            print("FAILED: OK button could not be clicked")
            raise Exception
        # 21. Click 'name'
        # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # name = driver.find_element(By.CSS_SELECTOR,
        #                         "[name='name']")
        # name.click()

        # # 22. Type 'united states' in 'name'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # name = driver.find_element(By.CSS_SELECTOR,
        #                         "[name='name']")
        # name.send_keys("united states")

        # # 23. Click 'OK'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # ok = driver.find_element(By.XPATH,
        #                         "//div[2]/section//button[. = 'OK']")
        # ok.click()

        try:
            #time.sleep(4)
            #driver.switch_to.default_content()
            #officeproperty=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[3]/div/div[2]/iframe")))
            name = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@type='text'][@class='InputField-sc-__sc-26uh88-0 gddNmG']")))
            name.click()
            name.send_keys("Ibrahim")

            print('SUCCESS: First name entered successfully')
        except:
            print("FAILED: First name could not be entered")
            raise Exception
        
        try:
            
            okbutton=wait.until(EC.presence_of_element_located((By.XPATH,"//div[2]/section//button[. = 'OK']")))
            okbutton.click()
            print('SUCCESS: OK button clicked successfully')
        except:
            print("FAILED: OK button could not be clicked")
            raise Exception
        # 24. Click 'name'
        # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # name = driver.find_element(By.CSS_SELECTOR,
        #                         "[name='name']")
        # name.click()

        # # 25. Type 'ibrahim' in 'name'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # name = driver.find_element(By.CSS_SELECTOR,
        #                         "[name='name']")
        # name.send_keys("ibrahim")

        # # 26. Click 'OK'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # ok = driver.find_element(By.XPATH,
        #                         "//div[2]/section//button[. = 'OK']")
        # ok.click()



        try:
            #driver.switch_to.default_content()
            #officeproperty=wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,
            name = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@type='text'][@class='InputField-sc-__sc-26uh88-0 gddNmG']")))
            name.click()
            name.send_keys("Rehman")

            print('SUCCESS: Last name entered successfully')
        except:
            print("FAILED: Last name could not be entered")
            raise Exception
        
        try:
            #time.sleep(4)
            okbutton=wait.until(EC.presence_of_element_located((By.XPATH,"//div[2]/section//button[. = 'OK']")))
            okbutton.click()
            print('SUCCESS: OK button clicked successfully')
        except:
            print("FAILED: OK button could not be clicked")
            raise Exception
        # 27. Click 'name'
        # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # name = driver.find_element(By.CSS_SELECTOR,
        #                         "[name='name']")
        # name.click()

        # # 28. Type 'rehman' in 'name'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # name = driver.find_element(By.CSS_SELECTOR,
        #                         "[name='name']")
        # name.send_keys("rehman")

        # # 29. Click 'OK'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # ok = driver.find_element(By.XPATH,
        #                         "//div[2]/section//button[. = 'OK']")
        # ok.click()



        # 30. Click 'email2'
        # Step switches frame driver context.

        try:
            name = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='name@example.com']")))
            name.click()
            name.send_keys(variables.email)

            print('SUCCESS: email entered successfully')
        except:
            print("FAILED: Email could not be entered")
            raise Exception
        
        try:
            okbutton=wait.until(EC.presence_of_element_located((By.XPATH,"//div[2]/section//button[. = 'OK']")))
            okbutton.click()
            print('SUCCESS: OK button clicked successfully')
        except:
            print("FAILED: OK button could not be clicked")
            raise Exception
        
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # email2 = driver.find_element(By.CSS_SELECTOR,
        #                             "[name='email']")
        # email2.click()

        # # 31. Type 'ibrahimpo16@yopmail.com' in 'email2'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # email2 = driver.find_element(By.CSS_SELECTOR,
        #                             "[name='email']")
        # email2.send_keys("ibrahimpo16@yopmail.com")

        # # 32. Click 'OK'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # ok = driver.find_element(By.XPATH,
        #                         "//div[2]/section//button[. = 'OK']")
        # ok.click()

        # 33. Click 'tel'
        # Step switches frame driver context.

        try:
            #time.sleep(4)
            name = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@type='tel']")))
            name.click()
            name.send_keys(variables.number)

            print('SUCCESS: Number entered successfully')
        except:
            print("FAILED: Number could not be entered")
            raise Exception
        
        try:
            #time.sleep(4)
            submitbutton=wait.until(EC.presence_of_element_located((By.XPATH,"//button[. = 'Submit']")))
            submitbutton.click()
            print('SUCCESS: Submit button clicked successfully')
        except:
            print("FAILED: Submit button could not be clicked")
            raise Exception

        # try:
        #     LoginToasterMessage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body')))
        #     print('SUCCESS: Toaster Appeared')
        #     toasterappear = True
        # except:
        #     print('FAILED: Toaster could not be appeared')

        # try:
        #     if toasterappear:
        #         if LoginToasterMessage.text == 'Successfully submitted property':
        #             print('\nSUCCESS: Send Invite successfully. Toaster Appeared having text: "'+LoginToasterMessage.text+'"\n')
        #         else:
        #             print('\nFAILED: Invite could not be sended. Instead toaster with the text: "'+LoginToasterMessage.text+'" appeared\n')
        #             raise Exception
        # except:
        #     print("FAILED: Toaster could not be appered")

        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # tel = driver.find_element(By.CSS_SELECTOR,
        #                         "#VFiOY7E8Hfzr")
        # tel.click()

        # # 34. Type '(201) 555-389' in 'tel'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # tel = driver.find_element(By.CSS_SELECTOR,
        #                         "#VFiOY7E8Hfzr")
        # tel.send_keys("(201) 555-389")

        # # 35. Click 'Submit'
        # # Step switches frame driver context.
        # driver.switch_to.default_content()
        # driver.switch_to.frame(
        #     driver.find_element(By.XPATH,
        #                         "/html/body/div[3]/div/div[2]/iframe"))
        # submit = driver.find_element(By.XPATH,
        #                             "//button[. = 'Submit']")
        # submit.click()


        
    def tearDown(self):
        time.sleep(3)
        self.driver.save_screenshot("entsig.PNG")
        allure.attach.file(r"entsig.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
