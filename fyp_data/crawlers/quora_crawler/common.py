from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

import random
import time

xpath_patterns = [
        'div/div/div/div/div[2]/div/div[1]/div[2]/div/div/span',
        'div/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div/span',
        'div/div/div/div/div[1]/div[2]/div/div[1]/div[3]/div/div/span',
        'div/div/div/div/div[2]/div/div[1]/div[3]/div/div/span',
        'div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/span',
    ]


def scroll_down(driver: WebDriver, scrolls=5):
    for _ in range(scrolls):
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(random.uniform(1,3))

def login_quora(driver: WebDriver, email: str, password: str):
    
    email_input = driver.find_element(by=By.ID, value='email')
    password_input = driver.find_element(by=By.ID, value='password')
    login_button = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button')
    
    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()
    
    time.sleep(random.uniform(2, 3))

def expand_replies(driver: WebDriver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    
    scroll_down(driver, scrolls=5)

    more_elements = driver.find_elements(By.XPATH, "//*[contains(text(), '(more)')]")

    # Click on each element found
    for element in more_elements:
        try:
            # Use JavaScript to click the element
            driver.execute_script("arguments[0].click();", element)
            print("Element clicked")
            time.sleep(random.uniform(1.2, 2))
        except Exception as e:
            print(f"Could not click on element: {e}")
            
            
############# for text "more"
# def expand_replies(driver: WebDriver):
#     content_list = driver.find_elements(By.XPATH, '//*[@id="mainContent"]/div[3]/div')
#     for content in content_list:
#         found = False
#         for xpath in xpath_patterns:
#             try:
#                 # Wait for the element to be present and visible
#                 temp_element = WebDriverWait(content, 10).until(
#                     EC.presence_of_element_located((By.XPATH, xpath))
#                 )
#                 temp_element = WebDriverWait(content, 10).until(
#                     EC.visibility_of_element_located((By.XPATH, xpath))
#                 )
                
#                 # Find the last span element and click it
#                 span_elements = temp_element.find_elements(By.TAG_NAME, 'span')
#                 if span_elements:
#                     span_elements[-1].click()
#                     print(f"Span element clicked for XPath: {xpath}")
#                     found = True
#                     break
#                 else:
#                     print(f"No span elements found for XPath: {xpath}")
#             except Exception as e:
#                 print(f"Exception for XPath: {xpath}")
#                 continue

#         if not found:
#             print("No valid element found for this content.")




################# for button "show more"
# def expand_replies(driver: WebDriver, content: WebElement):
#     buttons = content.find_elements(By.TAG_NAME, "button")
#     for i in range(len(buttons)):
#         try:
#             if i == 0:
#                 continue
#             buttons[i].click()
#             time.sleep(random.uniform(1, 2))
#         except Exception as e:
#             print(f"Could not click button: {e}")
