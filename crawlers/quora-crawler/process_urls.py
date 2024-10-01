from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from database import get_all_url
from model import Url
import random
import time

# url_table_list = get_all_url()
# for i in url_table_list:
#     print(i['url'])
    
    
url = "https://www.quora.com/Is-there-any-way-to-transform-a-low-resolution-image-to-quality-high-resolution"

chrome_options = Options()
chrome_options.add_argument("--log-level=3") 

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

time.sleep(random.uniform(1,3))
driver.quit()