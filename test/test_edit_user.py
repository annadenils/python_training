from model.users import Users


def test_edit_user(app):
    app.session.login(login_name="admin", password="secret")
    app.user.edit_user(Users(users_name="Николай", name_company=u"ооо\"далеко и близко\""))
    app.session.logout()