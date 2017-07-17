#!/usr/bin/python



from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains
import unittest


class Actions():
    def login(self):
        driver = self.driver
        self.login_button = driver.find_element_by_xpath('//*[@id="page-top"]/div[1]/div[1]/div[2]'
                                                         '/div/div[2]/a[2]/i')
        self.login_button.click()

    def fill_userslogin(self, txt):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="kullanici-adi"]').send_keys(txt)

    def fill_userpassword(self, txt):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sifre"]').send_keys(txt)

    def submitbutton(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sifre"]').click()


class TestWebpage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://tst.bahsegel.info/')

    def test_login(self):
        login_button = Actions.login()
        users_login = Actions.fill_userslogin(self, 'qwerty')
        user_passsword = Actions.fill_userpassword(self, 'xyi')
        subbmit = Actions.submitbutton(self)


if __name__ == '__main__':
    unittest.main()
