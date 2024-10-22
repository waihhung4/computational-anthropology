from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

import pickle
from database import get_all_url
from model import Url
import random
import time
from bs4 import BeautifulSoup
from constants import Constant
from common import expand_replies, xpath_patterns

# xpath_patterns = [
#         'div/div/div/div/div[1]/div[2]/div/   div[1]/div[2]/div/div/span',
#         'div/div/div/div/div[1]/div[2]/div/div[1]/div[3]/div/div/span',
#         'div/div/div/div/div[2]/div/div[1]/div[3]/div/div/span/span',
#         'div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/span'
#         'div/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div/span/span',
#     ]

def login_quora(driver: WebDriver, email: str, password: str):
    
    email_input = driver.find_element(by=By.ID, value='email')
    password_input = driver.find_element(by=By.ID, value='password')
    login_button = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button')
    
    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()
    
    time.sleep(random.uniform(2, 3))


# # for text "more"
# def expand_replies(driver: WebDriver, content: WebElement):
#     content_list = driver.find_elements(By.XPATH, '//*[@id="mainContent"]/div[3]/div')

    
#     for content in content_list:
#         found = False
#         for xpath in xpath_patterns:
#             try:
#                 temp_element = content.find_element(By.XPATH, xpath)
#                 a = temp_element.find_elements(By.TAG_NAME, 'span')[-1]
#                 a.click()
#                 found = True  # Element found and clicked
#                 break  # Exit the loop once the element is clicked
#             except Exception as e:
#                 print(f"XPath '{xpath}' failed: {e}")
#                 continue

#         if not found:
#             print("No valid element found for this content.")

login_url = "https://www.quora.com/"
url = "https://www.quora.com/Could-Chinese-characters-have-been-developed-from-or-inspired-by-the-Sumerian-writing-system"

chrome_options = Options()
chrome_options.add_argument("--log-level=3") 

driver = webdriver.Chrome(options=chrome_options)   
driver.get(login_url)
    
    # Log in to Quora
login_quora(driver, Constant.LOGIN_EMAIL, Constant.LOGIN_PASSWORD)


driver.get(url)

content_list = driver.find_elements(By.XPATH, '//*[@id="mainContent"]/div[3]/div')


span_list = []

expand_replies(driver)
input("-------------------------------------------------")

for content in content_list:
    
    
    try:
        
        temp_element = None
        
        for xpath in xpath_patterns:
            try:
                temp_element = content.find_element(By.XPATH, xpath)
                if temp_element:
                    break
            except Exception as e:
                print(f"XPath '{xpath}' failed: {e}")
                continue
        
        span_element_list = temp_element.find_elements(By.TAG_NAME, 'span')
        
        filtered_spans = [span for span in span_element_list if 'q-box' in span.get_attribute('class') and 'qu-userSelect--text' in span.get_attribute('class')]
        
        for spans in filtered_spans[:10]:
            print(spans.text)
            input("-------------------------------------------------")
        
        time.sleep(random.uniform(1, 3))
    except Exception as e:
        continue

time.sleep(random.uniform(1, 3))
driver.quit()