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


from just_actions import Bahsegel
import unittest,time,sys

class SmokeBahsegel(unittest.TestCase):
    def setUp(self):
        print 'Testing now...'+self.__class__.__name__
    def test_01_forgot_password(self):
        '''Check forgot password'''
        test = Bahsegel()
        test.enter_site()
        test.forgot_password()
        test.driver.close()

    def test_02_show_passw(self):
        '''Check show password'''
        test_2 = Bahsegel()
        test_2.enter_site()
        test_2.login('Bahsegel_26' ,'qwerty26',show_pass=True)
        test_2.enter_site()
        time.sleep(5)
        test_2.driver.close()

    def test_03_elements_nav_menu_with_login(self):
        '''Check nav menu elements'''
        test_3 = Bahsegel()
        test_3.enter_site()
        test_3.login("Bahsegel_26",'qwerty26')
        test_3.top_menu()
        test_3.driver.close()

    def test_04_elements_nav_menu_without_login(self):
        '''Check nav menu elements '''
        test_3 = Bahsegel()
        test_3.top_menu()
        test_3.driver.close()

    def test_04_simple_bet(self):
        '''Place simple bet'''
        test_4 = Bahsegel()
        test_4.enter_site()
        test_4.login("Bahsegel_26", 'qwerty26')
        time.sleep(3)
        test_4.place_bet_bahsegel()
        test_4.driver.close()

    def test_05_multi_bet(self):
        '''Place multi bet'''
        test_5 = Bahsegel()
        test_5.enter_site()
        test_5.login("Bahsegel_26", 'qwerty26')
        time.sleep(3)
        test_5.place_bet_bahsegel(multi_bet=True)
        test_5.driver.close()

    def test_06_casino_slots(self):
        '''games in casino slots'''
        test_6 = Bahsegel()
        test_6.enter_site()

        test_6.login("Bahsegel_26", 'qwerty26')
        time.sleep(5)
        test_6.casino_slots()
        test_6.driver.close()

    def test_07_virtual_sport_menu(self):
        '''Elements of virtual sport menu '''
        test_7 = Bahsegel()
        test_7.enter_site()
        test_7.login("Bahsegel_26", 'qwerty26')
        time.sleep(5)
        test_7.virtual_sport_click()
        test_7.driver.close()

    def test_08_user_menu(self):
        '''Elements of user menu '''
        test_8 = Bahsegel()
        test_8.enter_site()
        test_8.login("Bahsegel_26", 'qwerty26')
        test_8.usermenu_click()
        test_8.driver.close()

    def test_09_deposit(self):
        '''Create deposite'''
        test_9 = Bahsegel()
        test_9.enter_site()
        test_9.login("Bahsegel_26", 'qwerty26')
        test_9.deposit()
        test_9.driver.close()

    def test_10_registration(self):
        '''Register of user '''
        test_10 = Bahsegel()
        test_10.enter_site()
        test_10.registration()
        test_10.usermenu_click()
        test_10.driver.close()

    def test_11_withdraw(self):
        '''Try to make withdraw request'''
        test_11 = Bahsegel()
        test_11.enter_site()
        test_11.withdraw_request(100)
        test_11.driver.close()

    def test_12_forgot_password(self):
        '''Check forgot password'''
        test = BahsegelChrome()
        test.forgot_password()
        test.driver.close()

    def test_13_show_passw(self):
        '''Check show password'''
        test_2 = BahsegelChrome()
        test_2.enter_site()
        test_2.login('Bahsegel_26' ,'qwerty26',show_pass=True)
        time.sleep(5)
        test_2.driver.close()

    def test_14_elements_nav_menu(self):
        '''Check nav menu elements'''
        test_3 = BahsegelChrome()
        test_3.enter_site()
        test_3.login("Bahsegel_26",'qwerty26')
        time.sleep(4)
        test_3.top_menu()
        test_3.driver.close()

    def test_15_simple_bet(self):
        '''Place simple bet'''
        test_4 = BahsegelChrome()
        test_4.enter_site()
        test_4.login("Bahsegel_26", 'qwerty26')
        time.sleep(3)
        test_4.place_bet_bahsegel()
        test_4.driver.close()

    def test_16_multi_bet(self):
        '''Place multi bet'''
        test_5 = BahsegelChrome()
        test_5.enter_site()
        test_5.login("Bahsegel_26", 'qwerty26')
        time.sleep(3)
        test_5.place_bet_bahsegel(multi_bet=True)
        test_5.driver.close()


    def test_17_casino_slots(self):
        '''games in casino slots'''
        test_6 = BahsegelChrome()
        test_6.enter_site()
        # time.sleep(5)
        test_6.login("Bahsegel_26", 'qwerty26')
        time.sleep(5)
        test_6.casino_slots()
        test_6.driver.close()

    def test_18_virtual_sport_menu(self):
        '''Elements of virtual sport menu '''
        test_7 = BahsegelChrome()
        test_7.enter_site()
        test_7.login("Bahsegel_26", 'qwerty26')
        time.sleep(5)
        test_7.virtual_sport_click()
        test_7.driver.close()


    def test_19_user_menu(self):
        '''Elements of user menu '''
        test_8 = BahsegelChrome()
        test_8.enter_site()
        test_8.login("Bahsegel_26", 'qwerty26')

        test_8.usermenu_click()
        test_8.driver.close()

    def test_20_deposit(self):
        '''Create deposite'''
        test_9 = BahsegelChrome()
        test_9.enter_site()
        test_9.login("Bahsegel_26", 'qwerty26')
        test_9.deposit()
        test_9.driver.close()

    def test_21_registration(self):
        '''Register of user '''
        test_10 = BahsegelChrome()
        test_10.enter_site()
        test_10.registration()
        test_10.usermenu_click()
        test_10.driver.close()

    def test_22_withdraw(self):
        '''Try to make withdraw request'''
        test_11 = BahsegelChrome()
        test_11.enter_site()
        test_11.withdraw_request(100)
        test_11.driver.close()

    def tearDown(self):
        pass



if __name__ == '__main__':
    my_args = sys.argv[1:]
    del sys.argv[1:]
    unittest.main(verbosity =2)
