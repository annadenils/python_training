from selenium.webdriver.support.ui import Select
from model.users import Users


class UserHelper:

    def __init__(self, app):
        self.app = app

    def add_new_user(self, users):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_user_form(users)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_homepage()
        self.user_cashe = None

    def fill_user_form(self, users):
        self.change_value("firstname", users.users_name)
        self.change_value("middlename", users.users_middlename)
        self.change_value("lastname", users.users_lastname)
        self.change_value("nickname", users.nickname)
        self.change_value("company", users.name_company)
        self.change_value("address", users.address_company)
        self.change_value("home", users.home_phone)
        self.change_value("mobile", users.mobile_phone)
        self.change_value("work", users.work_phone)
        self.change_value("fax", users.fax)
        self.change_value("email", users.email)
        self.change_value_select("bday", users.bday)
        self.change_value_select("bmonth", users.bmonth)
        self.change_value("byear", users.byear)
        self.change_value("address2", users.address2)

    def change_value_select(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_user(index)
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.user_cashe = None

    def select_user(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_user_by_index(self, index, users):
        wd = self.app.wd
        wd.find_element_by_xpath(f"/html/body/div/div[4]/form[2]/table/tbody/tr[{index+2}]/td[8]/a/img").click()
        self.change_value("firstname", users.users_name)
        self.change_value("company", users.name_company)
        wd.find_element_by_name("update").click()
        self.app.return_homepage()
        self.user_cashe = None

    def edit_user(self):
        self.edit_user_by_index(0)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    user_cashe = None

    def get_users_list(self):
        if self.user_cashe is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.user_cashe = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("id")
                users_name = element.find_element_by_xpath("td[3]").text
                users_lastname = element.find_element_by_xpath("td[2]").text
                self.user_cashe.append(Users(id=id, users_name=users_name, users_lastname=users_lastname))
        return list(self.user_cashe)