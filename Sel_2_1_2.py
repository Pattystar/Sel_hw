from selenium import webdriver # import webdriver
import time # import time
import math # import math

browser = webdriver.Chrome() # init. browser
link = "http://suninjuly.github.io/get_attribute.html" # get link
time.sleep(10)
browser.get(link) # set link to browser

try:
    #x_element = browser.find_element_by_id("treasure") # find x by css selector
    x_element = browser.find_element_by_xpath("//img[@id='treasure']") # find x by xPath
    x = x_element.get_attribute("valuex") # get attribute
    res = str(math.log(abs(12*math.sin(int(x))))) # calculating result
    #input1 = browser.find_element_by_id("answer") # find textfield by css celector
    input1 = browser.find_element_by_xpath("//input[@id='answer']") # find textfield by xPath
    input1.send_keys(res) # fill in textfield
    #checkbox = browser.find_element_by_id("robotCheckbox") # find check-box by css celector
    checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']") # find check-box by xPath
    checkbox.click()# click check-box
    #radiobutton2 = browser.find_element_by_id("robotsRule") # find second radio button by css celector
    radiobutton2 = browser.find_element_by_xpath("//input[@id='robotsRule']") # find second radio button by xPath
    radiobutton2.click()# click radio button
    #button = browser.find_element_by_class_name("btn") # find sumbit button by css celector
    button = browser.find_element_by_xpath("//button[contains(@class, 'btn-default')]") # find sumbit button by xPath
    button.click() # click sumbit button
finally:
    time.sleep(15)
    browser.quit()

    #28.87650825835904

