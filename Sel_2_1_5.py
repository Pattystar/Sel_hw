from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Q")
    input2 = browser.find_element_by_xpath("//input[@name = 'lastname']")
    input2.send_keys("Werty")
    input3 = browser.find_element_by_xpath("//input[@name = 'email']")
    input3.send_keys("q@q.q")
    loadfile = browser.find_element_by_id("file")
    loadfile.send_keys(file_path)
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
    
