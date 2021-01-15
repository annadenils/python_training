from model.group import Group

def test_modify_group(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(group_name="modify_group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
