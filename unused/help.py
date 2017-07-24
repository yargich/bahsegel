# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class help(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://tst.bahsegel.info/")
        self.selenium.start()
    
    def test_help(self):
        sel = self.selenium
        sel.open("/tr")
        sel.select_window("null")
        sel.click("css=#login-Button > span")
        sel.wait_for_page_to_load("30000")
        self.assertEqual(u"BahseGel.Com | Online Bahis | Spora heyecan katın", sel.get_title())
        sel.type("id=username", "Bahsegel_26")
        sel.type("id=password", "qwerty26")
        sel.click("id=loginBtnSubmit")
        self.assertEqual(u"BahseGel - Türkiye'nin En İyi Bahis Sitesi | Üye Ol 300 TL Bonus Kazan", sel.get_title())
        self.assertEqual(u"BahseGel.Com | Online Bahis | Spora heyecan katın", sel.get_title())
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
