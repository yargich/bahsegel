#!/usr/bin/env python
# -*- coding: utf-8 -*-

from just_actions import *

import unittest,time,sys

class Bahsegel(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'



    def test_04(self):
        '''check url on login page'''
        test = Action()


        link_to_login = test.enter_to_page()
        self.assertEqual(link_to_login[0], link_to_login[1])
        test.close_driver()

    def test_06(self):
        '''successfully login'''
        test = Action()

        test.login(NAME,PASSW)
        test.close_driver()



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
