

def test_del_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.del_group()
    app.session.logout()