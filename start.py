#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import pdb
'''
https://selenium2.ru/docs/selenium-grid.h
Test functionality of site	
check base URL	https://tst.bahsegel.info/tr
Check logo image	 
Check url of logo image	/img/logo.svg
check login input	 
check password input	
Functionality of forgot password button	
Functionality of Not a member yet button	
New user registration on test enviroment only	
Check quantities of main menu elements	
Check text values of main menu elements	
 	
Enter bet and check result for first game in list	
open menu element in iframe	
close menu element in iframe
logout

'''
URL = "https://tst.bahsegel.info"
NAME = "Bahsegel_26"
PASSW = "qwerty26"

class Action(object):
    pass

class TestBahsegel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://stg.bahsegel.info')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('login-Button').click()

    def test_login(self):
       self.driver.find_element_by_id('username').send_keys(NAME)
       self.driver.find_element_by_id('password').send_keys(PASSW)
       self.driver.find_element_by_id('loginBtnSubmit').click()


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()