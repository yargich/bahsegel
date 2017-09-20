# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os,selenium,requests
import traceback

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time, random,sys

# comand_executor = "http://192.168.11.83:4444/wd/hub"
# BASEURL = sys.argv[1]
# BASEURL = "https://beta5:gamma8@stg.bahsegel.info"
# BASEURL = "https://www.bettilt2.com"
# BASEURL = "https://stg.bettilt.com"
# BASEURL = "https://tst.bettilt.com"

# BASEURL = "https://www.bahsegel.com"
# BASEURL = "https://beta5:gamma8@www.bahsegel99.com"
# BASEURL = 'https://preprod.bahsegel.info'
# BASEURL = "https://tst.bahsegel.info"
BASEURL = "https://stg.bahsegel.info"
# BASEURL = "https://beta5:gamma8@wwwlive_casino.lebull.com"
# BASEURL = "https://www.lebull.com"
# BASEURL = "https://stg.lebull.com"
# BASEURL = "https://tst.lebull.com"
Generationed_Users_details = []


class Base(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(50)

class Email():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://mailinator.com/')
        self.new_user_login = Generationed_Users_details[0]
        self.new_user_email = Generationed_Users_details[1]
        self.new_user_password = Generationed_Users_details[2]

    def enter_value(self, value):
        self.driver.find_element_by_xpath('//*[@id="inboxfield"]').send_keys(value)
        self.driver.find_element_by_xpath('/html/body/section[1]/div/div[3]/div[2]/div[2]/div[1]/span/button').click()
        time.sleep(4)
        self.driver.find_element_by_class_name('all_message-min_text').click()


class CardDetails():
    def __init__(self):
        self.number = '4716 0277 1826 2637'
        self.typeCard = 'Visa '
        self.cvv = '641'
        self.exp = '08/2018'
        self.name = 'CODY GUSTMAN'

class UsersDetails:
    def __init__(self):
        self.personal_suffix = str(random.randint(0, 999999))
        self.passw = 'Qazwsx11'
        self.postal_code = self.generate_postalcode()
        self.accountNumber = '1100803777'

    def generate_users_data(self):
        NewUserName = 'tst711_' + str(self.personal_suffix)
        email = NewUserName + '@' + 'mailinator.com'
        return NewUserName, email

    def generate_postalcode(self):
        index_1 = str(random.randint(1, 9))
        index_2 = str(random.randint(1, 9))
        index_3 = str(random.randint(1, 9))
        index_4 = str(random.randint(1, 9))
        index_5 = str(random.randint(1, 9))
        new_number = index_1 + index_2 + index_3 + index_4 + index_5
        return new_number


class Bahsegel(Base):
    def __init__(self):
        super(Bahsegel , self).__init__()
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Remote(comand_executor, webdriver.DesiredCapabilities.FIREFOX)
        self.driver.get(BASEURL)

    def landing_pages(self,num_of_land=5):
        URL = BASEURL+"/landing/"
        for i in range(1,num_of_land):
            NewURL = URL+str(i)
            self.driver.get(NewURL)
            if self.driver.title!='404 Not Found':
                logo = self.driver.find_element_by_tag_name('img').get_attribute('src')
                print "Logo on  landing {} exist...".format(NewURL)
            else:

                print NewURL, "It is doesnt exist"
                break

    def submit_button(self, id='loginBtnSubmit'):
        self.driver.find_element_by_id(id).click()

    def enter_site(self):
        self.submit_button('login-Button')

    def login_bettilt(self, usr, passw):
        self.login(usr, passw)
        self.submit_button('loginBtnSubmit')
        time.sleep(4)

    def login(self, name, passw, show_pass=False,class_name = 'submit-button'):
        '''Login to site with creds'''

        self.driver.find_element_by_id('username').send_keys(name)
        self.driver.find_element_by_id('password').send_keys(passw)
        if show_pass:
            self.show_password('show-password')
        time.sleep(2)

        # To make separate function
        # self.driver.find_element_by_class_name(class_name).click()

        # time.sleep(5)
        # self.submit_button()
        # user = self.driver.find_element_by_id('userId').text
        # if len(user)<1:
        #     print 'Login is Failed ...'
        #     error_msg = self.driver.find_element_by_class_name('errors').text
        #     print error_msg
        #     return error_msg
        #
        # else:
        #     print 'Login is ok...'
        #     print user





    def forgot_password(self):
        self.driver.find_element_by_css_selector('a.btn.btn-login').click()

        login_url = BASEURL + '/tr/login'
        time.sleep(4)
        if login_url == self.driver.current_url:
            self.driver.find_element_by_link_text(u'Şifremi Unuttum?').click()
            time.sleep(3)
            self.driver.find_element_by_css_selector('button.btn.btn-default').click()
            time.sleep(5)
        else:
            print 'Something went wrong...'


    def show_password(self, class_name):
        time.sleep(3)
        self.driver.find_element_by_class_name(class_name).click()

        return 'show password is ok...'
    def live_bet(self):
        self.click_on_menu()
        time.sleep(3)
        my_frame = self.driver.find_element_by_id('sport_iframe_1')
        self.driver.switch_to.frame(my_frame)
        sub_menu=[]
        for sub_element in self.driver.find_elements_by_class_name('sportSubheadMenu')[0].text:
            sub_menu.append(sub_element)
        new_sub_menu = ''.join(sub_menu).split('\n')
        for key in new_sub_menu:
            self.driver.find_element_by_link_text(key).click()
            print key , ' is ok...'
            time.sleep(3)
    def live_bet_lebull(self):
        self.click_on_menu('In-play')
    def click_on_menu(self,class_name = 'nav-menu', mainKey = u'CANLI BAHİS'):

        menu = (self.driver.find_elements_by_class_name(class_name)[0].text).split('\n')
        for key in menu:
            if key == mainKey:
                self.driver.find_element_by_link_text(mainKey).click()
                break
        print mainKey, ' is ok...'
        time.sleep(5)

    def virtual_sport_button(self, class_name):
        # driver = self.driver
        name = self.driver.find_element_by_class_name(class_name).text
        self.driver.find_element_by_class_name(class_name).click()
        print name, 'is ok...\n'

    def my_account_button(self, class_name):
        self.driver.find_element_by_class_name(class_name).click()
        time.sleep(10)
        button_name = self.driver.find_element_by_class_name(class_name).text
        print button_name
        time.sleep(10)
        return button_name + ' is ok'

    def withdraw_lebull(self):
        self.driver.find_element_by_class_name('user').click()
        time.sleep(4)
        # self.driver.find_elements_by_class_name('list-unstyled')
        self.driver.find_element_by_partial_link_text('Withdraw').click()
        time.sleep(5)
        self.driver.find_element_by_class_name('btn-lg').click()

    def withdraw_request(self, value=100):
        accountNumber = UsersDetails().accountNumber
        self.driver.find_element_by_class_name('myAccBtn').click()
        self.my_account_button('myAccBtn')
        self.driver.find_element_by_class_name('atm').click()
        self.driver.find_element_by_xpath('//*[@id="pageContent"]/section/content/section/ul[2]/li[10]/div/a').click()
        self.driver.find_element_by_id('withdrawal-amount-field').send_keys(value)
        self.driver.find_element_by_xpath(
            '//*[@id="pageContent"]/section/content/section/form/div[1]/div[2]/span').click()
        time.sleep(1)
        self.driver.find_element_by_id('gamingtec_withdrawal_account_accountNumber').send_keys(accountNumber)
        self.driver.find_element_by_xpath('//*[@id="pageContent"]/section/content/section/form/div[2]/button').click()
        print "Withdraw request {} was successfull".format(100)
        return 'Successfully'

    def enter_to_virtual_sport(self, button_title):
        self.driver.find_element_by_link_text(button_title).click()

    def virtual_sport_click(self, button_title=u'Sanal Sporlar'):
        self.enter_to_virtual_sport(button_title)
        class_names = ['basketball', 'greyhounds', 'horseracing', 'tennis', 'soccer', ]
        time.sleep(4)
        for title in class_names:
            self.virtual_sport_button(title)
            # insert checking of loading page'''
            self.driver.find_element_by_class_name(title).click()

    def casino_slots(self, en=False):
        if en:
            nav_menu = Leng().user_menu_title_en
            submenu = Leng().submenu_en

        else:
            nav_menu = Leng().user_menu_title
            submenu = Leng().submenu_tr
        game_buttons = []

        self.driver.find_element_by_link_text(nav_menu[2]).click()
        self.driver.find_element_by_link_text(submenu[1]).click()
        time.sleep(6)
        for i in self.driver.find_elements_by_class_name('title'):
            title = i.text.replace('\nYeni', '')
            game_buttons.append(title)
            print title
        quantity_of_games = len(game_buttons)
        print "{} are available...".format(quantity_of_games)
        return game_buttons

    def switch_frame(self, frame_name):
        my_frame = self.driver.find_element_by_id(frame_name)
        self.driver.switch_to.frame(my_frame)

    def prematch_stake(self):
        time.sleep(4)
        my_frame = self.driver.find_element_by_id('sport_iframe_1')
        self.driver.switch_to.frame(my_frame)
        self.driver.find_elements_by_class_name('leftMenuIcon')[0].click()
        time.sleep(3)
        self.driver.find_elements_by_class_name('prematch_stake_odd_name')[0].click()


        # if multi_bet:
        #     time.sleep(2)
            # row[4].click()
            # self.driver.find_elements_by_class_name('Decimal')[4].click()

        self.driver.find_element_by_class_name("prematch_stake_odd_factor").click()
        prematch_stake = self.driver.find_element_by_class_name("prematch_stake_odd_factor").text
        print "prematch stake is {}".format(prematch_stake)
        return len(prematch_stake)

    def place_bet_bahsegel(self, value=2, multi_bet=False):
        '''place a bet'''
        #
        time.sleep(6)
        # self.driver.implicitly_wait(10)
        my_frame = self.driver.find_element_by_id('sport_iframe_1')
        self.driver.switch_to.frame(my_frame)
        self.driver.find_elements_by_class_name('leftMenuIcon')[0].click()
        time.sleep(4)

        self.driver.find_elements_by_class_name('prematch_stake_odd_name')[0].click()

        # if multi_bet:
        #     time.sleep(2)
        #     # row[4].click()
        #     self.driver.find_elements_by_class_name('Decimal')[4].click()
        prematch_stake = self.driver.find_element_by_class_name("prematch_stake_odd_factor").text
        print "prematch stake is {}".format(prematch_stake)
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.driver.switch_to.frame(my_frame)
        coupon_factor = self.driver.find_element_by_class_name('coupon_factor').text
        self.driver.find_element_by_class_name('amount').send_keys(value)


        # assert (prematch_stake!=coupon_factor)
        self.driver.find_element_by_class_name('btn_bet').click()

        time.sleep(12)

        # self.driver.find_element_by_id("betAmountInput").clear()
        # self.driver.find_element_by_id("betAmountInput").send_keys(value)
        #
        # self.driver.find_element_by_class_name('btn_bet').click()
        # time.sleep(5)


    def click_top_menu(self, name, en=True):
        # clicks on determined users element define' in variable 'name
        driver = self.driver
        if en:
            menu_titles = Leng().user_menu_title_en
        else:
            menu_titles = Leng().user_menu_title
        for item in menu_titles:
            if item == name:
                driver.find_element_by_link_text(item).click()
                return name + ' was clicked...'

    def top_menu_all_clicks_bettilt(self):
        # Clicked on all top menu elements.
        titles = self.driver.find_elements_by_class_name('nav-menu')[0].text
        menu = titles.split('\n')
        for item in menu:
            print item

    def place_bet(self, value=2, multi_bet=False, button_name=u'SPOR BAHİSLERİ'):
        '''place a bet'''
        driver = self.driver
        self.click_top_menu(button_name)

        my_frame = driver.find_element_by_id('sport_iframe_1')
        driver.switch_to.frame(my_frame)
        row = driver.find_elements_by_class_name('leftMenuIcon')
        if multi_bet is False:
            row[0].click()
        else:
            row[0].click()
            time.sleep(2)
            row[0].click()
        driver.find_element_by_class_name("prematch_stake_odd_factor").click()

        driver.execute_script("window.scrollTo(0, 200);")
        driver.find_element_by_id("betAmountInput").clear()
        driver.find_element_by_id("betAmountInput").send_keys(value)
        driver.find_element_by_class_name('btn_bet').click()
    def get_url(self,url):
        from urlparse import urlparse
        o = urlparse(url)
        name = o.netloc
        new_name = name.split('.')[1]
        print new_name

        return new_name
    # def top_menu_lebull(self):
    #     self.top_menu()
    def top_menu(self, class_name='nav-menu'):
        # Clicked on all top menu elements.
        name = self.get_url(BASEURL)
        menu = (self.driver.find_elements_by_class_name(class_name)[0].text).split('\n')
        for i in menu:
            if name== 'bahsegel':
                source_url = [BASEURL + '/', BASEURL + '/canli-bahis', BASEURL + '/online-casino', BASEURL + '/canli-casino',
                                  BASEURL + '/sanal-sporlar#soccer', BASEURL + '/canli-oyunlar', BASEURL + '/tr/bonuses']
            elif name == 'bettilt':
                #  'Sportsbook',  'In-play', u'Virtual sports', u'Casino', u'Live casino', u'Live games', u'Bonuses']
                source_url = [BASEURL + '/en#prematch', BASEURL + '/en/in-play#live/event/1936132', BASEURL + '/en/virtual-sports#soccer',
                              BASEURL + '/en/casino',BASEURL + '/en/casino/live-casino', BASEURL + '/en/virtual-games', BASEURL + '/en/bonuses']
            elif name == 'lebull':
                #  'Sportsbook',  'In-play', u'Casino', u'Virtual sports', u'Live games', u'Live casino',  u'Bonuses']
                source_url = [BASEURL + '/en#prematch', BASEURL + '/en/in-play#live/event/1936132',
                              BASEURL + '/en/virtual-sports#soccer',
                              BASEURL + '/en/casino', BASEURL + '/en/casino/live-casino', BASEURL + '/en/virtual-games',
                              BASEURL + '/en/bonu']

            else:
                source_url = [BASEURL + '/en/sportsbook', BASEURL + '/en/sportsbook#live', BASEURL + '/en/casino',
                              BASEURL + '/en/casino/live-casino',
                              BASEURL + '/en/virtual-games', BASEURL + '/en/virtual-sports', BASEURL + '/en/bonuses']


        index = -1
        for i in xrange(0,len(menu)):
            try:
                index +=1
                print menu[i], ' is testing...'
                self.driver.find_element_by_partial_link_text(menu[i]).click()

                # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                #
                # time.sleep(6)
                print menu[i], ' is ok...'
                if self.driver.current_url != source_url[index]:
                    print menu[i] + ' is broken...'
                    print 'current_url {}'.format(self.driver.current_url)
                    print  'source_url {}'.format(source_url[index])


            except:
                self.driver.find_element_by_xpath('//*[@id="bodyScope"]/header[1]/nav/div/ul/li[' + str(index) + ']').click()
                print self.driver.find_element_by_xpath(
                    '//*[@id="bodyScope"]/header[1]/nav/div/ul/li[' + str(index) + ']').text , ' is ok...'
                index += 1
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def top_menu_bettilt(self):
        self.top_menu_2('main-menu')

    def top_menu_mobile(self):
        time.sleep(5)
        click_menu = self.driver.find_element_by_class_name('controls-left-mainmenu')
        # time.sleep(10)
        click_menu.click()

        menu = self.driver.find_elements_by_css_selector('div.header-menu.header-menu-main')[0].text.split('\n')
        for element in menu[1:]:
            self.driver.find_element_by_partial_link_text(element).send_keys(Keys.RETURN)
            print element, ' is ok...'
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_css_selector('button.btn.btn-mainmenu').click()

    def top_menu_2(self, class_name='nav-menu'):
        name = self.get_url(BASEURL)
        menu = (self.driver.find_elements_by_class_name(class_name)[0].text).split('\n')
        index = -1
        for i in xrange(0, len(menu)):
            index += 1
            print menu[i], ' is testing...'
            self.driver.find_element_by_partial_link_text(menu[i]).click()
            time.sleep(12)
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def usermenu_click(self, stop_word):
        self.driver.find_element_by_class_name('btn-usermenu').click()
        for i in self.driver.find_elements_by_class_name('nav-links')[0].text.split('\n'):
            if i != stop_word:
                print i
                print '****************'
                self.driver.find_element_by_link_text(i).click()
                print '****************'
                self.driver.find_element_by_class_name('btn-usermenu').click()
            else:
                break

    def click_users_menu_element(self, name):

        # click  on determined users element define' in variable 'name
        driver = self.driver
        menu_titles = Leng().my_account_button_title_tr
        for item in menu_titles:
            if item == name:
                driver.find_element_by_class_name('btn-usermenu').click()
                driver.find_element_by_link_text(item).click()

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
        exp_data_month = card.exp.split('/')[0]
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

    def deposit(self, keyName=u'PARA YATIRMA'):
        self.driver.find_element_by_id('header-depoist').click()
        self.select_card()

    def input(self, id, value):
        driver = self.driver
        driver.find_element_by_id(id).send_keys(value)

    def registration(self):
        driver = self.driver
        driver.find_elements_by_class_name('header-login')[0].click()
        time.sleep(3)
        users_data = UsersDetails().generate_users_data()
        NewName = users_data[0]
        mail = users_data[1]

        passw = UsersDetails().passw
        postal_code = UsersDetails().postal_code

        self.input('gamingtec_register_username', NewName)
        self.input('gamingtec_register_password', passw)
        self.input('gamingtec_register_repeatPassword', passw)
        self.input('gamingtec_register_email', mail)
        self.input('gamingtec_register_repeatEmail', mail)
        select = Select(self.driver.find_element_by_id('gamingtec_register_securityQuestion'))
        select.select_by_value('What is your date of birth?')
        self.input('gamingtec_register_securityAnswer', '12.03.1993')

        select_currency = Select(self.driver.find_element_by_id('currencySelect'))
        select_currency.select_by_index(1)

        self.input('gamingtec_register_firstName', 'Omar')
        self.input('gamingtec_register_lastName', 'Asker')

        select_gender = Select(self.driver.find_element_by_id('gamingtec_register_gender'))
        select_gender.select_by_value('M')

        select_birth_day = Select(self.driver.find_element_by_id('gamingtec_register_birthDate_day'))
        select_birth_day.select_by_value('11')
        select_birth_month = Select(self.driver.find_element_by_id('gamingtec_register_birthDate_month'))
        select_birth_month.select_by_value('7')

        select_birth_year = Select(self.driver.find_element_by_id('gamingtec_register_birthDate_year'))
        select_birth_year.select_by_value('1970')
        self.input('gamingtec_register_address', 'Harbiye Mahallesi, Cumhuriyet  50')
        self.input('gamingtec_register_postalCode', postal_code)
        self.input('gamingtec_register_city', 'Istanbul')

        select_country = Select(self.driver.find_element_by_id('gamingtec_register_country'))
        select_country.select_by_value('TR')
        self.input('gamingtec_register_mobilePhone', '902123156000')

        self.driver.find_elements_by_xpath('//*[@id="gamingtec_register_receiveEmail"]')[0].click()
        self.driver.find_elements_by_xpath('//*[@id="gamingtec_register_agreeTermAndConditions"]')[0].click()
        self.driver.find_element_by_xpath('//*[@id="bodyScope"]/div[1]/div[3]/div[1]/form/button').click()
        successfully_message = 'registration' + ' for user ' + NewName + ' ' + mail + " is completed... "
        print successfully_message

        if successfully_message:
            Generationed_Users_details.append(NewName)
            Generationed_Users_details.append(mail)
            Generationed_Users_details.append(passw)
            go_to_mail = Email()
            go_to_mail.enter_value(NewName)
            for i in Generationed_Users_details:
                print i
            return Generationed_Users_details

            # if self.driver.find_element_by_class_name('registration') is True:
            #     i = 0
            #     break
            # self.driver.refresh()
            # go_to_mail = Email()
            # go_to_mail.enter_value(NewName)
            #

    def close_driver(self):
        self.driver.close()


        # def place_bet(self, value=2, multi_bet=False, button_name=u'SPOR BAHİSLERİ'):
        #     '''place a bet'''
        #
        #     # self.driver.set_window_size(1800, 1800)
        #     self.click_top_menu(button_name)
        #     self.driver.implicitly_wait(3)
        #     my_frame = self.driver.find_element_by_id('sport_iframe_1')
        #     self.driver.switch_to.frame(my_frame)
        #     row = self.driver.find_elements_by_class_name('leftMenuIcon')
        #     if multi_bet is False:
        #         row[0].click()
        #     else:
        #         row[0].click()
        #         time.sleep(2)
        #         row[0].click()
        #     self.driver.find_element_by_class_name("prematch_stake_odd_factor").click()
        #     # self.driver.switch_to.default_content()
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     self.driver.find_element_by_id("betAmountInput").clear()
        #     self.driver.find_element_by_id("betAmountInput").send_keys(value)
        #     self.driver.find_element_by_class_name('btn_bet').click()


class BahsegelChrome(Bahsegel):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Remote(executorURL,desired_capabilities=DesiredCapabilities.CHROME)

        self.driver.get(BASEURL)
        self.driver.set_window_size(1920, 1080)



class BahsegelSafari(Bahsegel):
    def __init__(self):
        self.driver = webdriver.Safari()
        self.driver.get(BASEURL)
        # self.driver.set_window_size(1920, 1080)
        # self.driver.find_element_by_class_name('user-panel-logo' ).click()


        # address = self.driver.find_element_by_tag_name('iframe').get_attribute('src')
        # self.driver.get(address)
            # my_frame = self.driver.find_element_by_id('sport_iframe_1')
            # self.driver.switch_to.frame(my_frame)
        # print address


        # self.driver.get(address)
        # time.sleep(3)
        # self.driver.find_element_by_partial_link_text('TAMAM').send_keys(Keys.RETURN)
        # self.driver.close()


class BahsegelMobile(BahsegelChrome):
    def __init__(self):
        mobile_emulation = {
            "deviceMetrics": {"width": 375, "height": 667, "pixelRatio": 3.0}
            # "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        }
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(BASEURL)
        self.driver.implicitly_wait(30)

    def enter_site_mobile(self):
        self.driver.find_element_by_class_name('btn-login').click()

    def login_mobile_lebull(self, name, passw):
        self.driver.find_element_by_class_name('t-main-login-button').click()
        # time.sleep(7)

        self.driver.find_elements_by_css_selector('input.form-control.form-control-sm')[0].send_keys(name)
        self.driver.find_elements_by_css_selector('input.form-control.form-control-sm')[1].send_keys(passw)
        self.driver.find_element_by_css_selector('button.btn.btn-sm-gold3').click()
        time.sleep(10)

    def login_mobile(self, name, passw):
        self.driver.find_element_by_class_name('btn-login').click()
        self.driver.find_element_by_css_selector("div.col-sm-12 input#username").send_keys(name)
        self.driver.find_element_by_css_selector("div.col-sm-12 input#password").send_keys(passw)
        self.driver.find_elements_by_class_name("submit-button")[2].click()
        time.sleep(3)
        all_text = self.driver.find_elements_by_class_name('mb')[0].text.split('\n')
        balance = all_text[0]
        print 'Users balance is ', balance
        return 'Login successfully'

class LebullActions(Bahsegel):
    def __init__(self):
        super(LebullActions, self).__init__()
        self.driver.get(BASEURL)
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(50)

    def forgot_password_lebull(self):
        self.driver.find_element_by_css_selector("form.filled > div.form-group > small > a.btn.btn-link").click()
        time.sleep(5)
        self.driver.close()

    def top_menu_lebull(self):
        self.top_menu('user-panel-nav')


    def virtual_sport_click_lebull(self, button_title=u'Virtual sports'):
        self.driver.find_element_by_partial_link_text(button_title).click()
        name_list = self.driver.find_element_by_class_name('betradarTabs').text.split('\n')
        for name in name_list:
            print '{} is testing...'.format(name)
            self.driver.find_element_by_link_text(name).click()
            print name, ' is ok...'

    def login_lebull(self, UserName, UserPass):
        '''Login to lebull site with creds'''

        self.driver.find_element_by_css_selector(
            "form.filled > div.form-group > input[name=\"signin_username\"]").clear()
        self.driver.find_element_by_css_selector(
            "form.filled > div.form-group > input[name=\"signin_username\"]").send_keys(UserName)
        self.driver.find_element_by_css_selector(
            "form.filled > div.form-group > input[name=\"signin_password\"]").clear()
        self.driver.find_element_by_css_selector(
            "form.filled > div.form-group > input[name=\"signin_password\"]").send_keys(UserPass)
        self.driver.find_element_by_css_selector("form.filled > div.form-group > button.btn.btn-sm-gray1").click()
        time.sleep(4)
        return 'Login with credential {0} and password {1} was successfully...'.format(UserName, UserPass)

    def multi_place_bet_lebull(self):
        self.place_bet_lebull(multi_bet=True)

    def place_bet_lebull(self, button_name='Sportsbook', multi_bet=False):
        self.driver.find_element_by_partial_link_text(button_name).click()
        time.sleep(10)


        my_frame = self.driver.find_element_by_id('sport_iframe_1')
        self.driver.switch_to.frame(my_frame)

        self.driver.find_elements_by_class_name('Decimal')[0].click()
        if multi_bet:
            self.driver.find_elements_by_class_name('Decimal')[3].click()
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0, 200);")
        self.driver.switch_to.frame(my_frame)
        time.sleep(5)
        self.driver.find_element_by_class_name('amount').send_keys('2')
        self.driver.find_element_by_id("betAmountInput").send_keys(Keys.RETURN)
        print 'Place bet...'
        time.sleep(5)


    def withdraw_request(self, value=100):
        self.my_account_button('user')
        self.driver.find_element_by_xpath('//*[@id="pageContent"]/section/content/section/ul[2]/li[10]/div/a').click()
        # self.driver.find_element_by_id('withdrawal-amount-field').send_keys(value)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pageContent"]/section/content/section/form/div[1]/div[2]/span').click()
        # time.sleep(1)
        # self.driver.find_element_by_id('gamingtec_withdrawal_account_accountNumber').send_keys(self.accountNumber)
        # self.driver.find_element_by_xpath('//*[@id="pageContent"]/section/content/section/form/div[2]/button').click()
        # print "Withdraw request {} was successfull".format(100)
        # return 'Successfully'

    def user_menu_click(self):
        driver = self.driver
        for user_button in driver.find_elements_by_id('user-panel-actions'):
            user_button.click()
        GetItems_name = str(driver.find_element_by_class_name('user-profile-nav').text).split('\n')

        for link in GetItems_name:
            driver.find_element_by_link_text(link).click()
            print link, ' is ok...'
            time.sleep(12)

    def casino_slots_le_bull(self, button_name='Casino'):
        self.driver.find_element_by_link_text(button_name).click()
        time.sleep(4)
        self.driver.find_element_by_link_text("Slots").click()
        time.sleep(3)
        # print self.driver.find_element_by_css_selector("div.title").text
        # for i in self.driver.find_elements_by_css_selector("div.title").click()

        # i = 0

        # self.driver.find_elements_by_class_name('game-name')[0].text
        # for game in self.driver.find_elements_by_class_name('game-name'):
        #     print game.text
        #     game.click()
        #     i += 1
        # print "{} games are available...".format(i)

    def check_url(self):
        ExpectedURL = BASEURL + '/profile/deposit/methods'

        ActualURL = self.driver.current_url
        if ActualURL == ExpectedURL:
            print "Passed"
        else:
            print "Failed..."

    def deposit_lebull(self):
        # click on deposit button

        deposit_button = self.driver.find_elements_by_class_name('btn-sm-gray1')[1]

        deposit_button.click()

        # select amount
        time.sleep(7)

        self.driver.find_element_by_class_name('btn-lg').click()
        time.sleep(5)
        self.driver.find_element_by_class_name('predefined-amount').click()

        self.driver.find_element_by_class_name('btn-forward').click()
        time.sleep(3)

        self.driver.find_element_by_class_name('btn-forward').click()
        time.sleep(3)
        card_number = CardDetails().number
        name = CardDetails().name
        exp_date = (CardDetails().exp).split('/')[1]
        cvv = CardDetails().cvv
        self.driver.find_element_by_name('cc-number').send_keys(card_number)

        self.driver.find_element_by_name("year").click()

        self.driver.find_element_by_xpath("//form[@class='form']//option[.='2022']").click()
        if not self.driver.find_element_by_xpath(
                "//form[@class='form']/div/div[3]/div[2]/div/div/div/div/select//option[3]").is_selected():
            self.driver.find_element_by_xpath(
                "//form[@class='form']/div/div[3]/div[2]/div/div/div/div/select//option[3]").click()

        self.driver.find_element_by_name('cc-cvv').send_keys(cvv)
        self.driver.find_element_by_class_name('btn-forward').click()
        self.driver.find_element_by_class_name('predefined-amount').click()
        self.driver.find_element_by_class_name('btn-forward').click()
        self.driver.find_element_by_class_name('btn').click()
        self.driver.find_element_by_class_name('btn-lg').click()

    def amount_of_deposit_lebull(self):
        # select user button
        # click on deposit button
        time.sleep(6)
        amount = self.driver.find_elements_by_class_name('btn-sm-gray1')[0].text
        deposit_button = self.driver.find_elements_by_class_name('btn-sm-gray1')[1]

        print amount


        # self.driver.find_element_by_class_name('btn-sm-gray1').click()
        # select amount

        # self.driver.find_element_by_class_name('btn-lg').click()
        # self.driver.find_element_by_class_name('predefined-amount').click()
        #
        # self.driver.find_element_by_class_name('btn-forward').click()
        #
        #
        # self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]'
        #                                   '/div[1]/div/div[2]/div/div/div/div/'
        #                                   'div[2]/div/div/div[2]/div[2]/div[2]/'
        #                                   'button').click()
        #
        # card_number = CardDetails().number
        # name =CardDetails().name
        # exp_date = (CardDetails().exp).split('/')[1]
        # self.driver.find_element_by_name('cc-number').send_keys(card_number)
        # select = Select(self.driver.find_element_by_name('year').click())
        # select.select_by_value(exp_date)

        # self.driver.find_element_by_class_name('predefined-amount').click()
        # self.driver.find_element_by_class_name('btn-forward').click()
        # self.driver.find_element_by_class_name('btn').click()
        # self.driver.find_element_by_class_name('btn-lg').click()


class LebullChrome(LebullActions):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASEURL)
        self.driver.set_window_size(1920, 1080)

