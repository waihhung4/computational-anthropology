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


def login_quora(driver: WebDriver, email: str, password: str):
    
    email_input = driver.find_element(by=By.ID, value='email')
    password_input = driver.find_element(by=By.ID, value='password')
    login_button = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button')
    
    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()
    time.sleep(random.uniform(2, 3))

login_url = "https://www.quora.com/"
url = "https://www.quora.com/Is-there-any-way-to-transform-a-low-resolution-image-to-quality-high-resolution"

chrome_options = Options()
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=chrome_options)   
driver.get(login_url)
    
    # Log in to Quora
login_quora(driver, Constant.LOGIN_EMAIL, Constant.LOGIN_PASSWORD)

time.sleep(random.uniform(2, 3))
driver.get(url)


driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div/div[1]/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/span').click()

input("-------------------------------------------------")