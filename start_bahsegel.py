#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest,time
URL = "https://stg.bahsegel.info"
NAME = "Bahsegel_26"
PASSW = "qwerty26"

class Bahsegel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.set_window_size(1800, 1800)
        driver.get(URL)
        driver.implicitly_wait(30)
        driver.find_element_by_id('login-Button').click()
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(NAME)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(PASSW)
        driver.find_element_by_id('loginBtnSubmit').click()


    def test1(self):
        '''check url of login page'''
        driver = self.driver
        driver.get(URL)
        driver.find_element_by_id('login-Button').click()
        login_url = URL+"/tr/login"
        self.assertEqual(login_url,self.driver.current_url)


    def test2(self):
        '''chek quantity of elements in top menu'''
        driver = self.driver
        base_xpath = '//*[@id="bodyScope"]/header[1]/nav/div/ul/li'
        top_menu = driver.find_elements_by_xpath(base_xpath)
        num_of_element = len(top_menu)
        i = 1
        while i < num_of_element:
            new_xpath = base_xpath + '[' + str(i) + ']' + '/a'
            driver.find_element_by_xpath(new_xpath).click()
            element_name = driver.find_element_by_xpath(new_xpath)
            print element_name.text

            i += 1

        self.assertEqual(num_of_element-1,7)

    def test3(self,value=1):
        '''make a bet'''
        driver = self.driver
        # self.switch_frame()
        my_frame = driver.find_element_by_id('sport_iframe_1')
        driver.switch_to.frame(my_frame)
        #select first element in left menu
        driver.find_element_by_xpath('//*[@id="champFav4485"]/span').click()
        class_name = "prematch_stake_odd_factor"
        driver.find_element_by_class_name(class_name).click()
        #enter value in input field
        driver.find_element_by_id("betAmountInput").send_keys(value)
        #press the bet button
        driver.find_element_by_class_name('btn_bet').click()
        # time.sleep(10)
        congrat_etalon_text = u"Bahis oynanmıştır.\nİyi Şanslar!"
        if len(driver.find_element_by_css_selector("div.congratText").text)>1:
            print driver.find_element_by_css_selector("div.congratText").text
        time.sleep(9)

    def switch_frame(self):
        driver = self.driver
        my_frame = driver.find_element_by_id('sport_iframe_1')
        driver.switch_to.frame(my_frame)

    def tearDown(self):
        self.driver.close()