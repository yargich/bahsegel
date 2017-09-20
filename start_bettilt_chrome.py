#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1.Check Forgot password user
2.Login with credentials.
3.Check top menu :
'SPOR BAHİSLERİ','CANLI BAHİS','CASİNO','CANLI CASİNO','Sanal Sporlar','CANLI OYUNLAR’,’Bonus’
4.Try simple multi bet.

5.Try place multi bet.
6. Check games in casino slots
7.Check virtual sport menu:
	'soccer','basketball','greyhounds','horseracing','tennis'
8. Check games in casino slots
9. Check user menu:
	'HESAP BİLGİLERİ','HESAP DOĞRULAMA','PARA YATIRMA','PARA ÇEKME','BAHİS 	GEÇMİŞİ','HESAP HAREKETLERİ','BONUS GEÇMİŞİ','ÇIKIŞ YAP'

10.Create deposit.
11.Registration of new users.
12.Confirmation of new users registration

'''


from just_actions import *
import unittest,time,sys

class SmokeBettiltChrome(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'+self.__class__.__name__

    # def test_01_forgot_pass(self):
    #     '''Check forgot password '''
    #     test_1 = BettiltChrome()
    #     test_1.forgot_password()
    #     test_1.close_driver()

    # def test_02_elements_nav_no_login(self):
    #     '''Check top menu without login'''
    #     test_2 = BettiltChrome()
    #     test_2.top_menu_bettilt()
    #     test_2.close_driver()

    # def test_03_elements_nav_menu(self):
    #     '''Check top menu'''
    #     test_3 = BettiltChrome()
    #     test_3.login_bettilt('btsaparkar','q1q1q1')
    #
    #     test_3.top_menu_bettilt()
    #     test_3.close_driver()

    # def test_04_simple_bet(self):
    #     '''Place simple bet'''
    #
    #     test_4 = BettiltChrome()
    #     test_4.login_bettilt('btsaparkar','q1q1q1')
    #     test_4.place_bet_bettilt()
    #     test_4.close_driver()
    #
    # def test_05_multi_bet(self):
    #     '''Place multi bet'''
    #     test_5 = BettiltChrome()
    #     test_5.login_bettilt('btsaparkar','q1q1q1')
    #     test_5.place_bet_bettilt(multi_bet=True)
    #     test_5.close_driver()
    #
    def test_06_casino_slots(self):
        '''games in casino slots'''
        test_6 = BettiltChrome()
        test_6.login_bettilt('btsaparkar','q1q1q1')
        test_6.casino_slots_bettilt()
        # test_6.driver.close()
    #
    # def test_5_virtual_sport_menu(self):
    #     '''Elements of virtual sport menu '''
    #     test_5 = BettiltChrome()
    #     test_5.login_lebull("Lebull_1", "q1q1q1q1")
    #     test_5.virtual_sport_click_lebull()
    #     test_5.driver.close()
    #
    # def test_6_user_menu(self):
    #     '''Elements of user menu '''
    #     test_6 = LebullActions()
    #     test_6.login_lebull("Lebull_1", "q1q1q1q1")
    #
    #     test_6.user_menu_click()
    #     test_6.driver.close()
    #
    # def test_7_deposit(self):
    #     '''Checks elements of user menu'''
    #     test_7 = LebullActions()
    #     test_7.login_lebull("Lebull_1", "q1q1q1q1")
    #     test_7.deposit_lebull()
    #
    #     test_7.driver.close()
    #
    # def test_8_registration(self):
    #     test = LebullActions()
    #
    #     test.registration()
    #     test.click_users_menu_element(u'ÇIKIŞ YAP')
    #     test.driver.close()
    def tearDown(self):


        pass



if __name__ == '__main__':
    my_args = sys.argv[1:]
    del sys.argv[1:]
    unittest.main(verbosity =2)
