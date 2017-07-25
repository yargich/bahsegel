#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
# URL ="https://stg.bahsegel.info"
import webbrowser, sys

# NAME = "Bahsegel_26"
NAME = "testbahsegel"
URLtst = "https://tst.bahsegel.info"
URLstg = "https://stg.bahsegel.info"
URLprod = "https://www.bahsegel96.com"
# PASSW = "qwerty26"
PASSW = "240207test"


class Action(object):
    def __init__(self):
        self.url = URLstg
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1800, 1800)
        self.driver.get(self.url)
        self.driver.implicitly_wait(30)

    def enter_to_page(self):
        url = self.url
        driver = self.driver
        self.driver.get(self.url)
        driver.find_element_by_id('login-Button').click()
        link_to_login = url + "/tr/login"
        current_url = self.driver.current_url
        return link_to_login, current_url

    def click_registration(self):
        driver = self.driver
        button_xpath ='//*[@id="bodyScope"]/header[1]/div/div[2]/a[1]/span'
        button_name = driver.find_element_by_xpath(button_xpath).text
        driver.find_element_by_link_text(button_name).click()
        

        print(driver.current_url)




    def login(self, name, passw):
        driver = self.driver
        driver.find_element_by_id('login-Button').click()
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(name)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(passw)
        driver.find_element_by_id('loginBtnSubmit').click()
        current_url = driver.current_url
        base_url = self.url + "/tr/login"
        return current_url, base_url

    def enter_to_virtual_sport(self):
        driver = self.driver
        virtual_sports_button = './/*[@id="bodyScope"]/header[1]/nav/div/ul/li[5]/a'
        driver.find_element_by_xpath(virtual_sports_button).click()
        name_of_button = driver.find_element_by_xpath(virtual_sports_button).text
        print(name_of_button)
        driver.find_element_by_link_text(name_of_button).click()
        return name_of_button

    def existing_logo(self):
        driver = self.driver
        logo = driver.find_element_by_css_selector("img.logo").text
        print(logo)
        return logo

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

    def virtual_sport_click(self):
        driver = self.driver
        self.enter_to_virtual_sport()
        footbollXPATH = '//*[@id="bodyScope"]/div[1]/div/ul/li[1]/a/span'
        driver.find_element_by_xpath(footbollXPATH).click()
        basquetlXPATH = '//*[@id="bodyScope"]/div[1]/div/ul/li[2]/a/span'
        driver.find_element_by_xpath(basquetlXPATH).click()
        greyhoundsXPATH = '//*[@id="bodyScope"]/div[1]/div/ul/li[3]/a/span'
        driver.find_element_by_xpath(greyhoundsXPATH).click()
        horseracingXPATH = '//*[@id="bodyScope"]/div[1]/div/ul/li[4]/a/span'
        driver.find_element_by_xpath(horseracingXPATH).click()
        horseracingXPATH = '//*[@id="bodyScope"]/div[1]/div/ul/li[5]/a/span'
        driver.find_element_by_xpath(horseracingXPATH).click()

    def open_result_in_browser(self, file):
        filename = "nosetests.html"
        webbrowser.open(filename)

    def switch_frame(self):
        driver = self.driver
        my_frame = driver.find_element_by_id('sport_iframe_1')
        driver.switch_to.frame(my_frame)

    def close_driver(self):
        self.driver.quit()

    def close_all(self):
        sys.exit()


if __name__ == "__main__":
    test = Action()
    test.click_registration()
    # test.login("Bahsegel_26","qwerty26")
    # test.enter_to_virtual_sport()
    # test.virtual_sport_click()
