from model.group import Group
import random
import allure

def test_del_group(app, db, check_ui):
    with allure.step('Given a group list. Empty - add group'):
        if len(db.get_group_list()) == 0:
            app.group.init_group(Group(group_name="test-test"))
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('Given random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When i delete a group %s to the list' % group):
        app.group.del_group_by_id(group.id)
    with allure.step('Then the new group list is less than the old list'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
