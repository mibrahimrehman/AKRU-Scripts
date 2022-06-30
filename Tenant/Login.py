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
        PATH = "chromedriver"
        self.driver = webdriver.Chrome(PATH, options=chrome_options)

    def test_search_in_python_org(self):
        self.driver.maximize_window()
        url = "https://avaxdevtenants.akru.co/"
        fname = names.get_first_name()
        lname = names.get_last_name()
        email = fname + lname + '123@yopmail.com'
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


        log_in = self.driver.find_element(By.CSS_SELECTOR,
                                 "#navbar-header-sticky-login")
        log_in.click()

    # 3. Click 'Tenant portal'
        tenant_portal = self.driver.find_element(By.XPATH,
                                        "//button[. = 'Tenant portal']")
        tenant_portal.click()

    # 4. Click 'navbar-select-magic'
        navbar_select_magic = self.driver.find_element(By.CSS_SELECTOR,
                                              "#navbar-select-magic")
        navbar_select_magic.click()

     # 5. Click 'email'
        email = self.driver.find_element(By.CSS_SELECTOR,
                                "#navbar-magic-email")
        email.click()

    # 6. Type 'tenantav3@yopmail.com' in 'email'
        email = self.driver.find_element(By.CSS_SELECTOR,
                                "#navbar-magic-email")
        email.send_keys("tenantav3@yopmail.com")

    # 7. Click 'navbar-magic-next'
        navbar_magic_next = self.driver.find_element(By.CSS_SELECTOR,
                                            "#navbar-magic-next")
        navbar_magic_next.click()

    # 8. Switch to window '1'
        self.driver.execute_script("window.open('http://www.yopmail.com', 'new window')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        

    # 9. Navigate to 'https://yopmail.com/'
        self.driver.get("https://yopmail.com/")

    # 10. Click 'login'
        login = self.driver.find_element(By.CSS_SELECTOR,
                                "#login")
        login.click()

    # 11. Type 'tenantav3@yopmail.com' in 'login'
        login = self.driver.find_element(By.CSS_SELECTOR,
                                "#login")
        login.send_keys("tenantav3@yopmail.com")

    # 12. Send 'ENTER' key(s)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    # 13. Click 'Log in to Akru TestNet'
    # Step switches frame driver context.
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(
        self.driver.find_element(By.XPATH,
                            "//*[@id = 'ifmail']|//*[@name = 'ifmail']|/html/body/div[1]/div/main/div[2]/div[3]/div/div[1]/iframe"))
        log_in_to_akru_testnet = self.driver.find_element(By.XPATH,
                                                 "//strong[. = 'Log in to Akru TestNet']")
        log_in_to_akru_testnet.click()

    # 14. Switch to window '2'
        self.driver.switch_to.window(self.driver.window_handles[2])

    # 15. Switch to window '0'
        self.driver.switch_to.window(self.driver.window_handles[0])

    # 16. Is 'Dashboard' present?
        dashboard = self.driver.find_element(By.CSS_SELECTOR,
                                        "#navbar-header-sticky-dashboard")

    # 17. Scroll window by ('0','554')
        self.driver.execute_script("window.scrollBy(0,554)")
        
        
        
    def tearDown(self):
        time.sleep(3)
        self.driver.save_screenshot("entsig.PNG")
        allure.attach.file(r"entsig.PNG", "screenshot",attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
