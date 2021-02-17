# -*- coding: utf-8 -*-
from model.users import Users
import allure


def test_add_user(app, db, json_users):
    user = json_users
    with allure.step('Given a user list'):
        old_users = db.get_user_list()
    with allure.step('When i add a user %s to the list' % user):
        app.user.add_new_user(user)
    with allure.step('Then the new group list is equal to the old list with the added user'):
        new_users = db.get_user_list()
        old_users.append(user)
        assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)


