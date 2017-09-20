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



class SmokeLebull(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'+self.__class__.__name__

    def test_01_landing(self):
        '''Check landing pages'''
        test = BahsegelChrome()
        test.landing_pages()
        test.driver.close()

    def test_02_elements_nav_menu(self):
        '''Check top menu with login'''
        test_2 = LebullChrome()
        test_2.login_lebull("Lebull_1","q1q1q1q1")
        test_2.top_menu_2('user-panel-nav')
        test_2.driver.close()

    def test_03_elements_nav_menu(self):
        '''Check top menu without login'''
        test_3 = LebullChrome()
        test_3.top_menu_2('user-panel-nav')
        test_3.driver.close()


    def test_2_simple_bet(self):
        '''Place simple bet'''
        test_2 = LebullChrome()
        test_2.login_lebull("Lebull_1", "q1q1q1q1")
        test_2.place_bet_lebull()
        test_2.driver.close()

    def test_3_multi_bet(self):
        '''Place multi bet'''
        test_3 = LebullChrome()
        test_3.login_lebull("Lebull_1", "q1q1q1q1")
        test_3.multi_place_bet_lebull(multi_bet=True)
        test_3.driver.close()

    def test_4_casino_slots(self):
        '''games in casino slots'''
        test_4 = LebullChrome()
        time.sleep(3)
        test_4.login_lebull("Lebull_1", "q1q1q1q1")
        test_4.casino_slots_le_bull()
        test_4.driver.close()

    def test_5_virtual_sport_menu(self):
        '''Elements of virtual sport menu '''
        test_5 = LebullChrome()
        test_5.login_lebull("Lebull_1", "q1q1q1q1")
        test_5.virtual_sport_click_lebull()
        test_5.driver.close()

    def test_6_user_menu(self):
        '''Elements of user menu '''
        test_6= LebullChrome()
        test_6.login_lebull("Lebull_1", "q1q1q1q1")
        test_6.user_menu_click()
        test_6.driver.close()

    def test_7_deposit(self):
        '''Checks elements of user menu'''
        test_7 = LebullChrome()
        test_7.login_lebull("Lebull_1", "q1q1q1q1")
        test_7.deposit_lebull()
        test_7.driver.close()

    def test_8_withdraw(self):
        test_8 = LebullChrome()
        test_8.login_lebull("Lebull_1", "q1q1q1q1")
        test_8.withdraw_lebull()

    def test_9_registration(self):
        test = LebullChrome()
        test.registration()
        test.click_users_menu_element(u'ÇIKIŞ YAP')
        test.driver.close()

    def tearDown(self):
        pass

if __name__ == '__main__':
    my_args = sys.argv[1:]
    del sys.argv[1:]
    unittest.main(verbosity =2)
