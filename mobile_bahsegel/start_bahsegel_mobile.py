#!/usr/bin/env python
# -*- coding: utf-8 -*-

from just_actions import *

import unittest,time,sys

class Bahsegel(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'


    # def pre_condition(self):
    #     for i in os.listdir('./'):
    #         Suff = ['.png','.svg']
    #         for item in Suff:
    #             if i.endswith(item):
    #                 os.remove(i)
    #
    #
    # def test_favicon(self):
    #     ''' Favicon exists'''
    #     test = Action()
    #
    #     test.get_favicon()
    #     test.close_driver()
    # def test_02(self):
    #     ''' Logo exists'''
    #     self.pre_condition()
    #     test = Action()
    #     test.logo_exist()
    #     test.close_driver()

    # def test_url_for_logo(self):
    #     '''check url for logo'''
    #     suff = '/img/logo.svg'
    #     test = Action()
    #     etalon_url = BASEURL+suff
    #     getting_url = test.logo_url()
    #     print getting_url
    #     self.assertEqual(getting_url,etalon_url)
    #     test.close_driver()

    # def test_url_login_page(self):
    #     '''check url on login page'''
    #     test = Action()
    #
    #     link_to_login = test.enter_to_page()
    #     self.assertEqual(link_to_login[0], link_to_login[1])
    #     test.close_driver()
    # def test_forgot_password_button_value(self):
    #     '''checks forgot_password button value'''
    #     test=Action()
    #
    #     current_value = test.forgot_password()
    #     self.assertEqual( u"Şifremi Unuttum?", current_value)
    #     test.close_driver()

    # def test_2_successfully_login(self):
    #     '''successfully login'''
    #     test = Action()
    #
    #     test.login(NAME,PASSW)
    #     test.close_driver()

    # def test_1_elements_nav_menu_without_login(self):
    #     '''Checks elements of nav menu without login'''
    #     test = Action()
    #
    #     test.check_top_menu()
    #     test.close_driver()
    #
    # def test_3_quantity_elements_nav_menu(self):
    #     '''counts quantity of elements in nav menu'''
    #     test = Action()
    #
    #     test.login(NAME, PASSW)
    #
    #     self.assertEqual(test.check_top_menu(),7)
    #     test.close_driver()
    #
    # def test_4_nav_menu_login(self):
    #     '''Checks elements of nav menu with login'''
    #     test = Action()
    #
    #     test.login(NAME,PASSW)
    #     time.sleep(5)
    #     test.check_top_menu()
    #     test.close_driver()
    #
    # def test_5_virtual_sport_menu_login(self):
    #     '''Elements of virtual sport menu with login'''
    #     test = Action()
    #     test.login(NAME,PASSW)
    #     time.sleep(3)
    #     test.virtual_sport_click()
    #     test.close_driver()
    #
    # def test_6_multy_bet(self):
    #     '''Place multy bet'''
    #     test = Action()
    #     test.multi_bet(2)
    #     test.close_driver()
    #
    # def test_7_simple_bet(self):
    #     '''Place simple bet'''
    #     test = Action()
    #     test.simple_bet()
    #     test.close_driver()
    #
    # def test_8_elements_of_user_menu(self):
    #     '''Checks elements of user menu'''
    #     test = Action()
    #     test.my_account()
    #     test.close_driver()

    def test_9_deposit(self):
        test =Action()
        test.deposit()

    # def test_registration(self):
    #     test =Action()
    #     test.registration()
    #     test.close_driver()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
