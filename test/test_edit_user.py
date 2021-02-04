from model.users import Users
import random


def test_edit_user(app, db, check_ui):
    app.open_home_page()
    user1 = Users(users_name="специальный юзер", users_lastname="Никалаев", home_phone="2345678", mobile_phone="89655783498", work_phone="812-567-90-89", phone2="812-789-56-37")
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(user1)
    old_users = db.get_user_list()
    user2 = random.choice(old_users)
    index = old_users.index(user2)
    user3 = Users(users_name="Николай", users_lastname="Николаев", name_company=u"ооо\"далеко и близко\"")
    user3.id = user2.id
    app.user.edit_user_by_id(user2.id, user3)
    new_users = db.get_user_list()
    assert len(old_users) == len(new_users)
    old_users[index] = user3
    if check_ui:
        assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)


