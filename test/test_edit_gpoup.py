from model.group import Group

def test_edit_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.edit_group(Group(group_name="новая группа", header="logo", comment="комментарий"))
    app.session.logout()