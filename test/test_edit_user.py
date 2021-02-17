from model.users import Users
import random
import allure


def test_edit_user(app, db, check_ui):
    app.open_home_page()
    with allure.step('Given a user list. Empty - add user'):
        user1 = Users(users_name="специальный юзер", users_lastname="Никалаев", home_phone="2345678", mobile_phone="89655783498", work_phone="812-567-90-89", phone2="812-789-56-37")
        if len(db.get_user_list()) == 0:
            app.user.add_new_user(user1)
    with allure.step('Given a user list'):
        old_users = db.get_user_list()
    with allure.step('Given random user from the list'):
        user2 = random.choice(old_users)
        index = old_users.index(user2)
    user3 = Users(users_name="Николай", users_lastname="Николаев", name_company=u"ооо\"далеко и близко\"")
    user3.id = user2.id
    with allure.step('When i edit a user %s to the list' % user3):
        app.user.edit_user_by_id(user2.id, user3)
    with allure.step('Then the new user list is equal to the old list with the edit user'):
        new_users = db.get_user_list()
        assert len(old_users) == len(new_users)
        old_users[index] = user3
        if check_ui:
            assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)


