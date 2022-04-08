from selenium import webdriver
import math
import time

browser = webdriver.Chrome() #set browser
time.sleep(8)
browser.get("http://suninjuly.github.io/alert_accept.html") #set link

try:
    button1 = browser.find_element_by_class_name("btn").click() #find a button
    #click the buton
    confirm = browser.switch_to.alert #switch to confirm 
    confirm.accept() #click OK
    x = int(browser.find_element_by_xpath("//span[@id='input_value']").text) #get a num and set the num to var
    result = str(math.log(abs(12*math.sin(x)))) #calculate
    input1 = browser.find_element_by_xpath("//input[@name='text']").send_keys(result) #find a textfield
    #input1.send_keys(result) #set a res to textfield
    button2 = browser.find_element_by_xpath("//button[@type='submit']")#find a submit button
    button2.click()#click
    
finally:
    time.sleep(15) #waiting 15 sec
    browser.quit() #end of session
