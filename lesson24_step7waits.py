import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def main():
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector('#book')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price'),'$100'))
    button.click()
    
    x = browser.find_element_by_css_selector('#input_value').text
    r_answer = calc(int(x))
    button1 = browser.find_element_by_css_selector('#solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    browser.find_element_by_css_selector('#answer').send_keys(str(r_answer))
    button1.click()
    time.sleep(15)
    
    browser.quit()



if __name__ == '__main__':
    main()
