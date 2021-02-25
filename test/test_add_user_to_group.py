from model.users import Users
from model.group import Group
import random


def test_add_user_to_group(app, db, orm):
    app.open_home_page()
    new_user = Users(users_name="специальный юзер", users_lastname="Никалаев", home_phone="2345678",
                  mobile_phone="89655783498", work_phone="812-567-90-89", phone2="812-789-56-37")
    new_group = Group(group_name="test-test")
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(new_user)
    if len(db.get_group_list()) == 0:
        app.group.init_group(new_group)
    groups = db.get_group_list()
    if orm.all_users_in_groups(groups):
        app.group.init_group(new_group)
    for x in groups:
        users = orm.get_users_not_in_group(x)
        user = random.choice(users)
        app.user.add_to_group(user.id, x.id)
        user_in_group = orm.get_users_in_group(x)
        assert user in user_in_group
        break


    # else:
    #     app.group.init_group(new_group)
    #     groups = sorted(db.get_group_list(), key=Group.id_or_max)
    #     group = groups[-1]
    #     app.user.add_to_group(user.id, group.id)
    #     user_in_group = orm.get_users_in_group(group)
    #     assert user in user_in_group











    # if user_not_in_group:
    #     app.user.add_to_group(user_not_in_group[0].id, group[0].id)
    # else:
    #     app.user.add_new_user(new_user)
    #     user_not_in_group = orm.get_users_not_in_group(group[0])
    #     app.user.add_to_group(user_not_in_group[0].id, group[0].id)
    # list_user = orm.get_users_in_group(group[0])
    # assert user_not_in_group[0] in list_user
