from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import random
import time
from constants import Constant
import database
from model import Url
from bs4 import BeautifulSoup

def login_quora(driver: WebDriver, email: str, password: str):
    email_input = driver.find_element(by=By.ID, value = 'email')
    password_input = driver.find_element(by=By.ID, value='password')
    login_button = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button')
    
    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()
    
def search_keyword(driver: WebDriver, keyword:str):
    try:
        search_session = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/form/div/div/div/div/div/input'))
        )
        search_session.send_keys(keyword)
        time.sleep(3)
        search_session.send_keys(Keys.RETURN)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
def scroll_down(driver: WebDriver, scrolls=5):
    for _ in range(scrolls):
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(random.uniform(1,3))
        
def get_all_url(driver: WebDriver):
    url_list = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    main_content = soup.find("div", {"id": "mainContent"}).find("div").find("div").find_all("div", recursive=False)[1]
    tiny_content_div_block_list = main_content.find_all("div", {"class": "q-box qu-borderBottom qu-p--medium qu-pb--tiny"})
    medium_content_div_block_list = main_content.find_all("div", {"class": "q-box qu-borderBottom qu-p--medium"})

    for content_div_block in medium_content_div_block_list:
        url = content_div_block.find("a", {"class": "q-box qu-display--block qu-cursor--pointer qu-hover--textDecoration--underline b2c1r2a puppeteer_test_link"}).get("href")
        url_list.append(url)
        
    for content_div_block in tiny_content_div_block_list:
        url = content_div_block.find("a", {"class": "q-box qu-display--block qu-cursor--pointer qu-hover--textDecoration--underline b2c1r2a puppeteer_test_link"}).get("href")
        url_list.append(url)
        
    return url_list

if __name__ == "__main__":
    

    keyword_list = ['sumerian', 'sumer', 'old china', 'xia dynasty', 
                    'ancient china', 'ancient culture', 'china and sumer', 'chinese and sumerian', 'china sumer', 'sumerian chinese']
    
    keyword = 'sumerian chinese'
    dns = "https://www.quora.com"
    
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3") 
    
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get(dns)
    login_quora(driver=driver, email=Constant.LOGIN_EMAIL, password=Constant.LOGIN_PASSWORD)
    search_keyword(driver=driver, keyword=keyword)
    scroll_down(driver=driver)
    for url in get_all_url(driver=driver):
        crawlers_url = Url()
        crawlers_url.set_search_keyword(keyword)
        crawlers_url.set_source('quora')
        crawlers_url.set_url(url)
        database.insert_url_table(crawlers_url)

    time.sleep(2)
    driver.quit()
    
    