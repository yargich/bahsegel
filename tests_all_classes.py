from selenium import webdriver

class Base(object):
    def __init__(self):
        self.driver = webdriver.Safari()
        if __name__ == '__main__':
            my_args = sys.argv[1:]
            del sys.argv[1:]
            unittest.main(verbosity=2)


class GetURL1(Base):
    def __init__(self):

        super(GetURL1, self).__init__()
        self.driver.get('https://google.com')
    def message(self):
        self.driver.get("http://korrespondent.net")


class GetURL2(Base):
    def __init__(self):
        super(GetURL2, self).__init__()
        self.driver.get('https://ukr.net')
        self.driver.close()
class NewDriver(GetURL1):
    def __init__(self):
        super(NewDriver, self).__init__()
        self.driver = webdriver.Firefox()


class NewDriver_2(GetURL1):
    def __init__(self):
        super(NewDriver_2, self).__init__()
        self.driver = webdriver.Safari()


if __name__ == "__main__":
    test = NewDriver()
    test.message()
    test_1 = NewDriver()
    test_2 = NewDriver_2()


