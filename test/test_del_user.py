from model.users import Users
import random


def test_delete_some_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(Users(users_name="специальный юзер"))
    old_users = db.get_user_list()
    user = random.choice(old_users)
    app.user.delete_user_by_id(user.id)
    new_users = db.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    old_users.remove(user)
    if check_ui:
        assert sorted(new_users, key=Users.id_or_max) == sorted(app.user.get_users_list(), key=Users.id_or_max)
