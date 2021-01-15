from model.group import Group

def test_del_group(app):
    if app.group.count() == 0:
        app.group.init_group(Group(group_name="test-test"))
    old_groups = app.group.get_group_list()
    app.group.del_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
