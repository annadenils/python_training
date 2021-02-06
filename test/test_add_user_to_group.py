from model.users import Users
from fixture.orm import ORMFixture
from model.group import Group
import random


def test_add_user_to_group(app, db, orm):
    app.open_home_page()
    user = Users(users_name="специальный юзер", users_lastname="Никалаев", home_phone="2345678",
                  mobile_phone="89655783498", work_phone="812-567-90-89", phone2="812-789-56-37")
    if len(db.get_user_list()) == 0:
        app.user.add_new_user(user)
    if len(db.get_group_list()) == 0:
        app.group.init_group(Group(group_name="test-test"))
    group = db.get_group_list()
    groupid = random.choice(group).id
    user_not_in_group = orm.get_users_not_in_group(Group(id=groupid))
    orm_user = random.choice(user_not_in_group)
    app.user.add_to_group(orm_user.id, groupid)
    user_not_in_group_1 = orm.get_users_not_in_group(Group(id=groupid))
    assert len(user_not_in_group) - 1 == len(user_not_in_group_1)