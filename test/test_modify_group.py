from model.group import Group

def test_modify_group(app):
    if app.group.count() == 0:
        app.group.init_group(Group(group_name="test-test"))
    app.group.modify_first_group(Group(group_name="modify_group"))
