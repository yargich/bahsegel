#!/usr/bin/env python
import selenium
from selenium import webdriver
class BigTest:
    def __init__(self):
        comand_executor =  "http://192.168.11.83:4444/wd/hub"
        self.driver = webdriver.Remote(comand_executor,  webdriver.DesiredCapabilities.FIREFOX)
        self.driver.get('http://oto.ru')


if __name__ == "__main__":
    test = BigTest()