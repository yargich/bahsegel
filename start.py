#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
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
class Bahsegel:
    def __init__(self):
        '''Open site which based on URL parameter'''
        self.driver = webdriver.Firefox()
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.base_url = URL
        driver.get(self.base_url + '/tr')


    def login(self):
        '''Enter login and password and provides login of user'''
        driver = self.driver
        username = "bahsegel_26"
        passw = "qwerty26"
        self.driver.find_element_by_id("login-Button").click()
        driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(passw)
        self.driver.find_element_by_id("loginBtnSubmit").click()



    def test_make_bet(self):

        '''
        Enter bet and check result for first game in list
        '''

        driver = self.driver
        frame = driver.find_element_by_xpath('//*[@id="sport_iframe_1"]')
        driver.switch_to.frame(frame)
        pdb.set_trace()
        driver.find_element_by_xpath('//*[@id="champFav15829"]/span').click()
        # driver.find_element_by_xpath("//div[@id='mCSB_8_container']/div/div[2]/div[2]/a/div[2]").click()
        # driver.find_element_by_xpath("//*[@id='mCSB_7_container']/div/div[2]/div[2]/a[1]/div[2]").click()
        # driver.find_element_by_id("betAmountInput").clear()
        # driver.find_element_by_id("betAmountInput").send_keys("2")


        driver.find_element_by_id("mCSB_8_container").click()


        # driver.find_element_by_id("betAmountInput").clear()
        # driver.find_element_by_id("betAmountInput").send_keys("2")
        # driver.find_element_by_xpath("//input[@value='BAHIS YAP']").click()
        # # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # driver.find_element_by_id("lst-ib").click()
        # driver.find_element_by_id("lst-ib").click()
        # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | sport_iframe_1 | ]]
        # self.assertEqual("Home | Bahsegel Sport", driver.title)


# if __name__ == "__main__":
#     unittest.main()
test = Bahsegel()
test.login()
test.test_make_bet()