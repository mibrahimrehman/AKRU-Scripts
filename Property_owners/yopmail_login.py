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
#import allure
import variables
#from Login import PythonOrgSearch


class yopmail():

    def __init__(self , driver):
        self.driver = driver
        print("instanace generated")
    
    def run(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 120)

        driver.execute_script("window.open('http://www.yopmail.com', 'new window')")
        driver.switch_to.window(self.driver.window_handles[1])



        # try:
        #     email_text = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,  "#login")))
        #     email_text.click()
        #     print('SUCCESS:Email Text feild clicked')
        # except:
        #     print("FAILED:Email Text feild could not be clicked")
        #     raise Exception


        try:
            login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#login")))
            login.click()

            login.clear()

            login.send_keys(variables.emailhandler)
            login.send_keys(Keys.ENTER)
            print('SUCCESS: Email entered successfully')
            
        except:
            print("FAILED:Email could not be entered")
            raise Exception

        time.sleep(3)
        driver.refresh()
        time.sleep(5)

        try:
                driver.switch_to.frame('ifmail')
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



        time.sleep(10)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)