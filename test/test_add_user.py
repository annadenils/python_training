# -*- coding: utf-8 -*-
from model.users import Users


def test_add_user(app, json_users):
    user = json_users
    old_users = app.user.get_users_list()
    app.user.add_new_user(user)
    new_users = app.user.get_users_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)


