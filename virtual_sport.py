#!/usr/bin/env python
# -*- coding: utf-8 -*-

from just_actions import *

import unittest, time, sys


class BahsegelVirtualSport(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'


    def test_10(self):
        '''Elements of virtual sport menu with login'''
        test = Action()
        test.login(NAME, PASSW)
        time.sleep(3)
        test.virtual_sport_click()
        test.close_driver()


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