class BettiltActions(Bahsegel):
    def __init__(self):
        super(BettiltActions, self).__init__()
        self.driver.get(BASEURL)
        self.driver.set_window_size(1920, 1080)
        self.user_acount_class_names = ['myAccBtn', 'edit', 'atm', 'file', 'credit-card', 'gift', 'money', 'game-pad',
                                        'cup']


class BettiltChrome(BahsegelChrome):
    def __init__(self):
        super(BettiltChrome, self).__init__()
        self.driver.get(BASEURL)
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(50)

    def virtual_sport_click_bettilt(self, button_title=u'Sanal Sporlar'):

        self.enter_to_virtual_sport(button_title)
        # class_names = ['basketball','greyhounds','horseracing','tennis','soccer',]
        class_names = (self.driver.find_elements_by_class_name('betradarTabs')[0].text).split('\n')
        # print class_names

        time.sleep(4)
        for title in class_names:
            title_new = str(title).lower().replace(' ', '')
            self.driver.find_element_by_class_name(title_new).click()
            print title_new
            # time.sleep(4)
            # self.virtual_sport_button(title)
            # #insert checking of loading page'''
            #
            # self.driver.find_element_by_class_name(title).click()


    def my_account_bettilt(self):
        time.sleep(4)
        self.driver.find_element_by_class_name('myAccBtn').click()
        my_account = ['myAccBtn', 'edit', 'atm', 'file', 'credit-card', 'gift', 'money', 'game-pad', 'cup']
        for class_name in my_account:
            self.driver.find_element_by_class_name(class_name).click()

    def place_bet_bettilt(self, value=2, multi_bet=False):
        test_name = 'place_bet'
        try:
            self.driver.find_elements_by_class_name("osg-outcome")[0].click()

            stake = self.driver.find_elements_by_class_name("osg-outcome")[0].text
            print 'Stack is {}'.format(stake)

            if multi_bet:
                another_stake = self.driver.find_elements_by_class_name("osg-outcome")[3].text
                print 'Stack is {}'.format(another_stake)
                self.driver.find_elements_by_class_name("osg-outcome")[3].click()

            self.driver.find_element_by_css_selector("input.betslip_selection_stake.half").send_keys(value)
            self.driver.find_element_by_link_text('Place Bet').click()
            self.driver.find_element_by_link_text('Ok').click()
            receipt = self.driver.find_element_by_class_name('receipt_item').text
            return receipt
        except:
            self.driver.save_screenshot(test_name + '.png')
            #
            #






            # self.driver.find_element_by_class_name("osg-menu-price").click()


            # stake.send_keys(value)
            # time.sleep(4)



    def casino_slots_bettilt(self, menu_name="Casino", menu_index=2):
        self.driver.find_element_by_link_text(menu_name).click()
        # time.sleep(4)
        casino_menu = str(self.driver.find_elements_by_class_name('casinoNav')[0].text).split('\n')
        submenu = casino_menu[menu_index]
        game_buttons = []
        self.driver.find_element_by_link_text(submenu).click()
        time.sleep(2)
        for i in self.driver.find_elements_by_css_selector("span.gameName"):
            # i.click()

            print self.driver.find_element_by_css_selector("div.gameHold > img").text
            # i.click()
            time.sleep(1)
            #
            # for i in self.driver.find_elements_by_class_name('gameName'):
            #     title = i.text.replace('\nYeni', '')
            #     game_buttons.append(title)
            #     print title

        quantity_of_games = len(game_buttons)
        print "{} are available...".format(quantity_of_games)
        return game_buttons


