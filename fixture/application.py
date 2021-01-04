from selenium import webdriver
from fixture.session import SessionHelper
from fixture.user import UserHelper
from fixture.group import GroupHelper

class Application():

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.user = UserHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.get("http://127.0.0.1/addressbook/index.php")

    def return_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()
