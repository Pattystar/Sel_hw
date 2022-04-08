from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
time.sleep(10)
browser.get("http://suninjuly.github.io/redirect_accept.html")

try:
    browser.find_element_by_class_name("trollface").click() #find a button
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = int(browser.find_element_by_id("input_value").text) #find a x variable
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12*math.sin(x))))) #find anf fill in a textfield
    browser.find_element_by_xpath("//button[contains(@class, 'btn-primary')]").click() #find and click a submit button
    print(browser.switch_to.alert.text)#print alert to console 
    
finally:
    browser.quit()
