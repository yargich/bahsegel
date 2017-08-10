#!/usr/bin/env python
# -*- coding: utf-8 -*-

from just_actions import *

import unittest, time, sys


class BahsegelRegistration(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'


    def test_registration(self):
        '''User creates a new account'''
        test = Action()
        test.registration()

        def tearDown(self):
            pass


if __name__ == '__main__':
    unittest.main()
