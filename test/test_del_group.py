from model.group import Group

def test_del_group(app):
    if app.group.count() == 0:
        app.group.init_group(Group(group_name="test-test"))
    app.group.del_group()