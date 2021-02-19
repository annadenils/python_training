from fixture.orm import ORMFixture
from model.users import Users
from model.group import Group
import random


def test_del_user_from_group(app, db, orm):
    app.open_home_page()
    group = db.get_group_list()
    user = Users(users_name="специальный юзер", users_lastname="Никалаев", home_phone="2345678",
                 mobile_phone="89655783498", work_phone="812-567-90-89", phone2="812-789-56-37")
    new_group = Group(group_name="test-test")
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(user)
    if len(db.get_group_list()) == 0:
        app.group.init_group(new_group)
    for x in group:
        if orm.get_users_in_group(x) == []:
            user_not_in_group = orm.get_users_not_in_group(Group(x.id))
            orm_user = random.choice(user_not_in_group)
            app.user.add_to_group(orm_user, x)
            app.user.del_from_group(x.id, orm_user.id)
            assert len(x) == []
        else:
            user = orm.get_users_in_group(x)
            app.user.del_from_group(x.id, user[0].id)
            user1 = orm.get_users_in_group(x)
            assert len(user) - 1 == len(user1)
        break
