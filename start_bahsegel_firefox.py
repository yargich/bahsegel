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

class SmokeBahsegel(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'+self.__class__.__name__

    def test_01_landing(self):
        '''Check forgot password'''
        test = Bahsegel()
        test.landing_pages()
        test.driver.close()

    # def test_02_forgot_password(self):
    #     '''Check forgot password'''
    #     test_1 = Bahsegel()
    #     test_1.enter_site()
    #     test_1.forgot_password()
    #     test_1.driver.close()
    #
    # def test_03_show_passw(self):
    #     '''Check show password'''
    #     test_2 = Bahsegel()
    #     test_2.enter_site()
    #     test_2.login('tst_711_0001', 'q1q1q1q1', show_pass=True)
    #     test_2.driver.close()
    #
    # def test_04_live_bet_without_login(self):
    #     '''Check live bet functionality without login'''
    #     test_3 = Bahsegel()
    #     test_3.enter_site()
    #     test_3.live_bet()
    #     test_3.driver.close()
    #
    # def test_05_wrong_login(self):
    #     '''checks errors message'''
    #     test_4 = Bahsegel()
    #     test_4.enter_site()
    #     test_4.login('tst_711_0001', 'q1q1q1q1!')
    #     test_4.close_driver()
    #
    # def test_06_live_bet(self):
    #     '''Check live bet functionality with login'''
    #     test_5 = Bahsegel()
    #     test_5.enter_site()
    #     test_5.login('tst_711_0001', 'q1q1q1q1')
    #     test_5.live_bet()
    #     test_5.driver.close()
    #
    # def test_07_elements_nav_menu_with_login(self):
    #     '''Check top menu elements with_login'''
    #     test_6 = Bahsegel()
    #     test_6.enter_site()
    #     test_6.login('tst_711_0001', 'q1q1q1q1')
    #     test_6.top_menu()
    #     test_6.driver.close()
    #
    # def test_08_elements_nav_menu(self):
    #     '''Check nav menu elements without login'''
    #     test_7 = Bahsegel()
    #     test_7.top_menu()
    #     test_7.driver.close()
    #
    # def test_09_prematch_stake(self):
    #     '''Place simple bet'''
    #     test_8 = Bahsegel()
    #     test_8.enter_site()
    #     test_8.login('tst_711_0001', 'q1q1q1q1')
    #     test_8.prematch_stake()
    #     test_8.driver.close()
    #
    # def test_10_simple_bet(self):
    #     '''Place simple bet'''
    #     test_9 = Bahsegel()
    #     test_9.enter_site()
    #     test_9.login('tst_711_0001', 'q1q1q1q1')
    #     test_9.place_bet_bahsegel()
    #     test_9.driver.close()
    #
    # def test_11_multi_bet(self):
    #     '''Place multi bet'''
    #     test_10 = Bahsegel()
    #     test_10.enter_site()
    #     test_10.login('tst_711_0001', 'q1q1q1q1')
    #     test_10.place_bet_bahsegel(multi_bet=True)
    #     test_10.driver.close()
    #
    # def test_12_casino_slots(self):
    #     '''games in casino slots'''
    #     test_11 = Bahsegel()
    #     test_11.enter_site()
    #     test_11.login('tst_711_0001', 'q1q1q1q1')
    #     test_11.casino_slots()
    #     test_11.driver.close()
    #
    # def test_13_virtual_sport_menu(self):
    #     '''Elements of virtual sport menu '''
    #     test_12 = Bahsegel()
    #     test_12.enter_site()
    #     test_12.login('tst_711_0001', 'q1q1q1q1')
    #     test_12.virtual_sport_click()
    #     test_12.driver.close()
    #
    # def test_14_user_menu(self):
    #     '''Elements of user menu '''
    #     test_13 = Bahsegel()
    #     test_13.enter_site()
    #     test_13.login('tst_711_0001', 'q1q1q1q1')
    #     test_13.usermenu_click('CANLI BAHİS')
    #     test_13.driver.close()
    #
    # def test_15_deposit(self):
    #     '''Create deposite'''
    #     test_14 = Bahsegel()
    #     test_14.enter_site()
    #     test_14.login('tst_711_0001', 'q1q1q1q1')
    #     test_14.deposit()
    #     test_14.driver.close()
    #
    # def test_16_registration(self):
    #     '''Register of user '''
    #     test_16 = Bahsegel()
    #     test_16.enter_site()
    #     test_16.registration()
    #     test_16.click_users_menu_element(u'ÇIKIŞ YAP')
    #     test_16.driver.close()
    #
    # def test_17_withdraw(self):
    #     '''Try to make withdraw request'''
    #     test_17 = Bahsegel()
    #     test_17.enter_site()
    #     test_17.withdraw_request(100)
    #     test_17.driver.close()

    def tearDown(self):
        pass

    if __name__ == '__main__':
        my_args = sys.argv[1:]
        del sys.argv[1:]
        unittest.main(verbosity=2)
