from seleniumwire import webdriver
import time
from selenium.webdriver.common.by import By

proxy_options = {
    'proxy': {
        'http': f'http://Addensure:Welcome123_country-in_streaming-1@geo.iproyal.com:12321',
        'https': f'http://Addensure:Welcome123_country-in_streaming-1@geo.iproyal.com:12321',
     
    }
}


driver = webdriver.Chrome(seleniumwire_options=proxy_options)
driver.get('http://httpbin.org/ip')
print(driver.find_element(By.TAG_NAME, 'body').text) 
time.sleep(60)

