from selenium import webdriver
from fixture.session import SessionHelper
from fixture.user import UserHelper
from fixture.group import GroupHelper

class Application():

    def __init__(self, browser, baseUrl):
        if browser == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser == "Chrome":
            self.wd = webdriver.Chrome('/Users/annakosolapova/Downloads/chromedriver')
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.user = UserHelper(self)
        self.group = GroupHelper(self)
        self.baseUrl = baseUrl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.get(self.baseUrl)

    def return_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()
