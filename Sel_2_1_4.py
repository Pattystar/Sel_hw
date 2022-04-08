from selenium import webdriver
import time
import math #import

browser = webdriver.Chrome() #set browser
link = "http://suninjuly.github.io/execute_script.html" #set link
browser.get(link)

try:
    #x = int(browser.find_element_by_id("input_value").text) #get x
    x = int(browser.find_element_by_xpath("//span[@id='input_value']").text)
    result = str(math.log(abs(12*math.sin(x)))) #calculate function
    #input1 = browser.find_element_by_class_name("form-control").send_keys(result) #find and fill in a input field 1
    #input1.send_keys(result)
    input1 = browser.find_element_by_xpath("//input[@class='form-control']").send_keys(result) #find and fill in a input field 2
    #chbox = browser.find_element_by_id("robotCheckbox").click() #find and fill in a checkbox 1
    chbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']").click() #find and fill in a checkbox 2
    #rb = browser.find_element_by_id("robotsRule")#find a radio button 1
    rb = browser.find_element_by_xpath("//input[@id='robotsRule']") #find a radio button 2
    browser.execute_script("return arguments[0].scrollIntoView(true);", rb) #scroll to the radio button
    rb.click() #fill in the radio button
    #button = browser.find_element_by_class_name("btn") #find a sumbit button 1
    button = browser.find_element_by_xpath("//button[contains(@class, 'btn')]") #find a sumbit button 2
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) #scroll to the sumbit button
    button.click()#click the sumbit button
    
    

finally:
    time.sleep(10)
    browser.quit()
