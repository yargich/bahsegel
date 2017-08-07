from just_actions import *

import unittest, time, sys


class BahsegelBet(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'


    # def test_multy_bet(self):
    #     '''Place multy bet'''
    #     test = Action()
    #
    #     test.multy_bet(2)
    #
    #     test.close_driver()

    def test_11(self):
        '''Place simple bet'''
        test = Action()

        test.simple_bet()
        test.close_driver()






        def tearDown(self):
            pass


if __name__ == '__main__':
    unittest.main()
