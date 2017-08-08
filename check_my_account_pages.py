#!/usr/bin/env python
# -*- coding: utf-8 -*-

from just_actions import *

import unittest,time,sys

class Bahsegel(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'

    def test_elements_of_user_menu(self):
        '''Checks elements of user menu'''
        test = Action()
        test.my_account()
        test.close_driver()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
