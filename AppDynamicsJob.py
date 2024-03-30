# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import random

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

def main():
    try:
        driver = webdriver.Chrome()
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
        time.sleep(5)
        driver.quit()
    except Exception as e:
        print(str(e))
        driver.quit()
    finally:
        driver.quit()
main()

