# -*- coding: utf-8 -*-
from seleniumwire import webdriver
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import unittest, time, re
import random

# logging.basicConfig(filename='web_automation.log')
chrome_options = Options()
chrome_options.add_argument("--headless")

options_list = [
    "Select option",
    "Gainda",
    "Trishul",
    "Doctor",
    "Cross",
    "Cleanzo",
    "Lemonex",
    "Ozone",
    "White Tiger",
    "Floorosol",
    "Kirubas",
    "Other"
]

proxy_options = {
    'proxy': {
        'http': f'http://Addensure:Welcome123_country-in_streaming-1@geo.iproyal.com:12321',
        'https': f'http://Addensure:Welcome123_country-in_streaming-1@geo.iproyal.com:12321',
    
    }
}

def main():
    driver = webdriver.Chrome(seleniumwire_options=proxy_options ,options=chrome_options)
    try:     
        driver.get("https://track.adzmonk.com/click?pid=15&offer_id=887")    
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(2)
        driver.find_element(By.ID, "oppp").click()
        getRandom =random.choice(options_list)
        time.sleep(2)
        Select(driver.find_element(By.ID, "oppp")).select_by_visible_text(f'{getRandom}')
        time.sleep(2)
        driver.find_element(By.ID, "nominatebtn").click()
        driver.find_element(By.ID, "proceed_btn").click()
        driver.find_element(By.ID, "username").click()
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys("asdfasdf")
        driver.find_element(By.ID, "mobileno").click()
        driver.find_element(By.ID, "mobileno").clear()
        driver.find_element(By.ID, "mobileno").send_keys("9876543210")
        driver.find_element(By.ID, "submitentry_btn").click()
        time.sleep(5)
        driver.find_element(By.ID, "otplizol1").click()
        driver.find_element(By.ID, "otplizol1").clear()
        driver.find_element(By.ID, "otplizol1").send_keys("2")
        driver.find_element(By.ID, "otplizol2").clear()
        driver.find_element(By.ID, "otplizol2").send_keys("5")
        driver.find_element(By.ID, "otplizol3").clear()
        driver.find_element(By.ID, "otplizol3").send_keys("2")
        driver.find_element(By.ID, "otplizol4").clear()
        driver.find_element(By.ID, "otplizol4").send_keys("3")
        driver.find_element(By.ID, "otpsubmitentry_btn").click()
        time.sleep(16)
        element = driver.find_element(By.ID, "lizol_step_4")
        driver.execute_script("arguments[0].style.display = 'block';", element)
        time.sleep(5)
        driver.find_element(By.LINK_TEXT,"Redeem Now").click()
        with open('data.txt', 'w') as file:
            file.write('1')

        time.sleep(25)
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
for i in range(10000):
    main()

