import requests
import re

#import imp
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





class emailapi:

    def __init__(self , driver):
        self.driver = driver
        print("instanace generated")

    def fetchlink(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 120)

        url = "https://mailsac.com/api/addresses/ibrahim@mailsac.com/messages"



        x = requests.get(url, headers = {"Mailsac-Key": "k_ERVRFvh4EaskK6QTm93EkbsgPCtqvf1Ad" })
        y = x.json()
        print(y[0])
        lenthofmails = len(y)
        print(lenthofmails)
        i = 0
        stringlink = None
        while i < lenthofmails:
            z = y[i]
            #print("value of i is: ", i)
            a = z['from']
            id = z['_id']
            datntime = z['received']
            print(datntime)
            #print(a)
            #print(type(a[0]))
            k = a[0]
            target = k['address']
            print(target)
            if target== "noreply@trymagic.com":
                print("######################## INSIDE IF ######################")
                #print(target)
                tnum = i
                print(id)




                url2 = "https://mailsac.com/api/text/ibrahim@mailsac.com/" + id
                tex = requests.get(url2, headers = {"Mailsac-Key": "k_ERVRFvh4EaskK6QTm93EkbsgPCtqvf1Ad" })
                ty = tex.text
                print(ty)
                linktolgin  = re.search("(https:.*factor=)\B", ty)
                print("############################ Link text ################")
                stringlink  = str(linktolgin[0])


                # url3 = "https://mailsac.com/api/addresses/ibrahim@mailsac.com/messages/" + id
                # delc = requests.delete(url3, headers = {"Mailsac-Key": "k_ERVRFvh4EaskK6QTm93EkbsgPCtqvf1Ad"})
                # print(delc)

            else:
                print("FAILED: Email not found")


            i = i + 1
        
        driver.switch_to.new_window('tab')
        # driver.execute_script('''window.open(stringlink,"_blank");''')
        # #driver.execute_script("window.open("stringlink", 'new window')")
        # driver.switch_to.window(self.driver.window_handles[1])
        driver.get(stringlink)
        print('SUCCESS: "'+url+'" saved in webdriver')

        time.sleep(10)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)

