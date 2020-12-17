
def test_del_first_user(app):
    app.session.login(login_name="admin", password="secret")
    app.user.del_first_user()
    app.session.logout()