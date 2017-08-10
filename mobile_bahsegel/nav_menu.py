#!/usr/bin/env python
# -*- coding: utf-8 -*-

from just_actions import *

import unittest,time,sys

class Bahsegel(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'


    def test_elements_nav_menu_without_login(self):
        '''Checks elements of nav menu without login'''
        test = Action()

        test.check_top_menu()
        test.close_driver()

    def test_quantity_elements_nav_menu(self):
        '''counts quantity of elements in nav menu'''
        test = Action()

        test.login(NAME, PASSW)

        self.assertEqual(test.check_top_menu(),7)
        test.close_driver()

    def test_nav_menu_login(self):
        '''Checks elements of nav menu with login'''
        test = Action()

        test.login(NAME,PASSW)
        time.sleep(5)
        test.check_top_menu()
        test.close_driver()


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
