from model.users import Users
import random
import allure


def test_delete_some_user(app, db, check_ui):
    with allure.step('Given a user list. Empty - add user'):
        if len(db.get_user_list()) == 0:
            app.user.add_new_user(Users(users_name="специальный юзер"))
    with allure.step('Given a user list'):
        old_users = db.get_user_list()
    with allure.step('Given random user from the list'):
        user = random.choice(old_users)
    with allure.step('When i delete a user %s to the list' % user):
        app.user.delete_user_by_id(user.id)
    with allure.step('Then the new user list is less than the old list'):
        new_users = db.get_user_list()
        assert len(old_users) - 1 == len(new_users)
        old_users.remove(user)
        if check_ui:
            assert sorted(new_users, key=Users.id_or_max) == sorted(app.user.get_users_list(), key=Users.id_or_max)
