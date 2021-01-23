# -*- coding: utf-8 -*-
from model.users import Users
import random
import string
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).replace('  ', ' ').strip(' ')

testdata = [Users(users_name=random_string("", 10), users_lastname=random_string("", 20), users_middlename=random_string("", 20), nickname=random_string("", 15), name_company=random_string("", 15), address_company=random_string("", 30), home_phone="812-567-89-90", mobile_phone="89655783498", work_phone="812-567-90-89", fax="-", email="dfghj@dfgh.ru", email2="rtyu@rt.ru", email3="poiuyt@jg.tu", bday="7", bmonth="March", byear="1971", address2="Спб, Приморский пр. 56", phone2="812-789-56-37") for i in range(2)]

@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, user):
    old_users = app.user.get_users_list()
    # user = Users(users_name="Иван", users_lastname="Иванов", users_middlename="Иванович", nickname="ivan-ivan", name_company=u"ооо \"рога и копыта\"",
    #                       address_company="СПб, Мира ул. 6 - 56", home_phone="812-567-89-90", mobile_phone="89655783498", work_phone="812-567-90-89", fax="-",
    #                       email="dfghj@dfgh.ru", email2="rtyu@rt.ru", email3="poiuyt@jg.tu", bday="7", bmonth="March", byear="1971", address2="Спб, Приморский пр. 56", phone2="812-789-56-37")
    app.user.add_new_user(user)
    new_users = app.user.get_users_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)


