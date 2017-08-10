#!/usr/bin/env python
# -*- coding: utf-8 -*-

from just_actions import *

import unittest,time,sys

class Bahsegel(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'

    def test_deposit(self):
        test = Action()
        test.deposit()


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
