#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, time

import webbrowser,os,sys, random
from selenium import webdriver


from selenium.webdriver.support.ui import Select
from conf import *

BASEURL = BahsegelTST
NAME = BahsegelLogin
PASSW = BahsegelPassw


class Email():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://mailinator.com/')
    def enter_value(self,value):
        self.driver.find_element_by_xpath('//*[@id="inboxfield"]').send_keys(value)
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[3]/div[2]/div[2]/div[1]/span/button').click()
        # time.sleep(2)
        # self.driver.get('https://www.mailinator.com/v2/inbox.jsp?zone=public&query='+value)
        self.driver.find_element_by_class_name('all_message-min_text').click()
        time.sleep(3)
        self.driver.switch_to.active_element()
        self.driver.find_element_by_xpath("//img[contains(@src,'https://i.hizliresim.com/pWX32z.png')]").click()
        print 'OK'

    # def check_email(self):
    #     self.driver.find_element_by_xpath('//*[@id="row_1502123813-100059284591-qwerty"]/div/div[3]')

class Action():
    def __init__(self):
        self.url = BASEURL
        self.driver = webdriver.Firefox()

        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.login(NAME, PASSW)


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



    def input(self,id,value):
        driver =self.driver
        driver.find_element_by_id(id).send_keys(value)


    def drop_down(self,id,value):
        select  = Select(self.driver.find_element_by_id(id))
        select.select_by_value(value)

    def registration(self):
        driver = self.driver
        self.signup_button()
        users_data = UsersDetails().generate_users_data()
        NewName = users_data[0]
        mail =   users_data[1]

        passw =UsersDetails().passw
        postal_code = UsersDetails().postal_code


        self.input('gamingtec_register_username', NewName)
        self.input('gamingtec_register_password', passw)
        self.input('gamingtec_register_repeatPassword', passw)

        self.input('gamingtec_register_email', mail)
        self.input('gamingtec_register_repeatEmail',mail)

        select = Select(self.driver.find_element_by_id('gamingtec_register_securityQuestion'))
        select.select_by_value('What is your date of birth?')



        self.input('gamingtec_register_securityAnswer', '11.07.1970')


        select_currency = Select(self.driver.find_element_by_id('currencySelect'))
        select_currency.select_by_index(1)


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
        self.input('gamingtec_register_postalCode', postal_code)
        self.input('gamingtec_register_city','Istanbul')
        select_country = Select(self.driver.find_element_by_id('gamingtec_register_country'))

        select_country.select_by_value('TR')
        self.input('gamingtec_register_mobilePhone', '902123156000')

        time.sleep(2)
        self.driver.find_elements_by_xpath('//*[@id="gamingtec_register_receiveEmail"]')[0].click()

        self.driver.find_elements_by_xpath('//*[@id="gamingtec_register_agreeTermAndConditions"]')[0].click()


        self.driver.find_element_by_xpath('//*[@id="bodyScope"]/div[1]/div[3]/div[1]/form/button').click()

        print self.driver.find_element_by_class_name('registration').text
        # go_to_mail = Email()
        # go_to_mail.enter_value(NewName)



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


    def check_top_menuu(self,name,passw):
        driver = self.driver
        self.login(name,passw)
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


    def check_top_menu(self):
        driver = self.driver

        menu_titles = [u'SPOR BAHİSLERİ',u'CANLI BAHİS',u'CASİNO',u'CANLI CASİNO',u'Sanal Sporlar',u'CANLI OYUNLAR',u"Bonus"]
        for item in menu_titles:
            driver.find_element_by_link_text(item).click()

    def forgot_password(self):
        driver = self.driver
        driver.find_element_by_id('login-Button').click()
        forgot_password = driver.find_element_by_xpath('//*[@id="bodyScope"]/div[1]/div[3]/div/div[2]/form/div[4]/div[1]/a')
        forgot_password.click()
        value = forgot_password.text
        time.sleep(2)
        return value, 'is ok...'


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


    def multi_bet(self, value=2):
        '''place a multi bet'''
        driver = self.driver
        # self.driver.set_window_size(1800, 1800)
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
        # self.driver.set_window_size(1800, 1800)
        self.login(NAME,PASSW)
        my_frame = driver.find_element_by_id('sport_iframe_1')
        driver.switch_to.frame(my_frame)
        row = driver.find_elements_by_class_name('leftMenuIcon')
        row[0].click()
        class_name = "prematch_stake_odd_factor"
        driver.find_element_by_class_name(class_name).click()

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



    def click_users_menu_element(self,i=1):
        '''Login 1, Personal information 2, Account verification 3, Deposit 4, Withdraw 5 , Play history 6, Payment history 7, My bonuses 8 '''
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_class_name('btn-usermenu').click()
        myXPATH = '//*[@id="myAccBtn"]/ul/li[' + str(i) + ']'
        time.sleep(1)

        buttons_name = driver.find_element_by_xpath(myXPATH).text
        driver.find_element_by_xpath(myXPATH).click()
        print buttons_name
        return buttons_name
    def select_card(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="bodyScope"]/div[1]/section/ul[2]/li[1]/div/a').click()

        driver.find_element_by_xpath('//*[@id="bodyScope"]/div[1]/section/form/div/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@id="bodyScope"]/div[1]/section/form/div/button/span').click()
        driver.find_element_by_xpath('//*[@id="bodyScope"]/div[1]/section/div[2]/ul/li/a/span').click()
        driver.find_element_by_xpath('//*[@id="bodyScope"]/div[1]/section/form/div/div[2]/button/span').click()
        card = CardDetails()
        number = card.number
        cvv = card.cvv
        exp_data_month =card.exp.split('/')[0]
        exp_data_year = card.exp.split('/')[1]
        driver.find_element_by_id("gamingtec_deposit_creditcard_cardNumber").send_keys(number)
        select_card_details_month = Select(driver.find_element_by_id('gamingtec_deposit_creditcard_expirationMonth'))
        select_card_details_month.select_by_value(exp_data_month)

        select_card_details_year = Select(driver.find_element_by_id('gamingtec_deposit_creditcard_expirationYear'))
        select_card_details_year.select_by_value(exp_data_year)

        driver.find_element_by_id('gamingtec_deposit_creditcard_cvv').click()
        driver.find_element_by_id('gamingtec_deposit_creditcard_cvv').send_keys(cvv)

        driver.find_element_by_xpath('//*[@id="bodyScope"]/div[1]/section/form/div/div[2]/button/span').click()
        message = driver.find_element_by_xpath('//*[@id="inPageMsgBox"]/p/span').text

        return message


    def deposit(self):
        self.login(NAME,PASSW)
        self.click_users_menu_element(3)
        self.select_card()

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

class CardDetails():
    def __init__(self):
        self.number = '4716 0277 1826 2637'
        self.typeCard = 'Visa '
        self.cvv = '641'
        self.exp = '08/2018'
        self.name= 'CODY GUSTMAN'

class UsersDetails:
    def __init__(self):
        self.personal_suffix = str(random.randint(0,99))
        self.passw = 'Qazwsx11'
        self.postal_code =self.generate_postalcode()
    def generate_users_data(self):
        NewUserName = 'tst711_' + str(self.personal_suffix)
        email = NewUserName + '@' + 'mailinator.com'
        return NewUserName,email

    def generate_postalcode(self):
        index_1 = str(random.randint(1,9))
        index_2 = str(random.randint(1, 9))
        index_3 = str(random.randint(1, 9))
        index_4 = str(random.randint(1, 9))
        index_5= str(random.randint(1, 9))
        new_number = index_1+index_2+index_3+index_4+index_5
        return  new_number


if __name__ == "__main__":
    test = Action()
    # test.login(NAME, PASSW)
    test.check_top_menu()


    # test.deposit()
    # test.multy_bet()
    # test.simple_bet()
    # test.registration()




    # test.my_account()

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

    # test.enter_to_virtual_sport()
    # test.virtual_sport_click()

