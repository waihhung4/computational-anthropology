from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.wpewebkit import By

from database import get_all_url
from model import Url
import random
import time
from bs4 import BeautifulSoup
from constants import Constant

# url_table_list = get_all_url()
# for i in url_table_list:
#     print(i['url'])



def login_quora(driver: WebDriver, email: str, password: str):
    email_input = driver.find_element(by=By.ID, value = 'email')
    password_input = driver.find_element(by=By.ID, value='password')
    login_button = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button')
    
    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()
    
    
def expand_replies(driver: WebDriver, button: WebElement):
    for i in range(len(content_button)):
        try:
            if i == 0:
                continue
            content_button[i].click()
            time.sleep(random.uniform(1,2))
            break
        except:
            pass
    
login_url = "https://www.quora.com/"
url = "https://www.quora.com/Is-there-any-way-to-transform-a-low-resolution-image-to-quality-high-resolution"

chrome_options = Options()
chrome_options.add_argument("--log-level=3") 

driver = webdriver.Chrome(options=chrome_options)
driver.get(login_url)

login_quora(driver, Constant.LOGIN_EMAIL, Constant.LOGIN_PASSWORD)
driver.get(url)

content_list = driver.find_elements(By.XPATH, '//*[@id="mainContent"]/div[3]/div')
span_list = []

for content in content_list:
    content_button = content.find_elements(By.TAG_NAME, "button")
    
    expand_replies(driver, content_button)
        
    input("Go")

    
# print(len(span_list))
time.sleep(random.uniform(1,3))
driver.quit()