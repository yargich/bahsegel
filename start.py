#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

from time import sleep

''' 
Test functionality of site	
'''
URL = "https://tst.bahsegel.info"
NAME = "Bahsegel_26"
PASSW = "qwerty26"

class Bahsegel:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://tst.bahsegel.info')

        self.driver.implicitly_wait(50)
        self.driver.find_element_by_id('login-Button').click()

        self.driver.find_element_by_id('username').send_keys(NAME)
        self.driver.find_element_by_id('password').send_keys(PASSW)
        self.driver.find_element_by_id('loginBtnSubmit').click()


    def print_message(self,txt):
        print txt

    def left_menu(self):
        frame = self.driver.find_element_by_id('sport_iframe_1')
        self.driver.switch_to.frame(frame)
        self.driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()
        self.driver.switch_to.default_content()

test = Bahsegel()
test.left_menu()