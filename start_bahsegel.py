#!/usr/bin/env python
# -*- coding: utf-8 -*-

from just_actions import *


import unittest,time,sys


NAME = "Bahsegel_26"
# NAME = "testbahsegel"

PASSW = "qwerty26"

class Bahsegel(unittest.TestCase):
    def setUp(self):
        print 'Testing now:'

    def test_favicon_exists(self):


        test = Action()
        test.show_name('favicon exists)
        test.get_favicon()
        test.close_driver()

    def test_logo_exists(self):

        test = Action()
        test.show_name('logo exists')
        test.logo_exist()
        # test.open_svg_in_browser()
        time.sleep(5)
        test.close_driver()

    def test_logo_url(self):

        suff = '/img/logo.svg'
        test = Action()
        test.show_name('logo url')
        etalon_url = URLtst+suff
        self.assertEqual(test.logo_url(),etalon_url)
        test.close_driver()
    #
    # def test_url_of_login_page(self):
    #     '''check url of login page'''
    #     test = Action()
    #     link_to_login = test.enter_to_page()
    #     self.assertEqual(link_to_login[0], link_to_login[1])
    #     test.close_driver()
    # def test_forgot_password(self):
    #     '''checks forgot_password button value'''
    #     test=Action()
    #     current_value = test.forgot_password()
    #     test.close_driver()
    #     self.assertEqual( u"Şifremi Unuttum?",current_value)
    #
    # def test_successfully_login(self):
    #     '''successfully login'''
    #     test = Action()
    #     test.login(NAME,PASSW)
    #     test.close_driver()
    #
    # def test_nav_menu_unregistered(self):
    #     '''Checks elements of nav menu without login'''
    #     test = Action()
    #     test.check_top_menu()
    #     test.close_driver()
    #
    # def test_number_elements_nav_menu(self):
    #     '''count quantity of elements in nav menu'''
    #     test = Action()
    #     test.login(NAME, PASSW)
    #
    #     self.assertEqual(test.check_top_menu(),7)
    #     test.close_driver()
    #
    # def test_nav_nenu_with_login(self):
    #     '''Checks elements of nav menu with login'''
    #     test = Action()
    #     test.login(NAME,PASSW)
    #     time.sleep(5)
    #     test.check_top_menu()
    #     test.close_driver()
    #
    #
    # def test_virtual_sport_menu(self):
    #     test = Action()
    #     test.login(NAME,PASSW)
    #
    #     time.sleep(4)
    #     test.virtual_sport_click()
    #     test.close_driver()
    #
    # def test_open_result_page(self):
    #     test =Action()
    #     test.open_result_in_browser()


    # def test3(self,value=2):
    #     '''make a bet'''
    #     driver = self.driver
    #     # self.switch_frame()
    #     my_frame = driver.find_element_by_id('sport_iframe_1')
    #     driver.switch_to.frame(my_frame)
    #     #select first element in left menu
    #     driver.find_element_by_xpath('//*[@id="champFav4485"]/span').click()
    #     class_name = "prematch_stake_odd_factor"
    #     driver.find_element_by_class_name(class_name).click()
    #     #enter value in input field
    #     driver.find_element_by_id("betAmountInput").send_keys(value)
    #     #press the bet button
    #     driver.find_element_by_class_name('btn_bet').click()
    #     # time.sleep(10)
    #     congrat_etalon_text = u"Bahis oynanmıştır.\nİyi Şanslar!"
    #     if len(driver.find_element_by_css_selector("div.congratText").text)>1:
    #         print (driver.find_element_by_css_selector("div.congratText").text)
    #     time.sleep(9)
    # def test_check_logo(self):
    #     '''logo'''
    #     test =Action()
    #     logo = test.existing_logo()
    #     self.assertEqual("", logo)

    # def virtual_menu(self):
    #     element_name = []
    #     my_text = self.driver.find_elements_by_xpath('//*[@id="page-top"]/div[1]/div[2]/ul/li')
    #     for i in  my_text:
    #         element_name.append(i.text)
    #     for name in element_name:
    #         self.driver.find_element_by_link_text(name).click()
    # def test_open_virtual_sport_menu_element(self):
    #     self.virtual_menu()

    # def test_quantity_virtual_sports_menu_elements(self):
    #     num_of_elements = len(self.virtual_sport_menu())
    #     assert (num_of_elements,5)
    # def test_virtual_sports_footbol(self):
    #     '''virtual sports footbol'''
    #     # self.login(NAME, PASSW)
    #     driver = self.driver
    #     xpath = ".//*[@id='bodyScope']/header[1]/nav/div/ul/li[5]/a"
    #     driver.find_element_by_xpath(xpath).click()
    #     driver.find_element_by_xpath(".//*[@id='bodyScope']/div[1]/div/ul/li[1]").click()

    # def test_virtual_sports_basquet(self):
    #     '''virtual sports basquet'''
    #     self.login(NAME,PASSW)
    #     driver = self.driver
    #     xpath = ".//*[@id='bodyScope']/header[1]/nav/div/ul/li[5]/a"
    #     driver.find_element_by_xpath(xpath).click()
    #     driver.find_element_by_xpath(".//*[@id='bodyScope']/div[1]/div/ul/li[2]").click()
    # #
    # def test_9(self):
    #     pass
    # def test_7(self):
    #     '''virtual sports greyhounds'''
    #
    #     pass
    # def test_8(self):
    #     '''virtual sports basquet'''
    #     driver = self.driver
    #
    #     xpath = ".//*[@id='bodyScope']/header[1]/nav/div/ul/li[5]/a"
    #     driver.find_element_by_xpath(xpath).click()
    #     driver.find_element_by_xpath(".//*[@id='bodyScope']/div[1]/div/ul/li[2]").click()
    # def test_9(self):
    #     '''virtual sports horseracing'''
    #     pass

    def tearDown(self):
        pass




if __name__ == '__main__':
    unittest.main()
