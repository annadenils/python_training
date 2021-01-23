from sys import maxsize

class Users():
    def __init__(self, users_lastname = None, users_middlename = None, users_name = None, nickname = None, address_company = None, name_company = None, fax = None, work_phone=None, mobile_phone=None, home_phone=None, email=None, email2=None, email3=None, byear = None, bmonth = None, bday = None, address2 = None, id = None, phone2 = None, all_phones_from_home_page=None, all_email_from_home_page=None):
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
        self.email2 = email2
        self.email3 = email3
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.address2 = address2
        self.id = id
        self.phone2 = phone2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.users_name, self.users_lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.users_name == other.users_name and self.users_lastname == other.users_lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

