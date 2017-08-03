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


    def pre_condition(self):
        for i in os.listdir('./'):
            Suff = ['.png','.html']
            for item in Suff:
                if i.endswith(item):
                    os.remove(i)
                    print i + " is deleted..."

    # def test_favicon_exists(self):
    #     test = Action()
    #
    #     test.show_name('favicon exists')
    #     test.get_favicon()
    #     test.close_driver()
    #
    # def test_logo_exists(self):
    #     self.pre_condition()
    #
    #     test = Action()
    #     test.show_name('logo exists')
    #     test.logo_exist()
    #     # test.open_svg_in_browser()
    #     time.sleep(5)
    #     test.close_driver()
    #
    # def test_logo_url(self):
    #     suff = '/img/logo.svg'
    #     test = Action()
    #     test.show_name('Url of logo')
    #
    #     etalon_url = URLtst+suff
    #     self.assertEqual(test.logo_url(),etalon_url)
    #     test.close_driver()

    # def test_url_of_login_page(self):
    #     '''check url on login page'''
    #     test = Action()
    #     test.show_name('Url of login page')
    #     link_to_login = test.enter_to_page()
    #     self.assertEqual(link_to_login[0], link_to_login[1])
    #     test.close_driver()
    # def test_forgot_password(self):
    #     '''checks forgot_password button value'''
    #     test=Action()
    #     test.show_name('Forgot password button')
    #     current_value = test.forgot_password()
    #     self.assertEqual( u"Şifremi Unuttum?", current_value)
    #     test.close_driver()
    #
    # def test_successfully_login(self):
    #     '''successfully login'''
    #     test = Action()
    #     test.show_name('Successfully login')
    #     test.login(NAME,PASSW)
    #     test.close_driver()

    # def test_nav_menu_without_ligin(self):
    #     '''Checks elements of nav menu without login'''
    #     test = Action()
    #     test.show_name('Elements of nav menu without login')
    #     test.check_top_menu()
    #     test.close_driver()
    #
    # def test_number_elements_nav_menu(self):
    #     '''counts quantity of elements in nav menu'''
    #     test = Action()
    #     test.show_name('Counts quantity of elements in nav menu')
    #     test.login(NAME, PASSW)
    #
    #     self.assertEqual(test.check_top_menu(),7)
    #     test.close_driver()
    #
    # def test_nav_nenu_with_login(self):
    #     '''Checks elements of nav menu with login'''
    #     test = Action()
    #     test.show_name('Elements of nav menu with login')
    #     test.login(NAME,PASSW)
    #     time.sleep(5)
    #     test.check_top_menu()
    #     test.close_driver()


    # def test_virtual_sport_menu_login(self):
    #     '''Elements of virtual sport menu with login'''
    #     test = Action()
    #     test.show_name('Elements of virtual sport menu with login')
    #     test.login(NAME,PASSW)
    #
    #     time.sleep(3)
    #     test.virtual_sport_click()
    #     test.close_driver()


    def test_simple_bet(self):
        '''Checks elements of nav menu with login'''
        test = Action()
        test.show_name('Simple bet')
        test.simple_bet()

        test.close_driver()


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
