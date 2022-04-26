from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def main():
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()

    browser.get(link)

    browser.find_element_by_css_selector('.trollface.btn.btn-primary').click()
    sec_tab = browser.window_handles[1]
    browser.switch_to.window(sec_tab)
    x = browser.find_element_by_css_selector('#input_value').text
    r_answer = calc(int(x))
    browser.find_element_by_css_selector('#answer').send_keys(str(r_answer))
    browser.find_element_by_css_selector('.btn.btn-primary').click()
    time.sleep(10)
    browser.quit()


if __name__ == '__main__':
    main()