from model.group import Group
import random
import allure

def test_modify_group(app, db, check_ui):
    with allure.step('Given a group list. Empty - add group'):
        if len(db.get_group_list()) == 0:
            app.group.init_group(Group(group_name="test-test"))
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('Given random group from the list'):
        group = random.choice(old_groups)
        index = old_groups.index(group)
    group1 = Group(group_name="modify_group")
    group1.id = group.id
    with allure.step('When i edit a group %s to the list' % group1):
        app.group.modify_group_by_id(group.id, group1)
    with allure.step('Then the new group list is equal to the old list with the edit group'):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[index] = group1
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
