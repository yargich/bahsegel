#!/usr/bin/env python

from selenium import webdriver

from selenium.webdriver.support.ui import Select

''' 
Test functionality of site	
'''
URL = "https://tst.bahsegel.info"
NAME = "Bahsegel_26"
PASSW = "qwerty26"


class Bahsegel:
    def __init__(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.get(URL)
        driver.implicitly_wait(30)
        driver.find_element_by_id('login-Button').click()
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(NAME)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(PASSW)
        driver.find_element_by_id('loginBtnSubmit').click()

    def switch_frame(self):
        driver = self.driver
        my_frame = driver.find_element_by_id('sport_iframe_1')
        driver.switch_to.frame(my_frame)

    def left_menu(self):
        '''select first element of left menu and change the bet to 2'''
        driver = self.driver
        self.switch_frame()
        driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()

    def select_bet(self):
        driver = self.driver
        class_name = 'prematch_staks_left'
        driver.find_elements_by_class_name(class_name)[0].click()

    def scroll_browser(self):
        driver = self.driver
        driver.switch_to.default_content()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def top_menu_elements(self):
        driver = self.driver
        base_xpath = '//*[@id="bodyScope"]/header[1]/nav/div/ul/li'

        top_menu = driver.find_elements_by_xpath(base_xpath)
        num_of_element = len(top_menu)

        i = 1
        NavMenuNames = []
        while i < num_of_element:
            new_xpath = base_xpath + '[' + str(i) + ']' + '/a'

            driver.find_element_by_xpath(new_xpath).click()
            element_name = driver.find_element_by_xpath(new_xpath)
            print element_name.text
            NavMenuNames.append(element_name.text)

            i += 1
        print str(num_of_element - 1) + "elements of menu are present..."
        return NavMenuNames

    def enter_value(self, value):
        driver = self.driver
        self.switch_frame()
        driver.find_element_by_xpath('//*[@id="betAmountInput"]').send_keys(value)


test = Bahsegel()
test.left_menu()
test.select_bet()
test.scroll_browser()
# test.enter_value(8)
test.top_menu_elements()
