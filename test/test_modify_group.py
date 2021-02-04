from model.group import Group
import random

def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.init_group(Group(group_name="test-test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    group1 = Group(group_name="modify_group")
    group1.id = group.id
    app.group.modify_group_by_id(group.id, group1)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group1
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
