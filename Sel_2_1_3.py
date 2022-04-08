from selenium import webdriver #import
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome() #init browser
browser.get("http://suninjuly.github.io/selects2.html") #set link to browser

try:
    #first_num = browser.find_element_by_id("num1")
    first_num = int(browser.find_element_by_xpath("//span[@id='num1']").text) #set first num to variable
    #second_num = browser.find_element_by_id("num2")
    second_num = int(browser.find_element_by_xpath("//span[@id='num2']").text)
    res = first_num + second_num #get result
    select = Select(browser.find_element_by_id("dropdown")) #get list
    sel = select.select_by_value(str(res))#get right variant
    browser.find_element_by_xpath("//button[contains(@class, 'btn')]").click()
finally:
    time.sleep(10)
    browser.quit()