class Leng:
    def __init__(self):
        self.submenu_tr = [u'POPÜLER', u'CANLI CASİNO', u'SLOT', u'RULET', u'BLACKJACK', u'POKER', u'JACKPOT',
                           u'DİĞER OYUNLAR']
        self.submenu_en = [u'POPÜLER', u'CANLI CASİNO', u'SLOT', u'RULET', u'BLACKJACK', u'POKER', u'JACKPOT',
                           u'DİĞER OYUNLAR']
        self.my_account_button_title_tr = [
            u'HESAP BİLGİLERİ',
            u'HESAP DOĞRULAMA',
            u'PARA YATIRMA',
            u'PARA ÇEKME',
            u'BAHİS GEÇMİŞİ',
            u'HESAP HAREKETLERİ',
            u'BONUS GEÇMİŞİ',
            u'ÇIKIŞ YAP'
        ]
        self.my_account_button_title_en = [
            'Personal information',
            'Account verification',
            'Deposit',
            'Withdraw',
            'Play history',
            'Payment history',
            'My bonuses',
            'Logout'
        ]
        self.user_menu_title = [
            u'SPOR BAHİSLERİ',
            u'CANLI BAHİS',
            u'CASİNO',
            u'CANLI CASİNO',
            u'Sanal Sporlar',
            u'CANLI OYUNLAR',
            u"Bonus"
        ]
        self.user_menu_title_en = [
            'Sportsbook',
            'In-play',
            'Casino',
            'Live Casino',
            'Live Games',
            'Virtual sports',
            'Bonuses'
        ]


