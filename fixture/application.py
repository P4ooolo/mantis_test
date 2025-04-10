from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from fixture.project import projectHelper
from fixture.session import sessionHelper
from fixture.soap import soapHelper
from fixture.james import jamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper


class Application:

    def __init__(self, browser, configuration):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(20)
        self.session = sessionHelper(self)
        self.james = jamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = soapHelper(self)
        self.project = projectHelper(self)
        self.configuration = configuration
        self.base_url = configuration['web']['baseUrl']



    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def destroy(self):
        self.wd.quit()


    def return_to_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/index.php"):
            wd.get(self.base_url)






