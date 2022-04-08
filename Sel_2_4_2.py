from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
def reslt():
    return math.log(abs(12*math.sin(x)))

try:
    cost = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    x = int(browser.find_element(By.ID, "input_value").text)
    res = str(reslt())
    input1 = browser.find_element_by_class_name("form-control")
    input1.send_keys(res)
    button = browser.find_element_by_xpath("//button[@id='solve']")
    button.click()
    print(browser.switch_to.alert.text)
finally:
    browser.quit()
