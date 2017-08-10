#!/usr/bin/env python
# -*- coding: utf-8 -*-

from just_actions import *

import unittest,time,sys

class Bahsegel(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'


    def pre_condition(self):
        for i in os.listdir('./'):
            Suff = ['.png','.svg']
            for item in Suff:
                if i.endswith(item):
                    os.remove(i)


    def test_favicon(self):
        ''' Favicon exists'''
        test = Action()

        test.get_favicon()
        test.close_driver()
    def test_02(self):
        ''' Logo exists'''
        self.pre_condition()
        test = Action()
        test.logo_exist()
        test.close_driver()

    def test_03(self):
        '''check url for logo'''
        suff = '/img/logo.svg'
        test = Action()
        etalon_url = BASEURL+suff
        getting_url = test.logo_url()
        print getting_url
        self.assertEqual(getting_url,etalon_url)
        test.close_driver()

    def test_04(self):
        '''check url on login page'''
        test = Action()

        link_to_login = test.enter_to_page()
        self.assertEqual(link_to_login[0], link_to_login[1])
        test.close_driver()
    def test_05(self):
        '''checks forgot_password button value'''
        test=Action()

        current_value = test.forgot_password()
        self.assertEqual( u"Şifremi Unuttum?", current_value)
        test.close_driver()



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
