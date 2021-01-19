from model.users import Users
from random import randrange


def test_delete_some_user(app):
    if app.user.count() == 0:
        app.user.add_new_user(Users(users_name="специальный юзер"))
    old_users = app.user.get_users_list()
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    new_users = app.user.get_users_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[index:index+1] = []
    assert old_users == new_users
