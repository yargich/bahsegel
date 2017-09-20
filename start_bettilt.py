#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1.Check Forgot password user
2.Login with credentials.
3.Check top menu :
  Sportsbook, In-play was, Casino, Live Casino, Live Games, Virtual sports,Bonuses
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

#for jenkins
# BASEURL =  sys.argv[1]

class Smoke_Bettilt(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'+self.__class__.__name__


    # def test_01_forgot_password(self):
    #     '''Check forgot password'''
    #     test = BettiltActions()
    #     test.forgot_password_bettilt()
    #
    #     test.close_driver()

    # def test_02_elements_nav_menu(self):
    #     '''Check top menu'''
    #     test = BettiltActions()
    #     test.login("btsaparkar","q1q1q1")
    #     time.sleep(4)
    #     test.top_menu_bettilt()
    #     test.close_driver()

    def test_2_simple_bet(self):
            '''Place simple bet'''

            test_2 = BettiltActions()
            test_2.login("btsaparkar", "q1q1q1")
            time.sleep(3)

            test_2.place_bet_bahsegel(button_name='Sportsbook', multi_bet=False)

            test_2.close_driver()

    # def test_3_multi_bet(self):
    #     '''Place multi bet'''
    #     test = BettiltActions()
    #     test.login("btsaparkar", "q1q1q1", login_button=False)
    #     test.place_bet(multi_bet=True)
    #     test.close_driver()
    #
    # def test_4_casino_slots(self):
    #     '''games in casino slots'''
    #     test_4 = BettiltActions()
    #
    #     test_4.login("btsaparkar", "q1q1q1", login_button=False)
    #     test_4.casino_slots_bettilt()
    #     test_4.close_driver()
    #
    # def test_05_virtual_sport_menu(self):
    #     '''Elements of virtual sport menu '''
    #     test_5 = BettiltActions()
    #     test_5.login("btsaparkar", "q1q1q1")
    #     test_5.virtual_sport_click_bettilt('Virtual sports')
    #     test_5.close_driver()
    #
    # def test_6_user_menu(self):
    #     '''Elements of user menu '''
    #     test_6 = BettiltActions()
    #     test_6.login("btsaparkar", "q1q1q1", login_button=False)
    #     test_6.my_account_bettilt()
    #     test_6.close_driver()
    # def test_7_deposit(self):
    #     '''Checks elements of user menu'''
    #     test_7 = BettiltActions()
    #     test_7.login("btsaparkar", "q1q1q1", login_button=False)
    #     test_7.deposit("Deposit")
    #     test_7.close_driver()
    # #
    # def test_8_registration(self):
    #     test = BahsegelAction()
    #     test.registration()
    #     test.click_users_menu_element(u'ÇIKIŞ YAP')
    #     test.close_driver()

    def tearDown(self):
        pass

if __name__ == '__main__':
    my_args = sys.argv[1:]
    del sys.argv[1:]
    unittest.main(verbosity =2)
