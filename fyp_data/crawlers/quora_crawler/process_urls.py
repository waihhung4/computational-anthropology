from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


from tqdm import tqdm
from database import get_all_content, get_all_url, insert_content_table
from model import Url, Content
import random
import time
from bs4 import BeautifulSoup
from constants import Constant
from common import expand_replies, xpath_patterns

xpath_patterns = [
        'div/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div/span',
        'div/div/div/div/div[1]/div[2]/div/div[1]/div[3]/div/div/span',
        'div/div/div/div/div[2]/div/div[1]/div[3]/div/div/span/span',
        'div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/span'
        'div/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div/span/span',
    ]

def login_quora(driver: WebDriver, email: str, password: str):
    
    time.sleep(random.uniform(1, 1.2))
    
    email_input = driver.find_element(by=By.ID, value='email')
    password_input = driver.find_element(by=By.ID, value='password')
    login_button = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button')
    
    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()
    
    time.sleep(random.uniform(2, 3))


login_url = "https://www.quora.com/"

chrome_options = Options()
chrome_options.add_argument("--log-level=3") 


driver = webdriver.Chrome(options=chrome_options)   
driver.get(login_url)
login_quora(driver, Constant.LOGIN_EMAIL, Constant.LOGIN_PASSWORD)

content_url_list = [url["url"] for url in get_all_content()]

url_list: List[Tuple[str]]= [(url["url"], url["search_keyword"]) for url in get_all_url() if url["url"] not in content_url_list]

print("The length of the url_list is: ", len(url_list))

input("Press Enter to continue...")
for url in tqdm(url_list):
    driver.get(url[0])
    
    input("Press Enter to continue...")
    
    time.sleep(random.uniform(2, 3))
    span_list = []
    expand_replies(driver)
    maincontent_list = driver.find_elements(By.XPATH, '//*[@id="mainContent"]/div[3]/div')


    print("The length is the maincontent_list is: ", len(maincontent_list))
    for maincontent in maincontent_list:
        try:
            temp_element = maincontent.find_element(By.XPATH, "div/div/div/div/div[1]")

            span_element_list = temp_element.find_elements(By.TAG_NAME, 'span')
            filtered_spans = [span for span in span_element_list if 'q-box' in span.get_attribute('class') and 'qu-userSelect--text' in span.get_attribute('class')]
            
            print("The length is the span_element_list is: ", len(filtered_spans))
            
            if len(filtered_spans) <= 0:
                continue
            
            result_text: str = " ".join(span.text for span in filtered_spans)
            
            content: Content = Content(result_text, url[1], url=url[0])
            insert_content_table(content)
            
            time.sleep(random.uniform(0.5, 1))
        except Exception as e:
            print("fall error")
            continue

time.sleep(random.uniform(1, 3))
driver.quit()