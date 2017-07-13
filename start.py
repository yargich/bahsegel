#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium import webdriver
URL = "https://tst.bahsegel.info"
class Bahsegel:
    def __init__(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.base_url = URL

        driver.get(self.base_url + "/tr")


    def login(self):
        username = "bahsegel_26"
        passw = "qwerty26"

        self.driver.find_element_by_id("login-Button").click()
        # driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        # driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(passw)
        self.driver.find_element_by_id("loginBtnSubmit").click()



    def test_make_bet(self):
        driver = self.driver
        frame = driver.find_element_by_xpath('//*[@id="sport_iframe_1"]')
        driver.switch_to.frame(frame)
        driver.find_element_by_xpath('//*[@id="champFav15829"]/span').click()


        driver.find_element_by_xpath("id('mCSB_8_container')/x:div/x:div[2]/x:div[2]/x:a[1]/x:div[2]").click()


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