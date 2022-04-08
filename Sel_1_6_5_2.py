from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    in1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
    in1.send_keys("First Name")
    in2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
    in2.send_keys("Second Name")
    in3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
    in3.send_keys("EMail")


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
 
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    #####

    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    in1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
    in1.send_keys("First Name")
    in2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
    in2.send_keys("Second Name")
    in3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
    in3.send_keys("EMail")


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
 
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

    browser.quit()
