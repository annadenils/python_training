from fixture.orm import ORMFixture
from model.users import Users
from model.group import Group


def test_del_user_from_group(app, db, orm):
    group = db.get_group_list()
    for x in group:
        if orm.get_users_in_group(x) == []:
            app.open_home_page()
            user = Users(users_name="специальный юзер", users_lastname="Никалаев", home_phone="2345678",
                         mobile_phone="89655783498", work_phone="812-567-90-89", phone2="812-789-56-37")
            if len(db.get_user_list()) == 0:
                app.user.add_new_user(user)
            if len(db.get_group_list()) == 0:
                app.group.init_group(Group(group_name="test-test"))
            group = db.get_group_list()
            user_not_in_group = orm.get_users_not_in_group(group[0])
            app.user.add_to_group(user_not_in_group[0].id, group[0].id)
            break
    for x in group:
        if orm.get_users_in_group(x) == []:
            pass
        else:
            user = orm.get_users_in_group(x)
            app.user.del_from_group(x.id, user[0].id)
            user1 = orm.get_users_in_group(x)
            assert len(user) - 1 == len(user1)
            break