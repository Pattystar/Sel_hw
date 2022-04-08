from selenium import webdriver # importing webdriver
import time
import math
def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()# initializing browser
time.sleep(10)

link = "http://suninjuly.github.io/math.html" # get link
browser.get(link)

try:
    #x_element = browser.find_element_by_id("input_value")
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    #res = str(math.log(abs(12*math.sin(int(x))))) # calculating result
    #y = calc(x)
    #input1 = browser.find_element_by_id("answer") # find textfield by css celector
    input1 = browser.find_element_by_xpath("//input[@id='answer']") # find textfield by xPath
    #input1.send_keys(res) # fill in textfield
    input1.send_keys(calc(x))
    #input2 = browser.find_element_by_css_selector("[for='robotCheckbox']") # find check-box by css celector
    input2 = browser.find_element_by_xpath("//label[@for='robotCheckbox']")# find check-box by xPath
    input2.click()# click check-box
    #input3 = browser.find_element_by_id("robotsRule") # find second radio button by css celector
    input3 = browser.find_element_by_xpath("//input[@value='robots']") # find second radio button by xPath
    input3.click() # click radio button
    #button = browser.find_element_by_class_name("btn") # find sumbit button by css celector
    button = browser.find_element_by_xpath("//button[contains(@class, 'btn')]")# find sumbit button by xPath
    button.click()# click sumbit button

finally:
    time.sleep(10)# pause
    browser.quit()# browser quit
