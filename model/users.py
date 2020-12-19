class Users():
    def __init__(self, users_lastname, users_middlename, users_name, nickname, address_company, name_company, fax, work_phone, mobile_phone, home_phone, email, byear, bmonth, bday, address2):
        self.users_lastname = users_lastname
        self.users_middlename = users_middlename
        self.users_name = users_name
        self.nickname = nickname
        self.address_company = address_company
        self.name_company = name_company
        self.fax = fax
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone
        self.email = email
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.address2 = address2

class EditUsers():
    def __init__(self, new_users_name, new_name_company):
        self.new_users_name = new_users_name
        self.new_name_company = new_name_company
