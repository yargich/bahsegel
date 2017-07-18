#!/usr/bin/env python

from selenium import webdriver


''' 
Test functionality of site	
'''
URL = "https://stg.bahsegel.info"
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


    def left_menu(self):
        '''select first element of left menu and change the bet to 2'''
        driver = self.driver
        frame = driver.find_element_by_id('sport_iframe_1')
        driver.switch_to.frame(frame)
        driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()
        class_name = 'prematch_staks_left'
        driver.find_elements_by_class_name(class_name)[0].click()
        driver.maximize_window()






test = Bahsegel()
test.left_menu()