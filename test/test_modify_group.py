from model.group import Group

def test_modify_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.modify_first_group(Group(group_name="modify_group"))
    app.session.logout()
