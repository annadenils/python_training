# -*- coding: utf-8 -*-
from model.users import Users


def test_add_user(app):
    old_users = app.user.get_users_list()
    user = Users(users_name="Иван", users_lastname="Иванов", users_middlename="Иванович", nickname="ivan-ivan", name_company=u"ооо \"рога и копыта\"",
                          address_company="СПб, Мира ул. 6 - 56", home_phone="812-567-89-90", mobile_phone="89655783498", work_phone="812-567-90-89", fax="-",
                          email="dfghj@dfgh.ru", bday="7", bmonth="March", byear="1971", address2="Спб, Приморский пр. 56")
    app.user.add_new_user(user)
    new_users = app.user.get_users_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)


