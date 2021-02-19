from model.users import Users
from model.group import Group


def test_add_user_to_group(app, db, orm):
    app.open_home_page()
    new_user = Users(users_name="специальный юзер", users_lastname="Никалаев", home_phone="2345678",
                  mobile_phone="89655783498", work_phone="812-567-90-89", phone2="812-789-56-37")
    new_group = Group(group_name="test-test")
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(new_user)
    if len(db.get_group_list()) == 0:
        app.group.init_group(new_group)
    group = db.get_group_list()
    user_not_in_group = orm.get_users_not_in_group(group[0])
    if user_not_in_group:
        app.user.add_to_group(user_not_in_group[0].id, group[0].id)
    else:
        app.user.add_new_user(new_user)
        user_not_in_group = orm.get_users_not_in_group(group[0])
        app.user.add_to_group(user_not_in_group[0].id, group[0].id)
