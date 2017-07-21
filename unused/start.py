#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest,time
from selenium.webdriver.support.ui import Select

''' 
Test functionality of bahsegel
'''
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
    def login(self):
        driver = self.driver
        driver.find_element_by_id('login-Button').click()
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(NAME)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(PASSW)
        driver.find_element_by_id('loginBtnSubmit').click()
    def test_login_url(self):
        driver = self.driver
        driver.find_element_by_id('login-Button').click()
        login_url = URL+"/tr/login"
        self.assertEqual(login_url,self.driver.current_url)

    def test_logout(self):
        driver = self.driver
        time.sleep(10)
        self.login()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]

        driver.find_element_by_xpath(".//*[@id='bodyScope']/header[1]/div/div[2]/a[1]").click()
        # driver.find_element_by_link_text(u"Hesabım").click()
        # driver.find_element_by_link_text(u"ÇIKIŞ YAP").click()
        # driver.find_element_by_link_text(u"ÇIKIŞ YAP").click()
        # self.assertEqual(u"BahseGel - Türkiye'nin En İyi Bahis Sitesi | Üye Ol 300 TL Bonus Kazan", driver.title)
        # driver.get(self.base_url + "/tr")
        # self.assertEqual(u"BahseGel.Com | Online Bahis | Spora heyecan katın", driver.title)
        # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | sport_iframe_1 | ]]
        # driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()
        # driver.find_element_by_xpath("//div[@id='mCSB_16_container']/div/div[2]/div[2]/a/div[2]").click()
        # driver.find_element_by_xpath("//div[@id='mCSB_16_container']/div/div[2]/div[2]/a/div[2]").click()
        # driver.find_element_by_xpath("//div[@id='mCSB_16_container']/div/div[2]/div[2]/a/div[2]").click()
        # driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()
        # # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=sport_iframe_1 | ]]
        # driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()
        # driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()
        # driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()
        # driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()
        # driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()
    def switch_frame(self):
        driver = self.driver
        my_frame = driver.find_element_by_id('sport_iframe_1')
        driver.switch_to.frame(my_frame)

    def left_menu(self):
        '''select first element of left menu and change the bet to 2'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="bodyScope"]/header[1]/nav/div/ul/li').click()
        self.switch_frame()
        driver.find_element_by_xpath("//div[@id='champFav4485']/span").click()

    def select_bet(self):
        driver = self.driver
        class_name = 'prematch_stake_odd_factor'
        driver.find_elements_by_class_name(class_name)[0].click()
        self.scroll_browser()

    def scroll_browser(self):
        driver = self.driver
        driver.switch_to.default_content()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def test_top_menu_elements(self):
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

    # def enter_value(self, value):
    #     driver = self.driver
    #     self.switch_frame()
    #     driver.find_element_by_xpath('.//*[@id="betAmountInput"]').send_keys(value)
    #     self.driver.find_element_by_xpath(".//*[@id='mCSB_4_container']/div[2]/div[5]/div[5]/div[1]/div[2]").click()


    def test_make_bet(self,value=1):
        driver = self.driver
        self.switch_frame()
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





    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main().verbosity==2


