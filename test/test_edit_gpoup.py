from model.group import EditGroup

def test_edit_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.edit_group(EditGroup(new_group_name="новая группа", new_comment="комментарий"))
    app.session.logout()