if __name__ == "__main__":
    # test_firefox_1 = Bahsegel()
    # test_firefox_1.landing_pages()
    # test_firefox_1.enter_site()
    # test_firefox_1.login('Bahsegel_26', 'qwerty26',show_pass=True)
    # test_firefox_1.submit_button('loginBtnSubmit')
    # test_firefox_1.top_menu()
    # test_firefox_1.live_casino()
    # test_firefox_1.place_bet_bahsegel()
    # test_firefox_1.place_bet_bahsegel(multi_bet=True)
    # test_firefox_1.casino_slots()
    # test_firefox_1.virtual_sport_click()
    # test_firefox_1.usermenu_click(u'ÇIKIŞ YAP')
    # test_firefox_1.registration()
    # test_firefox_1.deposit()
    # test_firefox_1.withdraw_request(100)

    # test_on_crome_1 = BahsegelChrome()
    # test_on_crome_1.enter_site()
    # test_on_crome_1.forgot_password()
    # test_on_crome_1.login('tst_711_0001', 'q1q1q1q1')
    # test_on_crome_1.submit_button()
    # test_on_crome_1.landing_pages()
    # test_on_crome_1.top_menu()
    # test_on_crome_1.live_casino()
    # test_on_crome_1.place_bet_bahsegel()
    # test_on_crome_1.place_bet_bahsegel(multi_bet=True)
    # test_on_crome_1.casino_slots()
    # test_on_crome_1.virtual_sport_click()
    # test_on_crome_1.usermenu_click(u'ÇIKIŞ YAP')
    # test_on_crome_1.registration()
    # test_on_crome_1.deposit()
    # test_on_crome_1.withdraw_request(100)

    # test_on_safari = BahsegelSafari()
    # test_on_safari.enter_site()
    # test_on_safari.login('Bahsegel_26', 'qwerty26',show_pass=True)
    # test_on_safari.top_menu()
    # test_on_safari.live_casino()
    # test_on_safari.place_bet()
    # test_on_safari.place_bet_bahsegel(multi_bet=True)
    # test_on_safari.casino_slots()
    # test_on_safari.virtual_sport_click()
    # test_on_safari.user_menu_click()
    # test_on_safari.registration()
    # test_on_safari.deposit()


    # test_on_fire_fox_2 = LebullActions()
    # test_on_fire_fox_2.forgot_password_lebull()
    # test_on_fire_fox_2.show_password()
    # test_on_fire_fox_2.login_lebull("Lebull_1","q1q1q1q1")
    # test_on_fire_fox_2.top_menu_lebull()
    # test_on_fire_fox_2.click_on_menu('user-panel-nav',u'In-play')
    # test_on_fire_fox_2.top_menu_lebull()
    # test_on_fire_fox_2.place_bet_lebull()
    # test_on_fire_fox_2.place_bet_lebull( multi_bet=True)
    # test_on_fire_fox_2.casino_slots_le_bull()
    # test_on_fire_fox_2.virtual_sport_click_lebull()
    # test_on_fire_fox_2.user_menu_click()
    # test_on_fire_fox_2.deposit_lebull()
    # test_on_fire_fox_2.withdraw_request()
    # test_on_fire_fox_2.registration()

    # test_on_chrome_2 = LebullChrome()
    # test_on_chrome_2.forgot_password_lebull()
    # test_on_chrome_2.login_lebull("Lebull_1","q1q1q1q1")
    # test_on_chrome_2.top_menu_lebull()
    # test_on_chrome_2.place_bet_lebull()
    # test_on_chrome_2.place_bet_lebull( multi_bet=True)
    # test_on_chrome_2.casino_slots_le_bull()
    # test_on_chrome_2.virtual_sport_click_lebull()
    # test_on_chrome_2.user_menu_click()
    # test_on_chrome_2.deposit_lebull()
    # test_on_chrome_2.withdraw_request()
    # test_on_chrome_2.registration()



    # test_on_fire_fox_3 = BettiltActions()
    # test_on_fire_fox_3.forgot_password()
    # test_on_fire_fox_3.login("btsaparkar", "q1q1q1",'button-preset')
    # test_on_fire_fox_3.top_menu('main-menu')
    # test_on_fire_fox_3.top_menu_bettilt()
    # test_2.virtual_sport_click_bettilt('Virtual sports')
    # test_2.place_bet_bettilt()
    # test_2.place_bet_bettilt(multi_bet=True)
    # test_2.casino_slots_bettilt()



    # test_2.my_account_bettilt()

    # test_2.withdraw_request()
    # test_5 = BahsegelMobile()
    # test_5.forgot_password()
    # test_5.enter_site_mobile()

    # test_5.login_mobile('Bahsegel_26' )
    # test_5.top_menu()

    test_on_mobile = BahsegelMobile()
    test_on_mobile.login_mobile('tst_711_0001', 'q1q1q1q1')
 
