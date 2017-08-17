#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

class Fire(Singleton):
    def __init__(self):
        self.url = 'https://tst.bahsegel.info'
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

        self.driver.implicitly_wait(50)

    def login(self, name, passw):
        '''Login to site with creds'''
        driver = self.driver

        driver.find_element_by_id('login-Button').click()
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(name)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(passw)
        driver.find_element_by_id('loginBtnSubmit').click()
        # print "\nLogin with users name {0} and password {1} was successfull...\n".format(NAME,PASSW)
        # return 'login successfull'

    def check_top_menu(self):
        driver = self.driver
        self.login()
        menu_titles = [u'SPOR BAHİSLERİ', u'CANLI BAHİS', u'CASİNO', u'CANLI CASİNO', u'Sanal Sporlar',
                       u'CANLI OYUNLAR', u"Bonus"]
        for item in menu_titles:
            driver.find_element_by_link_text(item).click()


f1 = Fire()
f1.login("Bahsegel_26","qwerty26")

f1.check_top_menu()