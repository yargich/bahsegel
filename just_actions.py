#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, time
import webbrowser,os,sys, random
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select


BASEURL = 'https://tst.bahsegel.info'

NAME = "Bahsegel_26"
PASSW = "qwerty26"

class Email():
    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.get('https://mailinator.com/')
    def enter_value(self,value):
        self.driver.find_element_by_xpath('//*[@id="inboxfield"]').send_keys(value)
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[3]/div[2]/div[2]/div[1]/span/button').click()
        time.sleep(10)


class Action():
    def __init__(self):
        self.url = BASEURL
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1800, 1800)
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.personal_suffix = random.randint(0,123999)

    def get_favicon(self):
        favicon_url= self.url+'/favicon.png'
        print favicon_url
        picture = requests.get(favicon_url, auth=('beta5', 'gamma8'))
        code = picture.status_code

        if code == 200:
            filename = open('favicon.png', 'wb')
            filename.write(picture.content)
            filename.close()

            return filename.name
    def get_picture(self,picture):
        '''open localy file logo.svg'''
        file_name = picture
        path_to_picture = '/img/'+file_name
        try:
            file = open(file_name)
            os.remove(file_name)
        except IOError as e:
            path_to_picture = '/'+picture
            pic  = requests.get(self.url+path_to_picture, auth=('beta5', 'gamma8'))
            code = pic .status_code
            if code == 200:
                filename = open(picture,'wb')
                filename.write(pic.content)
                filename.close()

                return filename.name

    def get_logo(self):
        '''open localy file logo.svg'''
        file_name = 'logo.svg'
        path_to_picture = '/img/'+file_name
        try:
            file = open(file_name)
            os.remove(file_name)
        except IOError as e:
            path_to_picture = '/img/logo.svg'
            picture = requests.get(self.url+path_to_picture, auth=('beta5', 'gamma8'))
            code = picture.status_code
            if code == 200:
                filename = open('logo.svg','wb')
                filename.write(picture.content)
                filename.close()

                return filename.name
    def open_svg_in_browser(self):
        '''open saved localy logo.svg in browser'''
        filename = self.get_logo()
        webbrowser.open_new_tab('file://' + os.path.realpath(filename))

    def signup_button(self):
        driver = self.driver
        driver.find_elements_by_class_name('header-login')[0].click()
        # for i in driver.find_elements_by_class_name('header-login'):
        #     print i.click()


    def input(self,id,value):
        driver =self.driver
        driver.find_element_by_id(id).send_keys(value)


    def drop_down(self,id,value):
        select  = Select(self.driver.find_element_by_id(id))
        select.select_by_value(value)

    def generate_int(self):
        return self.personal_suffix

    def generate_NewUserName(self,name):
        return name
    def go_to_mail(self):
        new_driver = self.driver.get('https://www.mailinator.com/')
        return new_driver.find_element_by_xpath('//*[@id="inboxfield"]').send

    def registration(self):
        driver = self.driver
        self.signup_button()
        NewName =  'bahsegel'+str(self.generate_int())
        email_provider = 'mailinator.com'
        mail = NewName + '@' + email_provider

        self.input('gamingtec_register_username',NewName)
        self.input('gamingtec_register_password', 'qazwsx123')
        self.input('gamingtec_register_repeatPassword', 'qazwsx123')

        self.input('gamingtec_register_email', mail)
        self.input('gamingtec_register_repeatEmail',mail)

        select = Select(self.driver.find_element_by_id('gamingtec_register_securityQuestion'))
        select.select_by_value('What is your date of birth?')



        self.input('gamingtec_register_securityAnswer', '11.07.1970')


        select_currency = Select(self.driver.find_element_by_id('currencySelect'))
        select_currency.select_by_index(2)


        self.input('gamingtec_register_firstName','Omar')

        self.input('gamingtec_register_lastName', 'Asker')
        select_gender =Select(self.driver.find_element_by_id('gamingtec_register_gender'))
        select_gender.select_by_value('M')


        select_birth_day =Select(self.driver.find_element_by_id('gamingtec_register_birthDate_day'))
        select_birth_day.select_by_value('11')

        select_birth_month = Select(self.driver.find_element_by_id('gamingtec_register_birthDate_month'))
        select_birth_month.select_by_value('7')

        select_birth_year =Select(self.driver.find_element_by_id('gamingtec_register_birthDate_year'))
        select_birth_year.select_by_value('1970')

        self.input('gamingtec_register_address','Harbiye Mahallesi, Cumhuriyet  50')
        self.input('gamingtec_register_postalCode', '34367')
        self.input('gamingtec_register_city','Istanbul')
        select_country = Select(self.driver.find_element_by_id('gamingtec_register_country'))
        select_country.select_by_value('TN')
        select_country.select_by_value('TR')
        self.input('gamingtec_register_mobilePhone', '902123156000')

        time.sleep(2)
        self.driver.find_elements_by_xpath('//*[@id="gamingtec_register_receiveEmail"]')[0].click()

        self.driver.find_elements_by_xpath('//*[@id="gamingtec_register_agreeTermAndConditions"]')[0].click()


        self.driver.find_element_by_xpath('//*[@id="bodyScope"]/div[1]/div[3]/div[1]/form/button').click()


        go_to_mail = Email()
        go_to_mail.enter_value(NewName)



    def enter_to_page(self):
        url = self.url
        driver = self.driver
        self.driver.get(self.url)
        driver.find_element_by_id('login-Button').click()
        link_to_login = url + "/tr/login"
        current_url = self.driver.current_url
        print "current_url is {0}".format(current_url)
        return link_to_login, current_url

    def click_registration(self):
        '''open registration page'''
        driver = self.driver
        button_xpath ='//*[@id="bodyScope"]/header[1]/div/div[2]/a[1]/span'
        button_name = driver.find_element_by_xpath(button_xpath).text
        driver.find_element_by_link_text(button_name).click()
        current_url = driver.current_url
        print current_url
        return current_url

    def login(self,name,passw):
        driver = self.driver

        driver.find_element_by_id('login-Button').click()
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(name)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(passw)
        subbutton_xpath = '//*[@id="loginBtnSubmit"]'
        driver.find_element_by_xpath(subbutton_xpath).click()
        print "\nLogin with users name {0} and password {1} was successfull...\n".format(NAME,PASSW)
        return 'login successfull'

    def login_redirect(self, name, passw):
        driver = self.driver
        base_url = self.url + "/tr/login"
        driver.find_element_by_id('login-Button').click()
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(name)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(passw)
        driver.find_element_by_id('loginBtnSubmit').click()
        current_url = driver.current_url
        user_id = driver.find_element_by_class_name('userId').text
        print  user_id
        return current_url, base_url

    def enter_to_virtual_sport(self):
        driver = self.driver
        virtual_sports_xpath = './/*[@id="bodyScope"]/header[1]/nav/div/ul/li[5]/a'
        virtual_sport_button = driver.find_element_by_xpath(virtual_sports_xpath)
        virtual_sport_button.click()
        # name_of_button = virtual_sport_button.text
        # print name_of_button


    def logo_url(self):
        '''check url of logo '''
        driver = self.driver
        driver.find_element_by_css_selector("img.logo").click()
        logo = driver.find_element_by_css_selector("img.logo").get_attribute("src")
        return logo

    def logo_exist(self):
        '''check url of logo '''
        driver = self.driver
        if driver.find_element_by_css_selector("img.logo").click():
            return 'Logo exists'


    def check_top_menu(self):
        driver = self.driver
        base_xpath = '//*[@id="bodyScope"]/header[1]/nav/div/ul/li'
        top_menu = driver.find_elements_by_xpath(base_xpath)
        num_of_element = len(top_menu)
        i = 1
        while i < num_of_element:
            new_xpath = base_xpath + '[' + str(i) + ']' + '/a'
            driver.find_element_by_xpath(new_xpath).click()
            element_name = driver.find_element_by_xpath(new_xpath)
            print(element_name.text)
            i += 1
        return num_of_element - 1

    def forgot_password(self):
        driver = self.driver
        driver.find_element_by_id('login-Button').click()
        forgot_password = driver.find_element_by_xpath('//*[@id="bodyScope"]/div[1]/div[3]/div/div[2]/form/div[4]/div[1]/a')
        forgot_password.click()
        value = forgot_password.text
        time.sleep(5)
        return value
    def soccer_button(self):
        driver =self.driver
        base_xpath = '//*[@id="bodyScope"]/div[1]/div/ul/li[1]'
        driver.find_element_by_xpath(base_xpath).click()
        name = driver.find_element_by_xpath(base_xpath).text
        print name,'is ok...'

    def basquet_button(self):
        driver = self.driver
        base_xpath = '//*[@id="bodyScope"]/div[1]/div/ul/li[2]'
        driver.find_element_by_xpath(base_xpath).click()
        name = driver.find_element_by_xpath(base_xpath).text
        print name,'is ok...'

    def greyhounds_button(self):
        driver = self.driver
        base_xpath = '//*[@id="bodyScope"]/div[1]/div/ul/li[3]'
        driver.find_element_by_xpath(base_xpath).click()
        name = driver.find_element_by_xpath(base_xpath).text
        print name,'is ok...'


    def horseracing_button(self):
        '''click on button '''
        driver = self.driver
        base_xpath = '//*[@id="bodyScope"]/div[1]/div/ul/li[4]'
        driver.find_element_by_xpath(base_xpath).click()
        name = driver.find_element_by_xpath(base_xpath).text
        print name,'is ok...'

    def tennis_button(self):
        driver = self.driver
        base_xpath = '//*[@id="bodyScope"]/div[1]/div/ul/li[5]'
        driver.find_element_by_xpath(base_xpath).click()
        name = driver.find_element_by_xpath(base_xpath).text
        print name,'is ok...'


    def virtual_sport_click(self):
        driver = self.driver
        self.enter_to_virtual_sport()
        self.tennis_button()
        self.horseracing_button()
        self.greyhounds_button()
        self.basquet_button()
        self.soccer_button()

    def open_result_in_browser(self, filename = "nosetests.html"):
        '''opens results in Chrome'''
        pass

        # webbrowser.open(filename)


    def switch_frame(self):
        driver = self.driver
        my_frame = driver.find_element_by_id('sport_iframe_1')
        driver.switch_to.frame(my_frame)

    def close_driver(self):
        self.driver.quit()
    def enter_registered_users(self,user_name,user_login):
        self.login(user_name,user_login)
        self.close_driver()
    def close_all(self):
        sys.exit()
    def if_logo_are_exists(self):
        self.logo_url()
        self.logo_exist()


    def multy_bet(self, value=2):
        '''place a multi bet'''
        driver = self.driver
        self.driver.set_window_size(1800, 1800)
        self.login(NAME, PASSW)
        my_frame = driver.find_element_by_id('sport_iframe_1')
        driver.switch_to.frame(my_frame)
        row = driver.find_elements_by_class_name('leftMenuIcon')
        row[0].click()

        driver.find_element_by_xpath('//*[@id="mCSB_8_container"]/div[1]/div[2]/div[2]/a[1]/div[2]').click()
        driver.find_element_by_xpath('//*[@id="mCSB_8_container"]/div[2]/div[2]/div[2]/a[1]/div[1]').click()

        driver.switch_to.default_content()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.switch_to.frame(my_frame)
        time.sleep(1)
        driver.find_element_by_id("betAmountInput").clear()
        driver.find_element_by_id("betAmountInput").send_keys(value)

        driver.find_element_by_class_name('btn_bet').click()
        congrat_etalon_text = u"Bahis oynanmıştır.\nİyi Şanslar!"
        if len(driver.find_element_by_css_selector("div.congratText").text) > 1:
            print (driver.find_element_by_css_selector("div.congratText").text)

    def simple_bet(self,value = 2):
        '''place a bet'''
        driver = self.driver
        self.driver.set_window_size(1800, 1800)
        self.login(NAME,PASSW)
        my_frame = driver.find_element_by_id('sport_iframe_1')
        driver.switch_to.frame(my_frame)
        row = driver.find_elements_by_class_name('leftMenuIcon')
        row[0].click()
        class_name = "prematch_stake_odd_factor"
        driver.find_element_by_class_name(class_name).click()

        # driver.find_element_by_id("betAmountInput").send_keys(value)
        driver.switch_to.default_content()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.switch_to.frame(my_frame)
        driver.find_element_by_id("betAmountInput").clear()
        driver.find_element_by_id("betAmountInput").send_keys(value)
        driver.find_element_by_class_name('btn_bet').click()
        congrat_etalon_text = u"Bahis oynanmıştır.\nİyi Şanslar!"
        if len(driver.find_element_by_css_selector("div.congratText").text)>1:
            print (driver.find_element_by_css_selector("div.congratText").text)

    def my_account(self):
        driver = self.driver
        self.login(NAME,PASSW)
        driver.switch_to.default_content()
        self.user_menu_click()


    def user_menu_click(self,numbers_menu_elements=8):
        i=1
        driver = self.driver
        time.sleep(3)
        while i< numbers_menu_elements:
            driver.find_element_by_class_name('btn-usermenu').click()
            myXPATH = '//*[@id="myAccBtn"]/ul/li[' + str(i) + ']'
            time.sleep(2)
            buttons_name = driver.find_element_by_xpath(myXPATH).text
            driver.find_element_by_xpath(myXPATH).click()
            i += 1


            print buttons_name+" was clicked...\n"

if __name__ == "__main__":
    test = Action()
    # test.multy_bet()
    # test.simple_bet()
    test.registration()


    # test.my_account()
    # test.login(NAME,PASSW)
    # test.open_svg_in_browser()
    # test.forgot_password()
    # test.precondition()
    # test.get_favicon()


    # test.get_picture('favicon.png')
    # test.if_logo_are_exists()
    # test.open_svg_in_browser()
    # test.click_registration()
    # test.enter_registered_users(NAME,PASSW)
    # test.virtual_sport_click()
    # test.login("Bahsegel_26","qwerty26")
    # test.enter_to_virtual_sport()
    # test.virtual_sport_click()

