# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Aaa(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://tst.bahsegel.info/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_aaa(self):
        driver = self.driver
        driver.get(self.base_url + "/tr/login")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("Bahsegel_26")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("qwerty26")
        driver.find_element_by_id("loginBtnSubmit").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | sport_iframe_1 | ]]
        driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()

        driver.find_element_by_xpath("//div[@id='mCSB_10_container']/div/div[2]/div[2]/a/div[2]").click()


        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=fbMainContainer | ]]
        driver.find_element_by_id("fbCloseButton").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=sport_iframe_1 | ]]
        driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()
        driver.find_element_by_xpath("//div[@id='mCSB_13_container']/div/div[2]/div[2]/a/div[2]").click()
        driver.find_element_by_xpath("//div[@id='mCSB_13_container']/div/div[2]/div[2]/a/div[2]").click()
        driver.find_element_by_xpath("//div[@id='mCSB_13_container']/div/div[2]/div[2]/a/div[2]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
