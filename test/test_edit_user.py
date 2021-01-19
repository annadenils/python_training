from model.users import Users
from random import randrange


def test_edit_user(app):
    app.open_home_page()
    user1 = Users(users_name="специальный юзер")
    if app.user.count() == 0:
        app.user.add_new_user(user1)
    old_users = app.user.get_users_list()
    index = randrange(len(old_users))
    user2 = Users(users_name="Николай", name_company=u"ооо\"далеко и близко\"")
    user2.id = old_users[index].id
    app.user.edit_user_by_index(index, user2)
    new_users = app.user.get_users_list()
    assert len(old_users) == len(new_users)
    old_users[index] = user2
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)