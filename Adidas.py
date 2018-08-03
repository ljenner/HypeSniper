from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        

def login():
    browser = webdriver.Chrome()
    browser.get(('https://www.adidas.co.uk/'))

    try:
        browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div/div/a[3]').click()
    except NoSuchElementException:
        pass
    

if __name__ == "__main__":
    login()