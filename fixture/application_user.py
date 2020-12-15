from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.user import UserHelper

class Application_user():

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.user = UserHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://127.0.0.1/addressbook/index.php")

    def return_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()
